import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { useForm, useWatch } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { ArrowLeft, Plus, Pencil, Trash, Save, Calculator, CheckCircle2, XCircle } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Checkbox } from "@/components/ui/checkbox";
import { Badge } from "@/components/ui/badge";
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "@/components/ui/table";
import {
  Dialog, DialogContent, DialogHeader, DialogTitle,
} from "@/components/ui/dialog";
import {
  Form, FormControl, FormField, FormItem, FormLabel, FormMessage, FormDescription
} from "@/components/ui/form";
import {
    AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogTitle, AlertDialogDescription, AlertDialogFooter
} from "@/components/ui/alert-dialog";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Separator } from "@/components/ui/separator";

// Hooks
import { useSelection, postulanteSchema, PostulanteFormValues } from "../hooks/useSelection";

export const SelectionDetailPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const processId = Number(id);

  // Usamos el hook pasando el ID del proceso para filtrar postulantes
  const { 
    procesos, // Para obtener la info del padre (Ponderaciones)
    postulantes, 
    isLoadingPostulantes, 
    createPostulanteMutation, 
    updatePostulanteMutation, 
    deletePostulanteMutation 
  } = useSelection(processId);

  // Buscamos el proceso actual para leer sus reglas
  const currentProcess = procesos.find((p: any) => p.id === processId);

  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [deleteId, setDeleteId] = useState<number | null>(null);

  const form = useForm<PostulanteFormValues>({
    resolver: zodResolver(postulanteSchema),
    defaultValues: {
      proceso_de_seleccion: processId,
      postulante: "",
      educacion: 0, formacion: 0, experiencia: 0, habilidades: 0, conocimientotecnico: 0,
      pasa_a_entrevista: false,
      item_entrevista1: 0, item_entrevista2: 0, item_entrevista3: 0, item_entrevista4: 0, item_entrevista5: 0,
      seleccionado: false
    },
  });

  // --- LÓGICA DE CALCULADORA EN TIEMPO REAL ---
  // Observamos los valores del formulario
  const watchedValues = useWatch({ control: form.control });

  useEffect(() => {
    if (!currentProcess) return;

    // 1. Calcular Resultado CV
    // Fórmula: (Nota / 100) * Peso
    // Asumimos que las notas ingresadas son sobre 100
    const calcCV = 
      (watchedValues.educacion || 0) * (currentProcess.ponderacion_educacion / 100) +
      (watchedValues.formacion || 0) * (currentProcess.ponderacion_formacion / 100) +
      (watchedValues.experiencia || 0) * (currentProcess.ponderacion_experiencia / 100) +
      (watchedValues.habilidades || 0) * (currentProcess.ponderacion_habilidades / 100) +
      (watchedValues.conocimientotecnico || 0) * (currentProcess.ponderacion_conocimientotecnico / 100);
    
    // 2. Calcular Resultado Entrevista
    const calcEntrevista = 
      (watchedValues.item_entrevista1 || 0) * (currentProcess.ponderacion_entrevista_1 / 100) +
      (watchedValues.item_entrevista2 || 0) * (currentProcess.ponderacion_entrevista_2 / 100) +
      (watchedValues.item_entrevista3 || 0) * (currentProcess.ponderacion_entrevista_3 / 100) +
      (watchedValues.item_entrevista4 || 0) * (currentProcess.ponderacion_entrevista_4 / 100) +
      (watchedValues.item_entrevista5 || 0) * (currentProcess.ponderacion_entrevista_5 / 100);

    // Actualizamos valores internos visuales o para enviar (opcional, el backend lo podría recalcular, pero mejor aquí)
    // Nota: No seteamos el valor en el input directamente para no causar re-renders infinitos, 
    // pero lo usaremos en el submit.
  }, [watchedValues, currentProcess]);

  // Función para mostrar el cálculo visualmente en el modal
  const getCurrentCalculatedCV = () => {
    if (!currentProcess) return 0;
    const val = 
      (form.getValues("educacion") || 0) * (currentProcess.ponderacion_educacion / 100) +
      (form.getValues("formacion") || 0) * (currentProcess.ponderacion_formacion / 100) +
      (form.getValues("experiencia") || 0) * (currentProcess.ponderacion_experiencia / 100) +
      (form.getValues("habilidades") || 0) * (currentProcess.ponderacion_habilidades / 100) +
      (form.getValues("conocimientotecnico") || 0) * (currentProcess.ponderacion_conocimientotecnico / 100);
    return val.toFixed(2);
  };

  const getCurrentCalculatedEntrevista = () => {
    if (!currentProcess) return 0;
    const val = 
      (form.getValues("item_entrevista1") || 0) * (currentProcess.ponderacion_entrevista_1 / 100) +
      (form.getValues("item_entrevista2") || 0) * (currentProcess.ponderacion_entrevista_2 / 100) +
      (form.getValues("item_entrevista3") || 0) * (currentProcess.ponderacion_entrevista_3 / 100) +
      (form.getValues("item_entrevista4") || 0) * (currentProcess.ponderacion_entrevista_4 / 100) +
      (form.getValues("item_entrevista5") || 0) * (currentProcess.ponderacion_entrevista_5 / 100);
    return val.toFixed(2);
  };

  const handleCreate = () => {
    setEditingId(null);
    form.reset({
      proceso_de_seleccion: processId,
      postulante: "",
      educacion: 0, formacion: 0, experiencia: 0, habilidades: 0, conocimientotecnico: 0,
      pasa_a_entrevista: false,
      item_entrevista1: 0, item_entrevista2: 0, item_entrevista3: 0, item_entrevista4: 0, item_entrevista5: 0,
      seleccionado: false
    });
    setIsDialogOpen(true);
  };

  const handleEdit = (postulante: any) => {
    setEditingId(postulante.id);
    form.reset(postulante);
    setIsDialogOpen(true);
  };

  const onSubmit = async (data: PostulanteFormValues) => {
    // Inyectamos los cálculos finales antes de enviar
    const finalData = {
        ...data,
        resultado_cv: parseFloat(getCurrentCalculatedCV() as string),
        resultado_entrevista: parseFloat(getCurrentCalculatedEntrevista() as string),
        // La calificación final podría ser un promedio simple o ponderado de ambos, 
        // aquí usaremos la suma o lo que tú definas. Por ahora guardo el de entrevista como calificacion principal.
        calificacion: parseFloat(getCurrentCalculatedEntrevista() as string)
    };

    if (editingId) {
        await updatePostulanteMutation.mutateAsync({ ...finalData, id: editingId });
    } else {
        await createPostulanteMutation.mutateAsync(finalData);
    }
    setIsDialogOpen(false);
  };

  if (!currentProcess) return <div className="p-10 text-center">Cargando proceso...</div>;

  return (
    <div className="space-y-6 animate-in fade-in">
      {/* Header */}
      <div className="flex items-center gap-4 border-b pb-4">
        <Button variant="ghost" size="icon" onClick={() => navigate('/personal/seleccion')}>
            <ArrowLeft className="h-5 w-5" />
        </Button>
        <div>
            <h1 className="text-xl font-bold text-slate-800">Evaluación de Postulantes</h1>
            <p className="text-sm text-slate-500">
                Proceso: <span className="font-semibold text-blue-600">{currentProcess.puesto}</span> | 
                ID: {currentProcess.id}
            </p>
        </div>
      </div>

      <div className="flex justify-between items-center bg-slate-50 p-4 rounded-lg border">
        <div className="text-sm space-y-1">
            <div className="text-slate-500">Nota Mínima CV: <b>{currentProcess.ponderacion_minima_cv}</b></div>
            <div className="text-slate-500">Nota Mínima Selección: <b>{currentProcess.ponderacion_minima_entrevista}</b></div>
        </div>
        <Button onClick={handleCreate} className="bg-blue-600">
            <Plus className="mr-2 h-4 w-4" /> Registrar Postulante
        </Button>
      </div>

      {/* Tabla de Postulantes */}
      <div className="border rounded-lg bg-white overflow-hidden shadow-sm">
        <Table>
            <TableHeader>
                <TableRow className="bg-slate-100">
                    <TableHead>Postulante</TableHead>
                    <TableHead className="text-center">Nota CV</TableHead>
                    <TableHead className="text-center">Estado CV</TableHead>
                    <TableHead className="text-center">Entrevista</TableHead>
                    <TableHead className="text-center">Resultado Final</TableHead>
                    <TableHead className="text-right">Acciones</TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                {postulantes.length === 0 ? (
                    <TableRow><TableCell colSpan={6} className="text-center h-24 text-slate-400">No hay postulantes registrados.</TableCell></TableRow>
                ) : postulantes.map((post: any) => (
                    <TableRow key={post.id}>
                        <TableCell className="font-medium">{post.postulante}</TableCell>
                        
                        {/* Nota CV */}
                        <TableCell className="text-center">
                            <Badge variant="outline" className="font-mono">
                                {post.resultado_cv?.toFixed(2)}
                            </Badge>
                        </TableCell>
                        
                        {/* Pasa a Entrevista? */}
                        <TableCell className="text-center">
                            {post.pasa_a_entrevista ? (
                                <Badge className="bg-blue-100 text-blue-700 hover:bg-blue-200">Aprobado</Badge>
                            ) : (
                                <span className="text-xs text-slate-400">No apto</span>
                            )}
                        </TableCell>

                        {/* Nota Entrevista */}
                        <TableCell className="text-center">
                            {post.pasa_a_entrevista ? (
                                <Badge variant="outline" className="font-mono border-blue-200 bg-blue-50">
                                    {post.resultado_entrevista?.toFixed(2)}
                                </Badge>
                            ) : '-'}
                        </TableCell>

                        {/* Seleccionado? */}
                        <TableCell className="text-center">
                            {post.seleccionado ? (
                                <div className="flex items-center justify-center gap-1 text-green-600 font-bold text-sm">
                                    <CheckCircle2 className="h-4 w-4" /> SELECCIONADO
                                </div>
                            ) : (
                                <span className="text-slate-400">-</span>
                            )}
                        </TableCell>

                        <TableCell className="text-right space-x-1">
                            <Button variant="ghost" size="sm" onClick={() => handleEdit(post)}>
                                <Pencil className="h-4 w-4 text-slate-500" />
                            </Button>
                            <Button variant="ghost" size="sm" onClick={() => setDeleteId(post.id)}>
                                <Trash className="h-4 w-4 text-red-500" />
                            </Button>
                        </TableCell>
                    </TableRow>
                ))}
            </TableBody>
        </Table>
      </div>

      {/* MODAL DE EVALUACIÓN (CALCULADORA) */}
      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
        <DialogContent className="sm:max-w-[800px] max-h-[90vh] overflow-y-auto">
            <DialogHeader>
                <DialogTitle>Ficha de Evaluación: {form.watch("postulante") || "Nuevo Candidato"}</DialogTitle>
            </DialogHeader>
            <Form {...form}>
                <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                    <FormField
                        control={form.control}
                        name="postulante"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Nombre Completo del Postulante</FormLabel>
                                <FormControl><Input placeholder="Ej: Juan Perez" {...field} /></FormControl>
                            </FormItem>
                        )}
                    />

                    <Tabs defaultValue="cv" className="w-full">
                        <TabsList className="grid w-full grid-cols-2">
                            <TabsTrigger value="cv">1. Evaluación Curricular</TabsTrigger>
                            <TabsTrigger value="entrevista" disabled={!form.watch("pasa_a_entrevista")}>2. Entrevista Técnica</TabsTrigger>
                        </TabsList>

                        {/* FASE 1: CV */}
                        <TabsContent value="cv" className="space-y-4 py-4">
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                                {/* Inputs de Notas */}
                                <div className="space-y-3">
                                    <h4 className="font-semibold text-sm text-slate-600 mb-2">Calificación (0 - 100)</h4>
                                    {[
                                        { field: "educacion", label: "Educación", weight: currentProcess.ponderacion_educacion },
                                        { field: "formacion", label: "Formación", weight: currentProcess.ponderacion_formacion },
                                        { field: "experiencia", label: "Experiencia", weight: currentProcess.ponderacion_experiencia },
                                        { field: "habilidades", label: "Habilidades", weight: currentProcess.ponderacion_habilidades },
                                        { field: "conocimientotecnico", label: "Conoc. Técnico", weight: currentProcess.ponderacion_conocimientotecnico },
                                    ].map((item: any) => (
                                        <FormField
                                            key={item.field}
                                            control={form.control}
                                            name={item.field}
                                            render={({ field }) => (
                                                <FormItem className="grid grid-cols-12 gap-2 items-center space-y-0">
                                                    <FormLabel className="col-span-5 text-xs font-normal">
                                                        {item.label} <span className="text-slate-400">({item.weight}%)</span>
                                                    </FormLabel>
                                                    <FormControl className="col-span-4">
                                                        <Input type="number" {...field} min={0} max={100} className="h-8" />
                                                    </FormControl>
                                                    <div className="col-span-3 text-xs text-right text-slate-500 font-mono">
                                                        = {((field.value || 0) * (item.weight/100)).toFixed(1)} pts
                                                    </div>
                                                </FormItem>
                                            )}
                                        />
                                    ))}
                                </div>

                                {/* Resumen Fase 1 */}
                                <div className="bg-slate-50 p-6 rounded-lg border flex flex-col justify-between">
                                    <div>
                                        <h3 className="text-lg font-bold text-slate-800">Resultado CV</h3>
                                        <div className="text-4xl font-mono font-bold text-blue-600 mt-2">
                                            {getCurrentCalculatedCV()} <span className="text-base text-slate-400 font-normal">/ 100</span>
                                        </div>
                                        <Separator className="my-4" />
                                        <div className="text-sm">
                                            Mínimo requerido: <b>{currentProcess.ponderacion_minima_cv}</b>
                                        </div>
                                    </div>

                                    <FormField
                                        control={form.control}
                                        name="pasa_a_entrevista"
                                        render={({ field }) => (
                                            <FormItem className="flex flex-row items-start space-x-3 space-y-0 rounded-md border p-4 bg-white shadow-sm mt-4">
                                                <FormControl>
                                                    <Checkbox checked={field.value} onCheckedChange={field.onChange} />
                                                </FormControl>
                                                <div className="space-y-1 leading-none">
                                                    <FormLabel className="text-blue-700 font-bold">
                                                        Aprobar para Entrevista
                                                    </FormLabel>
                                                    <FormDescription>
                                                        Habilita la siguiente pestaña.
                                                    </FormDescription>
                                                </div>
                                            </FormItem>
                                        )}
                                    />
                                </div>
                            </div>
                        </TabsContent>

                        {/* FASE 2: ENTREVISTA */}
                        <TabsContent value="entrevista" className="space-y-4 py-4">
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                                <div className="space-y-3">
                                    <h4 className="font-semibold text-sm text-slate-600 mb-2">Evaluación de Competencias (0 - 100)</h4>
                                    {[1, 2, 3, 4, 5].map((num) => {
                                        // Obtener nombre y peso dinámicamente del proceso padre
                                        const itemName = currentProcess[`item_entrevista_${num}`];
                                        const itemWeight = currentProcess[`ponderacion_entrevista_${num}`];
                                        
                                        // Si no tiene nombre ni peso, no lo mostramos (o lo mostramos deshabilitado)
                                        if (!itemName && !itemWeight) return null;

                                        return (
                                            <FormField
                                                key={num}
                                                control={form.control}
                                                // @ts-ignore
                                                name={`item_entrevista${num}`}
                                                render={({ field }) => (
                                                    <FormItem className="grid grid-cols-12 gap-2 items-center space-y-0">
                                                        <FormLabel className="col-span-5 text-xs font-normal truncate" title={itemName}>
                                                            {itemName || `Item ${num}`} <span className="text-slate-400">({itemWeight}%)</span>
                                                        </FormLabel>
                                                        <FormControl className="col-span-4">
                                                            <Input type="number" {...field} min={0} max={100} className="h-8" />
                                                        </FormControl>
                                                        <div className="col-span-3 text-xs text-right text-slate-500 font-mono">
                                                            = {((field.value || 0) * (itemWeight/100)).toFixed(1)} pts
                                                        </div>
                                                    </FormItem>
                                                )}
                                            />
                                        );
                                    })}
                                </div>

                                {/* Resumen Final */}
                                <div className="bg-slate-50 p-6 rounded-lg border flex flex-col justify-between">
                                    <div>
                                        <h3 className="text-lg font-bold text-slate-800">Nota Entrevista</h3>
                                        <div className="text-4xl font-mono font-bold text-purple-600 mt-2">
                                            {getCurrentCalculatedEntrevista()} <span className="text-base text-slate-400 font-normal">/ 100</span>
                                        </div>
                                        <Separator className="my-4" />
                                        <div className="text-sm">
                                            Mínimo selección: <b>{currentProcess.ponderacion_minima_entrevista}</b>
                                        </div>
                                    </div>

                                    <FormField
                                        control={form.control}
                                        name="seleccionado"
                                        render={({ field }) => (
                                            <FormItem className="flex flex-row items-start space-x-3 space-y-0 rounded-md border-2 border-green-100 p-4 bg-green-50 mt-4">
                                                <FormControl>
                                                    <Checkbox checked={field.value} onCheckedChange={field.onChange} />
                                                </FormControl>
                                                <div className="space-y-1 leading-none">
                                                    <FormLabel className="text-green-800 font-bold text-lg">
                                                        SELECCIONAR CANDIDATO
                                                    </FormLabel>
                                                    <FormDescription className="text-green-600">
                                                        Marcar si el postulante ha ganado la vacante.
                                                    </FormDescription>
                                                </div>
                                            </FormItem>
                                        )}
                                    />
                                </div>
                            </div>
                        </TabsContent>
                    </Tabs>

                    <div className="flex justify-end pt-4 gap-2">
                         <Button type="button" variant="outline" onClick={() => setIsDialogOpen(false)}>Cancelar</Button>
                        <Button type="submit" className="bg-blue-600">
                            <Save className="mr-2 h-4 w-4" /> Guardar Evaluación
                        </Button>
                    </div>
                </form>
            </Form>
        </DialogContent>
      </Dialog>

      {/* ALERTA DE BORRADO */}
      <AlertDialog open={!!deleteId} onOpenChange={() => setDeleteId(null)}>
        <AlertDialogContent>
            <AlertDialogTitle>¿Eliminar Postulante?</AlertDialogTitle>
            <AlertDialogDescription>Se eliminarán todos los registros de evaluación de este candidato.</AlertDialogDescription>
            <AlertDialogFooter>
                <AlertDialogCancel>Cancelar</AlertDialogCancel>
                <AlertDialogAction className="bg-red-600" onClick={() => { if(deleteId) deletePostulanteMutation.mutate(deleteId); setDeleteId(null); }}>
                    Eliminar
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
};
