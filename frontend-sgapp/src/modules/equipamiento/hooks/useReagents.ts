import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { z } from "zod";

// ==========================================
// 1. SCHEMAS DE VALIDACIÓN (ZOD)
// ==========================================

// Esquema para la Bitácora (Hijo)
export const movementSchema = z.object({
  id: z.number().optional(),
  id_reactivo: z.number().optional(),
  registrado_por: z.string().min(1, "Requerido"),
  fecha_movimiento: z.date(),
  tipo_movimiento: z.string(), // Entrada, Salida, Ajuste
  cantidad: z.string().transform((val) => parseFloat(val) || 0),
  observaciones: z.string().optional().nullable().transform(v => v || ""),
});

// Esquema para el Reactivo (Padre)
export const reagentSchema = z.object({
  // Aceptamos id numérico opcional
  id: z.number().optional(),
  
  // Identificación
  nombre_reactivo: z.string().min(1, "El nombre es obligatorio"),
  codigo_interno: z.string().optional().nullable().transform(v => v || ""),
  no_articulo: z.string().optional().nullable().transform(v => v || ""), // CAS
  
  // Detalles
  marca: z.string().optional().nullable().transform(v => v || ""),
  grado_calidad: z.string().optional().nullable().transform(v => v || ""),
  proveedor: z.string().optional().nullable().transform(v => v || ""),
  serie: z.string().optional().nullable().transform(v => v || ""), // Lote
  
  // Stock
  unidad_almacen: z.string().optional().nullable().transform(v => v || "ml"),
  unidad: z.string().optional().nullable().transform(v => v || ""), // Presentación
  valor: z.string().transform((val) => parseFloat(val) || 0), // Stock actual
  stock_minimo: z.string().transform((val) => parseInt(val) || 0),
  
  // Ubicación y Estado
  ubicacion: z.string().optional().nullable().transform(v => v || ""),
  estado: z.string().default("VIGENTE"),
  sustancia_controlada: z.boolean().default(false),
  
  // Fechas y Comentarios
  fecha_de_apertura: z.date().optional().nullable(),
  fecha_de_vencimiento: z.date().optional().nullable(),
  comentarios: z.string().optional().nullable().transform(v => v || ""),
});

// Tipos inferidos
export type ReagentFormValues = z.infer<typeof reagentSchema>;
export type MovementFormValues = z.infer<typeof movementSchema>;

// ==========================================
// 2. HOOK PRINCIPAL
// ==========================================

export const useReagents = () => {
  const queryClient = useQueryClient();

  // --- OBTENER TODOS (GET) ---
  const reagentsQuery = useQuery({
    queryKey: ['reactivos'],
    queryFn: async () => {
      // Ajusta '/pa-eq-re/' si tu API tiene otro prefijo, pero según lo visto es este.
      const { data } = await api.get('/pa-eq-re/');
      // Manejo robusto de la respuesta paginada o lista directa
      return Array.isArray(data) ? data : data.items || [];
    },
  });

  // --- CREAR REACTIVO (POST) ---
  const createReagentMutation = useMutation({
    mutationFn: async (data: ReagentFormValues) => {
      // Preparamos payload asegurando fechas en ISO
      const payload = {
        ...data,
        fecha_de_apertura: data.fecha_de_apertura?.toISOString() || null,
        fecha_de_vencimiento: data.fecha_de_vencimiento?.toISOString() || null,
        // No enviamos ID, dejamos que la BD lo genere
        id: undefined 
      };
      await api.post('/pa-eq-re/', payload);
    },
    onSuccess: () => {
      toast.success("Reactivo registrado exitosamente");
      queryClient.invalidateQueries({ queryKey: ['reactivos'] });
    },
    onError: (error: any) => {
      console.error(error);
      toast.error("Error al crear: " + (error.response?.data?.detail || "Revise los datos"));
    }
  });

  // --- ACTUALIZAR REACTIVO (PUT) ---
  const updateReagentMutation = useMutation({
    mutationFn: async (data: ReagentFormValues) => {
      // 1. DETECCIÓN ROBUSTA DEL ID
      // A veces viene como 'id' (frontend) y a veces como 'id_reactivo' (backend raw)
      // @ts-ignore
      const idReal = data.id || data.id_reactivo;

      if (!idReal) {
        throw new Error("No se pudo identificar el ID del reactivo para editar.");
      }

      // 2. LIMPIEZA DE DATOS (CRÍTICO)
      // Extraemos el ID y la lista de movimientos para NO enviarlos en el cuerpo
      // @ts-ignore
      const { id, id_reactivo, pa_eq_mo_items, ...restData } = data;

      // 3. Preparar payload limpio
      const payload = {
        ...restData,
        fecha_de_apertura: data.fecha_de_apertura?.toISOString() || null,
        fecha_de_vencimiento: data.fecha_de_vencimiento?.toISOString() || null,
      };

      // 4. Enviar a la URL correcta
      await api.put(`/pa-eq-re/${idReal}`, payload);
    },
    onSuccess: () => {
      toast.success("Reactivo actualizado correctamente");
      queryClient.invalidateQueries({ queryKey: ['reactivos'] });
    },
    onError: (error: any) => {
      console.error(error);
      const msg = error.response?.data?.detail;
      // Manejo de errores comunes de validación
      if (Array.isArray(msg)) {
         toast.error("Error de validación: " + msg[0].msg);
      } else {
         toast.error("Error al actualizar: " + (msg || "Intente nuevamente"));
      }
    }
  });

  // --- ELIMINAR REACTIVO (DELETE) ---
  const deleteReagentMutation = useMutation({
    mutationFn: async (id: number) => {
      if (!id) throw new Error("ID inválido para eliminar");
      await api.delete(`/pa-eq-re/${id}`);
    },
    onSuccess: () => {
      toast.success("Reactivo eliminado");
      queryClient.invalidateQueries({ queryKey: ['reactivos'] });
    },
    onError: (error: any) => {
      console.error(error);
      toast.error("Error al eliminar: " + (error.response?.data?.detail || "Verifique si tiene movimientos asociados"));
    }
  });

  // --- REGISTRAR MOVIMIENTO (BITÁCORA) ---
  const createMovementMutation = useMutation({
    mutationFn: async (data: MovementFormValues) => {
      const payload = {
        ...data,
        fecha_movimiento: data.fecha_movimiento.toISOString(),
      };
      // El id_reactivo debe venir dentro de 'data' desde el formulario
      await api.post('/pa-eq-mo/', payload);
    },
    onSuccess: () => {
      toast.success("Movimiento registrado en bitácora");
      queryClient.invalidateQueries({ queryKey: ['reactivos'] });
    },
    onError: (error: any) => {
      console.error(error);
      toast.error("Error al registrar movimiento: " + (error.response?.data?.detail || ""));
    }
  });

  return {
    reagents: reagentsQuery.data || [],
    isLoading: reagentsQuery.isLoading,
    createReagentMutation,
    updateReagentMutation,
    deleteReagentMutation,
    createMovementMutation
  };
};