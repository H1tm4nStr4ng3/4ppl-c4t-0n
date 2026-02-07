import { useState } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Plus, Pencil, Trash, Save, ArrowLeft, Loader2 } from "lucide-react";
import { useNavigate } from "react-router-dom";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Dialog, DialogContent, DialogHeader, DialogTitle,
} from "@/components/ui/dialog";
import {
  Form, FormControl, FormField, FormItem, FormLabel, FormMessage,
} from "@/components/ui/form";
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "@/components/ui/table";
import {
    AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogTitle, AlertDialogDescription, AlertDialogFooter
} from "@/components/ui/alert-dialog";

import { useCargos, cargoSchema, Cargo } from "../hooks/useCargos";

export const CargosPage = () => {
  const navigate = useNavigate();
  const { cargos, isLoading, createMutation, updateMutation, deleteMutation } = useCargos();
  
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingCargo, setEditingCargo] = useState<Cargo | null>(null);
  
  // CAMBIO: Ahora el ID a borrar es un string (la abreviación)
  const [deleteId, setDeleteId] = useState<string | null>(null); 

  const form = useForm<Cargo>({
    resolver: zodResolver(cargoSchema),
    defaultValues: { abreviacion: "", cargo: "" },
  });

  const handleCreate = () => {
    setEditingCargo(null);
    form.reset({ abreviacion: "", cargo: "" });
    setIsDialogOpen(true);
  };

  const handleEdit = (cargo: Cargo) => {
    setEditingCargo(cargo);
    form.reset(cargo);
    setIsDialogOpen(true);
  };

  const onSubmit = (data: Cargo) => {
    if (editingCargo) {
      // Al editar, mantenemos el ID numérico interno por si acaso, 
      // pero la mutación usará la abreviación
      updateMutation.mutate({ ...data, id: editingCargo.id }); 
    } else {
      createMutation.mutate(data);
    }
    setIsDialogOpen(false);
  };

  return (
    <div className="space-y-6 animate-in fade-in">
      <div className="flex items-center gap-4">
        <Button variant="ghost" size="icon" onClick={() => navigate('/personal')}>
            <ArrowLeft className="h-5 w-5" />
        </Button>
        <h1 className="text-2xl font-bold">Gestión de Cargos</h1>
      </div>

      <div className="flex justify-end">
        <Button onClick={handleCreate} className="bg-blue-600 hover:bg-blue-700">
          <Plus className="mr-2 h-4 w-4" /> Nuevo Cargo
        </Button>
      </div>

      <div className="border rounded-lg bg-white shadow-sm">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Abreviación (ID)</TableHead>
              <TableHead>Nombre del Cargo</TableHead>
              <TableHead className="text-right">Acciones</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {isLoading ? (
               <TableRow><TableCell colSpan={3} className="text-center h-24">Cargando...</TableCell></TableRow>
            ) : cargos.map((cargo: any, index: number) => (
              // Usamos index como fallback para la key visual
              <TableRow key={cargo.id || index}>
                <TableCell className="font-mono font-bold text-blue-600">{cargo.abreviacion}</TableCell>
                <TableCell>{cargo.cargo}</TableCell>
                <TableCell className="text-right space-x-2">
                  <Button variant="ghost" size="sm" onClick={() => handleEdit(cargo)}>
                    <Pencil className="h-4 w-4 text-slate-500" />
                  </Button>
                  {/* Pasamos la abreviación al botón de borrar */}
                  <Button variant="ghost" size="sm" onClick={() => setDeleteId(cargo.abreviacion)}>
                    <Trash className="h-4 w-4 text-red-500" />
                  </Button>
                </TableCell>
              </TableRow>
            ))}
            {cargos.length === 0 && !isLoading && (
                 <TableRow><TableCell colSpan={3} className="text-center h-24 text-muted-foreground">No hay cargos definidos.</TableCell></TableRow>
            )}
          </TableBody>
        </Table>
      </div>

      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>{editingCargo ? "Editar Cargo" : "Crear Nuevo Cargo"}</DialogTitle>
          </DialogHeader>
          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
              <FormField
                control={form.control}
                name="abreviacion"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Abreviación (Código Único)</FormLabel>
                    <FormControl>
                        {/* Bloqueamos la edición de la abreviación si estamos editando, porque es la PK */}
                        <Input 
                            placeholder="Ej: AS" 
                            {...field} 
                            maxLength={5} 
                            disabled={!!editingCargo} 
                            className={!!editingCargo ? "bg-slate-100" : ""}
                        />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="cargo"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Nombre del Cargo</FormLabel>
                    <FormControl><Input placeholder="Ej: Analista de Sistemas" {...field} /></FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <Button type="submit" className="w-full bg-blue-600">
                <Save className="mr-2 h-4 w-4" /> Guardar
              </Button>
            </form>
          </Form>
        </DialogContent>
      </Dialog>

      <AlertDialog open={!!deleteId} onOpenChange={() => setDeleteId(null)}>
        <AlertDialogContent>
            <AlertDialogTitle>¿Eliminar Cargo?</AlertDialogTitle>
            <AlertDialogDescription>
                Se eliminará el cargo <b>{deleteId}</b>. 
                Si hay personal asignado a este cargo, la operación fallará por seguridad.
            </AlertDialogDescription>
            <AlertDialogFooter>
                <AlertDialogCancel>Cancelar</AlertDialogCancel>
                <AlertDialogAction 
                    className="bg-red-600 hover:bg-red-700" 
                    onClick={() => {
                        if(deleteId) deleteMutation.mutate(deleteId);
                        setDeleteId(null);
                    }}
                >
                    Eliminar
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
};