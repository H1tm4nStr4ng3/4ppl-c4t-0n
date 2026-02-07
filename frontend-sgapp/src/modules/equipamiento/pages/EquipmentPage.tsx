import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { format, isValid, parseISO } from "date-fns";
import { 
  Plus, CalendarIcon, Microscope, Trash, Pencil, 
  Settings2, Cpu, FileCode, Scale, ClipboardList, Tag
} from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
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
import {
    AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogTitle, AlertDialogDescription, AlertDialogFooter
} from "@/components/ui/alert-dialog";

import { useInventory, equipmentSchema, EquipmentFormValues } from "../hooks/useInventory";

export const EquipmentPage = () => {
  const { 
    categories, 
    equipments, 
    isLoading, 
    createCategoryMutation, 
    deleteCategoryMutation,
    createEquipmentMutation, 
    updateEquipmentMutation, 
    deleteEquipmentMutation 
  } = useInventory();

  // Estados
  const [isEqDialogOpen, setIsEqDialogOpen] = useState(false); 
  const [isCatDialogOpen, setIsCatDialogOpen] = useState(false); 
  const [editingId, setEditingId] = useState<number | null>(null);
  const [deleteId, setDeleteId] = useState<number | null>(null);
  const [dateInputValue, setDateInputValue] = useState("");
  const [newCategoryName, setNewCategoryName] = useState(""); 

  // Formulario Equipo - Inicialización completa
  const form = useForm<EquipmentFormValues>({
    resolver: zodResolver(equipmentSchema),
    defaultValues: {
      equipamiento: "", codigo_interno: "", marca: "", serie: "", ubicacion: "", estado: "OPERATIVO",
      material: "", numero_de_piezas: "", max_vn: "", d: "", clase_de_exactitud: "",
      version_software: "", version_firmware: "",
      requiere: "",
      frecuencia_de_calibracion: "", frecuencia_de_mantenimiento: "",
      frecuencia_de_comprobacion_intermedia: "", frecuencia_de_calificacion: "",
      comentarios: ""
    },
  });

  // Sincronizar fecha manual
  useEffect(() => {
    const currentDate = form.getValues("puesta_en_funcionamiento");
    if (currentDate) {
        setDateInputValue(format(currentDate, "yyyy-MM-dd"));
    } else {
        setDateInputValue("");
    }
  }, [form.watch("puesta_en_funcionamiento"), isEqDialogOpen]);

  // Manejadores
  const handleCreateEq = () => {
      setEditingId(null);
      form.reset({
        equipamiento: "", codigo_interno: "", marca: "", serie: "", ubicacion: "", estado: "OPERATIVO",
        material: "", numero_de_piezas: "", max_vn: "", d: "", clase_de_exactitud: "",
        version_software: "", version_firmware: "",
        requiere: "", frecuencia_de_calibracion: "", frecuencia_de_mantenimiento: "",
        frecuencia_de_comprobacion_intermedia: "", frecuencia_de_calificacion: "",
        puesta_en_funcionamiento: new Date(), comentarios: ""
      });
      setIsEqDialogOpen(true);
  };

  const handleEditEq = (item: any) => {
      setEditingId(item.id);
      const cleanData: any = { ...item };
      if (cleanData.puesta_en_funcionamiento) cleanData.puesta_en_funcionamiento = new Date(cleanData.puesta_en_funcionamiento);
      Object.keys(cleanData).forEach(key => {
          if (cleanData[key] === null) cleanData[key] = "";
      });
      form.reset(cleanData);
      setIsEqDialogOpen(true);
  };

  const onSubmitEq = async (data: EquipmentFormValues) => {
    if (editingId) {
        await updateEquipmentMutation.mutateAsync({ ...data, id: editingId });
    } else {
        await createEquipmentMutation.mutateAsync(data);
    }
    setIsEqDialogOpen(false);
  };

  const handleCreateCategory = async () => {
      if (!newCategoryName.trim()) return;
      await createCategoryMutation.mutateAsync({ lista_de_equipos: newCategoryName });
      setNewCategoryName("");
  };

  const onInvalid = (errors: any) => {
      console.error("Errores:", errors);
      toast.error("Formulario incompleto. Revise los campos obligatorios.");
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Inventario de Equipamiento</h1>
          <p className="text-slate-500">Hoja de vida de equipos conforme a norma.</p>
        </div>
        <div className="flex gap-2">
            <Button variant="outline" onClick={() => setIsCatDialogOpen(true)}>
                <Settings2 className="mr-2 h-4 w-4" /> Tipos de Equipo
            </Button>
            <Button onClick={handleCreateEq} className="bg-blue-600 hover:bg-blue-700">
                <Plus className="mr-2 h-4 w-4" /> Nuevo Equipo
            </Button>
        </div>
      </div>

      {/* LISTADO DE EQUIPOS */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {isLoading ? (
             <div className="col-span-3 text-center p-10 text-slate-500">Cargando inventario...</div>
        ) : equipments.length === 0 ? (
            <div className="col-span-3 text-center p-10 border-2 border-dashed rounded-xl bg-slate-50 text-slate-500">
                No hay equipos registrados.
            </div>
        ) : equipments.map((eq: any) => (
            <Card key={eq.id} className="hover:shadow-md transition-shadow flex flex-col justify-between border-t-4 border-t-blue-500">
                <CardHeader className="pb-2">
                    <div className="flex justify-between items-start">
                         <Badge variant="outline" className="mb-2 text-xs truncate max-w-[150px]">{eq.equipamiento}</Badge>
                         <Badge className={eq.estado === 'OPERATIVO' ? 'bg-green-600' : 'bg-red-600'}>
                            {eq.estado}
                         </Badge>
                    </div>
                    <CardTitle className="text-xl font-bold text-slate-800 truncate">
                        {eq.codigo_interno}
                    </CardTitle>
                    <CardDescription className="text-xs font-mono truncate">
                        SN: {eq.serie || "S/N"} | {eq.marca}
                    </CardDescription>
                </CardHeader>
                <CardContent className="text-sm space-y-3">
                    <div className="grid grid-cols-2 gap-2 text-xs text-slate-600 bg-slate-50 p-2 rounded">
                        <div className="flex items-center gap-1">
                            <Scale className="h-3 w-3 text-orange-600" />
                            <span>Max: {eq.max_vn || "-"}</span>
                        </div>
                        <div className="flex items-center gap-1">
                            <Tag className="h-3 w-3 text-blue-600" />
                            <span>d: {eq.d || "-"}</span>
                        </div>
                    </div>
                    <div className="flex items-center gap-2 text-xs text-slate-500">
                        <CalendarIcon className="h-3 w-3" />
                        Alta: {eq.puesta_en_funcionamiento ? format(new Date(eq.puesta_en_funcionamiento), 'yyyy-MM-dd') : '-'}
                    </div>
                </CardContent>
                <CardFooter className="flex justify-end gap-2 pt-2 border-t mt-2">
                    <Button variant="ghost" size="sm" onClick={() => handleEditEq(eq)}>
                        <Pencil className="h-4 w-4 text-slate-500" />
                    </Button>
                    <Button variant="ghost" size="sm" onClick={() => setDeleteId(eq.id)}>
                        <Trash className="h-4 w-4 text-red-500" />
                    </Button>
                </CardFooter>
            </Card>
        ))}
      </div>

      {/* DIÁLOGO ALTA/EDICIÓN EQUIPO - FORMATO COMPLETO */}
      <Dialog open={isEqDialogOpen} onOpenChange={setIsEqDialogOpen}>
        <DialogContent className="sm:max-w-[900px] max-h-[90vh] overflow-y-auto">
          <DialogHeader>
            <DialogTitle>{editingId ? "Editar Ficha de Equipo" : "Alta de Equipo (Hoja de Vida)"}</DialogTitle>
          </DialogHeader>

          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmitEq, onInvalid)} className="space-y-6">
                
                {/* 1. IDENTIFICACIÓN */}
                <div className="border rounded-md p-4 bg-slate-50/50">
                    <h3 className="text-sm font-bold text-blue-700 mb-3 flex items-center gap-2">
                        <Tag size={16}/> Identificación del Equipo
                    </h3>
                    <div className="grid grid-cols-3 gap-4">
                        <FormField
                            control={form.control}
                            name="equipamiento"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Tipo de Equipo *</FormLabel>
                                    <Select onValueChange={field.onChange} value={field.value}>
                                        <FormControl><SelectTrigger><SelectValue placeholder="Seleccione..." /></SelectTrigger></FormControl>
                                        <SelectContent>
                                            {categories?.map((cat: any) => (
                                                <SelectItem key={cat.lista_de_equipos} value={cat.lista_de_equipos}>
                                                    {cat.lista_de_equipos}
                                                </SelectItem>
                                            ))}
                                        </SelectContent>
                                    </Select>
                                </FormItem>
                            )}
                        />
                        <FormField
                            control={form.control}
                            name="codigo_interno"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Código Interno (ID) *</FormLabel>
                                    <FormControl><Input placeholder="Ej: LAB-01" {...field} /></FormControl>
                                </FormItem>
                            )}
                        />
                        <FormField
                            control={form.control}
                            name="estado"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Estado</FormLabel>
                                    <Select onValueChange={field.onChange} value={field.value}>
                                        <FormControl><SelectTrigger><SelectValue /></SelectTrigger></FormControl>
                                        <SelectContent>
                                            <SelectItem value="OPERATIVO">OPERATIVO</SelectItem>
                                            <SelectItem value="MANTENIMIENTO">MANTENIMIENTO</SelectItem>
                                            <SelectItem value="FUERA_DE_SERVICIO">FUERA DE SERVICIO</SelectItem>
                                            <SelectItem value="BAJA">DE BAJA</SelectItem>
                                        </SelectContent>
                                    </Select>
                                </FormItem>
                            )}
                        />
                        <FormField control={form.control} name="marca" render={({ field }) => (
                            <FormItem><FormLabel>Marca</FormLabel><FormControl><Input {...field} /></FormControl></FormItem>
                        )}/>
                        <FormField control={form.control} name="serie" render={({ field }) => (
                            <FormItem><FormLabel>Serie</FormLabel><FormControl><Input {...field} /></FormControl></FormItem>
                        )}/>
                        <FormField control={form.control} name="ubicacion" render={({ field }) => (
                            <FormItem><FormLabel>Ubicación</FormLabel><FormControl><Input placeholder="Lab..." {...field} /></FormControl></FormItem>
                        )}/>
                    </div>
                </div>

                {/* 2. ESPECIFICACIONES TÉCNICAS */}
                <div className="border rounded-md p-4 bg-white border-slate-200">
                    <h3 className="text-sm font-bold text-slate-700 mb-3 flex items-center gap-2">
                        <Scale size={16}/> Especificaciones Metrológicas
                    </h3>
                    <div className="grid grid-cols-4 gap-4">
                        <FormField control={form.control} name="max_vn" render={({ field }) => (
                            <FormItem><FormLabel>Capacidad (Max)</FormLabel><FormControl><Input placeholder="Ej: 220 g" {...field} /></FormControl></FormItem>
                        )}/>
                        <FormField control={form.control} name="d" render={({ field }) => (
                            <FormItem><FormLabel>Resolución (d)</FormLabel><FormControl><Input placeholder="Ej: 0.001 g" {...field} /></FormControl></FormItem>
                        )}/>
                        <FormField control={form.control} name="clase_de_exactitud" render={({ field }) => (
                            <FormItem><FormLabel>Clase Exactitud</FormLabel><FormControl><Input placeholder="Ej: I, II, A..." {...field} /></FormControl></FormItem>
                        )}/>
                        <FormField control={form.control} name="material" render={({ field }) => (
                            <FormItem><FormLabel>Material</FormLabel><FormControl><Input placeholder="Ej: Acero Inox" {...field} /></FormControl></FormItem>
                        )}/>
                        <div className="col-span-2">
                            <FormField control={form.control} name="numero_de_piezas" render={({ field }) => (
                                <FormItem><FormLabel>Número de Piezas</FormLabel><FormControl><Input placeholder="Si aplica..." {...field} /></FormControl></FormItem>
                            )}/>
                        </div>
                    </div>
                    {/* Versiones */}
                    <div className="grid grid-cols-2 gap-4 mt-4 pt-4 border-t border-dashed">
                        <FormField control={form.control} name="version_firmware" render={({ field }) => (
                             <FormItem><FormLabel className="text-xs">Firmware (FW)</FormLabel><FormControl><Input className="h-8" placeholder="v1.0" {...field} /></FormControl></FormItem>
                        )}/>
                        <FormField control={form.control} name="version_software" render={({ field }) => (
                             <FormItem><FormLabel className="text-xs">Software (SW)</FormLabel><FormControl><Input className="h-8" placeholder="Build..." {...field} /></FormControl></FormItem>
                        )}/>
                    </div>
                </div>

                {/* 3. GESTIÓN Y FRECUENCIAS */}
                <div className="border rounded-md p-4 bg-slate-50/50">
                    <h3 className="text-sm font-bold text-orange-700 mb-3 flex items-center gap-2">
                        <ClipboardList size={16}/> Plan de Calidad (Frecuencias)
                    </h3>
                    <div className="grid grid-cols-1 mb-4">
                         <FormField control={form.control} name="requiere" render={({ field }) => (
                            <FormItem>
                                <FormLabel>Requisitos del Equipo</FormLabel>
                                <FormControl><Input placeholder="Ej: Calibración anual y verificación mensual..." {...field} /></FormControl>
                            </FormItem>
                        )}/>
                    </div>
                    <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
                        <FormField control={form.control} name="frecuencia_de_calibracion" render={({ field }) => (
                            <FormItem><FormLabel className="text-xs">Frec. Calibración</FormLabel><FormControl><Input placeholder="Ej: 12 meses" {...field} /></FormControl></FormItem>
                        )}/>
                        <FormField control={form.control} name="frecuencia_de_mantenimiento" render={({ field }) => (
                            <FormItem><FormLabel className="text-xs">Frec. Mantenimiento</FormLabel><FormControl><Input placeholder="Ej: 6 meses" {...field} /></FormControl></FormItem>
                        )}/>
                        <FormField control={form.control} name="frecuencia_de_comprobacion_intermedia" render={({ field }) => (
                            <FormItem><FormLabel className="text-xs">Frec. Comprobación</FormLabel><FormControl><Input placeholder="Ej: Semanal" {...field} /></FormControl></FormItem>
                        )}/>
                        <FormField control={form.control} name="frecuencia_de_calificacion" render={({ field }) => (
                            <FormItem><FormLabel className="text-xs">Frec. Calificación</FormLabel><FormControl><Input placeholder="Ej: 5 años" {...field} /></FormControl></FormItem>
                        )}/>
                    </div>
                </div>

                {/* 4. FECHA Y COMENTARIOS */}
                <div className="grid grid-cols-3 gap-4">
                    <FormField
                        control={form.control}
                        name="puesta_en_funcionamiento"
                        render={({ field }) => (
                            <FormItem className="flex flex-col">
                                <FormLabel>Puesta en Funcionamiento</FormLabel>
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
                                            selected={field.value || undefined}
                                            onSelect={field.onChange}
                                            initialFocus
                                        />
                                    </PopoverContent>
                                </Popover>
                            </FormItem>
                        )}
                    />
                    <div className="col-span-2">
                        <FormField control={form.control} name="comentarios" render={({ field }) => (
                            <FormItem><FormLabel>Observaciones</FormLabel><FormControl><Textarea className="h-10 min-h-[40px]" {...field} /></FormControl></FormItem>
                        )}/>
                    </div>
                </div>

                <div className="flex justify-end pt-4 border-t">
                    <Button type="submit" className="bg-blue-600 hover:bg-blue-700 w-full md:w-auto">
                        <Microscope className="mr-2 h-4 w-4" /> Guardar Ficha Técnica
                    </Button>
                </div>
            </form>
          </Form>
        </DialogContent>
      </Dialog>

      {/* DIÁLOGO GESTIÓN TIPOS - MANTENER IGUAL QUE ANTES */}
      <Dialog open={isCatDialogOpen} onOpenChange={setIsCatDialogOpen}>
        <DialogContent className="sm:max-w-[500px]">
            <DialogHeader>
                <DialogTitle>Gestión de Tipos de Equipo</DialogTitle>
                <CardDescription>Cree o elimine las categorías para clasificar sus activos.</CardDescription>
            </DialogHeader>
            <div className="space-y-6 py-4">
                <div className="flex items-end gap-2">
                    <div className="w-full space-y-2">
                        <label className="text-sm font-medium leading-none">Nuevo Tipo</label>
                        <Input placeholder="Ingrese nombre..." value={newCategoryName} onChange={(e) => setNewCategoryName(e.target.value)} />
                    </div>
                    <Button onClick={handleCreateCategory} className="bg-slate-800 text-white"><Plus className="h-4 w-4" /></Button>
                </div>
                <div className="border-t border-slate-100 my-4"></div>
                <div className="space-y-2">
                    <label className="text-sm font-bold text-slate-700">Tipos Existentes</label>
                    <div className="border rounded-md max-h-[200px] overflow-y-auto bg-slate-50 p-2 space-y-1">
                        {categories.length === 0 ? <p className="text-xs text-slate-400 text-center py-4">No hay tipos.</p> : categories.map((cat: any) => (
                            <div key={cat.id || cat.lista_de_equipos} className="flex justify-between items-center bg-white p-2 rounded border border-slate-200 shadow-sm text-sm">
                                <span className="font-medium text-slate-700">{cat.lista_de_equipos}</span>
                                <Button variant="ghost" size="sm" className="h-6 w-6 p-0 text-red-400 hover:text-red-600" onClick={() => deleteCategoryMutation.mutate(cat.lista_de_equipos)}><Trash className="h-3 w-3" /></Button>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </DialogContent>
      </Dialog>

      <AlertDialog open={!!deleteId} onOpenChange={() => setDeleteId(null)}>
        <AlertDialogContent>
            <AlertDialogTitle>¿Eliminar Equipo?</AlertDialogTitle>
            <AlertDialogDescription>Se eliminará este equipo del inventario.</AlertDialogDescription>
            <AlertDialogFooter>
                <AlertDialogCancel>Cancelar</AlertDialogCancel>
                <AlertDialogAction className="bg-red-600" onClick={() => { if(deleteId) deleteEquipmentMutation.mutate(deleteId); setDeleteId(null); }}>Eliminar</AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
};