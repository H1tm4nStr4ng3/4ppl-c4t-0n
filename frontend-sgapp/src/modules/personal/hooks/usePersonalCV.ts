import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { z } from "zod";

export const cvSchema = z.object({
  id: z.number().optional(),
  personal: z.string(),
  institucion: z.string().min(1, "Requerido"),
  carrera_curso_logro: z.string().min(1, "Requerido"),
  fecha_inicio: z.date().optional().nullable(),
  fecha_final: z.date().optional().nullable(),
  carga_horaria: z.coerce.number().optional(),
  descripcion: z.string().optional(),
});

export type CVFormValues = z.infer<typeof cvSchema>;

export const usePersonalCV = (personalId?: string) => {
  const queryClient = useQueryClient();

  const cvQuery = useQuery({
    queryKey: ['personal-cv', personalId],
    queryFn: async () => {
      if (!personalId) return [];
      const { data } = await api.get('/pa-pe-cv/');
      const todos = Array.isArray(data) ? data : (data.items || []);
      return todos.filter((item: any) => item.personal === personalId);
    },
    enabled: !!personalId && personalId !== 'new',
  });

  const createMutation = useMutation({
    mutationFn: async (data: CVFormValues) => {
      const payload = {
        ...data,
        fecha_inicio: data.fecha_inicio ? data.fecha_inicio.toISOString() : null,
        fecha_final: data.fecha_final ? data.fecha_final.toISOString() : null,
      };
      await api.post('/pa-pe-cv/', payload);
    },
    onSuccess: () => {
      toast.success("Registro agregado");
      queryClient.invalidateQueries({ queryKey: ['personal-cv'] });
    },
    onError: () => toast.error("Error al agregar")
  });

  // --- NUEVA FUNCIONALIDAD: EDITAR ---
  const updateMutation = useMutation({
    mutationFn: async (data: CVFormValues) => {
      if (!data.id) throw new Error("Falta ID para editar");
      const payload = {
        ...data,
        fecha_inicio: data.fecha_inicio ? data.fecha_inicio.toISOString() : null,
        fecha_final: data.fecha_final ? data.fecha_final.toISOString() : null,
      };
      await api.put(`/pa-pe-cv/${data.id}`, payload);
    },
    onSuccess: () => {
      toast.success("Registro actualizado");
      queryClient.invalidateQueries({ queryKey: ['personal-cv'] });
    },
    onError: () => toast.error("Error al actualizar")
  });

  const deleteMutation = useMutation({
    mutationFn: async (id: number) => {
      await api.delete(`/pa-pe-cv/${id}`);
    },
    onSuccess: () => {
      toast.success("Registro eliminado");
      queryClient.invalidateQueries({ queryKey: ['personal-cv'] });
    },
    onError: () => toast.error("No se pudo eliminar")
  });

  return {
    items: cvQuery.data || [],
    isLoading: cvQuery.isLoading,
    createMutation,
    updateMutation, // <--- Exportamos esto
    deleteMutation
  };
};