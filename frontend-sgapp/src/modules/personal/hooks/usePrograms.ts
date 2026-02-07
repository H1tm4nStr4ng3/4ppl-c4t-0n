import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { z } from "zod";

// Validaciones
export const programSchema = z.object({
  id: z.number().optional(),
  
  // Selects (Strings obligatorios)
  registrado_por: z.string().nullable().transform(v => v || "").refine(v => v.length > 0, { message: "Debe seleccionar quién solicita" }),
  dirigido_a: z.string().nullable().transform(v => v || "").refine(v => v.length > 0, { message: "Debe seleccionar al beneficiario" }),
  
  // Textos (Con transformación de nulos)
  actividad: z.string().nullable().optional().transform(v => v || "").refine(v => v.length >= 3, { message: "La actividad debe tener al menos 3 caracteres" }),
  
  competencia_por_adquirir: z.string().nullable().optional().transform(v => v || "").refine(v => v.length >= 3, { message: "Describa la competencia" }),
  
  fecha_programada: z.date({ required_error: "Fecha tentativa requerida" }),
  
  comentarios: z.string().nullable().optional().transform(val => val || ""),
});

export type ProgramFormValues = z.infer<typeof programSchema>;

export const usePrograms = () => {
  const queryClient = useQueryClient();

  // GET
  const programsQuery = useQuery({
    queryKey: ['competencias-programas'],
    queryFn: async () => {
      const { data } = await api.get('/pa-pe-pr/');
      return Array.isArray(data) ? data : (data.items || []);
    },
  });

  // POST
  const createProgramMutation = useMutation({
    mutationFn: async (data: ProgramFormValues) => {
      const payload = {
        ...data,
        fecha_programada: data.fecha_programada.toISOString(),
      };
      await api.post('/pa-pe-pr/', payload);
    },
    onSuccess: () => {
      toast.success("Necesidad de capacitación registrada");
      queryClient.invalidateQueries({ queryKey: ['competencias-programas'] });
    },
    onError: () => toast.error("Error al crear registro")
  });

  // PUT
  const updateProgramMutation = useMutation({
    mutationFn: async (data: ProgramFormValues) => {
      if (!data.id) throw new Error("Falta ID");
      const payload = {
        ...data,
        fecha_programada: data.fecha_programada.toISOString(),
      };
      await api.put(`/pa-pe-pr/${data.id}`, payload);
    },
    onSuccess: () => {
      toast.success("Registro actualizado");
      queryClient.invalidateQueries({ queryKey: ['competencias-programas'] });
    },
    onError: () => toast.error("Error al actualizar")
  });

  // DELETE
  const deleteProgramMutation = useMutation({
    mutationFn: async (id: number) => {
      await api.delete(`/pa-pe-pr/${id}`);
    },
    onSuccess: () => {
      toast.success("Registro eliminado");
      queryClient.invalidateQueries({ queryKey: ['competencias-programas'] });
    },
    onError: () => toast.error("Error al eliminar")
  });

  return {
    programs: programsQuery.data || [],
    isLoadingPrograms: programsQuery.isLoading,
    createProgramMutation,
    updateProgramMutation,
    deleteProgramMutation,
  };
};
