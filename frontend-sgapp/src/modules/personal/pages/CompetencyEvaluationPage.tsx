import { useState, useEffect } from "react";
import { useForm, useWatch } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { format, isValid, parseISO } from "date-fns";
import { es } from "date-fns/locale";
import { Plus, CalendarIcon, UserCheck, Trash, Pencil, Calculator, AlertTriangle, CheckCircle2 } from "lucide-react";

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
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Badge } from "@/components/ui/badge";
import {
    AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogTitle, AlertDialogDescription, AlertDialogFooter
} from "@/components/ui/alert-dialog";
import { Progress } from "@/components/ui/progress";

// Hooks
import { useEvaluacionCompetencias, evaluacionSchema, EvaluacionFormValues } from "../hooks/useEvaluacionCompetencias";
import { useCompetencias } from "../hooks/useCompetencias"; // Para leer Requisitos (RQ)
import { usePersonal } from "../hooks/usePersonal";
import { useCargos } from "../hooks/useCargos";

export const CompetencyEvaluationPage = () => {
  const { evaluaciones, isLoadingEvaluaciones, createEvaluacionMutation, updateEvaluacionMutation, deleteEvaluacionMutation } = useEvaluacionCompetencias();
  const { requirements } = useCompetencias(); // Traemos la matriz RQ
  const { data: personal } = usePersonal();
  const { cargos } = useCargos();

  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [deleteId, setDeleteId] = useState<number | null>(null);
  const [dateInputValue, setDateInputValue] = useState("");
  
  // Estado para guardar el Requisito (RQ) activo del empleado seleccionado
  const [activeReq, setActiveReq] = useState<any>(null);

  const form = useForm<EvaluacionFormValues>({
    resolver: zodResolver(evaluacionSchema),
    defaultValues: {
        promedio: 0,
        escala: 5,
        competencia_asegurada: false
    },
  });

  // --- LOGICA DE SELECCION DE PERSONAL ---
  // Cuando cambia el personal, buscamos su cargo y sus requisitos automáticamente
  const selectedPersonalId = useWatch({ control: form.control, name: "personal" });

  useEffect(() => {
    if (selectedPersonalId && personal && requirements) {
        const empleado = personal.find((p: any) => p.abreviatura === selectedPersonalId);
        if (empleado) {
            form.setValue("cargo", empleado.cargo); // Setear cargo FK
            
            // Buscar la matriz de requisitos (RQ) para ese cargo
            // Asumimos que tomamos la más reciente o vigente
            const reqEncontrado = requirements.find((r: any) => r.cargo_req === empleado.cargo && r.aprobado_vigente);
            
            if (reqEncontrado) {
                setActiveReq(reqEncontrado);
                form.setValue("requisitos", reqEncontrado.id);
            } else {
                setActiveReq(null); // No hay requisitos definidos para este cargo
            }
        }
    }
  }, [selectedPersonalId, personal, requirements, form]);

  // --- LOGICA DE CÁLCULO DE PROMEDIO EN VIVO ---
  // Observamos todos los campos numéricos (...n)
  const watchedValues = useWatch({ control: form.control });

  useEffect(() => {
    // Calculamos el promedio de todas las notas ingresadas (solo las que tienen valor > 0 o input)
    let totalPuntos = 0;
    let cantidadItems = 0;

    // Recorremos las claves del formulario para buscar las que terminan en 'n' (educacion1n, etc)
    Object.keys(watchedValues).forEach(key => {
        if (key.endsWith('n') && typeof watchedValues[key] === 'number') {
            const val = watchedValues[key] as number;
            // Solo contamos si el requisito existe en el activeReq para no promediar cosas vacías
            // O simplificamos: si tiene valor, lo contamos.
            if (val > 0) {
                totalPuntos += val;
                cantidadItems++;
            }
        }
    });

    const promedio = cantidadItems > 0 ? parseFloat((totalPuntos / cantidadItems).toFixed(2)) : 0;
    
    // No usamos setValue directo para evitar loop infinito, solo si cambia
    if (promedio !== form.getValues("promedio")) {
        form.setValue("promedio", promedio);
        // Si promedio es 5 (o mayor a 4.5 según criterio) marcamos competencia asegurada
        // Aquí dejo la lógica estricta: si promedio >= 4
        if (promedio >= 4) {
             // form.setValue("competencia_asegurada", true); // Opcional: auto-marcar
        }
    }
  }, [watchedValues]);

  // Sincronizar fecha manual
  useEffect(() => {
    const currentDate = form.getValues("fecha");
    if (currentDate) {
        setDateInputValue(format(currentDate, "yyyy-MM-dd"));
    } else {
        setDateInputValue("");
    }
  }, [form.watch("fecha"), isDialogOpen]);

const handleCreate = () => {
      setEditingId(null);
      setActiveReq(null);
      
      // Inicializamos TODO explícitamente para evitar "uncontrolled input" warnings
      form.reset({
        fecha: new Date(),
        promedio: 0, escala: 5, competencia_asegurada: false,
        personal: "", responsable: "", cargo: "", conclusion: "",
        // Nota: Los campos dinámicos se inician como undefined, Zod los manejará
      });
      setIsDialogOpen(true);
  };

const handleEdit = (item: any) => {
      setEditingId(item.id);
      
      // Recuperar el requisito activo visualmente
      if (requirements) {
          const req = requirements.find((r: any) => r.id === item.requisitos);
          setActiveReq(req || null);
      }

      const cleanData: any = { ...item };
      
      // 1. Arreglar Fecha
      if (cleanData.fecha) cleanData.fecha = new Date(cleanData.fecha);
      
      // 2. Limpieza agresiva de NULOS
      Object.keys(cleanData).forEach(key => {
          if (cleanData[key] === null) {
              if (key.startsWith('cumple_') || key === 'competencia_asegurada') cleanData[key] = false;
              else if (key.endsWith('n') || key === 'promedio' || key === 'escala') cleanData[key] = 0;
              else cleanData[key] = ""; // Strings nulos a vacío
          }
      });

      form.reset(cleanData);
      setIsDialogOpen(true);
  };

  // Función para ver errores en consola si no guarda
  const onInvalid = (errors: any) => {
      console.error("Errores de validación:", errors);
      // Opcional: Mostrar un toast
      // toast.error("Hay campos incompletos o inválidos. Revise el formulario.");
  };
  

  const onSubmit = async (data: EvaluacionFormValues) => {
    if (editingId) {
        await updateEvaluacionMutation.mutateAsync({ ...data, id: editingId });
    } else {
        await createEvaluacionMutation.mutateAsync(data);
    }
    setIsDialogOpen(false);
  };

  // --- HELPER PARA RENDERIZAR FILAS DE EVALUACION ---
  // Muestra: Texto del Requisito (RQ) | Input Evidencia (SE) | Input Nota (SE) | Check (SE)
  const renderEvalRow = (prefix: string, index: number, label: string) => {
      // Campos del Requisito (Read only)
      const reqText = activeReq ? activeReq[`${prefix}${index}`] : null;
      const reqCritico = activeReq ? activeReq[`${prefix}${index}c`] : false;

      // Si no hay requisito definido en la matriz para este item, no mostramos nada para no ensuciar
      if (!reqText && !editingId) return null; 
      // Nota: En edición mostramos si hay dato guardado aunque el requisito haya cambiado, por seguridad.

      // Nombres de campos en Evaluación (Write)
      const evName = `ev_${prefix}${index}`;
      const cumpleName = `cumple_${prefix}${index}`;
      const notaName = `${prefix}${index}n`;

      return (
        <div className="grid grid-cols-12 gap-3 items-start mb-4 border-b pb-4 last:border-0">
            {/* COLUMNA 1: LO QUE PIDE EL CARGO (RQ) */}
            <div className="col-span-4 pr-2 border-r border-slate-100">
                <div className="text-xs font-bold text-slate-500 uppercase mb-1">{label} {index}</div>
                <div className="text-sm text-slate-800 font-medium">
                    {reqText || <span className="text-slate-300 italic">(Sin requisito definido)</span>}
                </div>
                {reqCritico && (
                    <Badge variant="destructive" className="mt-1 text-[10px] h-5">Crítico</Badge>
                )}
            </div>

            {/* COLUMNA 2: LA EVALUACIÓN (SE) */}
            <div className="col-span-8 grid grid-cols-12 gap-2">
                {/* Evidencia */}
                <div className="col-span-7">
                    <FormField
                        control={form.control}
                        // @ts-ignore
                        name={evName}
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel className="text-[10px] text-slate-400">Evidencia / Observación</FormLabel>
                                <FormControl>
                                    <Textarea 
                                        placeholder="Ej: Certificado adjunto..." 
                                        className="h-14 resize-none text-xs" 
                                        {...field} 
                                        value={field.value || ""} 
                                    />
                                </FormControl>
                            </FormItem>
                        )}
                    />
                </div>
                
                {/* Nota */}
                <div className="col-span-3">
                    <FormField
                        control={form.control}
                        // @ts-ignore
                        name={notaName}
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel className="text-[10px] text-slate-400">Nota (1-5)</FormLabel>
                                <FormControl>
                                    <Input 
                                        type="number" 
                                        min={0} 
                                        max={5} 
                                        className="text-center font-bold" 
                                        {...field} 
                                        onChange={e => field.onChange(parseFloat(e.target.value))}
                                    />
                                </FormControl>
                            </FormItem>
                        )}
                    />
                </div>

                {/* Cumple */}
                <div className="col-span-2 flex flex-col justify-center items-center pt-4">
                    <FormField
                        control={form.control}
                        // @ts-ignore
                        name={cumpleName}
                        render={({ field }) => (
                            <FormItem className="flex flex-col items-center space-y-1">
                                <FormControl>
                                    <Checkbox checked={field.value} onCheckedChange={field.onChange} />
                                </FormControl>
                                <FormLabel className="text-[10px] font-normal text-slate-500">Cumple</FormLabel>
                            </FormItem>
                        )}
                    />
                </div>
            </div>
        </div>
      );
  };

  const renderGroup = (prefix: string, count: number, labelBase: string) => {
      const rows = [];
      for (let i = 1; i <= count; i++) {
          const row = renderEvalRow(prefix, i, labelBase);
          if (row) rows.push(<div key={i}>{row}</div>);
      }
      if (rows.length === 0) return <div className="text-center py-4 text-slate-400 text-sm italic">No hay requisitos definidos en esta categoría para este cargo.</div>;
      return <div className="p-4 bg-white rounded-md border">{rows}</div>;
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Evaluación de Competencias</h1>
          <p className="text-slate-500">Medición del personal frente a los requisitos del cargo.</p>
        </div>
        <Button onClick={handleCreate} className="bg-blue-600 hover:bg-blue-700">
          <Plus className="mr-2 h-4 w-4" /> Nueva Evaluación
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {isLoadingEvaluaciones ? (
             <div className="col-span-3 text-center p-10 text-slate-500">Cargando evaluaciones...</div>
        ) : evaluaciones.length === 0 ? (
            <div className="col-span-3 text-center p-10 border-2 border-dashed rounded-xl bg-slate-50 text-slate-500">
                No hay evaluaciones registradas.
            </div>
        ) : evaluaciones.map((ev: any) => (
            <Card key={ev.id} className="hover:shadow-md transition-shadow border-l-4 border-l-purple-600">
                <CardHeader className="pb-2">
                    <div className="flex justify-between items-start">
                        <CardTitle className="text-lg font-bold text-slate-800 truncate">
                            {personal?.find((p:any) => p.abreviatura === ev.personal)?.nombre || ev.personal}
                        </CardTitle>
                        <Badge variant={ev.competencia_asegurada ? "default" : "destructive"} className={ev.competencia_asegurada ? "bg-green-600" : ""}>
                            {ev.promedio} / 5
                        </Badge>
                    </div>
                    <CardDescription>
                         {cargos?.find((c:any) => c.abreviacion === ev.cargo)?.cargo || ev.cargo}
                    </CardDescription>
                </CardHeader>
                <CardContent className="text-sm text-slate-600 pb-2">
                    <div className="flex items-center gap-2 mb-2">
                        <CalendarIcon className="h-4 w-4 text-slate-400" />
                        {ev.fecha ? format(new Date(ev.fecha), 'yyyy-MM-dd') : '-'}
                    </div>
                    <div className="flex items-center gap-2">
                         <UserCheck className="h-4 w-4 text-slate-400" />
                         Evaluador: {ev.responsable}
                    </div>
                    
                    {/* Barra de progreso visual */}
                    <div className="mt-4">
                        <div className="flex justify-between text-xs mb-1">
                            <span>Nivel de Competencia</span>
                            <span>{((ev.promedio / 5) * 100).toFixed(0)}%</span>
                        </div>
                        <Progress value={(ev.promedio / 5) * 100} className={`h-2 ${ev.promedio < 4 ? 'bg-red-100' : 'bg-slate-100'}`} />
                    </div>
                </CardContent>
                <CardFooter className="flex justify-end gap-2 pt-2">
                    <Button variant="ghost" size="sm" onClick={() => handleEdit(ev)}>
                        <Pencil className="h-4 w-4 text-slate-500" />
                    </Button>
                    <Button variant="ghost" size="sm" onClick={() => setDeleteId(ev.id)}>
                        <Trash className="h-4 w-4 text-red-500" />
                    </Button>
                </CardFooter>
            </Card>
        ))}
      </div>

      {/* MODAL DE EVALUACIÓN */}
      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
        <DialogContent className="sm:max-w-[950px] max-h-[95vh] overflow-y-auto bg-slate-50">
          <DialogHeader>
            <DialogTitle>Ficha de Evaluación de Competencias</DialogTitle>
          </DialogHeader>

          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit, onInvalid)} className="space-y-4">
                
                {/* 1. SELECCIÓN DE PERSONAL */}
                <div className="bg-white p-4 rounded-lg border shadow-sm grid grid-cols-1 md:grid-cols-3 gap-4">
                     <FormField
                        control={form.control}
                        name="personal"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Personal a Evaluar</FormLabel>
                                <Select onValueChange={field.onChange} value={field.value} disabled={!!editingId}>
                                    <FormControl><SelectTrigger><SelectValue placeholder="Seleccione..." /></SelectTrigger></FormControl>
                                    <SelectContent>
                                        {personal?.map((p: any) => (
                                            <SelectItem key={p.abreviatura} value={p.abreviatura}>{p.nombre}</SelectItem>
                                        ))}
                                    </SelectContent>
                                </Select>
                            </FormItem>
                        )}
                    />
                    
                    {/* INFO AUTOMÁTICA DEL CARGO */}
                    <div className="space-y-2">
                        {/* Usamos label normal de HTML con las clases de shadcn para que se vea igual */}
                        <label className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                            Cargo Detectado
                        </label>
                        <div className="h-10 px-3 py-2 rounded-md border bg-slate-100 text-sm font-medium text-slate-700 truncate flex items-center">
                            {cargos?.find((c: any) => c.abreviacion === form.watch("cargo"))?.cargo || form.watch("cargo") || "---"}
                        </div>
                    </div>

                    <FormField
                        control={form.control}
                        name="responsable"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Responsable Evaluación</FormLabel>
                                <Select onValueChange={field.onChange} value={field.value}>
                                    <FormControl><SelectTrigger><SelectValue placeholder="Seleccione..." /></SelectTrigger></FormControl>
                                    <SelectContent>
                                        {personal?.map((p: any) => (
                                            <SelectItem key={p.abreviatura} value={p.abreviatura}>{p.nombre}</SelectItem>
                                        ))}
                                    </SelectContent>
                                </Select>
                            </FormItem>
                        )}
                    />

                    {/* FECHA MANUAL */}
                    <FormField
                        control={form.control}
                        name="fecha"
                        render={({ field }) => (
                            <FormItem className="flex flex-col">
                                <FormLabel>Fecha Evaluación</FormLabel>
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
                                            disabled={(date) => date > new Date()}
                                            initialFocus
                                        />
                                    </PopoverContent>
                                </Popover>
                            </FormItem>
                        )}
                    />

                    {/* ALERTA SI NO HAY RQ */}
                    {!activeReq && form.watch("personal") && (
                        <div className="col-span-2 flex items-center gap-2 text-amber-600 bg-amber-50 p-2 rounded border border-amber-200 text-xs">
                            <AlertTriangle className="h-4 w-4" />
                            <span>Atención: Este cargo no tiene una Matriz de Requisitos vigente definida.</span>
                        </div>
                    )}
                </div>

                {/* 2. MATRIZ DE EVALUACIÓN */}
                {activeReq && (
                    <Tabs defaultValue="educacion" className="w-full">
                         <TabsList className="grid w-full grid-cols-6 h-auto bg-white border">
                            <TabsTrigger value="educacion" className="text-xs py-2">Educación</TabsTrigger>
                            <TabsTrigger value="formacion" className="text-xs py-2">Formación</TabsTrigger>
                            <TabsTrigger value="experiencia" className="text-xs py-2">Experiencia</TabsTrigger>
                            <TabsTrigger value="habilidades" className="text-xs py-2">Habilidades</TabsTrigger>
                            <TabsTrigger value="conocimiento" className="text-xs py-2">Conocim.</TabsTrigger>
                            <TabsTrigger value="calificacion" className="text-xs py-2">Calific.</TabsTrigger>
                        </TabsList>

                        <div className="mt-4 max-h-[400px] overflow-y-auto pr-2">
                            <TabsContent value="educacion">{renderGroup('educacion', 3, 'Educación')}</TabsContent>
                            <TabsContent value="formacion">{renderGroup('formacion', 10, 'Formación')}</TabsContent>
                            <TabsContent value="experiencia">{renderGroup('experiencia', 5, 'Experiencia')}</TabsContent>
                            <TabsContent value="habilidades">{renderGroup('habilidades', 10, 'Habilidad')}</TabsContent>
                            <TabsContent value="conocimiento">{renderGroup('conocimiento', 10, 'Conocimiento')}</TabsContent>
                            <TabsContent value="calificacion">{renderGroup('calificacion', 5, 'Calificación')}</TabsContent>
                        </div>
                    </Tabs>
                )}

                {/* 3. RESULTADOS Y CONCLUSIONES */}
                <div className="bg-slate-900 text-slate-100 p-4 rounded-lg grid grid-cols-12 gap-4 items-center">
                    <div className="col-span-4 text-center border-r border-slate-700">
                        <div className="text-xs uppercase text-slate-400">Promedio General</div>
                        <div className={`text-4xl font-bold font-mono ${form.watch("promedio") < 4 ? "text-red-400" : "text-green-400"}`}>
                            {form.watch("promedio").toFixed(2)}
                        </div>
                        <div className="text-xs text-slate-500">Escala: 5</div>
                    </div>
                    
                    <div className="col-span-8 space-y-3 pl-2">
                         <FormField
                            control={form.control}
                            name="competencia_asegurada"
                            render={({ field }) => (
                                <FormItem className="flex flex-row items-center space-x-2 space-y-0 bg-slate-800 p-2 rounded border border-slate-700">
                                    <FormControl>
                                        <Checkbox 
                                            checked={field.value} 
                                            onCheckedChange={field.onChange} 
                                            className="data-[state=checked]:bg-green-500 border-slate-500"
                                        />
                                    </FormControl>
                                    <FormLabel className="text-sm font-bold text-white cursor-pointer">
                                        COMPETENCIA ASEGURADA
                                    </FormLabel>
                                </FormItem>
                            )}
                        />
                         <FormField
                            control={form.control}
                            name="conclusion"
                            render={({ field }) => (
                                <FormItem>
                                    <FormControl>
                                        <Input placeholder="Conclusión final de la evaluación..." {...field} className="bg-slate-800 border-slate-700 text-white placeholder:text-slate-500" />
                                    </FormControl>
                                </FormItem>
                            )}
                        />
                    </div>
                </div>

                <div className="flex justify-end pt-2">
                    <Button type="submit" className="bg-blue-600 hover:bg-blue-700 w-full md:w-auto">
                        Guardar Evaluación
                    </Button>
                </div>
            </form>
          </Form>
        </DialogContent>
      </Dialog>

      {/* ALERT DIALOG DELETE */}
      <AlertDialog open={!!deleteId} onOpenChange={() => setDeleteId(null)}>
        <AlertDialogContent>
            <AlertDialogTitle>¿Eliminar Evaluación?</AlertDialogTitle>
            <AlertDialogDescription>Se perderán los registros de calificación de este empleado.</AlertDialogDescription>
            <AlertDialogFooter>
                <AlertDialogCancel>Cancelar</AlertDialogCancel>
                <AlertDialogAction className="bg-red-600" onClick={() => { if(deleteId) deleteEvaluacionMutation.mutate(deleteId); setDeleteId(null); }}>
                    Eliminar
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
};
