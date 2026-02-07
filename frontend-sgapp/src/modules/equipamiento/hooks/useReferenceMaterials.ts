import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { z } from "zod";

// --- SCHEMAS ---

// 1. Hijo (Especificaciones)
export const mvSchema = z.object({
  id: z.number().optional(),
  id_mr: z.string().optional(), // Se llena automático con el padre
  parametro: z.string().min(1, "El parámetro es obligatorio"),
  valor: z.string().transform((val) => parseFloat(val) || 0), // Manejo de strings a float
  incertidumbre: z.string().transform((val) => parseFloat(val) || 0),
  unidad: z.string().min(1, "La unidad es obligatoria"),
});

// 2. Padre (Material Referencia)
export const mrSchema = z.object({
  id: z.number().optional(),
  codigo_interno: z.string().min(1, "El código interno es obligatorio"),
  equipamiento: z.string().nullable().optional().transform(v => v || ""),
  tipo: z.string().nullable().optional().transform(v => v || ""),
  certificado: z.string().nullable().optional().transform(v => v || ""),
  
  // Fechas
  fecha_de_certificado: z.date().optional().nullable(),
  fecha_de_apertura: z.date().optional().nullable(),
  fecha_de_vencimiento: z.date().optional().nullable(),

  codigo_original: z.string().nullable().optional().transform(v => v || ""),
  productor_del_material_de_referencia: z.string().nullable().optional().transform(v => v || ""),
  procedencia: z.string().nullable().optional().transform(v => v || ""),
  serie: z.string().nullable().optional().transform(v => v || ""),
  material: z.string().nullable().optional().transform(v => v || ""),
  ubicacion: z.string().nullable().optional().transform(v => v || ""),
  estado: z.string().default("VIGENTE"),
  comentarios: z.string().nullable().optional().transform(v => v || ""),
});

export type MRFormValues = z.infer<typeof mrSchema>;
export type MVFormValues = z.infer<typeof mvSchema>;

export const useReferenceMaterials = () => {
  const queryClient = useQueryClient();

  // 1. GET ALL
  const mrQuery = useQuery({
    queryKey: ['materiales-referencia'],
    queryFn: async () => {
      const { data } = await api.get('/pa-eq-mr/');
      // Ajuste por si viene paginado
      return Array.isArray(data) ? data : data.items || [];
    },
  });

  // 2. CREATE MR (Padre)
  const createMRMutation = useMutation({
    mutationFn: async (data: MRFormValues) => {
      const payload = {
        ...data,
        id: 0, // Blindaje
        fecha_de_certificado: data.fecha_de_certificado?.toISOString() || null,
        fecha_de_apertura: data.fecha_de_apertura?.toISOString() || null,
        fecha_de_vencimiento: data.fecha_de_vencimiento?.toISOString() || null,
      };
      await api.post('/pa-eq-mr/', payload);
    },
    onSuccess: () => {
      toast.success("Material de referencia creado");
      queryClient.invalidateQueries({ queryKey: ['materiales-referencia'] });
    },
    onError: () => toast.error("Error al crear. Revise el código interno.")
  });

  // 3. UPDATE MR
  const updateMRMutation = useMutation({
    mutationFn: async (data: MRFormValues) => {
      if (!data.id) throw new Error("Falta ID");
      const payload = {
        ...data,
        fecha_de_certificado: data.fecha_de_certificado?.toISOString() || null,
        fecha_de_apertura: data.fecha_de_apertura?.toISOString() || null,
        fecha_de_vencimiento: data.fecha_de_vencimiento?.toISOString() || null,
      };
      await api.put(`/pa-eq-mr/${data.id}`, payload);
    },
    onSuccess: () => {
      toast.success("Material actualizado");
      queryClient.invalidateQueries({ queryKey: ['materiales-referencia'] });
    },
    onError: () => toast.error("Error al actualizar")
  });

  // 4. DELETE MR
  const deleteMRMutation = useMutation({
    mutationFn: async (id: number) => {
      await api.delete(`/pa-eq-mr/${id}`);
    },
    onSuccess: () => {
      toast.success("Material eliminado");
      queryClient.invalidateQueries({ queryKey: ['materiales-referencia'] });
    },
    onError: () => toast.error("Error al eliminar")
  });

  // --- SUBMÓDULO HIJOS (MV) ---

  // 5. CREATE MV
  const createMVMutation = useMutation({
    mutationFn: async (data: MVFormValues) => {
      const payload = { ...data, id: 0 };
      await api.post('/pa-eq-mv/', payload);
    },
    onSuccess: () => {
      toast.success("Especificación agregada");
      queryClient.invalidateQueries({ queryKey: ['materiales-referencia'] });
    },
    onError: () => toast.error("Error al agregar especificación")
  });

  // 6. DELETE MV
  const deleteMVMutation = useMutation({
    mutationFn: async (id: number) => {
      await api.delete(`/pa-eq-mv/${id}`);
    },
    onSuccess: () => {
      toast.success("Especificación eliminada");
      queryClient.invalidateQueries({ queryKey: ['materiales-referencia'] });
    },
    onError: () => toast.error("Error al eliminar especificación")
  });

  return {
    materials: mrQuery.data || [],
    isLoading: mrQuery.isLoading,
    createMRMutation,
    updateMRMutation,
    deleteMRMutation,
    createMVMutation,
    deleteMVMutation
  };
};
