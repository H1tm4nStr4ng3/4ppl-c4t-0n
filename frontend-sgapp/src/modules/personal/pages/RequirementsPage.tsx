import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { format, isValid, parseISO } from "date-fns";
import { es } from "date-fns/locale";
import { Plus, CalendarIcon, Briefcase, Trash, Pencil, ShieldAlert } from "lucide-react";

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
import { Badge } from "@/components/ui/badge";
import {
    AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogTitle, AlertDialogDescription, AlertDialogFooter
} from "@/components/ui/alert-dialog";

// Hooks
import { useCompetencias, requirementsSchema, RequirementsFormValues } from "../hooks/useCompetencias";
import { useCargos } from "../hooks/useCargos";
import { usePersonal } from "../hooks/usePersonal";

export const RequirementsPage = () => {
  const { requirements, isLoadingRequirements, createRequirementMutation, updateRequirementMutation, deleteRequirementMutation } = useCompetencias();
  const { cargos } = useCargos();
  const { data: personal } = usePersonal();

  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [deleteId, setDeleteId] = useState<number | null>(null);
  const [dateInputValue, setDateInputValue] = useState("");

  // Inicializamos el formulario con TODOS los campos posibles
  const form = useForm<RequirementsFormValues>({
    resolver: zodResolver(requirementsSchema),
    defaultValues: {
        cargo_req: "", responsable: "", aprobado_vigente: true, comentarios: "",
        // Defaults para evitar errores de uncontrolled inputs
        educacion1c: false, educacion2c: false, educacion3c: false,
        formacion1c: false, formacion2c: false, formacion3c: false, formacion4c: false, formacion5c: false, formacion6c: false, formacion7c: false, formacion8c: false, formacion9c: false, formacion10c: false,
        experiencia1c: false, experiencia2c: false, experiencia3c: false, experiencia4c: false, experiencia5c: false,
        habilidades1c: false, habilidades2c: false, habilidades3c: false, habilidades4c: false, habilidades5c: false, habilidades6c: false, habilidades7c: false, habilidades8c: false, habilidades9c: false, habilidades10c: false,
        conocimiento1c: false, conocimiento2c: false, conocimiento3c: false, conocimiento4c: false, conocimiento5c: false, conocimiento6c: false, conocimiento7c: false, conocimiento8c: false, conocimiento9c: false, conocimiento10c: false,
        calificacion1c: false, calificacion2c: false, calificacion3c: false, calificacion4c: false, calificacion5c: false,
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

  const handleCreate = () => {
      setEditingId(null);
      form.reset({
        cargo_req: "", responsable: "", aprobado_vigente: true, comentarios: "",
        fecha: new Date(), // Fecha hoy por defecto
      });
      setIsDialogOpen(true);
  };

  const handleEdit = (item: any) => {
      setEditingId(item.id);
      // Rellenamos el form asegurando que los nulos sean strings vacíos
      const cleanData: any = { ...item };
      
      // Convertir fecha string a objeto Date
      if (cleanData.fecha) cleanData.fecha = new Date(cleanData.fecha);

      // Limpieza rápida de nulos para los campos dinámicos
      Object.keys(requirementsSchema.shape).forEach(key => {
          if (cleanData[key] === null || cleanData[key] === undefined) {
              if (key.endsWith('c')) cleanData[key] = false; // boleanos
              else if (key !== 'fecha' && key !== 'id') cleanData[key] = ""; // textos
          }
      });

      form.reset(cleanData);
      setIsDialogOpen(true);
  };

  const onSubmit = async (data: RequirementsFormValues) => {
    if (editingId) {
        await updateRequirementMutation.mutateAsync({ ...data, id: editingId });
    } else {
        await createRequirementMutation.mutateAsync(data);
    }
    setIsDialogOpen(false);
  };

  // --- HELPER PARA RENDERIZAR FILAS (Input Texto + Checkbox Crítico) ---
  const renderRow = (prefix: string, index: number, label: string) => {
      const textName = `${prefix}${index}`;
      const boolName = `${prefix}${index}c`;

      return (
        <div className="grid grid-cols-12 gap-3 items-center mb-3">
            <div className="col-span-9">
                <FormField
                    control={form.control}
                    // @ts-ignore
                    name={textName}
                    render={({ field }) => (
                        <FormItem>
                            <FormControl>
                                <Input placeholder={`${label} ${index}`} {...field} value={field.value || ""} />
                            </FormControl>
                        </FormItem>
                    )}
                />
            </div>
            <div className="col-span-3">
                 <FormField
                    control={form.control}
                    // @ts-ignore
                    name={boolName}
                    render={({ field }) => (
                        <FormItem className="flex flex-row items-center space-x-2 space-y-0 mt-2">
                            <FormControl>
                                <Checkbox checked={field.value} onCheckedChange={field.onChange} />
                            </FormControl>
                            <FormLabel className="text-xs font-normal text-red-600">
                                Crítico
                            </FormLabel>
                        </FormItem>
                    )}
                />
            </div>
        </div>
      );
  };

  // Helper para generar grupos de filas
  const renderGroup = (prefix: string, count: number, labelBase: string) => {
      const rows = [];
      for (let i = 1; i <= count; i++) {
          rows.push(<div key={i}>{renderRow(prefix, i, labelBase)}</div>);
      }
      return <div className="p-4 bg-slate-50 rounded-md border">{rows}</div>;
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Matriz de Competencias</h1>
          <p className="text-slate-500">Definición de requisitos críticos y competencias por cargo.</p>
        </div>
        <Button onClick={handleCreate} className="bg-blue-600 hover:bg-blue-700">
          <Plus className="mr-2 h-4 w-4" /> Definir Requisitos
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {isLoadingRequirements ? (
            <div className="col-span-3 text-center p-10 text-slate-500">Cargando matriz...</div>
        ) : requirements.length === 0 ? (
            <div className="col-span-3 text-center p-10 border-2 border-dashed rounded-xl bg-slate-50 text-slate-500">
                No hay requisitos definidos. Comience agregando uno para un cargo.
            </div>
        ) : requirements.map((req: any) => (
            <Card key={req.id} className="hover:shadow-md transition-shadow border-t-4 border-t-blue-600">
                <CardHeader>
                    <CardTitle className="flex justify-between items-start">
                        <span className="text-lg font-bold">
                             {cargos?.find((c: any) => c.abreviacion === req.cargo_req)?.cargo || req.cargo_req}
                        </span>
                        {req.aprobado_vigente ? (
                            <Badge className="bg-green-100 text-green-700 hover:bg-green-200">Vigente</Badge>
                        ) : (
                            <Badge variant="destructive">Obsoleto</Badge>
                        )}
                    </CardTitle>
                    <CardDescription>
                        Actualizado: {req.fecha ? format(new Date(req.fecha), 'yyyy-MM-dd') : '-'}
                    </CardDescription>
                </CardHeader>
                <CardContent className="text-sm text-slate-600 space-y-2">
                    <div className="flex gap-2">
                        <Briefcase className="h-4 w-4" />
                        Responsable: {personal?.find((p:any) => p.abreviatura === req.responsable)?.nombre || req.responsable}
                    </div>
                    {req.comentarios && (
                        <div className="italic bg-slate-50 p-2 rounded text-xs border">
                            "{req.comentarios}"
                        </div>
                    )}
                </CardContent>
                <CardFooter className="flex justify-end gap-2">
                    <Button variant="outline" size="sm" onClick={() => handleEdit(req)}>
                        <Pencil className="mr-2 h-3 w-3" /> Editar
                    </Button>
                    <Button variant="ghost" size="sm" className="text-red-500 hover:bg-red-50" onClick={() => setDeleteId(req.id)}>
                        <Trash className="h-4 w-4" />
                    </Button>
                </CardFooter>
            </Card>
        ))}
      </div>

      {/* MODAL GIGANTE DE REQUISITOS */}
      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
        <DialogContent className="sm:max-w-[900px] max-h-[95vh] overflow-y-auto">
          <DialogHeader>
            <DialogTitle>{editingId ? "Editar Matriz de Cargo" : "Nueva Matriz de Requisitos"}</DialogTitle>
          </DialogHeader>
          
          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                
                {/* CABECERA COMÚN */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4 bg-slate-50 p-4 rounded-lg border">
                    <FormField
                        control={form.control}
                        name="cargo_req"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Cargo</FormLabel>
                                <Select onValueChange={field.onChange} value={field.value}>
                                    <FormControl><SelectTrigger><SelectValue placeholder="Seleccione..." /></SelectTrigger></FormControl>
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
                        name="responsable"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Responsable Definición</FormLabel>
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
                     {/* FECHA MANUAL ISO */}
                     <FormField
                        control={form.control}
                        name="fecha"
                        render={({ field }) => (
                            <FormItem className="flex flex-col">
                                <FormLabel>Fecha Vigencia</FormLabel>
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
                                                    className="pl-10 w-full font-mono bg-white"
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
                                            disabled={(date) => date < new Date("1900-01-01")}
                                            initialFocus
                                        />
                                    </PopoverContent>
                                </Popover>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                </div>

                <div className="flex items-center space-x-2">
                    <FormField
                        control={form.control}
                        name="aprobado_vigente"
                        render={({ field }) => (
                            <FormItem className="flex flex-row items-center space-x-2 space-y-0">
                                <FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl>
                                <FormLabel>Documento Aprobado y Vigente</FormLabel>
                            </FormItem>
                        )}
                    />
                </div>

                {/* TABS PARA LAS CATEGORÍAS */}
                {/* TABS PARA LAS CATEGORÍAS (ACTUALIZADO CON CALIFICACIÓN) */}
                <Tabs defaultValue="educacion" className="w-full">
                    {/* Ajustamos grid-cols-6 para que quepan las 6 pestañas */}
                    <TabsList className="grid w-full grid-cols-3 lg:grid-cols-6 h-auto">
                        <TabsTrigger value="educacion" className="text-xs py-2">Educación</TabsTrigger>
                        <TabsTrigger value="formacion" className="text-xs py-2">Formación</TabsTrigger>
                        <TabsTrigger value="experiencia" className="text-xs py-2">Experiencia</TabsTrigger>
                        <TabsTrigger value="habilidades" className="text-xs py-2">Habilidades</TabsTrigger>
                        <TabsTrigger value="conocimiento" className="text-xs py-2">Conocim.</TabsTrigger>
                        <TabsTrigger value="calificacion" className="text-xs py-2">Calific.</TabsTrigger>
                    </TabsList>

                    <TabsContent value="educacion" className="mt-4">
                        <p className="text-sm text-slate-500 mb-2">Títulos académicos requeridos.</p>
                        {renderGroup('educacion', 3, 'Título / Grado')}
                    </TabsContent>

                    <TabsContent value="formacion" className="mt-4">
                        <p className="text-sm text-slate-500 mb-2">Cursos, talleres y capacitaciones específicas.</p>
                        {renderGroup('formacion', 10, 'Curso / Taller')}
                    </TabsContent>

                    <TabsContent value="experiencia" className="mt-4">
                        <p className="text-sm text-slate-500 mb-2">Años y tipo de experiencia previa.</p>
                        {renderGroup('experiencia', 5, 'Experiencia Requerida')}
                    </TabsContent>

                    <TabsContent value="habilidades" className="mt-4">
                        <p className="text-sm text-slate-500 mb-2">Competencias blandas y operativas.</p>
                        {renderGroup('habilidades', 10, 'Habilidad')}
                    </TabsContent>

                    <TabsContent value="conocimiento" className="mt-4">
                        <p className="text-sm text-slate-500 mb-2">Conocimientos técnicos específicos (Normas, Software, etc.).</p>
                        {renderGroup('conocimiento', 10, 'Conocimiento')}
                    </TabsContent>

                    {/* NUEVA PESTAÑA AGREGADA */}
                    <TabsContent value="calificacion" className="mt-4">
                        <p className="text-sm text-slate-500 mb-2">Criterios de calificación de desempeño o métricas específicas.</p>
                        {renderGroup('calificacion', 5, 'Criterio de Calificación')}
                    </TabsContent>
                </Tabs>
                <FormField
                    control={form.control}
                    name="comentarios"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Observaciones Generales</FormLabel>
                            <FormControl><Textarea {...field} /></FormControl>
                        </FormItem>
                    )}
                />

                <div className="flex justify-end pt-4">
                    <Button type="submit" className="bg-blue-600 hover:bg-blue-700 w-full md:w-auto">
                        {editingId ? "Guardar Cambios" : "Guardar Matriz de Requisitos"}
                    </Button>
                </div>
            </form>
          </Form>
        </DialogContent>
      </Dialog>
      
      {/* ALERTA DE BORRADO */}
      <AlertDialog open={!!deleteId} onOpenChange={() => setDeleteId(null)}>
        <AlertDialogContent>
            <AlertDialogTitle>¿Eliminar Matriz?</AlertDialogTitle>
            <AlertDialogDescription>Esta acción es irreversible.</AlertDialogDescription>
            <AlertDialogFooter>
                <AlertDialogCancel>Cancelar</AlertDialogCancel>
                <AlertDialogAction className="bg-red-600" onClick={() => { if(deleteId) deleteRequirementMutation.mutate(deleteId); setDeleteId(null); }}>
                    Eliminar
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
};
