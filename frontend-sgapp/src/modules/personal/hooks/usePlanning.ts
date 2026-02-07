import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { z } from "zod";

// Validaciones Robustas
export const planningSchema = z.object({
  id: z.number().optional(),
  item_del_programa: z.coerce.number().min(1, "Seleccione la necesidad vinculada"),

  // 1. ORGANIZADOR INTERNO (FK)
  elaborado_por: z.string().nullable().transform(v => v || "").refine(v => v.length > 0, { message: "Seleccione al organizador interno" }),
  
  // 2. INSTRUCTOR / ENTIDAD EXTERNA (TEXTO LIBRE)
  responsable_de_generacion_de_competencia: z.string().nullable().transform(v => v || "").refine(v => v.length > 0, { message: "Indique la Institución o Instructor" }),
  
  // 3. ASISTENTES (STRING CON COMAS)
  asistentes: z.string().nullable().transform(v => v || "").refine(v => v.length > 0, { message: "Debe seleccionar al menos un asistente" }),
  
  tematica: z.string().nullable().optional().transform(v => v || ""),
  fecha_inicio: z.date({ required_error: "Fecha de inicio requerida" }),
  fecha_final: z.date().optional().nullable(),

  // 4. CAMPO CORREGIDO (GUION BAJO)
  evaluacion_si_aplica: z.coerce.number().min(0).default(0),
  
  competencia: z.boolean().default(false),
  comentarios_de_la_generacion_de_competencia: z.string().nullable().optional().transform(v => v || ""),
  conclusion: z.string().nullable().optional().transform(v => v || ""),
});

export type PlanningFormValues = z.infer<typeof planningSchema>;

export const usePlanning = () => {
  const queryClient = useQueryClient();

  // GET
  const planningQuery = useQuery({
    queryKey: ['competencias-planificacion'],
    queryFn: async () => {
      const { data } = await api.get('/pa-pe-pl/');
      return Array.isArray(data) ? data : (data.items || []);
    },
  });

  // POST
  const createPlanningMutation = useMutation({
    mutationFn: async (data: PlanningFormValues) => {
      const payload = {
        ...data,
        fecha_inicio: data.fecha_inicio.toISOString(),
        fecha_final: data.fecha_final?.toISOString() || null,
      };
      await api.post('/pa-pe-pl/', payload);
    },
    onSuccess: () => {
      toast.success("Ejecución registrada exitosamente");
      queryClient.invalidateQueries({ queryKey: ['competencias-planificacion'] });
    },
    onError: () => toast.error("Error al registrar ejecución")
  });

  // PUT
  const updatePlanningMutation = useMutation({
    mutationFn: async (data: PlanningFormValues) => {
      if (!data.id) throw new Error("Falta ID");
      const payload = {
        ...data,
        fecha_inicio: data.fecha_inicio.toISOString(),
        fecha_final: data.fecha_final?.toISOString() || null,
      };
      await api.put(`/pa-pe-pl/${data.id}`, payload);
    },
    onSuccess: () => {
      toast.success("Registro actualizado");
      queryClient.invalidateQueries({ queryKey: ['competencias-planificacion'] });
    },
    onError: () => toast.error("Error al actualizar")
  });

  // DELETE
  const deletePlanningMutation = useMutation({
    mutationFn: async (id: number) => {
      await api.delete(`/pa-pe-pl/${id}`);
    },
    onSuccess: () => {
      toast.success("Registro eliminado");
      queryClient.invalidateQueries({ queryKey: ['competencias-planificacion'] });
    },
    onError: () => toast.error("Error al eliminar")
  });

  return {
    plannings: planningQuery.data || [],
    isLoadingPlannings: planningQuery.isLoading,
    createPlanningMutation,
    updatePlanningMutation,
    deletePlanningMutation,
  };
};
