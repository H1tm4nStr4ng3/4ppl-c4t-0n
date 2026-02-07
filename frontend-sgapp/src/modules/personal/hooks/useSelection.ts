import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { z } from "zod";

// ==========================================
// 1. ESQUEMA DEL PROCESO (PA_PE_SP)
// ==========================================
export const procesoSchema = z.object({
  id: z.number().optional(),
  puesto: z.string().min(1, "Debe seleccionar un cargo"), // FK a Cargos
  evaluadores: z.string().min(1, "Debe asignar un responsable"), // FK a Personal
  fecha_inicial: z.date(),
  fecha_final: z.date().optional().nullable(),

 
  // Ponderaciones CV
  ponderacion_educacion: z.coerce.number().min(0).default(0),
  ponderacion_formacion: z.coerce.number().min(0).default(0),
  ponderacion_habilidades: z.coerce.number().min(0).default(0),
  ponderacion_experiencia: z.coerce.number().min(0).default(0),
  ponderacion_conocimientotecnico: z.coerce.number().min(0).default(0),
  
  ponderacion_minima_cv: z.coerce.number().min(0).default(51),
  conclusion_cv: z.string().optional(),

  // Definición de Entrevista (Metadata)
  item_entrevista_1: z.string().optional(),
  ponderacion_entrevista_1: z.coerce.number().default(0),
  item_entrevista_2: z.string().optional(),
  ponderacion_entrevista_2: z.coerce.number().default(0),
  item_entrevista_3: z.string().optional(),
  ponderacion_entrevista_3: z.coerce.number().default(0),
  item_entrevista_4: z.string().optional(),
  ponderacion_entrevista_4: z.coerce.number().default(0),
  item_entrevista_5: z.string().optional(),
  ponderacion_entrevista_5: z.coerce.number().default(0),

  ponderacion_minima_entrevista: z.coerce.number().default(51),
  conclusion_entrevista: z.string().optional(),
});

// ==========================================
// 2. ESQUEMA DEL POSTULANTE (PA_PE_PO)
// ==========================================
export const postulanteSchema = z.object({
  id: z.number().optional(),
  proceso_de_seleccion: z.number(),
  postulante: z.string().min(3, "Nombre requerido"),
  
  // Notas CV
  educacion: z.coerce.number().min(0).max(100).default(0),
  formacion: z.coerce.number().min(0).max(100).default(0),
  habilidades: z.coerce.number().min(0).max(100).default(0),
  experiencia: z.coerce.number().min(0).max(100).default(0),
  conocimientotecnico: z.coerce.number().min(0).max(100).default(0),
  
  resultado_cv: z.coerce.number().optional(),
  pasa_a_entrevista: z.boolean().default(false),
  
  // Notas Entrevista
  item_entrevista1: z.coerce.number().min(0).max(100).default(0),
  item_entrevista2: z.coerce.number().min(0).max(100).default(0),
  item_entrevista3: z.coerce.number().min(0).max(100).default(0),
  item_entrevista4: z.coerce.number().min(0).max(100).default(0),
  item_entrevista5: z.coerce.number().min(0).max(100).default(0),
  
  resultado_entrevista: z.coerce.number().optional(),
  seleccionado: z.boolean().default(false),
});

export type ProcesoFormValues = z.infer<typeof procesoSchema>;
export type PostulanteFormValues = z.infer<typeof postulanteSchema>;

// ==========================================
// HOOK
// ==========================================
// ... (Mantén los imports y los esquemas Zod igual que antes) ...

export const useSelection = (procesoId?: number) => {
  const queryClient = useQueryClient();

  // ==========================================
  // 1. GESTIÓN DE PROCESOS (VACANTES)
  // ==========================================
  const procesosQuery = useQuery({
    queryKey: ['procesos-seleccion'],
    queryFn: async () => {
      const { data } = await api.get('/pa-pe-sp/');
      return Array.isArray(data) ? data : (data.items || []);
    },
  });

  const createProcesoMutation = useMutation({
    mutationFn: async (data: ProcesoFormValues) => {
      const payload = {
          ...data,
          fecha_inicial: data.fecha_inicial.toISOString(),
          fecha_final: data.fecha_final?.toISOString(),
      };
      await api.post('/pa-pe-sp/', payload);
    },
    onSuccess: () => {
      toast.success("Proceso configurado exitosamente");
      queryClient.invalidateQueries({ queryKey: ['procesos-seleccion'] });
    },
    onError: (e: any) => toast.error(e.response?.data?.detail || "Error al crear proceso")
  });

  // --- NUEVO: ACTUALIZAR PROCESO ---
  const updateProcesoMutation = useMutation({
    mutationFn: async (data: ProcesoFormValues) => {
      if (!data.id) throw new Error("Falta ID");
      const payload = {
          ...data,
          fecha_inicial: data.fecha_inicial.toISOString(),
          fecha_final: data.fecha_final?.toISOString(),
      };
      await api.put(`/pa-pe-sp/${data.id}`, payload);
    },
    onSuccess: () => {
      toast.success("Proceso actualizado");
      queryClient.invalidateQueries({ queryKey: ['procesos-seleccion'] });
    },
    onError: () => toast.error("Error al actualizar proceso")
  });

  // --- NUEVO: ELIMINAR PROCESO ---
  const deleteProcesoMutation = useMutation({
    mutationFn: async (id: number) => {
        await api.delete(`/pa-pe-sp/${id}`);
    },
    onSuccess: () => {
        toast.success("Proceso eliminado");
        queryClient.invalidateQueries({ queryKey: ['procesos-seleccion'] });
    },
    onError: () => toast.error("No se puede eliminar (posiblemente tenga postulantes)")
  });

  // ==========================================
  // 2. GESTIÓN DE POSTULANTES
  // ==========================================
  const postulantesQuery = useQuery({
    queryKey: ['postulantes', procesoId],
    queryFn: async () => {
      if (!procesoId) return [];
      const { data } = await api.get('/pa-pe-po/');
      const todos = Array.isArray(data) ? data : (data.items || []);
      return todos.filter((p: any) => p.proceso_de_seleccion === Number(procesoId));
    },
    enabled: !!procesoId,
  });

  const createPostulanteMutation = useMutation({
    mutationFn: async (data: PostulanteFormValues) => {
      await api.post('/pa-pe-po/', data);
    },
    onSuccess: () => {
      toast.success("Postulante registrado");
      queryClient.invalidateQueries({ queryKey: ['postulantes', procesoId] });
    },
  });

  const updatePostulanteMutation = useMutation({
    mutationFn: async (data: PostulanteFormValues) => {
      if(!data.id) throw new Error("Falta ID");
      await api.put(`/pa-pe-po/${data.id}`, data);
    },
    onSuccess: () => {
      toast.success("Evaluación guardada");
      queryClient.invalidateQueries({ queryKey: ['postulantes', procesoId] });
    },
  });

  const deletePostulanteMutation = useMutation({
      mutationFn: async (id: number) => {
          await api.delete(`/pa-pe-po/${id}`);
      },
      onSuccess: () => {
          toast.success("Postulante eliminado");
          queryClient.invalidateQueries({ queryKey: ['postulantes', procesoId] });
      }
  });

  return {
    procesos: procesosQuery.data || [],
    isLoadingProcesos: procesosQuery.isLoading,
    createProcesoMutation,
    updateProcesoMutation, // <--- Exportado
    deleteProcesoMutation, // <--- Exportado
    
    postulantes: postulantesQuery.data || [],
    isLoadingPostulantes: postulantesQuery.isLoading,
    createPostulanteMutation,
    updatePostulanteMutation,
    deletePostulanteMutation
  };
};