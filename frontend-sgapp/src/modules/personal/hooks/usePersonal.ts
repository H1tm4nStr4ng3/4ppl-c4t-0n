import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { PersonalFormValues } from "../components/personal-schema"; 

// Definimos la interfaz básica si no la tienes importada
export interface Personal {
  abreviatura: string;
  nombre: string;
  cargo: string;
  vigente: boolean;
  // ... otros campos
}

export const usePersonal = (id?: string) => {
  const queryClient = useQueryClient();

  // 1. Obtener LISTA COMPLETA (Para la tabla principal)
  const query = useQuery({
    queryKey: ['personal'],
    queryFn: async () => {
      const { data } = await api.get<any>('/pa-pe-pe/'); 
      if (Array.isArray(data)) return data;
      if (data.items) return data.items;
      return [];
    },
  });

  // 2. Obtener UN SOLO EMPLEADO (Para editar)
  const singleQuery = useQuery({
    queryKey: ['personal', id],
    queryFn: async () => {
        if (!id || id === 'new') return null;
        // El endpoint busca por abreviatura (PK)
        const { data } = await api.get(`/pa-pe-pe/${id}`);
        return data;
    },
    enabled: !!id && id !== 'new', // Solo se ejecuta si hay ID y no es nuevo
  });

  // 3. Crear Empleado (POST)
  const createMutation = useMutation({
    mutationFn: async (nuevoPersonal: PersonalFormValues) => {
      // Limpiamos los datos antes de enviar
      const payload = {
        ...nuevoPersonal,
        // Aseguramos que el cargo se envíe (es la abreviatura del cargo)
        cargo: nuevoPersonal.cargo, 
        // Si hay fechas, asegurarse que vayan como ISO string si el backend lo requiere
        // Pydantic suele ser inteligente, pero por seguridad:
        fecha_de_nacimiento: nuevoPersonal.fecha_de_nacimiento?.toISOString(),
      };
      
      console.log("Enviando a Backend:", payload);
      await api.post('/pa-pe-pe/', payload);
    },
    onSuccess: () => {
      toast.success("Empleado registrado correctamente");
      queryClient.invalidateQueries({ queryKey: ['personal'] });
    },
    onError: (error: any) => {
      console.error(error);
      const detail = error.response?.data?.detail;
      // Si el error es duplicado de llave primaria
      if (JSON.stringify(detail).includes("already exists")) {
         toast.error("El ID (Abreviatura) ya existe. Usa otro.");
      } else {
         toast.error("Error al guardar el empleado.");
      }
    }
  });

  // 4. Editar Empleado (PUT)
  const updateMutation = useMutation({
    mutationFn: async (datos: PersonalFormValues) => {
      const pk = datos.abreviatura; // La PK es la abreviatura
      const payload = {
          ...datos,
          fecha_de_nacimiento: datos.fecha_de_nacimiento ? 
             (typeof datos.fecha_de_nacimiento === 'string' ? datos.fecha_de_nacimiento : datos.fecha_de_nacimiento.toISOString()) 
             : null
      };
      
      await api.put(`/pa-pe-pe/${pk}`, payload);
    },
    onSuccess: () => {
      toast.success("Datos actualizados correctamente");
      queryClient.invalidateQueries({ queryKey: ['personal'] });
      queryClient.invalidateQueries({ queryKey: ['personal', id] });
    },
    onError: (error: any) => {
      console.error(error);
      toast.error("Error al actualizar los datos.");
    }
  });

  // 5. Eliminar (Ya lo tenías)
  const deleteMutation = useMutation({
    mutationFn: async (idToDelete: string) => {
      await api.delete(`/pa-pe-pe/${idToDelete}`);
    },
    onSuccess: () => {
      toast.success("Empleado eliminado");
      queryClient.invalidateQueries({ queryKey: ['personal'] });
    },
    onError: () => toast.error("No se pudo eliminar.")
  });

  return {
    // Lista general
    data: query.data,
    isLoading: query.isLoading,
    isError: query.isError,
    
    // Un solo empleado
    employee: singleQuery.data,
    isLoadingEmployee: singleQuery.isLoading,

    // Acciones
    createMutation,
    updateMutation,
    deleteMutation
  };
};