import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { format, isValid, parseISO } from "date-fns";
import { es } from "date-fns/locale";
import { 
  Plus, CalendarIcon, UserCheck, User, Trash, Pencil, 
  AlertTriangle, CheckCircle2, XCircle, Eye 
} from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Checkbox } from "@/components/ui/checkbox";
import { Badge } from "@/components/ui/badge";
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
import {
    AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogTitle, AlertDialogDescription, AlertDialogFooter
} from "@/components/ui/alert-dialog";
import { Switch } from "@/components/ui/switch";

// Hooks
import { useSupervision, supervisionSchema, SupervisionFormValues } from "../hooks/useSupervision";
import { usePersonal } from "../hooks/usePersonal";

export const SupervisionPage = () => {
  const { supervisions, isLoadingSupervisions, createSupervisionMutation, updateSupervisionMutation, deleteSupervisionMutation } = useSupervision();
  const { data: personal } = usePersonal();

  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [deleteId, setDeleteId] = useState<number | null>(null);
  const [dateInputValue, setDateInputValue] = useState("");

  const form = useForm<SupervisionFormValues>({
    resolver: zodResolver(supervisionSchema),
    defaultValues: {
      fecha: new Date(),
      supervisores: "", supervisados: "", cargo: "", item: "", comentarios: "",
      requiere_adquirir_o_aumentar_competencia: false,
      // Los items 1-10 se inicializan undefined y Zod los transforma a ""
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

  // AUTO-LLENADO DE CARGO
  const selectedSupervisado = form.watch("supervisados");
  useEffect(() => {
      if (selectedSupervisado && personal) {
          const p = personal.find((x: any) => x.abreviatura === selectedSupervisado);
          if (p) form.setValue("cargo", p.cargo);
      }
  }, [selectedSupervisado, personal, form]);

  const handleCreate = () => {
      setEditingId(null);
      form.reset({
        fecha: new Date(),
        supervisores: "", supervisados: "", cargo: "", item: "", comentarios: "",
        requiere_adquirir_o_aumentar_competencia: false,
      });
      setIsDialogOpen(true);
  };

  const handleEdit = (item: any) => {
      setEditingId(item.id);
      
      const cleanData: any = { ...item };
      
      if (cleanData.fecha) cleanData.fecha = new Date(cleanData.fecha);
      
      // Limpieza AGRESIVA de nulos
      Object.keys(cleanData).forEach(key => {
          if (cleanData[key] === null) {
              if (key.startsWith('supervision_exitosa') || key === 'requiere_adquirir_o_aumentar_competencia') cleanData[key] = false;
              else cleanData[key] = "";
          }
      });
      
      form.reset(cleanData);
      setIsDialogOpen(true);
  };

  const onSubmit = async (data: SupervisionFormValues) => {
    if (editingId) {
        await updateSupervisionMutation.mutateAsync({ ...data, id: editingId });
    } else {
        await createSupervisionMutation.mutateAsync(data);
    }
    setIsDialogOpen(false);
  };

  const onInvalid = (errors: any) => {
      console.error("Errores:", errors);
      const firstError = Object.values(errors)[0] as any;
      toast.error("Formulario incompleto", { description: firstError?.message });
  };

  // Renderizar filas de items 1-10
  const renderCheckItem = (index: number) => (
    <div key={index} className="grid grid-cols-12 gap-2 items-center mb-2 border-b pb-2 last:border-0">
        <div className="col-span-9">
             <FormField
                control={form.control}
                // @ts-ignore
                name={`item_de_supervision_${index}`}
                render={({ field }) => (
                    <FormItem>
                        <FormControl>
                            <Input placeholder={`Punto de control ${index}...`} {...field} value={field.value || ""} className="h-8 text-sm" />
                        </FormControl>
                    </FormItem>
                )}
            />
        </div>
        <div className="col-span-3 flex justify-center">
             <FormField
                control={form.control}
                // @ts-ignore
                name={`supervision_exitosa_${index}`}
                render={({ field }) => (
                    <FormItem className="flex items-center space-x-2 space-y-0">
                        <FormControl>
                             <Switch checked={field.value} onCheckedChange={field.onChange} />
                        </FormControl>
                        <FormLabel className="text-xs font-normal">
                            {field.value ? "OK" : "NO"}
                        </FormLabel>
                    </FormItem>
                )}
            />
        </div>
    </div>
  );

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Supervisión de Personal</h1>
          <p className="text-slate-500">Bitácora de seguimiento operativo y cumplimiento de procedimientos.</p>
        </div>
        <Button onClick={handleCreate} className="bg-blue-600 hover:bg-blue-700">
          <Plus className="mr-2 h-4 w-4" /> Nueva Supervisión
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {isLoadingSupervisions ? (
             <div className="col-span-3 text-center p-10 text-slate-500">Cargando supervisiones...</div>
        ) : supervisions.length === 0 ? (
            <div className="col-span-3 text-center p-10 border-2 border-dashed rounded-xl bg-slate-50 text-slate-500">
                No hay registros de supervisión.
            </div>
        ) : supervisions.map((sup: any) => (
            <Card 
                key={sup.id} 
                className={`hover:shadow-md transition-shadow border-t-4 flex flex-col justify-between ${
                    sup.requiere_adquirir_o_aumentar_competencia 
                    ? 'border-t-red-600 bg-red-50/50' 
                    : 'border-t-blue-500'
                }`}
            >
                <CardHeader className="pb-2">
                    <div className="flex justify-between items-start">
                        <CardTitle className="text-lg font-bold text-slate-800 leading-snug truncate pr-2">
                           {sup.item}
                        </CardTitle>
                        {sup.requiere_adquirir_o_aumentar_competencia && (
                            <div className="flex items-center gap-1 text-red-600 font-bold text-xs bg-red-100 px-2 py-1 rounded-full border border-red-200 animate-pulse">
                                <AlertTriangle className="h-3 w-3" /> ALERTA
                            </div>
                        )}
                    </div>
                    <CardDescription className="flex items-center gap-1 text-xs">
                        <CalendarIcon className="h-3 w-3" />
                        {sup.fecha ? format(new Date(sup.fecha), 'yyyy-MM-dd') : '-'}
                    </CardDescription>
                </CardHeader>
                <CardContent className="text-sm space-y-3">
                    <div className="flex flex-col gap-1 text-xs text-slate-600 bg-white/50 p-2 rounded border border-slate-100">
                         <div className="flex items-center gap-1">
                            <User className="h-3 w-3 text-blue-500" />
                            <span>Supervisado: <b>{sup.supervisados}</b></span>
                        </div>
                        <div className="flex items-center gap-1">
                            <UserCheck className="h-3 w-3 text-slate-400" />
                            <span>Supervisor: {sup.supervisores}</span>
                        </div>
                    </div>
                    
                    {sup.comentarios && (
                        <div className="text-xs italic text-slate-600 line-clamp-2">
                            "{sup.comentarios}"
                        </div>
                    )}

                    {sup.requiere_adquirir_o_aumentar_competencia && (
                        <div className="text-xs font-bold text-red-700 mt-2">
                            ⚠️ Se requiere plan de acción inmediata.
                        </div>
                    )}
                </CardContent>
                <CardFooter className="flex justify-end gap-2 pt-2 border-t mt-2">
                    <Button variant="ghost" size="sm" onClick={() => handleEdit(sup)}>
                        <Pencil className="h-4 w-4 text-slate-500" />
                    </Button>
                    <Button variant="ghost" size="sm" onClick={() => setDeleteId(sup.id)}>
                        <Trash className="h-4 w-4 text-red-500" />
                    </Button>
                </CardFooter>
            </Card>
        ))}
      </div>

      {/* DIÁLOGO FORMULARIO */}
      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
        <DialogContent className="sm:max-w-[700px] max-h-[95vh] overflow-y-auto">
          <DialogHeader>
            <DialogTitle>{editingId ? "Editar Supervisión" : "Registrar Supervisión"}</DialogTitle>
          </DialogHeader>

          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit, onInvalid)} className="space-y-4">
                
                {/* 1. SECCIÓN ACTORES */}
                <div className="grid grid-cols-2 gap-4">
                    <FormField
                        control={form.control}
                        name="supervisados"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Personal Supervisado</FormLabel>
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
                    <FormField
                        control={form.control}
                        name="supervisores"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Supervisor (Evaluador)</FormLabel>
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

                {/* 2. ACTIVIDAD Y FECHA */}
                <div className="grid grid-cols-12 gap-4">
                    <div className="col-span-8">
                        <FormField
                            control={form.control}
                            name="item"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Actividad o Ensayo Supervisado</FormLabel>
                                    <FormControl>
                                        <Input placeholder="Ej: Preparación de muestras para análisis..." {...field} />
                                    </FormControl>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                    </div>
                    <div className="col-span-4">
                        <FormField
                            control={form.control}
                            name="fecha"
                            render={({ field }) => (
                                <FormItem className="flex flex-col">
                                    <FormLabel>Fecha</FormLabel>
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
                    </div>
                </div>

                {/* 3. ALERTA CRÍTICA */}
                <FormField
                    control={form.control}
                    name="requiere_adquirir_o_aumentar_competencia"
                    render={({ field }) => (
                        <FormItem className="flex flex-row items-center justify-between rounded-lg border border-red-200 bg-red-50 p-4 shadow-sm">
                            <div className="space-y-0.5">
                                <FormLabel className="text-base font-bold text-red-700 flex items-center gap-2">
                                    <AlertTriangle className="h-5 w-5" />
                                    Alerta de Competencia
                                </FormLabel>
                                <div className="text-xs text-red-600">
                                    Marcar si el desempeño fue deficiente y requiere capacitación urgente.
                                </div>
                            </div>
                            <FormControl>
                                <Switch
                                    checked={field.value}
                                    onCheckedChange={field.onChange}
                                    className="data-[state=checked]:bg-red-600"
                                />
                            </FormControl>
                        </FormItem>
                    )}
                />

                {/* 4. LISTA DE VERIFICACIÓN (Pestañas para no saturar) */}
                {/* 4. LISTA DE VERIFICACIÓN (COMPLETA 1-10) */}
                <div className="border rounded-md p-4 bg-slate-50">
                    <label className="text-sm font-bold text-slate-700 mb-2 block">Puntos de Control / Checklist</label>
                    <div className="max-h-[300px] overflow-y-auto pr-2 space-y-1">
                        {renderCheckItem(1)}
                        {renderCheckItem(2)}
                        {renderCheckItem(3)}
                        {renderCheckItem(4)}
                        {renderCheckItem(5)}
                        
                        {/* Ítems adicionales activados */}
                        {renderCheckItem(6)}
                        {renderCheckItem(7)}
                        {renderCheckItem(8)}
                        {renderCheckItem(9)}
                        {renderCheckItem(10)}
                    </div>
                    <p className="text-xs text-slate-400 mt-2 text-center">
                        Llene solo los puntos que apliquen a esta actividad.
                    </p>
                </div>

                <FormField
                    control={form.control}
                    name="comentarios"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Observaciones Generales</FormLabel>
                            <FormControl>
                                <Textarea placeholder="Detalles de lo observado..." {...field} value={field.value || ""} />
                            </FormControl>
                        </FormItem>
                    )}
                />

                <div className="flex justify-end pt-2">
                    <Button type="submit" className="bg-blue-600 hover:bg-blue-700 w-full md:w-auto">
                        <Eye className="mr-2 h-4 w-4" /> Guardar Supervisión
                    </Button>
                </div>
            </form>
          </Form>
        </DialogContent>
      </Dialog>

      <AlertDialog open={!!deleteId} onOpenChange={() => setDeleteId(null)}>
        <AlertDialogContent>
            <AlertDialogTitle>¿Eliminar Supervisión?</AlertDialogTitle>
            <AlertDialogDescription>Se perderá este registro de auditoría.</AlertDialogDescription>
            <AlertDialogFooter>
                <AlertDialogCancel>Cancelar</AlertDialogCancel>
                <AlertDialogAction className="bg-red-600" onClick={() => { if(deleteId) deleteSupervisionMutation.mutate(deleteId); setDeleteId(null); }}>
                    Eliminar
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
};
