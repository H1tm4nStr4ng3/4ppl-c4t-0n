import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { toast } from "sonner";
import { z } from "zod";

// --- SCHEMAS ---
export const categorySchema = z.object({
    lista_de_equipos: z.string().min(1, "El nombre del tipo es obligatorio"),
    id: z.number().optional(),
});

// AQUI AGREGAMOS TODOS LOS CAMPOS DE LA NORMA
export const equipmentSchema = z.object({
  id: z.number().optional(),
  
  // 1. Identificación
  equipamiento: z.string().min(1, "Seleccione el tipo de equipo"), 
  codigo_interno: z.string().min(1, "El código interno es obligatorio"),
  marca: z.string().nullable().optional().transform(v => v || ""),
  serie: z.string().nullable().optional().transform(v => v || ""),
  ubicacion: z.string().nullable().optional().transform(v => v || ""),
  estado: z.string().default("OPERATIVO"),
  
  // 2. Especificaciones Técnicas (Metrología)
  material: z.string().nullable().optional().transform(v => v || ""),
  numero_de_piezas: z.string().nullable().optional().transform(v => v || ""),
  max_vn: z.string().nullable().optional().transform(v => v || ""), // Capacidad Máxima
  d: z.string().nullable().optional().transform(v => v || ""),      // Resolución
  clase_de_exactitud: z.string().nullable().optional().transform(v => v || ""),
  
  // 3. Versiones (Software/Firmware)
  version_software: z.string().nullable().optional().transform(v => v || ""),
  version_firmware: z.string().nullable().optional().transform(v => v || ""),

  // 4. Gestión y Frecuencias
  requiere: z.string().nullable().optional().transform(v => v || ""),
  frecuencia_de_calibracion: z.string().nullable().optional().transform(v => v || ""),
  frecuencia_de_mantenimiento: z.string().nullable().optional().transform(v => v || ""),
  frecuencia_de_comprobacion_intermedia: z.string().nullable().optional().transform(v => v || ""),
  frecuencia_de_calificacion: z.string().nullable().optional().transform(v => v || ""),

  // 5. Otros
  puesta_en_funcionamiento: z.date().optional().nullable(),
  comentarios: z.string().nullable().optional().transform(v => v || ""),
});

export type EquipmentFormValues = z.infer<typeof equipmentSchema>;
export type CategoryFormValues = z.infer<typeof categorySchema>;

export const useInventory = () => {
  const queryClient = useQueryClient();

  // 1. GET TIPOS
  const categoriesQuery = useQuery({
    queryKey: ['equipos-categorias'],
    queryFn: async () => {
      const { data } = await api.get('/pa-eq-le/');
      return data;
    },
  });

  // 2. GET EQUIPOS
  const equipmentQuery = useQuery({
    queryKey: ['equipos-inventario'],
    queryFn: async () => {
      const { data } = await api.get('/pa-eq-eq/');
      return data;
    },
  });

  // 3. CREATE TYPE
  const createCategoryMutation = useMutation({
    mutationFn: async (data: CategoryFormValues) => {
      const payload = { ...data, id: 0 };
      await api.post('/pa-eq-le/', payload);
    },
    onSuccess: () => {
      toast.success("Nuevo tipo de equipo agregado");
      queryClient.invalidateQueries({ queryKey: ['equipos-categorias'] });
    },
    onError: (error: any) => {
        console.error(error);
        toast.error("Error al crear tipo (¿Ya existe?)");
    }
  });

  // 4. CREATE EQUIPMENT
  const createEquipmentMutation = useMutation({
    mutationFn: async (data: EquipmentFormValues) => {
      const payload = {
        ...data,
        id: 0, 
        puesta_en_funcionamiento: data.puesta_en_funcionamiento ? data.puesta_en_funcionamiento.toISOString() : null,
      };
      await api.post('/pa-eq-eq/', payload);
    },
    onSuccess: () => {
      toast.success("Equipo registrado correctamente");
      queryClient.invalidateQueries({ queryKey: ['equipos-inventario'] });
    },
    onError: (err: any) => {
        const msg = err.response?.data?.detail || "Error al registrar equipo";
        toast.error(msg);
    }
  });

  // 5. UPDATE EQUIPMENT
  const updateEquipmentMutation = useMutation({
    mutationFn: async (data: EquipmentFormValues) => {
      if (!data.id) throw new Error("Falta ID");
      const payload = {
        ...data,
        puesta_en_funcionamiento: data.puesta_en_funcionamiento ? data.puesta_en_funcionamiento.toISOString() : null,
      };
      await api.put(`/pa-eq-eq/${data.id}`, payload);
    },
    onSuccess: () => {
      toast.success("Equipo actualizado");
      queryClient.invalidateQueries({ queryKey: ['equipos-inventario'] });
    },
    onError: () => toast.error("Error al actualizar")
  });

  // 6. DELETE EQUIPMENT
  const deleteEquipmentMutation = useMutation({
    mutationFn: async (id: number) => {
      await api.delete(`/pa-eq-eq/${id}`);
    },
    onSuccess: () => {
      toast.success("Equipo eliminado");
      queryClient.invalidateQueries({ queryKey: ['equipos-inventario'] });
    },
    onError: () => toast.error("Error al eliminar")
  });

  // 7. DELETE CATEGORY
  const deleteCategoryMutation = useMutation({
    mutationFn: async (nombreTipo: string) => {
        await api.delete(`/pa-eq-le/${nombreTipo}`);
    },
    onSuccess: () => {
      toast.success("Tipo eliminado");
      queryClient.invalidateQueries({ queryKey: ['equipos-categorias'] });
    },
    onError: () => toast.error("No se puede eliminar (¿Está en uso?)")
  });

  const getSafeList = (data: any) => {
    if (!data) return [];
    if (Array.isArray(data)) return data; 
    if (data.items && Array.isArray(data.items)) return data.items;
    return [];
  };

  return {
    categories: getSafeList(categoriesQuery.data),
    equipments: getSafeList(equipmentQuery.data),
    isLoading: categoriesQuery.isLoading || equipmentQuery.isLoading,
    createCategoryMutation,
    createEquipmentMutation,
    updateEquipmentMutation,
    deleteEquipmentMutation,
    deleteCategoryMutation 
  };
};