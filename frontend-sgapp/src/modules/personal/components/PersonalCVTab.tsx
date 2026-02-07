import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { format, isValid, parseISO } from "date-fns";
import { es } from "date-fns/locale";
import { Plus, Trash, School, CalendarIcon, Clock, Pencil } from "lucide-react"; // Importamos Pencil

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "@/components/ui/table";
import {
  Dialog, DialogContent, DialogHeader, DialogTitle,
} from "@/components/ui/dialog";
import {
  Form, FormControl, FormField, FormItem, FormLabel, FormMessage,
} from "@/components/ui/form";
import {
    Popover, PopoverContent, PopoverTrigger,
} from "@/components/ui/popover";
import { Calendar } from "@/components/ui/calendar";
import { usePersonalCV, cvSchema, CVFormValues } from "../hooks/usePersonalCV";

interface Props {
    personalId: string;
}

export const PersonalCVTab = ({ personalId }: Props) => {
  const { items, isLoading, createMutation, updateMutation, deleteMutation } = usePersonalCV(personalId);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingId, setEditingId] = useState<number | null>(null); // Controlamos si editamos
  const [dateInputValue, setDateInputValue] = useState("");

  const form = useForm<CVFormValues>({
    resolver: zodResolver(cvSchema),
    defaultValues: {
      personal: personalId,
      institucion: "",
      carrera_curso_logro: "",
      carga_horaria: 0,
    },
  });

  // Sincronizar fecha manual
  useEffect(() => {
    const currentDate = form.getValues("fecha_final");
    if (currentDate) {
        setDateInputValue(format(currentDate, "yyyy-MM-dd"));
    } else {
        setDateInputValue("");
    }
  }, [form.watch("fecha_final"), isDialogOpen]);

  // Abrir modal para CREAR
  const handleCreate = () => {
      setEditingId(null);
      form.reset({ personal: personalId, institucion: "", carrera_curso_logro: "", carga_horaria: 0 });
      setDateInputValue("");
      setIsDialogOpen(true);
  };

  // Abrir modal para EDITAR
  const handleEdit = (item: any) => {
      setEditingId(item.id);
      form.reset({
          id: item.id,
          personal: personalId,
          institucion: item.institucion,
          carrera_curso_logro: item.carrera_curso_logro,
          carga_horaria: item.carga_horaria,
          fecha_final: item.fecha_final ? new Date(item.fecha_final) : null,
      });
      setIsDialogOpen(true);
  };

  const onSubmit = async (data: CVFormValues) => {
    if (editingId) {
        await updateMutation.mutateAsync(data);
    } else {
        await createMutation.mutateAsync(data);
    }
    setIsDialogOpen(false);
  };

  if (isLoading) return <div className="p-4 text-center text-slate-500">Cargando...</div>;

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
            <h3 className="text-lg font-bold text-slate-800">Formación y Currículum</h3>
            <p className="text-sm text-slate-500">Registro de títulos, cursos y capacitaciones.</p>
        </div>
        <Button onClick={handleCreate} className="bg-blue-600 hover:bg-blue-700">
            <Plus className="mr-2 h-4 w-4" /> Agregar Estudio
        </Button>
      </div>

      <div className="border rounded-lg bg-white overflow-hidden shadow-sm">
        <Table>
            <TableHeader>
                <TableRow className="bg-slate-50">
                    <TableHead>Fecha</TableHead>
                    <TableHead>Título / Curso</TableHead>
                    <TableHead>Institución</TableHead>
                    <TableHead>Horas</TableHead>
                    <TableHead className="text-right">Acciones</TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                {items.length === 0 ? (
                    <TableRow><TableCell colSpan={5} className="text-center h-24 text-slate-400">Sin registros.</TableCell></TableRow>
                ) : items.map((item: any) => (
                    <TableRow key={item.id}>
                        <TableCell className="font-mono text-slate-600">
                            {item.fecha_final ? format(new Date(item.fecha_final), 'yyyy-MM-dd') : '-'}
                        </TableCell>
                        <TableCell className="font-bold text-slate-800">{item.carrera_curso_logro}</TableCell>
                        <TableCell>
                            <div className="flex items-center gap-2">
                                <School className="h-4 w-4 text-slate-400" />
                                {item.institucion}
                            </div>
                        </TableCell>
                        <TableCell>
                            {item.carga_horaria ? <span className="flex items-center gap-1 text-slate-600"><Clock className="h-3 w-3" /> {item.carga_horaria}h</span> : '-'}
                        </TableCell>
                        <TableCell className="text-right space-x-1">
                            {/* Botón EDITAR */}
                            <Button variant="ghost" size="sm" onClick={() => handleEdit(item)}>
                                <Pencil className="h-4 w-4 text-slate-500" />
                            </Button>
                            {/* Botón ELIMINAR */}
                            <Button variant="ghost" size="sm" onClick={() => deleteMutation.mutate(item.id)}>
                                <Trash className="h-4 w-4 text-red-500" />
                            </Button>
                        </TableCell>
                    </TableRow>
                ))}
            </TableBody>
        </Table>
      </div>

      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
        <DialogContent className="sm:max-w-[600px]">
            <DialogHeader>
                <DialogTitle>{editingId ? "Editar Registro" : "Nuevo Registro Académico"}</DialogTitle>
            </DialogHeader>
            <Form {...form}>
                <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                    <FormField
                        control={form.control}
                        name="carrera_curso_logro"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Nombre del Título / Curso</FormLabel>
                                <FormControl><Input {...field} /></FormControl>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    <FormField
                        control={form.control}
                        name="institucion"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Institución</FormLabel>
                                <FormControl><Input {...field} /></FormControl>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    <div className="grid grid-cols-2 gap-4">
                        <FormField
                            control={form.control}
                            name="fecha_final"
                            render={({ field }) => (
                                <FormItem className="flex flex-col">
                                    <FormLabel>Fecha Conclusión</FormLabel>
                                    <Popover>
                                        <PopoverTrigger asChild>
                                            <FormControl>
                                                <div className="relative flex items-center w-full">
                                                    <Input 
                                                        value={dateInputValue}
                                                        onChange={(e) => {
                                                            const val = e.target.value;
                                                            setDateInputValue(val);
                                                            const date = parseISO(val);
                                                            if (isValid(date) && val.length === 10) field.onChange(date);
                                                            else if (val === "") field.onChange(undefined);
                                                        }}
                                                        placeholder="AAAA-MM-DD"
                                                        className="pl-10 w-full font-mono"
                                                        maxLength={10}
                                                    />
                                                    <CalendarIcon className="absolute left-3 h-4 w-4 opacity-50 pointer-events-none" />
                                                </div>
                                            </FormControl>
                                        </PopoverTrigger>
                                        <PopoverContent className="w-auto p-0" align="start">
                                            <Calendar
                                                mode="single"
                                                selected={field.value || undefined}
                                                onSelect={(date) => field.onChange(date)}
                                                disabled={(date) => date > new Date()}
                                                initialFocus
                                                captionLayout="dropdown-buttons"
                                                fromYear={1970} 
                                                toYear={new Date().getFullYear()}
                                            />
                                        </PopoverContent>
                                    </Popover>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                        <FormField
                            control={form.control}
                            name="carga_horaria"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Horas</FormLabel>
                                    <FormControl>
                                        <Input type="number" {...field} onChange={e => field.onChange(parseFloat(e.target.value))} />
                                    </FormControl>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                    </div>
                    <div className="flex justify-end pt-4">
                        <Button type="submit" className="bg-blue-600">
                             {editingId ? "Guardar Cambios" : "Guardar Registro"}
                        </Button>
                    </div>
                </form>
            </Form>
        </DialogContent>
      </Dialog>
    </div>
  );
};