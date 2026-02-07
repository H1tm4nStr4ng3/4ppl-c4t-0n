import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { format, isValid, parseISO } from "date-fns";
import { es } from "date-fns/locale";
import { Plus, CalendarIcon, Users, Trash, Pencil, CheckCircle, XCircle, Award, ArrowRight } from "lucide-react";
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
import { useEffectiveness, effectivenessSchema, EffectivenessFormValues } from "../hooks/useEffectiveness";
import { usePlanning } from "../hooks/usePlanning"; // Fase 4
import { usePrograms } from "../hooks/usePrograms"; // Fase 3 (para nombres)

export const EffectivenessPage = () => {
  const { effectiveness, isLoadingEffectiveness, createEffectivenessMutation, updateEffectivenessMutation, deleteEffectivenessMutation } = useEffectiveness();
  const { plannings } = usePlanning();
  const { programs } = usePrograms();

  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [deleteId, setDeleteId] = useState<number | null>(null);
  const [dateInputValue, setDateInputValue] = useState("");

  const form = useForm<EffectivenessFormValues>({
    resolver: zodResolver(effectivenessSchema),
    defaultValues: {
      id_plan: 0,
      fecha: new Date(),
      comentarios_observaciones: "",
      actividad_evaluacion: "",
      conclusion_eficacia: "",
      eficaz: false,
      cerrado: false,
      // Los participantes se llenan dinámicamente
    },
  });

  // Sincronizar fecha manual
  useEffect(() => {
    const currentDate = form.getValues("fecha");
    if (currentDate) {
        setDateInputValue(format(currentDate, "yyyy-MM-dd"));
    } else {
        setDateInputValue("");
    }
  }, [form.watch("fecha"), isDialogOpen]);

  // --- LÓGICA AUTOMÁTICA DE PARTICIPANTES ---
  // Cuando seleccionamos un Plan (Fase 4), buscamos sus asistentes y llenamos los campos participante_1...10
  const selectedPlanId = form.watch("id_plan");

  useEffect(() => {
    if (selectedPlanId && plannings) {
        const plan = plannings.find((p: any) => p.id === selectedPlanId);
        if (plan && plan.asistentes) {
            const listaAsistentes = plan.asistentes.split(",");
            // Llenar hasta 10 participantes
            listaAsistentes.forEach((nombre: string, index: number) => {
                if (index < 10) {
                    // @ts-ignore
                    form.setValue(`participante_${index + 1}`, nombre.trim());
                }
            });
            // Limpiar los restantes si hay menos de 10
            for (let i = listaAsistentes.length + 1; i <= 10; i++) {
                // @ts-ignore
                form.setValue(`participante_${i}`, "");
            }
        }
    }
  }, [selectedPlanId, plannings, form]);
  // -------------------------------------------

  const handleCreate = () => {
      setEditingId(null);
      form.reset({
        id_plan: undefined,
        fecha: new Date(),
        comentarios_observaciones: "",
        actividad_evaluacion: "",
        conclusion_eficacia: "",
        eficaz: false,
        cerrado: false
      });
      setIsDialogOpen(true);
  };

  const handleEdit = (item: any) => {
      setEditingId(item.id);
      
      const cleanData: any = { ...item };
      
      if (cleanData.fecha) cleanData.fecha = new Date(cleanData.fecha);
      
      // Limpieza de Nulos
      Object.keys(cleanData).forEach(key => {
          if (cleanData[key] === null) {
              if (key === 'eficaz' || key === 'cerrado') cleanData[key] = false;
              else cleanData[key] = "";
          }
      });
      
      form.reset(cleanData);
      setIsDialogOpen(true);
  };

  const onSubmit = async (data: EffectivenessFormValues) => {
    if (editingId) {
        await updateEffectivenessMutation.mutateAsync({ ...data, id: editingId });
    } else {
        await createEffectivenessMutation.mutateAsync(data);
    }
    setIsDialogOpen(false);
  };

  const onInvalid = (errors: any) => {
      console.error("Errores:", errors);
      toast.error("Formulario incompleto. Seleccione una capacitación.");
  };

  // Helper para mostrar nombres bonitos en la tarjeta
  const getPlanDetails = (planId: number) => {
      const plan = plannings.find((p: any) => p.id === planId);
      if (!plan) return { nombre: `Plan ID: ${planId}`, asistentes: [] };
      
      const prog = programs.find((pr: any) => pr.id === plan.item_del_programa);
      return {
          nombre: prog ? prog.actividad : "Actividad desconocida",
          asistentes: plan.asistentes ? plan.asistentes.split(",") : []
      };
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Eficacia de la Formación</h1>
          <p className="text-slate-500">Evaluación posterior y cierre de brechas.</p>
        </div>
        <Button onClick={handleCreate} className="bg-blue-600 hover:bg-blue-700">
          <Plus className="mr-2 h-4 w-4" /> Evaluar Eficacia
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {isLoadingEffectiveness ? (
             <div className="col-span-3 text-center p-10 text-slate-500">Cargando datos...</div>
        ) : effectiveness.length === 0 ? (
            <div className="col-span-3 text-center p-10 border-2 border-dashed rounded-xl bg-slate-50 text-slate-500">
                No hay evaluaciones de eficacia registradas.
            </div>
        ) : effectiveness.map((item: any) => {
            const detalles = getPlanDetails(item.id_plan);
            return (
                <Card key={item.id} className={`hover:shadow-md transition-shadow border-t-4 flex flex-col justify-between ${item.eficaz ? 'border-t-green-500' : 'border-t-red-500'}`}>
                    <CardHeader className="pb-2">
                        <div className="flex justify-between items-start">
                            <CardTitle className="text-lg font-bold text-slate-800 leading-snug">
                                {detalles.nombre}
                            </CardTitle>
                            {item.cerrado && <Badge variant="secondary">CERRADO</Badge>}
                        </div>
                        <CardDescription className="flex items-center gap-1 text-xs">
                            <CalendarIcon className="h-3 w-3" />
                            Evaluado: {item.fecha ? format(new Date(item.fecha), 'yyyy-MM-dd') : '-'}
                        </CardDescription>
                    </CardHeader>
                    <CardContent className="text-sm space-y-3">
                        <div className="bg-slate-50 p-2 rounded border">
                            <div className="text-xs text-slate-500 font-bold mb-1">PARTICIPANTES EVALUADOS</div>
                            <div className="flex flex-wrap gap-1">
                                {detalles.asistentes.map((a: string) => (
                                    <Badge key={a} variant="outline" className="text-[10px] bg-white">{a}</Badge>
                                ))}
                            </div>
                        </div>
                        
                        <div className="flex items-center gap-2 justify-center p-2 rounded bg-slate-100">
                            {item.eficaz ? (
                                <div className="flex items-center gap-2 text-green-700 font-bold">
                                    <CheckCircle className="h-5 w-5" /> EFICAZ
                                </div>
                            ) : (
                                <div className="flex items-center gap-2 text-red-700 font-bold">
                                    <XCircle className="h-5 w-5" /> NO EFICAZ
                                </div>
                            )}
                        </div>
                        {item.conclusion_eficacia && (
                             <div className="text-xs italic text-slate-600">"{item.conclusion_eficacia}"</div>
                        )}
                    </CardContent>
                    <CardFooter className="flex justify-end gap-2 pt-2 border-t mt-2">
                        <Button variant="ghost" size="sm" onClick={() => handleEdit(item)}>
                            <Pencil className="h-4 w-4 text-slate-500" />
                        </Button>
                        <Button variant="ghost" size="sm" onClick={() => setDeleteId(item.id)}>
                            <Trash className="h-4 w-4 text-red-500" />
                        </Button>
                    </CardFooter>
                </Card>
            );
        })}
      </div>

      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
        <DialogContent className="sm:max-w-[650px] max-h-[95vh] overflow-y-auto">
          <DialogHeader>
            <DialogTitle>{editingId ? "Editar Evaluación" : "Registrar Eficacia"}</DialogTitle>
          </DialogHeader>

          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit, onInvalid)} className="space-y-4">
                
                {/* 1. SELECCIÓN DE CAPACITACIÓN EJECUTADA */}
                <FormField
                    control={form.control}
                    name="id_plan"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel className="font-bold text-blue-700">Capacitación Ejecutada (Fase 4)</FormLabel>
                            <Select onValueChange={(val) => field.onChange(Number(val))} value={field.value?.toString()} disabled={!!editingId}>
                                <FormControl><SelectTrigger><SelectValue placeholder="Seleccione la capacitación a cerrar..." /></SelectTrigger></FormControl>
                                <SelectContent>
                                    {plannings?.map((plan: any) => {
                                        const prog = programs.find((p:any) => p.id === plan.item_del_programa);
                                        return (
                                            <SelectItem key={plan.id} value={plan.id.toString()}>
                                                {prog ? prog.actividad : `Plan ${plan.id}`} - {plan.fecha_inicio ? format(new Date(plan.fecha_inicio), 'yyyy-MM-dd') : ''}
                                            </SelectItem>
                                        )
                                    })}
                                </SelectContent>
                            </Select>
                            <FormMessage />
                        </FormItem>
                    )}
                />

                {/* 2. LISTA DE ASISTENTES (READ ONLY, SE LLENA SOLO) */}
                <div className="bg-slate-50 p-3 rounded border space-y-2">
                    {/* CORRECCIÓN: Usamos label nativo con clases de estilo, no FormLabel */}
                    <label className="text-xs text-slate-500 uppercase font-bold block">
                        Participantes a Evaluar
                    </label>
                    
                    <div className="flex flex-wrap gap-2">
                         {[1,2,3,4,5,6,7,8,9,10].map(i => {
                             // @ts-ignore
                             const nombre = form.watch(`participante_${i}`);
                             if (!nombre) return null;
                             return <Badge key={i} variant="secondary" className="bg-white border-slate-300">{nombre}</Badge>
                         })}
                         {/* Mensaje si no hay plan seleccionado */}
                         {!form.watch("id_plan") && <span className="text-xs text-slate-400 italic">Seleccione una capacitación arriba...</span>}
                    </div>
                </div>

                {/* 3. FECHA DE EVALUACIÓN */}
                <FormField
                    control={form.control}
                    name="fecha"
                    render={({ field }) => (
                        <FormItem className="flex flex-col">
                            <FormLabel>Fecha de Evaluación (Posterior)</FormLabel>
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
                    name="actividad_evaluacion"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Método de Verificación</FormLabel>
                            <FormControl>
                                <Input placeholder="Ej: Evaluación de desempeño a los 3 meses, Examen..." {...field} value={field.value || ""} />
                            </FormControl>
                        </FormItem>
                    )}
                />

                <FormField
                    control={form.control}
                    name="comentarios_observaciones"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Comentarios y Observaciones</FormLabel>
                            <FormControl>
                                <Textarea placeholder="Detalle si se observaron mejoras en la competencia..." {...field} value={field.value || ""} />
                            </FormControl>
                        </FormItem>
                    )}
                />

                <div className="grid grid-cols-2 gap-4 p-4 border rounded-lg bg-slate-50">
                    <FormField
                        control={form.control}
                        name="eficaz"
                        render={({ field }) => (
                            <FormItem className="flex flex-row items-center space-x-3 space-y-0">
                                <FormControl>
                                    <Checkbox checked={field.value} onCheckedChange={field.onChange} className="h-5 w-5 data-[state=checked]:bg-green-600" />
                                </FormControl>
                                <div className="space-y-1 leading-none">
                                    <FormLabel className="font-bold text-green-800">¿Fue Eficaz?</FormLabel>
                                </div>
                            </FormItem>
                        )}
                    />
                    
                    <FormField
                        control={form.control}
                        name="cerrado"
                        render={({ field }) => (
                            <FormItem className="flex flex-row items-center space-x-3 space-y-0">
                                <FormControl>
                                    <Checkbox checked={field.value} onCheckedChange={field.onChange} className="h-5 w-5" />
                                </FormControl>
                                <div className="space-y-1 leading-none">
                                    <FormLabel className="font-bold text-slate-800">Cerrar Ciclo</FormLabel>
                                </div>
                            </FormItem>
                        )}
                    />
                </div>
                
                <FormField
                    control={form.control}
                    name="conclusion_eficacia"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Conclusión Final</FormLabel>
                            <FormControl>
                                <Input {...field} value={field.value || ""} />
                            </FormControl>
                        </FormItem>
                    )}
                />

                <div className="flex justify-end pt-2">
                    <Button type="submit" className="bg-blue-600 hover:bg-blue-700 w-full md:w-auto">
                        <Award className="mr-2 h-4 w-4" /> Registrar Eficacia
                    </Button>
                </div>
            </form>
          </Form>
        </DialogContent>
      </Dialog>

      <AlertDialog open={!!deleteId} onOpenChange={() => setDeleteId(null)}>
        <AlertDialogContent>
            <AlertDialogTitle>¿Eliminar Registro?</AlertDialogTitle>
            <AlertDialogDescription>Se eliminará la evaluación de eficacia.</AlertDialogDescription>
            <AlertDialogFooter>
                <AlertDialogCancel>Cancelar</AlertDialogCancel>
                <AlertDialogAction className="bg-red-600" onClick={() => { if(deleteId) deleteEffectivenessMutation.mutate(deleteId); setDeleteId(null); }}>
                    Eliminar
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
};
