import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { z } from "zod";

// Función auxiliar para los 10 participantes
const createParticipantFields = () => {
  const shape: any = {};
  for (let i = 1; i <= 10; i++) {
    shape[`participante_${i}`] = z.string().nullable().optional().transform(v => v || "");
  }
  return shape;
};

export const effectivenessSchema = z.object({
  id: z.number().optional(),
  id_plan: z.coerce.number().min(1, "Debe seleccionar una capacitación ejecutada"), // FK a PA_PE_PL
  fecha: z.date({ required_error: "Fecha de evaluación requerida" }),
  
  // Campos de texto de evaluación
  comentarios_observaciones: z.string().nullable().optional().transform(v => v || ""),
  actividad_evaluacion: z.string().nullable().optional().transform(v => v || ""),
  conclusion_eficacia: z.string().nullable().optional().transform(v => v || ""),
  
  // Booleans de cierre
  eficaz: z.boolean().default(false),
  cerrado: z.boolean().default(false),

  // Participantes 1-10 (Se llenan automático desde el frontend)
  ...createParticipantFields(),
});

export type EffectivenessFormValues = z.infer<typeof effectivenessSchema>;

export const useEffectiveness = () => {
  const queryClient = useQueryClient();

  // GET
  const effectivenessQuery = useQuery({
    queryKey: ['competencias-eficacia'],
    queryFn: async () => {
      const { data } = await api.get('/pa-pe-ef/');
      return Array.isArray(data) ? data : (data.items || []);
    },
  });

  // POST
  const createEffectivenessMutation = useMutation({
    mutationFn: async (data: EffectivenessFormValues) => {
      const payload = {
        ...data,
        fecha: data.fecha.toISOString(),
      };
      await api.post('/pa-pe-ef/', payload);
    },
    onSuccess: () => {
      toast.success("Eficacia registrada. Ciclo cerrado.");
      queryClient.invalidateQueries({ queryKey: ['competencias-eficacia'] });
    },
    onError: () => toast.error("Error al registrar eficacia")
  });

  // PUT
  const updateEffectivenessMutation = useMutation({
    mutationFn: async (data: EffectivenessFormValues) => {
      if (!data.id) throw new Error("Falta ID");
      const payload = {
        ...data,
        fecha: data.fecha.toISOString(),
      };
      await api.put(`/pa-pe-ef/${data.id}`, payload);
    },
    onSuccess: () => {
      toast.success("Registro actualizado");
      queryClient.invalidateQueries({ queryKey: ['competencias-eficacia'] });
    },
    onError: () => toast.error("Error al actualizar")
  });

  // DELETE
  const deleteEffectivenessMutation = useMutation({
    mutationFn: async (id: number) => {
      await api.delete(`/pa-pe-ef/${id}`);
    },
    onSuccess: () => {
      toast.success("Registro eliminado");
      queryClient.invalidateQueries({ queryKey: ['competencias-eficacia'] });
    },
    onError: () => toast.error("Error al eliminar")
  });

  return {
    effectiveness: effectivenessQuery.data || [],
    isLoadingEffectiveness: effectivenessQuery.isLoading,
    createEffectivenessMutation,
    updateEffectivenessMutation,
    deleteEffectivenessMutation,
  };
};
