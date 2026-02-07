import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { z } from "zod";

// Validaciones
export const cargoSchema = z.object({
  id: z.number().optional(), 
  abreviacion: z.string().min(1, "Requerido").max(5, "Máx 5 letras"),
  cargo: z.string().min(3, "Requerido"),
});

export type Cargo = z.infer<typeof cargoSchema>;

export const useCargos = () => {
  const queryClient = useQueryClient();

  // GET
  const cargosQuery = useQuery({
    queryKey: ['cargos'],
    queryFn: async () => {
      const { data } = await api.get('/pa-pe-de/');
      if (Array.isArray(data)) return data;
      if (data.items) return data.items;
      return [];
    },
  });

  // POST (Crear)
  const createMutation = useMutation({
    mutationFn: async (nuevoCargo: Cargo) => {
      // Enviamos SIN ID, el backend lo genera
      const payload = {
        abreviacion: nuevoCargo.abreviacion,
        cargo: nuevoCargo.cargo
      };
      await api.post('/pa-pe-de/', payload);
    },
    onSuccess: () => {
      toast.success("Cargo creado exitosamente");
      queryClient.invalidateQueries({ queryKey: ['cargos'] });
    },
    onError: (err: any) => {
      const mensaje = err.response?.data?.detail || "Error al crear el cargo.";
      toast.error(mensaje);
    }
  });

  // PUT (Editar) - CORREGIDO: Usa abreviacion en la URL
  const updateMutation = useMutation({
    mutationFn: async (cargo: Cargo) => {
      // Usamos la abreviación original para encontrar el registro
      const pk = cargo.abreviacion; 
      
      const payload = {
        cargo: cargo.cargo
        // Nota: Generalmente no se permite cambiar la PK (abreviacion) directamente 
        // en un PUT simple si es la clave de la URL.
      };

      // URL: /pa-pe-de/VGR (en lugar de /pa-pe-de/8)
      await api.put(`/pa-pe-de/${pk}`, payload);
    },
    onSuccess: () => {
      toast.success("Cargo actualizado");
      queryClient.invalidateQueries({ queryKey: ['cargos'] });
    },
    onError: (err: any) => {
        toast.error("Error al actualizar. (Nota: No se puede cambiar la Abreviación ya creada)");
    }
  });

  // DELETE (Eliminar) - CORREGIDO: Recibe string
  const deleteMutation = useMutation({
    mutationFn: async (abreviacion: string) => { // <--- Cambiado a string
      // URL: /pa-pe-de/VGR
      await api.delete(`/pa-pe-de/${abreviacion}`);
    },
    onSuccess: () => {
      toast.success("Cargo eliminado");
      queryClient.invalidateQueries({ queryKey: ['cargos'] });
    },
    onError: (err: any) => {
        // Manejo de error de llave foránea (Integridad)
        if (err.response?.status === 500 || err.response?.status === 409) {
            toast.error("No se puede eliminar: Hay personal asignado a este cargo.");
        } else {
            toast.error("Error al eliminar el cargo.");
        }
    }
  });

  return {
    cargos: cargosQuery.data || [],
    isLoading: cargosQuery.isLoading,
    createMutation,
    updateMutation,
    deleteMutation
  };
};