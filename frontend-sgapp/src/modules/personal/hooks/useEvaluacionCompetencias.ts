import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { z } from "zod";

// --- AYUDANTE PARA GENERAR CAMPOS REPETITIVOS ---
// Crea: ev_educacion1 (string), cumple_educacion1 (bool), educacion1n (int)
// --- AYUDANTE PARA GENERAR CAMPOS REPETITIVOS ---
const createEvalFields = (prefix: string, count: number) => {
  const shape: any = {};
  for (let i = 1; i <= count; i++) {
    // AQUI ESTA LA MAGIA: .nullable().transform(...)
    shape[`ev_${prefix}${i}`] = z.string().nullable().optional().transform(val => val || "");
    shape[`cumple_${prefix}${i}`] = z.boolean().default(false);
    shape[`${prefix}${i}n`] = z.coerce.number().min(0).max(5).default(0);
  }
  return shape;
};

export const evaluacionSchema = z.object({
  // ... (el resto queda igual, pero asegúrate de que 'conclusion' también tolere nulos)
  id: z.number().optional(),
  fecha: z.date({ required_error: "Fecha requerida" }),
  responsable: z.string().min(1, "Debe indicar quién evalúa"),
  personal: z.string().min(1, "Seleccione al empleado"),
  cargo: z.string().optional(),
  requisitos: z.number().optional(),
  
  // Campos dinámicos (usarán la nueva función createEvalFields)
  ...createEvalFields('educacion', 3),
  ...createEvalFields('formacion', 10),
  ...createEvalFields('experiencia', 5),
  ...createEvalFields('habilidades', 10),
  ...createEvalFields('conocimiento', 10),
  ...createEvalFields('calificacion', 5),

  promedio: z.coerce.number().default(0),
  escala: z.coerce.number().default(5),
  
  // Agregamos tolerancia a null aquí también
  conclusion: z.string().nullable().optional().transform(val => val || ""),
  competencia_asegurada: z.boolean().default(false),
});


export type EvaluacionFormValues = z.infer<typeof evaluacionSchema>;

export const useEvaluacionCompetencias = () => {
  const queryClient = useQueryClient();

  // GET
  const evaluacionesQuery = useQuery({
    queryKey: ['competencias-evaluaciones'],
    queryFn: async () => {
      const { data } = await api.get('/pa-pe-se/');
      return Array.isArray(data) ? data : (data.items || []);
    },
  });

  // POST
  const createEvaluacionMutation = useMutation({
    mutationFn: async (data: EvaluacionFormValues) => {
      const payload = { ...data, fecha: data.fecha.toISOString() };
      await api.post('/pa-pe-se/', payload);
    },
    onSuccess: () => {
      toast.success("Evaluación registrada");
      queryClient.invalidateQueries({ queryKey: ['competencias-evaluaciones'] });
    },
    onError: () => toast.error("Error al guardar evaluación")
  });

  // PUT
  const updateEvaluacionMutation = useMutation({
    mutationFn: async (data: EvaluacionFormValues) => {
      if (!data.id) throw new Error("Falta ID");
      const payload = { ...data, fecha: data.fecha.toISOString() };
      await api.put(`/pa-pe-se/${data.id}`, payload);
    },
    onSuccess: () => {
      toast.success("Evaluación actualizada");
      queryClient.invalidateQueries({ queryKey: ['competencias-evaluaciones'] });
    },
    onError: () => toast.error("Error al actualizar")
  });

  // DELETE
  const deleteEvaluacionMutation = useMutation({
      mutationFn: async (id: number) => {
          await api.delete(`/pa-pe-se/${id}`);
      },
      onSuccess: () => {
          toast.success("Evaluación eliminada");
          queryClient.invalidateQueries({ queryKey: ['competencias-evaluaciones'] });
      },
      onError: () => toast.error("No se pudo eliminar")
  });

  return {
    evaluaciones: evaluacionesQuery.data || [],
    isLoadingEvaluaciones: evaluacionesQuery.isLoading,
    createEvaluacionMutation,
    updateEvaluacionMutation,
    deleteEvaluacionMutation,
  };
};
