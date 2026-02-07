import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { format, isValid, parseISO } from "date-fns";
import { 
  Plus, CalendarIcon, Trash, Pencil, TestTube, Save, 
  Beaker, FileText, Factory, MapPin, Hash, List
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
  Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription,
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
import {
    Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "@/components/ui/table";

import { useReferenceMaterials, mrSchema, MRFormValues } from "../hooks/useReferenceMaterials";

// --- COMPONENTE DE FECHA MANUAL (EDITABLE Y CALENDARIO) ---
const ManualDatePicker = ({ value, onChange, label }: { value: Date | null | undefined | any, onChange: (date: Date | undefined) => void, label: string }) => {
    const [inputValue, setInputValue] = useState("");

    // Sincronizar input con valor externo
    useEffect(() => {
        if (value) {
            setInputValue(format(new Date(value), "yyyy-MM-dd"));
        } else {
            setInputValue("");
        }
    }, [value]);

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const val = e.target.value;
        setInputValue(val);
        
        if (val.trim() === "") {
            onChange(undefined);
            return;
        }

        const parsedDate = parseISO(val);
        if (isValid(parsedDate) && val.length === 10) {
            onChange(parsedDate);
        }
    };

    return (
        <FormItem className="flex flex-col">
            <FormLabel>{label}</FormLabel>
            <Popover>
                <PopoverTrigger asChild>
                    <FormControl>
                        <div className="relative flex items-center w-full">
                            <Input 
                                value={inputValue}
                                onChange={handleInputChange}
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
                        selected={value || undefined}
                        onSelect={(date) => onChange(date)}
                        initialFocus
                    />
                </PopoverContent>
            </Popover>
        </FormItem>
    );
};

export const ReferenceMaterialsPage = () => {
  const { 
    materials, isLoading, 
    createMRMutation, updateMRMutation, deleteMRMutation,
    createMVMutation, deleteMVMutation
  } = useReferenceMaterials();

  // Estados
  const [isMRDialogOpen, setIsMRDialogOpen] = useState(false); // Modal Administrativo
  const [isMVDialogOpen, setIsMVDialogOpen] = useState(false); // Modal Técnico (Especificaciones)
  
  const [editingMR, setEditingMR] = useState<any>(null); // Material en edición (Admin)
  const [selectedMR, setSelectedMR] = useState<any>(null); // Material seleccionado para ver especificaciones (Técnico)
  
  const [deleteId, setDeleteId] = useState<number | null>(null);

  // Estados para el subformulario MV (Especificaciones)
  const [newParam, setNewParam] = useState("");
  const [newVal, setNewVal] = useState("");
  const [newUncert, setNewUncert] = useState("");
  const [newUnit, setNewUnit] = useState("");

  // --- BUSQUEDA EN VIVO PARA EL MODAL TÉCNICO ---
  // Si tenemos un material seleccionado, buscamos su versión más fresca en la lista global
  const activeTechnicalMR = materials.find((m: any) => m.id === selectedMR?.id);

  // Formulario Principal (MR)
  const form = useForm<MRFormValues>({
    resolver: zodResolver(mrSchema),
    defaultValues: {
      codigo_interno: "", equipamiento: "", tipo: "", certificado: "",
      codigo_original: "", productor_del_material_de_referencia: "",
      procedencia: "", serie: "", material: "", ubicacion: "",
      estado: "VIGENTE", comentarios: ""
    },
  });

  // --- MANEJADORES ADMINISTRATIVOS (MR) ---
  const handleCreateMR = () => {
      setEditingMR(null);
      form.reset({
        codigo_interno: "", equipamiento: "", tipo: "", certificado: "",
        codigo_original: "", productor_del_material_de_referencia: "",
        procedencia: "", serie: "", material: "", ubicacion: "",
        estado: "VIGENTE", comentarios: "",
        fecha_de_certificado: null, fecha_de_apertura: null, fecha_de_vencimiento: null
      });
      setIsMRDialogOpen(true);
  };

  const handleEditMR = (item: any) => {
      setEditingMR(item);
      const cleanData = { ...item };
      // Convertir strings de fecha a Date
      ['fecha_de_certificado', 'fecha_de_apertura', 'fecha_de_vencimiento'].forEach(key => {
          if (cleanData[key]) cleanData[key] = new Date(cleanData[key]);
      });
      // Limpiar nulos
      Object.keys(cleanData).forEach(k => { if (cleanData[k] === null) cleanData[k] = ""; });

      form.reset(cleanData);
      setIsMRDialogOpen(true);
  };

  const onSubmitMR = async (data: MRFormValues) => {
    if (editingMR) {
        await updateMRMutation.mutateAsync({ ...data, id: editingMR.id });
    } else {
        await createMRMutation.mutateAsync(data);
    }
    setIsMRDialogOpen(false);
  };

  // --- MANEJADORES TÉCNICOS (MV - ESPECIFICACIONES) ---
  const handleOpenSpecs = (item: any) => {
      setSelectedMR(item);
      setIsMVDialogOpen(true);
      // Limpiar inputs al abrir
      setNewParam(""); setNewVal(""); setNewUncert(""); setNewUnit("");
  };

  const handleAddMV = async () => {
      if (!activeTechnicalMR || !activeTechnicalMR.id) {
          toast.error("Error al identificar el material.");
          return;
      }
      if (!newParam || !newUnit) {
          toast.error("Parámetro y Unidad son obligatorios");
          return;
      }

      await createMVMutation.mutateAsync({
          id_mr: activeTechnicalMR.codigo_interno, // Usamos el código del objeto activo
          parametro: newParam,
          unidad: newUnit,
          valor: newVal, 
          incertidumbre: newUncert, 
          id: 0
      });

      // Limpiar inputs
      setNewParam(""); setNewVal(""); setNewUncert(""); setNewUnit("");
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      
      {/* HEADER */}
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Materiales de Referencia</h1>
          <p className="text-slate-500">Gestión de patrones, CRM y estándares de verificación.</p>
        </div>
        <Button onClick={handleCreateMR} className="bg-blue-600 hover:bg-blue-700">
            <Plus className="mr-2 h-4 w-4" /> Nuevo Material
        </Button>
      </div>

      {/* LISTADO DE MATERIALES (CARDS) */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {isLoading ? (
             <div className="col-span-3 text-center p-10 text-slate-500">Cargando inventario...</div>
        ) : materials.length === 0 ? (
            <div className="col-span-3 text-center p-10 border-2 border-dashed rounded-xl bg-slate-50 text-slate-500">
                No hay materiales registrados.
            </div>
        ) : materials.map((mr: any) => (
            <Card key={mr.id} className="hover:shadow-md transition-shadow flex flex-col justify-between border-t-4 border-t-purple-500">
                <CardHeader className="pb-2">
                    <div className="flex justify-between items-start">
                         <Badge variant="outline" className="mb-2 text-xs truncate max-w-[120px]">{mr.tipo || "General"}</Badge>
                         <Badge className={mr.estado === 'VIGENTE' ? 'bg-green-600' : 'bg-red-600'}>{mr.estado}</Badge>
                    </div>
                    <CardTitle className="text-lg font-bold text-slate-800 truncate">
                        {mr.codigo_interno}
                    </CardTitle>
                    <CardDescription className="text-xs truncate font-mono">
                        {mr.codigo_original ? `Ref: ${mr.codigo_original}` : "Sin Ref. Original"}
                    </CardDescription>
                </CardHeader>
                <CardContent className="text-sm space-y-3">
                    <div className="flex items-center gap-2 text-xs font-medium text-slate-700 bg-slate-100 p-2 rounded">
                        <Beaker size={14} className="text-purple-600"/>
                        <span className="truncate">{mr.material || "Matriz N/A"}</span>
                    </div>

                    <div className="flex flex-col gap-1 text-xs text-slate-600 bg-slate-50 p-2 rounded border border-slate-100">
                        <div className="flex justify-between items-center">
                            <span className="flex items-center gap-1"><Factory size={10}/> Productor:</span>
                            <span className="font-semibold truncate max-w-[100px]">{mr.productor_del_material_de_referencia || '-'}</span>
                        </div>
                        <div className="flex justify-between items-center">
                            <span className="flex items-center gap-1"><MapPin size={10}/> Procedencia:</span>
                            <span className="truncate max-w-[100px]">{mr.procedencia || '-'}</span>
                        </div>
                        <div className="flex justify-between items-center text-orange-700 font-medium mt-1 pt-1 border-t border-slate-200">
                            <span>Vencimiento:</span>
                            <span>{mr.fecha_de_vencimiento ? format(new Date(mr.fecha_de_vencimiento), 'yyyy-MM-dd') : '-'}</span>
                        </div>
                    </div>
                    
                    {/* Resumen de especificaciones */}
                    <div className="text-xs text-slate-500 flex items-center justify-between">
                         <span>Valores certificados:</span>
                         <Badge variant="secondary">{mr.pa_eq_mv_items?.length || 0}</Badge>
                    </div>
                </CardContent>
                <CardFooter className="flex justify-between gap-2 pt-2 border-t mt-2 bg-slate-50/50">
                    <Button variant="outline" size="sm" className="flex-1 text-xs" onClick={() => handleOpenSpecs(mr)}>
                        <List className="mr-2 h-3 w-3" /> Valores
                    </Button>
                    <div className="flex gap-1">
                        <Button variant="ghost" size="sm" onClick={() => handleEditMR(mr)}>
                            <Pencil className="h-4 w-4 text-slate-500" />
                        </Button>
                        <Button variant="ghost" size="sm" onClick={() => setDeleteId(mr.id)}>
                            <Trash className="h-4 w-4 text-red-500" />
                        </Button>
                    </div>
                </CardFooter>
            </Card>
        ))}
      </div>

      {/* --- MODAL 1: ADMINISTRATIVO (DATOS DEL MATERIAL) --- */}
      <Dialog open={isMRDialogOpen} onOpenChange={setIsMRDialogOpen}>
        <DialogContent className="sm:max-w-[800px] max-h-[90vh] overflow-y-auto">
          <DialogHeader>
            <DialogTitle>{editingMR ? "Editar Ficha de Material" : "Alta de Nuevo Material"}</DialogTitle>
            <DialogDescription>Complete los datos de trazabilidad del patrón o reactivo.</DialogDescription>
          </DialogHeader>

          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmitMR)} className="space-y-4">
                
                {/* BLOQUE 1: IDENTIFICACIÓN CLAVE */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <FormField control={form.control} name="codigo_interno" render={({ field }) => (
                        <FormItem><FormLabel>Código Interno (ID) *</FormLabel><FormControl><Input placeholder="Ej: MR-PH-01" {...field} disabled={!!editingMR} /></FormControl></FormItem>
                    )}/>
                    <FormField control={form.control} name="codigo_original" render={({ field }) => (
                        <FormItem><FormLabel>Código Original (Fabr.)</FormLabel><FormControl><Input placeholder="Ej: CRM-1234" {...field} /></FormControl></FormItem>
                    )}/>
                    <FormField control={form.control} name="tipo" render={({ field }) => (
                        <FormItem>
                            <FormLabel>Tipo de Material</FormLabel>
                            <Select onValueChange={field.onChange} value={field.value}>
                                <FormControl><SelectTrigger><SelectValue placeholder="Seleccione..." /></SelectTrigger></FormControl>
                                <SelectContent>
                                    <SelectItem value="CRM">CRM (Certificado)</SelectItem>
                                    <SelectItem value="RM">RM (Referencia)</SelectItem>
                                    <SelectItem value="Patron Secundario">Patrón Secundario</SelectItem>
                                    <SelectItem value="Reactivo Critico">Reactivo Crítico</SelectItem>
                                    <SelectItem value="Estandar de Trabajo">Estándar de Trabajo</SelectItem>
                                </SelectContent>
                            </Select>
                        </FormItem>
                    )}/>
                </div>

                {/* BLOQUE 2: DETALLES DEL PRODUCTO */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 bg-slate-50 p-4 rounded-md border border-slate-200">
                    <FormField control={form.control} name="material" render={({ field }) => (
                        <FormItem>
                            <FormLabel className="flex items-center gap-2"><Beaker size={14}/> Matriz / Estado Físico</FormLabel>
                            <Select onValueChange={field.onChange} value={field.value}>
                                <FormControl><SelectTrigger><SelectValue placeholder="Seleccione..." /></SelectTrigger></FormControl>
                                <SelectContent>
                                    <SelectItem value="Liquido">Líquido (Solución)</SelectItem>
                                    <SelectItem value="Solido Polvo">Sólido (Polvo)</SelectItem>
                                    <SelectItem value="Solido Granulado">Sólido (Granulado/Pieza)</SelectItem>
                                    <SelectItem value="Gaseoso">Gaseoso</SelectItem>
                                    <SelectItem value="Gel">Gel / Pasta</SelectItem>
                                    <SelectItem value="Filtro">Filtro / Membrana</SelectItem>
                                </SelectContent>
                            </Select>
                        </FormItem>
                    )}/>
                    <FormField control={form.control} name="comentarios" render={({ field }) => (
                        <FormItem><FormLabel>Nombre / Descripción</FormLabel><FormControl><Input placeholder="Ej: Solución Buffer pH 4.01..." {...field} /></FormControl></FormItem>
                    )}/>
                    
                    <FormField control={form.control} name="productor_del_material_de_referencia" render={({ field }) => (
                        <FormItem><FormLabel>Productor / Fabricante</FormLabel><FormControl><Input placeholder="Ej: Merck, NIST..." {...field} /></FormControl></FormItem>
                    )}/>
                    <FormField control={form.control} name="procedencia" render={({ field }) => (
                        <FormItem><FormLabel>Procedencia / Origen</FormLabel><FormControl><Input placeholder="Ej: Alemania, USA..." {...field} /></FormControl></FormItem>
                    )}/>
                </div>

                {/* BLOQUE 3: TRAZABILIDAD Y LOTES */}
                <div className="grid grid-cols-3 gap-4">
                    <FormField control={form.control} name="certificado" render={({ field }) => (
                        <FormItem><FormLabel>Nro. Certificado</FormLabel><FormControl><Input placeholder="Ej: CERT-2024-X" {...field} /></FormControl></FormItem>
                    )}/>
                    <FormField control={form.control} name="serie" render={({ field }) => (
                        <FormItem><FormLabel>Lote / Serie</FormLabel><FormControl><Input placeholder="Lote..." {...field} /></FormControl></FormItem>
                    )}/>
                    <FormField control={form.control} name="ubicacion" render={({ field }) => (
                        <FormItem><FormLabel>Ubicación Física</FormLabel><FormControl><Input placeholder="Ej: Nevera 1, Estante 2..." {...field} /></FormControl></FormItem>
                    )}/>
                </div>

                {/* BLOQUE 4: FECHAS (EDITABLES MANUALMENTE) */}
                <div className="grid grid-cols-3 gap-4 border-t pt-4">
                     <FormField
                        control={form.control}
                        name="fecha_de_certificado"
                        render={({ field }) => (
                            <ManualDatePicker 
                                value={field.value} 
                                onChange={field.onChange} 
                                label="F. Emisión Cert." 
                            />
                        )}
                    />
                    <FormField
                        control={form.control}
                        name="fecha_de_apertura"
                        render={({ field }) => (
                            <ManualDatePicker 
                                value={field.value} 
                                onChange={field.onChange} 
                                label="F. Apertura" 
                            />
                        )}
                    />
                    <FormField
                        control={form.control}
                        name="fecha_de_vencimiento"
                        render={({ field }) => (
                            <ManualDatePicker 
                                value={field.value} 
                                onChange={field.onChange} 
                                label="F. Vencimiento" 
                            />
                        )}
                    />
                </div>
                
                <div className="grid grid-cols-2 gap-4 pt-2">
                     <FormField control={form.control} name="estado" render={({ field }) => (
                        <FormItem>
                            <FormLabel>Estado Operativo</FormLabel>
                            <Select onValueChange={field.onChange} value={field.value}>
                                <FormControl><SelectTrigger><SelectValue /></SelectTrigger></FormControl>
                                <SelectContent>
                                    <SelectItem value="VIGENTE">VIGENTE</SelectItem>
                                    <SelectItem value="AGOTADO">AGOTADO</SelectItem>
                                    <SelectItem value="CADUCADO">CADUCADO</SelectItem>
                                    <SelectItem value="CUARENTENA">EN CUARENTENA</SelectItem>
                                </SelectContent>
                            </Select>
                        </FormItem>
                    )}/>
                </div>

                <div className="flex justify-end pt-4 border-t">
                    <Button type="submit" className="bg-blue-600 hover:bg-blue-700 w-full md:w-auto">
                        <Save className="mr-2 h-4 w-4" /> {editingMR ? "Guardar Cambios" : "Crear Ficha"}
                    </Button>
                </div>
            </form>
          </Form>
        </DialogContent>
      </Dialog>


      {/* --- MODAL 2: TÉCNICO (ESPECIFICACIONES / VALORES) --- */}
      <Dialog open={isMVDialogOpen} onOpenChange={setIsMVDialogOpen}>
        <DialogContent className="sm:max-w-[700px]">
            <DialogHeader>
                <DialogTitle className="flex items-center gap-2">
                    <TestTube className="h-5 w-5 text-purple-600"/> 
                    Valores Certificados
                </DialogTitle>
                <DialogDescription>
                    Gestión de parámetros para: <span className="font-bold text-slate-800">{activeTechnicalMR?.codigo_interno}</span>
                </DialogDescription>
            </DialogHeader>

            {activeTechnicalMR ? (
                <div className="space-y-6">
                    {/* Formulario pequeño para agregar */}
                    <div className="bg-slate-50 p-3 rounded-md border border-slate-200 grid grid-cols-4 gap-2 items-end">
                        <div className="col-span-2 sm:col-span-1">
                            <label className="text-xs font-medium text-slate-500">Parámetro</label>
                            <Input 
                                placeholder="Ej: pH" 
                                className="h-8 text-sm" 
                                value={newParam} 
                                onChange={e => setNewParam(e.target.value)} 
                            />
                        </div>
                        <div className="col-span-2 sm:col-span-1">
                            <label className="text-xs font-medium text-slate-500">Valor</label>
                            <Input 
                                placeholder="0.00" 
                                className="h-8 text-sm" 
                                value={newVal} 
                                onChange={e => setNewVal(e.target.value)} 
                            />
                        </div>
                        <div className="col-span-2 sm:col-span-1">
                            <label className="text-xs font-medium text-slate-500">Incertidumbre (U)</label>
                            <Input 
                                placeholder="±" 
                                className="h-8 text-sm" 
                                value={newUncert} 
                                onChange={e => setNewUncert(e.target.value)} 
                            />
                        </div>
                        <div className="col-span-2 sm:col-span-1 flex gap-1">
                            <div className="w-full">
                                <label className="text-xs font-medium text-slate-500">Unidad</label>
                                <Input 
                                    placeholder="mg/L" 
                                    className="h-8 text-sm" 
                                    value={newUnit} 
                                    onChange={e => setNewUnit(e.target.value)} 
                                />
                            </div>
                            <Button onClick={handleAddMV} size="sm" className="bg-green-600 hover:bg-green-700 h-8 mt-auto px-2">
                                <Plus className="h-4 w-4" />
                            </Button>
                        </div>
                    </div>

                    {/* Tabla de valores */}
                    <div className="border rounded-md overflow-hidden max-h-[300px] overflow-y-auto">
                        <Table>
                            <TableHeader className="bg-slate-100">
                                <TableRow>
                                    <TableHead className="w-[150px]">Parámetro</TableHead>
                                    <TableHead>Valor</TableHead>
                                    <TableHead>Incertidumbre</TableHead>
                                    <TableHead>Unidad</TableHead>
                                    <TableHead className="w-[50px]"></TableHead>
                                </TableRow>
                            </TableHeader>
                            <TableBody>
                                {activeTechnicalMR.pa_eq_mv_items?.length === 0 ? (
                                    <TableRow>
                                        <TableCell colSpan={5} className="text-center text-slate-400 py-8">
                                            No hay especificaciones registradas.
                                        </TableCell>
                                    </TableRow>
                                ) : (
                                    activeTechnicalMR.pa_eq_mv_items?.map((mv: any) => (
                                        <TableRow key={mv.id}>
                                            <TableCell className="font-medium">{mv.parametro}</TableCell>
                                            <TableCell>{mv.valor}</TableCell>
                                            <TableCell>± {mv.incertidumbre}</TableCell>
                                            <TableCell className="text-slate-500">{mv.unidad}</TableCell>
                                            <TableCell>
                                                <Button 
                                                    variant="ghost" 
                                                    size="sm" 
                                                    className="h-6 w-6 p-0 text-red-500 hover:bg-red-50"
                                                    onClick={() => deleteMVMutation.mutate(mv.id)}
                                                >
                                                    <Trash className="h-3 w-3" />
                                                </Button>
                                            </TableCell>
                                        </TableRow>
                                    ))
                                )}
                            </TableBody>
                        </Table>
                    </div>
                </div>
            ) : (
                <div className="p-4 text-center text-red-500">Error: No se encontró el material seleccionado.</div>
            )}
        </DialogContent>
      </Dialog>

      {/* MODAL DE CONFIRMACIÓN DE ELIMINAR */}
      <AlertDialog open={!!deleteId} onOpenChange={() => setDeleteId(null)}>
        <AlertDialogContent>
            <AlertDialogTitle>¿Eliminar Material de Referencia?</AlertDialogTitle>
            <AlertDialogDescription>
                Esta acción es irreversible. Se eliminará el material y todas sus especificaciones asociadas.
            </AlertDialogDescription>
            <AlertDialogFooter>
                <AlertDialogCancel>Cancelar</AlertDialogCancel>
                <AlertDialogAction className="bg-red-600" onClick={() => { if(deleteId) deleteMRMutation.mutate(deleteId); setDeleteId(null); }}>
                    Eliminar Definitivamente
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>

    </div>
  );
};