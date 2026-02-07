import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { format, isValid, parseISO } from "date-fns";
import { es } from "date-fns/locale";
import { Plus, CalendarIcon, User, ArrowRight, Trash, Pencil, BookOpen } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import {
  Card, CardContent, CardDescription, CardHeader, CardTitle, CardFooter
} from "@/components/ui/card";
import {
  Dialog, DialogContent, DialogHeader, DialogTitle,
} from "@/components/ui/dialog";
import {
  Form, FormControl, FormField, FormItem, FormLabel, FormMessage
} from "@/components/ui/form";
import {
    Select, SelectContent, SelectItem, SelectTrigger, SelectValue,
} from "@/components/ui/select";
import {
    Popover, PopoverContent, PopoverTrigger,
} from "@/components/ui/popover";
import { Calendar } from "@/components/ui/calendar";
import {
    AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogTitle, AlertDialogDescription, AlertDialogFooter
} from "@/components/ui/alert-dialog";

// Hooks
import { usePrograms, programSchema, ProgramFormValues } from "../hooks/usePrograms";
import { usePersonal } from "../hooks/usePersonal";

export const TrainingProgramsPage = () => {
  const { programs, isLoadingPrograms, createProgramMutation, updateProgramMutation, deleteProgramMutation } = usePrograms();
  const { data: personal } = usePersonal();

  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [deleteId, setDeleteId] = useState<number | null>(null);
  const [dateInputValue, setDateInputValue] = useState("");

  const form = useForm<ProgramFormValues>({
    resolver: zodResolver(programSchema),
    defaultValues: {
      registrado_por: "",
      dirigido_a: "",
      actividad: "",
      competencia_por_adquirir: "",
      comentarios: ""
    },
  });

  // Sincronizar fecha manual
  useEffect(() => {
    const currentDate = form.getValues("fecha_programada");
    if (currentDate) {
        setDateInputValue(format(currentDate, "yyyy-MM-dd"));
    } else {
        setDateInputValue("");
    }
  }, [form.watch("fecha_programada"), isDialogOpen]);

  const handleCreate = () => {
      setEditingId(null);
      form.reset({
        registrado_por: "", 
        dirigido_a: "", 
        actividad: "", 
        competencia_por_adquirir: "", 
        comentarios: "",
        fecha_programada: new Date()
      });
      setIsDialogOpen(true);
  };

  const handleEdit = (item: any) => {
      setEditingId(item.id);
      
      const cleanData: any = { ...item };
      
      if (cleanData.fecha_programada) cleanData.fecha_programada = new Date(cleanData.fecha_programada);
      
      Object.keys(cleanData).forEach(key => {
          if (cleanData[key] === null) {
              cleanData[key] = "";
          }
      });
      
      form.reset(cleanData);
      setIsDialogOpen(true);
  };

  const onSubmit = async (data: ProgramFormValues) => {
    if (editingId) {
        await updateProgramMutation.mutateAsync({ ...data, id: editingId });
    } else {
        await createProgramMutation.mutateAsync(data);
    }
    setIsDialogOpen(false);
  };

  const onInvalid = (errors: any) => {
      console.error("Errores del formulario:", errors);
      const firstError = Object.values(errors)[0] as any;
      toast.error("Formulario incompleto", {
          description: firstError?.message || "Revise los campos obligatorios."
      });
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Programas de Capacitación (Necesidades)</h1>
          <p className="text-slate-500">Registro de actividades para cerrar brechas de competencia.</p>
        </div>
        <Button onClick={handleCreate} className="bg-blue-600 hover:bg-blue-700">
          <Plus className="mr-2 h-4 w-4" /> Nueva Necesidad
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {isLoadingPrograms ? (
             <div className="col-span-3 text-center p-10 text-slate-500">Cargando programas...</div>
        ) : programs.length === 0 ? (
            <div className="col-span-3 text-center p-10 border-2 border-dashed rounded-xl bg-slate-50 text-slate-500">
                No hay necesidades de capacitación registradas.
            </div>
        ) : programs.map((prog: any) => (
            <Card key={prog.id} className="hover:shadow-md transition-shadow border-t-4 border-t-amber-500 flex flex-col justify-between">
                <CardHeader className="pb-2">
                    <CardTitle className="text-lg font-bold text-slate-800 leading-snug">
                        {prog.actividad}
                    </CardTitle>
                    <CardDescription className="flex items-center gap-1 text-xs">
                         <CalendarIcon className="h-3 w-3" />
                         Tentativo: {prog.fecha_programada ? format(new Date(prog.fecha_programada), 'yyyy-MM-dd') : '-'}
                    </CardDescription>
                </CardHeader>
                <CardContent className="text-sm space-y-3">
                    <div className="bg-slate-50 p-2 rounded border border-slate-100">
                        <div className="text-xs text-slate-500 uppercase font-bold mb-1">Competencia Objetivo</div>
                        <div className="text-slate-700 italic">{prog.competencia_por_adquirir}</div>
                    </div>
                    
                    <div className="flex items-center justify-between text-xs text-slate-600">
                        <div className="flex items-center gap-1">
                            <User className="h-3 w-3" />
                            <span>Solicitante: <b>{prog.registrado_por}</b></span>
                        </div>
                        <ArrowRight className="h-3 w-3 text-slate-300" />
                        <div className="font-bold text-blue-700">
                            {prog.dirigido_a}
                        </div>
                    </div>
                </CardContent>
                <CardFooter className="flex justify-end gap-2 pt-2 border-t mt-2">
                    <Button variant="ghost" size="sm" onClick={() => handleEdit(prog)}>
                        <Pencil className="h-4 w-4 text-slate-500" />
                    </Button>
                    <Button variant="ghost" size="sm" onClick={() => setDeleteId(prog.id)}>
                        <Trash className="h-4 w-4 text-red-500" />
                    </Button>
                </CardFooter>
            </Card>
        ))}
      </div>

      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
        <DialogContent className="sm:max-w-[600px]">
          <DialogHeader>
            <DialogTitle>{editingId ? "Editar Necesidad" : "Registrar Necesidad de Capacitación"}</DialogTitle>
          </DialogHeader>

          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit, onInvalid)} className="space-y-4">
                
                <div className="grid grid-cols-2 gap-4">
                    <FormField
                        control={form.control}
                        name="registrado_por"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Solicitado Por</FormLabel>
                                <Select onValueChange={field.onChange} value={field.value}>
                                    <FormControl><SelectTrigger><SelectValue placeholder="Jefe/Evaluador" /></SelectTrigger></FormControl>
                                    <SelectContent>
                                        {personal?.map((p: any) => (
                                            <SelectItem key={p.abreviatura} value={p.abreviatura}>{p.nombre}</SelectItem>
                                        ))}
                                    </SelectContent>
                                </Select>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    <FormField
                        control={form.control}
                        name="dirigido_a"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Dirigido A (Beneficiario)</FormLabel>
                                <Select onValueChange={field.onChange} value={field.value}>
                                    <FormControl><SelectTrigger><SelectValue placeholder="Empleado" /></SelectTrigger></FormControl>
                                    <SelectContent>
                                        {personal?.map((p: any) => (
                                            <SelectItem key={p.abreviatura} value={p.abreviatura}>{p.nombre}</SelectItem>
                                        ))}
                                    </SelectContent>
                                </Select>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                </div>

                <FormField
                    control={form.control}
                    name="actividad"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Actividad / Curso Propuesto</FormLabel>
                            <FormControl>
                                <Input placeholder="Ej: Curso de Excel Avanzado" {...field} />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    )}
                />

                <FormField
                    control={form.control}
                    name="competencia_por_adquirir"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Competencia a Adquirir / Mejorar</FormLabel>
                            <FormControl>
                                <Textarea placeholder="Ej: Capacidad para automatizar reportes..." className="resize-none h-20" {...field} />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    )}
                />

                <div className="grid grid-cols-2 gap-4">
                     <FormField
                        control={form.control}
                        name="fecha_programada"
                        render={({ field }) => (
                            <FormItem className="flex flex-col">
                                <FormLabel>Fecha Tentativa</FormLabel>
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
                                            selected={field.value}
                                            onSelect={field.onChange}
                                            disabled={(date) => date < new Date("2000-01-01")}
                                            initialFocus
                                        />
                                    </PopoverContent>
                                </Popover>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                </div>
                
                <FormField
                    control={form.control}
                    name="comentarios"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Observaciones Adicionales</FormLabel>
                            <FormControl>
                                <Input {...field} value={field.value || ""} />
                            </FormControl>
                        </FormItem>
                    )}
                />

                <div className="flex justify-end pt-2">
                    <Button type="submit" className="bg-blue-600 hover:bg-blue-700 w-full md:w-auto">
                        <BookOpen className="mr-2 h-4 w-4" /> Guardar Programa
                    </Button>
                </div>
            </form>
          </Form>
        </DialogContent>
      </Dialog>

      <AlertDialog open={!!deleteId} onOpenChange={() => setDeleteId(null)}>
        <AlertDialogContent>
            <AlertDialogTitle>¿Eliminar Registro?</AlertDialogTitle>
            <AlertDialogDescription>Se eliminará esta necesidad de capacitación.</AlertDialogDescription>
            <AlertDialogFooter>
                <AlertDialogCancel>Cancelar</AlertDialogCancel>
                <AlertDialogAction className="bg-red-600" onClick={() => { if(deleteId) deleteProgramMutation.mutate(deleteId); setDeleteId(null); }}>
                    Eliminar
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
};