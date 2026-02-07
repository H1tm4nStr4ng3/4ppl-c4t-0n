import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { z } from "zod";

// Helper para generar los 10 ítems de revisión repetitivos
const createSupervisionItems = () => {
  const shape: any = {};
  for (let i = 1; i <= 10; i++) {
    // El texto del ítem (ej: "Uso de EPP")
    shape[`item_de_supervision_${i}`] = z.string().nullable().optional().transform(v => v || "");
    // El check de cumplimiento
    shape[`supervision_exitosa_${i}`] = z.boolean().default(false);
  }
  return shape;
};

export const supervisionSchema = z.object({
  id: z.number().optional(),
  
  // FECHA
  fecha: z.date({ required_error: "La fecha es obligatoria" }),

  // ACTORES (Strings porque son FK a Abreviatura)
  supervisores: z.string().min(1, "Debe seleccionar quién supervisa"),
  supervisados: z.string().min(1, "Debe seleccionar al personal supervisado"),
  
  // DETALLES
  cargo: z.string().nullable().optional().transform(v => v || ""),
  item: z.string().min(3, "Describa la actividad supervisada (Ensayo/Tarea)"),
  comentarios: z.string().nullable().optional().transform(v => v || ""),
  
  // EL CAMPO CRÍTICO (ALERTA)
  requiere_adquirir_o_aumentar_competencia: z.boolean().default(false),

  // ITEMS 1-10
  ...createSupervisionItems(),
});

export type SupervisionFormValues = z.infer<typeof supervisionSchema>;

export const useSupervision = () => {
  const queryClient = useQueryClient();

  // --- GET ---
  const supervisionQuery = useQuery({
    queryKey: ['personal-supervision'],
    queryFn: async () => {
      const { data } = await api.get('/pa-pe-su/');
      return Array.isArray(data) ? data : (data.items || []);
    },
  });

  // --- CREATE ---
  const createSupervisionMutation = useMutation({
    mutationFn: async (data: SupervisionFormValues) => {
      const payload = {
        ...data,
        fecha: data.fecha.toISOString(),
      };
      await api.post('/pa-pe-su/', payload);
    },
    onSuccess: () => {
      toast.success("Supervisión registrada correctamente");
      queryClient.invalidateQueries({ queryKey: ['personal-supervision'] });
    },
    onError: (error: any) => {
      console.error(error);
      toast.error("Error al guardar supervisión");
    }
  });

  // --- UPDATE ---
  const updateSupervisionMutation = useMutation({
    mutationFn: async (data: SupervisionFormValues) => {
      if (!data.id) throw new Error("Falta ID");
      const payload = {
        ...data,
        fecha: data.fecha.toISOString(),
      };
      await api.put(`/pa-pe-su/${data.id}`, payload);
    },
    onSuccess: () => {
      toast.success("Registro actualizado");
      queryClient.invalidateQueries({ queryKey: ['personal-supervision'] });
    },
    onError: () => toast.error("Error al actualizar")
  });

  // --- DELETE ---
  const deleteSupervisionMutation = useMutation({
    mutationFn: async (id: number) => {
      await api.delete(`/pa-pe-su/${id}`);
    },
    onSuccess: () => {
      toast.success("Registro eliminado");
      queryClient.invalidateQueries({ queryKey: ['personal-supervision'] });
    },
    onError: () => toast.error("Error al eliminar")
  });

  return {
    supervisions: supervisionQuery.data || [],
    isLoadingSupervisions: supervisionQuery.isLoading,
    createSupervisionMutation,
    updateSupervisionMutation,
    deleteSupervisionMutation,
  };
};
