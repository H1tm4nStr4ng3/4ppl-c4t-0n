import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { format, isValid, parseISO } from "date-fns";
import { es } from "date-fns/locale";
import { Plus, CalendarIcon, User, Users, Trash, Pencil, ClipboardCheck, ArrowRight, Building2, CheckSquare } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Checkbox } from "@/components/ui/checkbox";
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
import { Badge } from "@/components/ui/badge";

// Hooks
import { usePlanning, planningSchema, PlanningFormValues } from "../hooks/usePlanning";
import { usePrograms } from "../hooks/usePrograms"; 
import { usePersonal } from "../hooks/usePersonal";

export const TrainingPlanningPage = () => {
  const { plannings, isLoadingPlannings, createPlanningMutation, updatePlanningMutation, deletePlanningMutation } = usePlanning();
  const { programs } = usePrograms();
  const { data: personal } = usePersonal();

  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [deleteId, setDeleteId] = useState<number | null>(null);
  
  const [startDateValue, setStartDateValue] = useState("");
  const [endDateValue, setEndDateValue] = useState("");

  const form = useForm<PlanningFormValues>({
    resolver: zodResolver(planningSchema),
    defaultValues: {
      item_del_programa: 0, 
      elaborado_por: "", 
      responsable_de_generacion_de_competencia: "",
      asistentes: "", 
      tematica: "",
      evaluacion_si_aplica: 0, 
      competencia: false, 
      comentarios_de_la_generacion_de_competencia: "", 
      conclusion: ""
    },
  });

  const watchStart = form.watch("fecha_inicio");
  const watchEnd = form.watch("fecha_final");

  useEffect(() => {
    if (watchStart) setStartDateValue(format(watchStart, "yyyy-MM-dd"));
    else setStartDateValue("");
  }, [watchStart, isDialogOpen]);

  useEffect(() => {
    if (watchEnd) setEndDateValue(format(watchEnd, "yyyy-MM-dd"));
    else setEndDateValue("");
  }, [watchEnd, isDialogOpen]);

  const handleCreate = () => {
      setEditingId(null);
      form.reset({
        item_del_programa: undefined,
        elaborado_por: "", 
        responsable_de_generacion_de_competencia: "",
        asistentes: "", 
        tematica: "",
        fecha_inicio: new Date(),
        evaluacion_si_aplica: 0,
        competencia: false,
        comentarios_de_la_generacion_de_competencia: "",
        conclusion: ""
      });
      setIsDialogOpen(true);
  };

  const handleEdit = (item: any) => {
      setEditingId(item.id);
      
      const cleanData: any = { ...item };
      
      if (cleanData.fecha_inicio) cleanData.fecha_inicio = new Date(cleanData.fecha_inicio);
      if (cleanData.fecha_final) cleanData.fecha_final = new Date(cleanData.fecha_final);
      
      Object.keys(cleanData).forEach(key => {
          if (cleanData[key] === null) {
              if (key === 'competencia') cleanData[key] = false;
              else if (key === 'evaluacion_si_aplica') cleanData[key] = 0;
              else cleanData[key] = "";
          }
      });
      
      form.reset(cleanData);
      setIsDialogOpen(true);
  };

  const onSubmit = async (data: PlanningFormValues) => {
    if (editingId) {
        await updatePlanningMutation.mutateAsync({ ...data, id: editingId });
    } else {
        await createPlanningMutation.mutateAsync(data);
    }
    setIsDialogOpen(false);
  };

  const onInvalid = (errors: any) => {
      console.error("Errores:", errors);
      const firstError = Object.values(errors)[0] as any;
      toast.error("Formulario incompleto", { description: firstError?.message });
  };

  const getProgramName = (id: number) => {
      const prog = programs.find((p: any) => p.id === id);
      return prog ? prog.actividad : `ID: ${id}`;
  };

  // --- LÓGICA MULTI-SELECT ---
  // Convierte el string "A,B,C" en array ["A","B","C"]
  const currentAsistentes = form.watch("asistentes") ? form.watch("asistentes").split(",") : [];

  const toggleAsistente = (abreviatura: string) => {
      const current = [...currentAsistentes];
      if (current.includes(abreviatura)) {
          // Remover
          const filtered = current.filter(x => x !== abreviatura);
          form.setValue("asistentes", filtered.join(","));
      } else {
          // Agregar
          current.push(abreviatura);
          form.setValue("asistentes", current.join(","));
      }
  };
  // ---------------------------

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Ejecución de Capacitaciones</h1>
          <p className="text-slate-500">Registro de logística, instructor y asistentes.</p>
        </div>
        <Button onClick={handleCreate} className="bg-blue-600 hover:bg-blue-700">
          <Plus className="mr-2 h-4 w-4" /> Registrar Ejecución
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {isLoadingPlannings ? (
             <div className="col-span-3 text-center p-10 text-slate-500">Cargando datos...</div>
        ) : plannings.length === 0 ? (
            <div className="col-span-3 text-center p-10 border-2 border-dashed rounded-xl bg-slate-50 text-slate-500">
                No hay ejecuciones registradas.
            </div>
        ) : plannings.map((plan: any) => (
            <Card key={plan.id} className={`hover:shadow-md transition-shadow border-l-4 flex flex-col justify-between ${plan.competencia ? 'border-l-green-500' : 'border-l-amber-500'}`}>
                <CardHeader className="pb-2">
                    <CardTitle className="text-sm font-bold text-slate-500 uppercase tracking-wide">
                        ACTIVIDAD
                    </CardTitle>
                    <div className="text-lg font-bold text-slate-800 leading-snug mt-1">
                        {getProgramName(plan.item_del_programa)}
                    </div>
                    <CardDescription className="flex items-center gap-1 text-xs mt-1">
                         <CalendarIcon className="h-3 w-3" />
                         {plan.fecha_inicio ? format(new Date(plan.fecha_inicio), 'yyyy-MM-dd') : '-'}
                         <ArrowRight className="h-3 w-3" />
                         {plan.fecha_final ? format(new Date(plan.fecha_final), 'yyyy-MM-dd') : 'En curso'}
                    </CardDescription>
                </CardHeader>
                <CardContent className="text-sm space-y-3">
                    <div className="flex flex-col gap-1 text-xs text-slate-600 border-b pb-2">
                         <div className="flex items-center gap-1">
                            <Building2 className="h-3 w-3 text-blue-500" />
                            <span>Instructor: <b>{plan.responsable_de_generacion_de_competencia}</b></span>
                        </div>
                        <div className="flex items-center gap-1">
                            <User className="h-3 w-3" />
                            <span>Org. Interno: {plan.elaborado_por}</span>
                        </div>
                    </div>
                    
                    <div>
                        <div className="flex items-center gap-2 mb-1">
                            <Users className="h-4 w-4 text-slate-500" />
                            <span className="font-semibold text-slate-700">Asistentes ({plan.asistentes.split(',').length})</span>
                        </div>
                        <div className="flex flex-wrap gap-1">
                            {plan.asistentes.split(',').slice(0, 3).map((a: string) => (
                                <Badge key={a} variant="outline" className="text-[10px]">{a}</Badge>
                            ))}
                            {plan.asistentes.split(',').length > 3 && (
                                <Badge variant="outline" className="text-[10px]">+{plan.asistentes.split(',').length - 3}</Badge>
                            )}
                        </div>
                    </div>

                    {plan.competencia ? (
                        <div className="bg-green-100 text-green-800 text-xs px-2 py-1 rounded font-bold text-center">
                            COMPETENCIA ADQUIRIDA
                        </div>
                    ) : (
                        <div className="bg-amber-100 text-amber-800 text-xs px-2 py-1 rounded font-bold text-center">
                            PENDIENTE / NO ADQUIRIDA
                        </div>
                    )}
                </CardContent>
                <CardFooter className="flex justify-end gap-2 pt-2 border-t mt-2">
                    <Button variant="ghost" size="sm" onClick={() => handleEdit(plan)}>
                        <Pencil className="h-4 w-4 text-slate-500" />
                    </Button>
                    <Button variant="ghost" size="sm" onClick={() => setDeleteId(plan.id)}>
                        <Trash className="h-4 w-4 text-red-500" />
                    </Button>
                </CardFooter>
            </Card>
        ))}
      </div>

      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
        <DialogContent className="sm:max-w-[700px] max-h-[95vh] overflow-y-auto">
          <DialogHeader>
            <DialogTitle>{editingId ? "Editar Ejecución" : "Registrar Ejecución de Capacitación"}</DialogTitle>
          </DialogHeader>

          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit, onInvalid)} className="space-y-4">
                
                {/* 1. VINCULACIÓN AL PROGRAMA */}
                <FormField
                    control={form.control}
                    name="item_del_programa"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel className="text-blue-700 font-bold">Programa / Necesidad Vinculada</FormLabel>
                            <Select onValueChange={(val) => field.onChange(Number(val))} value={field.value?.toString()}>
                                <FormControl><SelectTrigger><SelectValue placeholder="Seleccione la actividad planificada..." /></SelectTrigger></FormControl>
                                <SelectContent>
                                    {programs?.map((prog: any) => (
                                        <SelectItem key={prog.id} value={prog.id.toString()}>
                                            {prog.actividad} ({prog.dirigido_a})
                                        </SelectItem>
                                    ))}
                                </SelectContent>
                            </Select>
                            <FormMessage />
                        </FormItem>
                    )}
                />

                <div className="grid grid-cols-2 gap-4">
                     <FormField
                        control={form.control}
                        name="fecha_inicio"
                        render={({ field }) => (
                            <FormItem className="flex flex-col">
                                <FormLabel>Fecha Inicio</FormLabel>
                                <Popover>
                                    <PopoverTrigger asChild>
                                        <FormControl>
                                            <div className="relative flex items-center w-full">
                                                <Input 
                                                    value={startDateValue}
                                                    onChange={(e) => {
                                                        const val = e.target.value;
                                                        setStartDateValue(val);
                                                        const date = parseISO(val);
                                                        if (isValid(date) && val.length === 10) field.onChange(date);
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
                                            initialFocus
                                        />
                                    </PopoverContent>
                                </Popover>
                                <FormMessage />
                            </FormItem>
                        )}
                    />

                    <FormField
                        control={form.control}
                        name="fecha_final"
                        render={({ field }) => (
                            <FormItem className="flex flex-col">
                                <FormLabel>Fecha Final (Opcional)</FormLabel>
                                <Popover>
                                    <PopoverTrigger asChild>
                                        <FormControl>
                                            <div className="relative flex items-center w-full">
                                                <Input 
                                                    value={endDateValue}
                                                    onChange={(e) => {
                                                        const val = e.target.value;
                                                        setEndDateValue(val);
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
                                            onSelect={field.onChange}
                                            initialFocus
                                        />
                                    </PopoverContent>
                                </Popover>
                            </FormItem>
                        )}
                    />
                </div>

                {/* RESPONSABLES */}
                <div className="grid grid-cols-2 gap-4">
                    <FormField
                        control={form.control}
                        name="responsable_de_generacion_de_competencia"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Instructor / Institución (Externo/Interno)</FormLabel>
                                <FormControl>
                                    <Input placeholder="Ej: Universidad Tecnica o Ing. Juan" {...field} value={field.value || ""} />
                                </FormControl>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                     <FormField
                        control={form.control}
                        name="elaborado_por"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Organizador Interno (Supervisor)</FormLabel>
                                <Select onValueChange={field.onChange} value={field.value}>
                                    <FormControl><SelectTrigger><SelectValue placeholder="Seleccione..." /></SelectTrigger></FormControl>
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

                {/* MULTI-SELECT DE ASISTENTES */}
                <FormField
                    control={form.control}
                    name="asistentes"
                    render={() => (
                        <FormItem>
                            <div className="mb-2">
                                <FormLabel>Seleccionar Asistentes</FormLabel>
                                <div className="text-xs text-slate-500">Marque a todos los empleados que participaron.</div>
                            </div>
                            <div className="border rounded-md h-40 overflow-y-auto p-3 space-y-2 bg-slate-50">
                                {personal?.map((p: any) => {
                                    const isSelected = currentAsistentes.includes(p.abreviatura);
                                    return (
                                        <div key={p.abreviatura} className="flex items-center space-x-2">
                                            <Checkbox 
                                                id={`chk-${p.abreviatura}`} 
                                                checked={isSelected}
                                                onCheckedChange={() => toggleAsistente(p.abreviatura)}
                                            />
                                            <label 
                                                htmlFor={`chk-${p.abreviatura}`}
                                                className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 cursor-pointer"
                                            >
                                                {p.nombre} <span className="text-xs text-slate-400">({p.cargo})</span>
                                            </label>
                                        </div>
                                    )
                                })}
                            </div>
                            <FormMessage />
                            {/* Resumen de seleccionados */}
                            <div className="flex flex-wrap gap-1 mt-2">
                                {currentAsistentes.filter(x => x).map(a => (
                                    <Badge key={a} variant="secondary" className="text-xs">{a}</Badge>
                                ))}
                            </div>
                        </FormItem>
                    )}
                />

                <FormField
                    control={form.control}
                    name="tematica"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Temática Específica (Detalle)</FormLabel>
                            <FormControl>
                                <Input placeholder="Detalle del contenido..." {...field} value={field.value || ""} />
                            </FormControl>
                        </FormItem>
                    )}
                />

                <div className="grid grid-cols-2 gap-4 items-center bg-slate-50 p-4 rounded border">
                    <FormField
                        control={form.control}
                        name="evaluacion_si_aplica"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Nota / Evaluación (Si aplica)</FormLabel>
                                <FormControl>
                                    <Input type="number" {...field} />
                                </FormControl>
                            </FormItem>
                        )}
                    />
                    
                    <FormField
                        control={form.control}
                        name="competencia"
                        render={({ field }) => (
                            <FormItem className="flex flex-row items-center space-x-3 space-y-0 mt-6">
                                <FormControl>
                                    <Checkbox checked={field.value} onCheckedChange={field.onChange} className="h-6 w-6" />
                                </FormControl>
                                <div className="space-y-1 leading-none">
                                    <FormLabel className="text-base font-bold text-green-700">Competencia Adquirida</FormLabel>
                                </div>
                            </FormItem>
                        )}
                    />
                </div>

                <FormField
                    control={form.control}
                    name="conclusion"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Conclusión / Comentarios</FormLabel>
                            <FormControl>
                                <Textarea {...field} value={field.value || ""} />
                            </FormControl>
                        </FormItem>
                    )}
                />

                <div className="flex justify-end pt-2">
                    <Button type="submit" className="bg-blue-600 hover:bg-blue-700 w-full md:w-auto">
                        <ClipboardCheck className="mr-2 h-4 w-4" /> Guardar Ejecución
                    </Button>
                </div>
            </form>
          </Form>
        </DialogContent>
      </Dialog>

      <AlertDialog open={!!deleteId} onOpenChange={() => setDeleteId(null)}>
        <AlertDialogContent>
            <AlertDialogTitle>¿Eliminar Ejecución?</AlertDialogTitle>
            <AlertDialogDescription>Se eliminará el registro de esta capacitación.</AlertDialogDescription>
            <AlertDialogFooter>
                <AlertDialogCancel>Cancelar</AlertDialogCancel>
                <AlertDialogAction className="bg-red-600" onClick={() => { if(deleteId) deletePlanningMutation.mutate(deleteId); setDeleteId(null); }}>
                    Eliminar
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
};