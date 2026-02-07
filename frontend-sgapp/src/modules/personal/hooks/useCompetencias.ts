import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { z } from "zod";

// ==========================================
// ESQUEMA: REQUISITOS DEL CARGO (PA_PE_RQ)
// ==========================================
// Función auxiliar para generar campos repetitivos (texto + boleano crítico)
const createReqFields = (prefix: string, count: number) => {
  const shape: any = {};
  for (let i = 1; i <= count; i++) {
    shape[`${prefix}${i}`] = z.string().optional();
    shape[`${prefix}${i}c`] = z.boolean().default(false);
  }
  return shape;
};

export const requirementsSchema = z.object({
  id: z.number().optional(),
  cargo_req: z.string().min(1, "Debe seleccionar un cargo"), // FK a PA_PE_DE
  responsable: z.string().min(1, "Responsable requerido"),   // FK a PA_PE_PE
  fecha: z.date({ required_error: "Fecha requerida" }),
  aprobado_vigente: z.boolean().default(true),
  comentarios: z.string().optional(),

  // Generamos dinámicamente los campos según tu DB
  ...createReqFields('educacion', 3),
  ...createReqFields('formacion', 10),
  ...createReqFields('experiencia', 5),
  ...createReqFields('habilidades', 10),
  ...createReqFields('conocimiento', 10),
  ...createReqFields('calificacion', 5),
});

export type RequirementsFormValues = z.infer<typeof requirementsSchema>;

export const useCompetencias = () => {
  const queryClient = useQueryClient();

  // --- 1. GESTIÓN DE REQUISITOS (RQ) ---

  const requirementsQuery = useQuery({
    queryKey: ['competencias-requisitos'],
    queryFn: async () => {
      const { data } = await api.get('/pa-pe-rq/');
      return Array.isArray(data) ? data : (data.items || []);
    },
  });

  const createRequirementMutation = useMutation({
    mutationFn: async (data: RequirementsFormValues) => {
      const payload = {
        ...data,
        fecha: data.fecha.toISOString(),
      };
      await api.post('/pa-pe-rq/', payload);
    },
    onSuccess: () => {
      toast.success("Matriz de requisitos guardada");
      queryClient.invalidateQueries({ queryKey: ['competencias-requisitos'] });
    },
    onError: (e: any) => toast.error("Error al guardar requisitos")
  });

  const updateRequirementMutation = useMutation({
    mutationFn: async (data: RequirementsFormValues) => {
        if (!data.id) throw new Error("Falta ID");
        const payload = {
            ...data,
            fecha: data.fecha.toISOString(),
        };
        await api.put(`/pa-pe-rq/${data.id}`, payload);
    },
    onSuccess: () => {
        toast.success("Requisitos actualizados");
        queryClient.invalidateQueries({ queryKey: ['competencias-requisitos'] });
    },
    onError: () => toast.error("Error al actualizar")
  });

  const deleteRequirementMutation = useMutation({
      mutationFn: async (id: number) => {
          await api.delete(`/pa-pe-rq/${id}`);
      },
      onSuccess: () => {
          toast.success("Registro eliminado");
          queryClient.invalidateQueries({ queryKey: ['competencias-requisitos'] });
      },
      onError: () => toast.error("No se pudo eliminar")
  });

  return {
    requirements: requirementsQuery.data || [],
    isLoadingRequirements: requirementsQuery.isLoading,
    createRequirementMutation,
    updateRequirementMutation,
    deleteRequirementMutation,
  };
};
