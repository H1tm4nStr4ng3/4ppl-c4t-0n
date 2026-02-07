import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { z } from "zod";

export const authSchema = z.object({
  id: z.number().optional(),
  autorizado_a: z.string(),
  autorizado_por: z.string().min(1, "Debe seleccionar quién autoriza"),
  cargo: z.string().optional(),
  fecha: z.date({ required_error: "Fecha requerida" }),
  autorizacion_a: z.string().min(1, "Describa la actividad"),
  comentario: z.string().optional(),
});

export type AuthFormValues = z.infer<typeof authSchema>;

export const usePersonalAuth = (personalId?: string) => {
  const queryClient = useQueryClient();

  const authQuery = useQuery({
    queryKey: ['personal-auth', personalId],
    queryFn: async () => {
      if (!personalId) return [];
      const { data } = await api.get('/pa-pe-au/');
      const items = Array.isArray(data) ? data : (data.items || []);
      return items.filter((item: any) => item.autorizado_a === personalId);
    },
    enabled: !!personalId && personalId !== 'new',
  });

  const createMutation = useMutation({
    mutationFn: async (data: AuthFormValues) => {
      const payload = { ...data, fecha: data.fecha.toISOString() };
      await api.post('/pa-pe-au/', payload);
    },
    onSuccess: () => {
      toast.success("Autorización registrada");
      queryClient.invalidateQueries({ queryKey: ['personal-auth'] });
    },
    onError: () => toast.error("Error al registrar")
  });

  // --- NUEVO: EDITAR ---
  const updateMutation = useMutation({
    mutationFn: async (data: AuthFormValues) => {
      if (!data.id) throw new Error("Falta ID");
      const payload = { ...data, fecha: data.fecha.toISOString() };
      await api.put(`/pa-pe-au/${data.id}`, payload);
    },
    onSuccess: () => {
      toast.success("Autorización actualizada");
      queryClient.invalidateQueries({ queryKey: ['personal-auth'] });
    },
    onError: () => toast.error("Error al actualizar")
  });

  const deleteMutation = useMutation({
    mutationFn: async (id: number) => {
      await api.delete(`/pa-pe-au/${id}`);
    },
    onSuccess: () => {
      toast.success("Autorización eliminada");
      queryClient.invalidateQueries({ queryKey: ['personal-auth'] });
    },
    onError: () => toast.error("Error al eliminar")
  });

  return {
    items: authQuery.data || [],
    isLoading: authQuery.isLoading,
    createMutation,
    updateMutation, // <--- Exportar
    deleteMutation
  };
};