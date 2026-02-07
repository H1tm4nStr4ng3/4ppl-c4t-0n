import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { format, isValid, parseISO } from "date-fns";
import { es } from "date-fns/locale";
import { Plus, Users, CalendarIcon, ChevronRight, Settings2, Pencil, Trash } from "lucide-react";
import { useNavigate } from "react-router-dom";

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
  Form, FormControl, FormField, FormItem, FormLabel, FormMessage, FormDescription
} from "@/components/ui/form";
import {
    Select, SelectContent, SelectItem, SelectTrigger, SelectValue,
} from "@/components/ui/select";
import {
    Popover, PopoverContent, PopoverTrigger,
} from "@/components/ui/popover";
import { Calendar } from "@/components/ui/calendar";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Separator } from "@/components/ui/separator";
import {
    AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogTitle, AlertDialogDescription, AlertDialogFooter
} from "@/components/ui/alert-dialog";

// Hooks
import { useSelection, procesoSchema, ProcesoFormValues } from "../hooks/useSelection";
import { useCargos } from "../hooks/useCargos";
import { usePersonal } from "../hooks/usePersonal";

export const SelectionPage = () => {
  const navigate = useNavigate();
  const { 
    procesos, 
    isLoadingProcesos, 
    createProcesoMutation, 
    updateProcesoMutation, 
    deleteProcesoMutation 
  } = useSelection();
  
  const { cargos } = useCargos();
  const { data: personal } = usePersonal();

  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [deleteId, setDeleteId] = useState<number | null>(null);
  
  // Estado para input manual de fecha
  const [dateInputValue, setDateInputValue] = useState("");

  const form = useForm<ProcesoFormValues>({
    resolver: zodResolver(procesoSchema),
    defaultValues: {
      puesto: "",
      evaluadores: "",
      ponderacion_educacion: 20,
      ponderacion_formacion: 20,
      ponderacion_experiencia: 30,
      ponderacion_habilidades: 15,
      ponderacion_conocimientotecnico: 15,
      ponderacion_minima_cv: 51,
      item_entrevista_1: "Presentación Personal",
      ponderacion_entrevista_1: 20,
      item_entrevista_2: "Comunicación Efectiva",
      ponderacion_entrevista_2: 20,
      item_entrevista_3: "Trabajo en Equipo",
      ponderacion_entrevista_3: 20,
      item_entrevista_4: "Resolución de Problemas",
      ponderacion_entrevista_4: 20,
      item_entrevista_5: "Adaptabilidad",
      ponderacion_entrevista_5: 20,
      ponderacion_minima_entrevista: 51
    },
  });

  // Sincronizar fecha manual
  useEffect(() => {
    const currentDate = form.getValues("fecha_inicial");
    if (currentDate) {
        setDateInputValue(format(currentDate, "yyyy-MM-dd"));
    } else {
        setDateInputValue("");
    }
  }, [form.watch("fecha_inicial"), isDialogOpen]);

  const handleCreate = () => {
      setEditingId(null);
      form.reset({
        puesto: "", evaluadores: "",
        ponderacion_educacion: 20, ponderacion_formacion: 20, ponderacion_experiencia: 30, ponderacion_habilidades: 15, ponderacion_conocimientotecnico: 15, ponderacion_minima_cv: 51,
        item_entrevista_1: "Presentación", ponderacion_entrevista_1: 20, item_entrevista_2: "Comunicación", ponderacion_entrevista_2: 20, item_entrevista_3: "Trabajo Equipo", ponderacion_entrevista_3: 20, item_entrevista_4: "Resolución", ponderacion_entrevista_4: 20, item_entrevista_5: "Adaptabilidad", ponderacion_entrevista_5: 20, ponderacion_minima_entrevista: 51
      });
      setIsDialogOpen(true);
  };

  const handleEdit = (proc: any) => {
      setEditingId(proc.id);
      
      // Sanitizamos los datos para evitar errores de "controlled vs uncontrolled" inputs
      form.reset({
          puesto: proc.puesto || "", // Si es null, pon string vacío
          evaluadores: proc.evaluadores || "",
          fecha_inicial: new Date(proc.fecha_inicial),
          fecha_final: proc.fecha_final ? new Date(proc.fecha_final) : null,
          
          // Ponderaciones (asegurar números)
          ponderacion_educacion: proc.ponderacion_educacion ?? 0,
          ponderacion_formacion: proc.ponderacion_formacion ?? 0,
          ponderacion_experiencia: proc.ponderacion_experiencia ?? 0,
          ponderacion_habilidades: proc.ponderacion_habilidades ?? 0,
          ponderacion_conocimientotecnico: proc.ponderacion_conocimientotecnico ?? 0,
          ponderacion_minima_cv: proc.ponderacion_minima_cv ?? 51,
          
          conclusion_cv: proc.conclusion_cv || "",

          // Entrevista
          item_entrevista_1: proc.item_entrevista_1 || "",
          ponderacion_entrevista_1: proc.ponderacion_entrevista_1 ?? 0,
          
          item_entrevista_2: proc.item_entrevista_2 || "",
          ponderacion_entrevista_2: proc.ponderacion_entrevista_2 ?? 0,
          
          item_entrevista_3: proc.item_entrevista_3 || "",
          ponderacion_entrevista_3: proc.ponderacion_entrevista_3 ?? 0,
          
          item_entrevista_4: proc.item_entrevista_4 || "",
          ponderacion_entrevista_4: proc.ponderacion_entrevista_4 ?? 0,
          
          item_entrevista_5: proc.item_entrevista_5 || "",
          ponderacion_entrevista_5: proc.ponderacion_entrevista_5 ?? 0,
          
          ponderacion_minima_entrevista: proc.ponderacion_minima_entrevista ?? 51,
          conclusion_entrevista: proc.conclusion_entrevista || ""
      });
      setIsDialogOpen(true);
  };
  
  const onSubmit = async (data: ProcesoFormValues) => {
    if (editingId) {
        await updateProcesoMutation.mutateAsync({ ...data, id: editingId });
    } else {
        await createProcesoMutation.mutateAsync(data);
    }
    setIsDialogOpen(false);
  };

  // Helper para inputs de %
  const renderWeightInput = (name: any, label: string) => (
    <FormField
        control={form.control}
        name={name}
        render={({ field }) => (
            <FormItem>
                <FormLabel className="text-xs">{label}</FormLabel>
                <FormControl>
                    <div className="relative">
                        <Input type="number" {...field} className="pr-6 text-right" />
                        <span className="absolute right-2 top-2 text-xs text-slate-400">%</span>
                    </div>
                </FormControl>
            </FormItem>
        )}
    />
  );

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Selección de Personal</h1>
          <p className="text-slate-500">Gestión de vacantes, ponderaciones y evaluaciones.</p>
        </div>
        <Button onClick={handleCreate} className="bg-blue-600 hover:bg-blue-700">
          <Plus className="mr-2 h-4 w-4" /> Nuevo Proceso
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {isLoadingProcesos ? (
            <div className="col-span-3 text-center p-10 text-slate-500">Cargando procesos...</div>
        ) : procesos.length === 0 ? (
            <div className="col-span-3 text-center p-10 border-2 border-dashed rounded-xl bg-slate-50 text-slate-500">
                No hay procesos de selección activos. Inicie uno nuevo.
            </div>
        ) : procesos.map((proc: any) => (
            <Card key={proc.id} className="hover:shadow-md transition-shadow border-l-4 border-l-blue-600 flex flex-col justify-between">
                <CardHeader className="pb-2">
                    <div className="flex justify-between items-start">
                        <CardTitle className="text-lg font-bold text-slate-800">
                             {cargos?.find((c: any) => c.abreviacion === proc.puesto)?.cargo || proc.puesto}
                        </CardTitle>
                        <div className="flex gap-1">
                            <Button variant="ghost" size="sm" className="h-6 w-6 p-0" onClick={() => handleEdit(proc)}>
                                <Pencil className="h-3 w-3 text-slate-500" />
                            </Button>
                            <Button variant="ghost" size="sm" className="h-6 w-6 p-0" onClick={() => setDeleteId(proc.id)}>
                                <Trash className="h-3 w-3 text-red-500" />
                            </Button>
                        </div>
                    </div>
                    <CardDescription className="flex items-center gap-1">
                        <CalendarIcon className="h-3 w-3" />
                        Inicio: {proc.fecha_inicial ? format(new Date(proc.fecha_inicial), 'yyyy-MM-dd') : '-'}
                    </CardDescription>
                </CardHeader>
                <CardContent>
                    <div className="space-y-3 text-sm">
                        <div className="flex items-center gap-2 text-slate-600">
                            <Users className="h-4 w-4" />
                            <span className="truncate">
                                Resp: {personal?.find((p:any) => p.abreviatura === proc.evaluadores)?.nombre || proc.evaluadores}
                            </span>
                        </div>
                        <Separator />
                        <div className="grid grid-cols-2 gap-2 text-xs text-slate-500">
                            <div>Min CV: <span className="font-bold text-slate-700">{proc.ponderacion_minima_cv}</span></div>
                            <div>Min Ent: <span className="font-bold text-slate-700">{proc.ponderacion_minima_entrevista}</span></div>
                        </div>
                    </div>
                </CardContent>
                <CardFooter>
                    <Button 
                        className="w-full" 
                        variant="outline"
                        onClick={() => navigate(`/personal/seleccion/${proc.id}`)}
                    >
                        Gestionar Postulantes <ChevronRight className="ml-2 h-4 w-4" />
                    </Button>
                </CardFooter>
            </Card>
        ))}
      </div>

      {/* DIALOGO DE EDICIÓN / CREACIÓN */}
      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
        <DialogContent className="sm:max-w-[700px] max-h-[90vh] overflow-y-auto">
          <DialogHeader>
            <DialogTitle>{editingId ? "Editar Proceso" : "Nuevo Proceso de Selección"}</DialogTitle>
          </DialogHeader>
          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                <Tabs defaultValue="general" className="w-full">
                    <TabsList className="grid w-full grid-cols-3">
                        <TabsTrigger value="general">1. General</TabsTrigger>
                        <TabsTrigger value="cv">2. Ponderación CV</TabsTrigger>
                        <TabsTrigger value="entrevista">3. Entrevista</TabsTrigger>
                    </TabsList>

                    <TabsContent value="general" className="space-y-4 py-4">
                        <div className="grid grid-cols-2 gap-4">
                            <FormField
                                control={form.control}
                                name="puesto"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>Puesto Vacante</FormLabel>
                                        <Select onValueChange={field.onChange} value={field.value}>
                                            <FormControl><SelectTrigger><SelectValue placeholder="Seleccione cargo..." /></SelectTrigger></FormControl>
                                            <SelectContent>
                                                {cargos?.map((c: any) => (
                                                    <SelectItem key={c.abreviacion} value={c.abreviacion}>{c.cargo}</SelectItem>
                                                ))}
                                            </SelectContent>
                                        </Select>
                                        <FormMessage />
                                    </FormItem>
                                )}
                            />
                            <FormField
                                control={form.control}
                                name="evaluadores"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>Responsable</FormLabel>
                                        <Select onValueChange={field.onChange} value={field.value}>
                                            <FormControl><SelectTrigger><SelectValue placeholder="Seleccione personal..." /></SelectTrigger></FormControl>
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
                        
                        {/* FECHA ARREGLADA: INPUT MANUAL + CALENDARIO */}
                        <FormField
                            control={form.control}
                            name="fecha_inicial"
                            render={({ field }) => (
                                <FormItem className="flex flex-col">
                                    <FormLabel>Fecha de Inicio</FormLabel>
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
                        
                        <FormField
                            control={form.control}
                            name="conclusion_cv"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Descripción / Observaciones</FormLabel>
                                    <FormControl><Textarea placeholder="Detalles sobre el perfil..." {...field} value={field.value || ""} /></FormControl>
                                </FormItem>
                            )}
                        />
                    </TabsContent>

                    <TabsContent value="cv" className="space-y-4 py-4">
                        <div className="grid grid-cols-3 gap-4">
                            {renderWeightInput("ponderacion_educacion", "Educación")}
                            {renderWeightInput("ponderacion_formacion", "Formación")}
                            {renderWeightInput("ponderacion_experiencia", "Experiencia")}
                            {renderWeightInput("ponderacion_habilidades", "Habilidades")}
                            {renderWeightInput("ponderacion_conocimientotecnico", "Conoc. Técnico")}
                        </div>
                        <Separator className="my-4" />
                        <div className="grid grid-cols-2 gap-4">
                            <FormField
                                control={form.control}
                                name="ponderacion_minima_cv"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel className="font-bold text-blue-700">Nota Mínima CV</FormLabel>
                                        <FormControl><Input type="number" {...field} /></FormControl>
                                    </FormItem>
                                )}
                            />
                        </div>
                    </TabsContent>

                    <TabsContent value="entrevista" className="space-y-4 py-4">
                         {[1, 2, 3, 4, 5].map((num) => (
                            <div key={num} className="grid grid-cols-12 gap-4 items-end">
                                <div className="col-span-8">
                                    <FormField
                                        control={form.control}
                                        // @ts-ignore
                                        name={`item_entrevista_${num}`}
                                        render={({ field }) => (
                                            <FormItem>
                                                <FormLabel className="text-xs">Criterio {num}</FormLabel>
                                                <FormControl><Input placeholder={`Ej: Liderazgo`} {...field} value={field.value || ""} /></FormControl>
                                            </FormItem>
                                        )}
                                    />
                                </div>
                                <div className="col-span-4">
                                    {/* @ts-ignore */}
                                    {renderWeightInput(`ponderacion_entrevista_${num}`, "Peso")}
                                </div>
                            </div>
                        ))}
                        <Separator className="my-4" />
                        <FormField
                            control={form.control}
                            name="ponderacion_minima_entrevista"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel className="font-bold text-green-700">Nota Mínima Entrevista</FormLabel>
                                    <FormControl><Input type="number" {...field} /></FormControl>
                                </FormItem>
                            )}
                        />
                    </TabsContent>
                </Tabs>

                <div className="flex justify-end pt-4">
                    <Button type="submit" className="bg-blue-600 hover:bg-blue-700">
                        <Settings2 className="mr-2 h-4 w-4" /> {editingId ? "Guardar Cambios" : "Crear Proceso"}
                    </Button>
                </div>
            </form>
          </Form>
        </DialogContent>
      </Dialog>
      
      {/* ALERTA DE BORRADO */}
      <AlertDialog open={!!deleteId} onOpenChange={() => setDeleteId(null)}>
        <AlertDialogContent>
            <AlertDialogTitle>¿Eliminar Proceso?</AlertDialogTitle>
            <AlertDialogDescription>
                Esta acción eliminará el proceso y <b>todos los postulantes</b> asociados. No se puede deshacer.
            </AlertDialogDescription>
            <AlertDialogFooter>
                <AlertDialogCancel>Cancelar</AlertDialogCancel>
                <AlertDialogAction className="bg-red-600" onClick={() => { if(deleteId) deleteProcesoMutation.mutate(deleteId); setDeleteId(null); }}>
                    Eliminar
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
};