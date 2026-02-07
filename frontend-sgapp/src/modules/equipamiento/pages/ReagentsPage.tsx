import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { format, isValid, parseISO } from "date-fns";
import { 
  Plus, CalendarIcon, Trash, Pencil, History, 
  ArrowDown, ArrowUp, Beaker, MapPin, Tag, AlertTriangle
} from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Badge } from "@/components/ui/badge";
import { Switch } from "@/components/ui/switch"; // Importante para sustancia controlada
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

import { useReagents, reagentSchema, ReagentFormValues, movementSchema, MovementFormValues } from "../hooks/useReagents";

// --- COMPONENTE DE FECHA MANUAL ---
const ManualDatePicker = ({ value, onChange, label }: { value: any, onChange: (d: any) => void, label: string }) => {
    const [inputValue, setInputValue] = useState("");
    
    useEffect(() => {
        if (value) setInputValue(format(new Date(value), "yyyy-MM-dd"));
        else setInputValue("");
    }, [value]);

    const handleInputChange = (e: any) => {
        setInputValue(e.target.value);
        if (e.target.value.trim() === "") { onChange(undefined); return; }
        const parsed = parseISO(e.target.value);
        if (isValid(parsed) && e.target.value.length === 10) onChange(parsed);
    };

    return (
        <FormItem className="flex flex-col">
            <FormLabel>{label}</FormLabel>
            <Popover>
                <PopoverTrigger asChild>
                    <FormControl>
                        <div className="relative flex items-center w-full">
                            <Input value={inputValue} onChange={handleInputChange} placeholder="AAAA-MM-DD" className="pl-10 font-mono" maxLength={10} />
                            <CalendarIcon className="absolute left-3 h-4 w-4 opacity-50 pointer-events-none" />
                        </div>
                    </FormControl>
                </PopoverTrigger>
                <PopoverContent className="w-auto p-0" align="start">
                    <Calendar mode="single" selected={value || undefined} onSelect={onChange} initialFocus />
                </PopoverContent>
            </Popover>
        </FormItem>
    );
};

export const ReagentsPage = () => {
  const { 
    reagents, isLoading, 
    createReagentMutation, updateReagentMutation, deleteReagentMutation,
    createMovementMutation
  } = useReagents();

  const [isDialogOpen, setIsDialogOpen] = useState(false); // Admin
  const [isLogOpen, setIsLogOpen] = useState(false); // Bitácora
  const [editingItem, setEditingItem] = useState<any>(null);
  const [selectedLogItem, setSelectedLogItem] = useState<any>(null);
  const [deleteId, setDeleteId] = useState<number | null>(null);

  // Formulario Reactivos (Padre)
  const form = useForm<ReagentFormValues>({
    resolver: zodResolver(reagentSchema),
    defaultValues: {
      nombre_reactivo: "", codigo_interno: "", marca: "", estado: "VIGENTE",
      unidad_almacen: "ml", unidad: "", valor: "", stock_minimo: "",
      no_articulo: "", grado_calidad: "", proveedor: "", serie: "", ubicacion: "", comentarios: "",
      sustancia_controlada: false
    },
  });

  // Formulario Bitácora (Hijo)
  const logForm = useForm<MovementFormValues>({
      resolver: zodResolver(movementSchema),
      defaultValues: {
          tipo_movimiento: "SALIDA",
          cantidad: "",
          registrado_por: "Usuario Actual", 
          fecha_movimiento: new Date(),
          observaciones: ""
      }
  });

  // Buscar la versión más reciente del reactivo seleccionado para la bitácora
  // Usamos una búsqueda segura por ID
  const activeReagent = reagents.find((r: any) => {
      const rId = r.id || r.id_reactivo;
      const sId = selectedLogItem?.id || selectedLogItem?.id_reactivo;
      return rId === sId;
  });

  // --- MANEJADORES ---

  const handleCreate = () => {
      setEditingItem(null);
      form.reset({ 
        nombre_reactivo: "", codigo_interno: "", marca: "", estado: "VIGENTE",
        unidad_almacen: "ml", unidad: "", valor: "", stock_minimo: "",
        no_articulo: "", grado_calidad: "", proveedor: "", serie: "", ubicacion: "", comentarios: "",
        sustancia_controlada: false, fecha_de_apertura: null, fecha_de_vencimiento: null
      });
      setIsDialogOpen(true);
  };

  const handleEdit = (item: any) => {
      setEditingItem(item);
      const data = { ...item };
      
      // Conversión segura de fechas
      ['fecha_de_apertura', 'fecha_de_vencimiento'].forEach(k => {
          if (data[k]) data[k] = new Date(data[k]);
          else data[k] = null;
      });

      // Conversión segura de números a string para inputs
      data.valor = (data.valor !== null && data.valor !== undefined) ? String(data.valor) : "";
      data.stock_minimo = (data.stock_minimo !== null && data.stock_minimo !== undefined) ? String(data.stock_minimo) : "";
      
      // Limpieza de nulos en textos
      ['codigo_interno', 'no_articulo', 'marca', 'grado_calidad', 'proveedor', 'serie', 'ubicacion', 'comentarios'].forEach(field => {
          if (!data[field]) data[field] = "";
      });

      form.reset(data);
      setIsDialogOpen(true);
  };

  const onSubmit = async (data: ReagentFormValues) => {
      if (editingItem) {
          // Aseguramos que el ID vaya en la petición
          const realId = editingItem.id || editingItem.id_reactivo;
          await updateReagentMutation.mutateAsync({ ...data, id: realId });
      } else {
          await createReagentMutation.mutateAsync(data);
      }
      setIsDialogOpen(false);
  };

  const handleOpenLog = (item: any) => {
      setSelectedLogItem(item);
      logForm.reset({
        tipo_movimiento: "SALIDA",
        cantidad: "",
        registrado_por: "Usuario Actual",
        fecha_movimiento: new Date(),
        observaciones: ""
      });
      setIsLogOpen(true);
  };

  const onSubmitLog = async (data: MovementFormValues) => {
      if (!activeReagent) return;
      const realId = activeReagent.id || activeReagent.id_reactivo;
      
      await createMovementMutation.mutateAsync({
          ...data,
          id_reactivo: realId,
      });
      logForm.reset({ ...data, cantidad: "", observaciones: "" }); 
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      <div className="flex flex-col md:flex-row justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-slate-900">Reactivos y Sustancias</h1>
          <p className="text-slate-500">Control de inventario, stock y bitácora de consumo.</p>
        </div>
        <Button onClick={handleCreate} className="bg-blue-600 hover:bg-blue-700">
            <Plus className="mr-2 h-4 w-4" /> Nuevo Reactivo
        </Button>
      </div>

      {/* LISTA DE REACTIVOS */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {isLoading && <div className="col-span-3 text-center p-10">Cargando inventario...</div>}
          
          {reagents.map((item: any) => {
              // DETECCIÓN INTELIGENTE DE ID
              const realId = item.id || item.id_reactivo;
              
              return (
              <Card key={realId} className={`border-t-4 ${item.sustancia_controlada ? 'border-t-red-500' : 'border-t-blue-500'} hover:shadow-md transition-shadow flex flex-col justify-between`}>
                  <CardHeader className="pb-2">
                      <div className="flex justify-between items-start">
                          <Badge variant={item.sustancia_controlada ? "destructive" : "outline"} className="text-xs truncate max-w-[150px]">
                              {item.sustancia_controlada ? "CONTROLADO" : (item.marca || 'Genérico')}
                          </Badge>
                          <Badge className={item.valor <= item.stock_minimo ? "bg-red-500" : "bg-green-600"}>
                              Stock: {item.valor} {item.unidad_almacen}
                          </Badge>
                      </div>
                      <CardTitle className="text-lg font-bold truncate" title={item.nombre_reactivo}>
                          {item.nombre_reactivo}
                      </CardTitle>
                      <CardDescription className="flex items-center gap-2 text-xs">
                          <Tag size={12}/> {item.codigo_interno || 'S/C'} | {item.grado_calidad || 'N/A'}
                      </CardDescription>
                  </CardHeader>
                  <CardContent className="text-sm space-y-2">
                      <div className="grid grid-cols-2 gap-2 text-xs text-slate-600 bg-slate-50 p-2 rounded">
                          <div className="flex items-center gap-1">
                             <MapPin size={12}/> <span className="truncate">{item.ubicacion || 'Sin ubicación'}</span>
                          </div>
                          <div className="flex items-center gap-1">
                             <Beaker size={12}/> <span className="truncate">{item.no_articulo || 'Sin Ref.'}</span>
                          </div>
                      </div>
                      <div className="flex justify-between border-b pb-1 text-xs">
                          <span className="text-slate-500">Vencimiento:</span>
                          <span className={item.fecha_de_vencimiento && new Date(item.fecha_de_vencimiento) < new Date() ? "text-red-600 font-bold" : ""}>
                             {item.fecha_de_vencimiento ? format(new Date(item.fecha_de_vencimiento), 'yyyy-MM-dd') : '-'}
                          </span>
                      </div>
                  </CardContent>
                  <CardFooter className="bg-slate-50/50 pt-2 flex justify-between gap-2 border-t">
                      <Button variant="outline" size="sm" className="flex-1" onClick={() => handleOpenLog({ ...item, id: realId })}>
                          <History className="mr-2 h-3 w-3" /> Bitácora
                      </Button>
                      <div className="flex gap-1">
                          {/* Pasamos el objeto con el ID asegurado */}
                          <Button variant="ghost" size="sm" onClick={() => handleEdit({ ...item, id: realId })}>
                              <Pencil className="h-4 w-4 text-slate-500"/>
                          </Button>
                          <Button variant="ghost" size="sm" onClick={() => setDeleteId(realId)}>
                              <Trash className="h-4 w-4 text-red-500"/>
                          </Button>
                      </div>
                  </CardFooter>
              </Card>
              );
          })}
      </div>

      {/* MODAL 1: ADMIN (CREAR/EDITAR) */}
      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
          <DialogContent className="sm:max-w-[800px] max-h-[90vh] overflow-y-auto">
              <DialogHeader><DialogTitle>{editingItem ? "Editar Ficha de Reactivo" : "Alta de Nuevo Reactivo"}</DialogTitle></DialogHeader>
              <Form {...form}>
                  <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                      
                      {/* 1. Identificación */}
                      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                          <FormField control={form.control} name="nombre_reactivo" render={({ field }) => (
                              <FormItem className="md:col-span-2"><FormLabel>Nombre Reactivo *</FormLabel><FormControl><Input placeholder="Ej: Ácido Clorhídrico 37%" {...field} /></FormControl></FormItem>
                          )}/>
                          <FormField control={form.control} name="codigo_interno" render={({ field }) => (
                              <FormItem><FormLabel>Código Interno</FormLabel><FormControl><Input placeholder="Ej: RE-001" {...field} /></FormControl></FormItem>
                          )}/>
                      </div>

                      {/* 2. Detalles Técnicos */}
                      <div className="grid grid-cols-3 gap-4 bg-slate-50 p-3 rounded border">
                          <FormField control={form.control} name="no_articulo" render={({ field }) => (
                              <FormItem><FormLabel>N° Artículo / CAS</FormLabel><FormControl><Input placeholder="Ej: 7647-01-0" {...field} /></FormControl></FormItem>
                          )}/>
                          <FormField control={form.control} name="grado_calidad" render={({ field }) => (
                              <FormItem><FormLabel>Grado / Pureza</FormLabel><FormControl><Input placeholder="Ej: PA, HPLC..." {...field} /></FormControl></FormItem>
                          )}/>
                           <FormField control={form.control} name="estado" render={({ field }) => (
                              <FormItem>
                                  <FormLabel>Estado</FormLabel>
                                  <Select onValueChange={field.onChange} value={field.value}>
                                      <FormControl><SelectTrigger><SelectValue/></SelectTrigger></FormControl>
                                      <SelectContent>
                                          <SelectItem value="VIGENTE">VIGENTE</SelectItem>
                                          <SelectItem value="AGOTADO">AGOTADO</SelectItem>
                                          <SelectItem value="CADUCADO">CADUCADO</SelectItem>
                                      </SelectContent>
                                  </Select>
                              </FormItem>
                          )}/>
                      </div>
                      
                      {/* 3. Datos del Fabricante */}
                      <div className="grid grid-cols-3 gap-4">
                          <FormField control={form.control} name="marca" render={({ field }) => (
                              <FormItem><FormLabel>Marca</FormLabel><FormControl><Input placeholder="Ej: Merck" {...field} /></FormControl></FormItem>
                          )}/>
                          <FormField control={form.control} name="proveedor" render={({ field }) => (
                              <FormItem><FormLabel>Proveedor</FormLabel><FormControl><Input placeholder="Ej: Droguería X" {...field} /></FormControl></FormItem>
                          )}/>
                          <FormField control={form.control} name="serie" render={({ field }) => (
                              <FormItem><FormLabel>Lote / Serie</FormLabel><FormControl><Input placeholder="Lote..." {...field} /></FormControl></FormItem>
                          )}/>
                      </div>

                      {/* 4. Stock e Inventario */}
                      <div className="grid grid-cols-3 gap-4">
                          <FormField control={form.control} name="valor" render={({ field }) => (
                              <FormItem><FormLabel>Stock Actual</FormLabel><FormControl><Input type="number" step="0.01" {...field} /></FormControl></FormItem>
                          )}/>
                          <FormField control={form.control} name="unidad_almacen" render={({ field }) => (
                              <FormItem>
                                  <FormLabel>Unidad Medida</FormLabel>
                                  <Select onValueChange={field.onChange} value={field.value || "ml"}>
                                      <FormControl><SelectTrigger><SelectValue /></SelectTrigger></FormControl>
                                      <SelectContent>
                                          <SelectItem value="ml">Mililitros (ml)</SelectItem>
                                          <SelectItem value="l">Litros (L)</SelectItem>
                                          <SelectItem value="gr">Gramos (g)</SelectItem>
                                          <SelectItem value="kg">Kilogramos (kg)</SelectItem>
                                          <SelectItem value="unidad">Unidad</SelectItem>
                                      </SelectContent>
                                  </Select>
                              </FormItem>
                          )}/>
                           <FormField control={form.control} name="stock_minimo" render={({ field }) => (
                              <FormItem><FormLabel>Stock Mínimo</FormLabel><FormControl><Input type="number" {...field} /></FormControl></FormItem>
                          )}/>
                      </div>

                      <div className="grid grid-cols-2 gap-4">
                          <FormField control={form.control} name="unidad" render={({ field }) => (
                              <FormItem><FormLabel>Presentación Comercial</FormLabel><FormControl><Input placeholder="Ej: Frasco vidrio 1L" {...field} /></FormControl></FormItem>
                          )}/>
                          <FormField control={form.control} name="ubicacion" render={({ field }) => (
                              <FormItem><FormLabel>Ubicación Física</FormLabel><FormControl><Input placeholder="Ej: Estante Ácidos" {...field} /></FormControl></FormItem>
                          )}/>
                      </div>

                      {/* 5. Fechas */}
                      <div className="grid grid-cols-2 gap-4 border-t pt-2">
                           <FormField control={form.control} name="fecha_de_apertura" render={({ field }) => (
                              <ManualDatePicker value={field.value} onChange={field.onChange} label="Fecha Apertura" />
                          )}/>
                          <FormField control={form.control} name="fecha_de_vencimiento" render={({ field }) => (
                              <ManualDatePicker value={field.value} onChange={field.onChange} label="Fecha Vencimiento" />
                          )}/>
                      </div>
                      
                      <FormField control={form.control} name="comentarios" render={({ field }) => (
                          <FormItem><FormLabel>Observaciones / Comentarios</FormLabel><FormControl><Textarea className="h-10" {...field} /></FormControl></FormItem>
                      )}/>

                      {/* CHECK DE SUSTANCIA CONTROLADA */}
                      <FormField
                          control={form.control}
                          name="sustancia_controlada"
                          render={({ field }) => (
                              <FormItem className="flex flex-row items-center justify-between rounded-lg border p-4 shadow-sm mt-4 bg-red-50 border-red-100">
                                  <div className="space-y-0.5">
                                      <FormLabel className="text-base font-bold text-red-900 flex items-center gap-2">
                                          <AlertTriangle size={16}/> Sustancia Controlada
                                      </FormLabel>
                                      <DialogDescription className="text-red-700 text-xs">
                                          Activar si este reactivo requiere fiscalización especial.
                                      </DialogDescription>
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

                      <Button type="submit" className="w-full bg-blue-600">Guardar Ficha de Reactivo</Button>
                  </form>
              </Form>
          </DialogContent>
      </Dialog>

      {/* MODAL 2: BITÁCORA (MOVIMIENTOS) */}
      <Dialog open={isLogOpen} onOpenChange={setIsLogOpen}>
          <DialogContent className="sm:max-w-[800px]">
              <DialogHeader>
                  <DialogTitle className="flex items-center gap-2"><History/> Bitácora de Movimientos</DialogTitle>
                  <DialogDescription>Historial para: <strong>{activeReagent?.nombre_reactivo}</strong></DialogDescription>
              </DialogHeader>
              
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  {/* Formulario de Registro */}
                  <div className="md:col-span-1 border-r pr-4 space-y-4">
                      <h4 className="font-bold text-sm">Registrar Movimiento</h4>
                      <Form {...logForm}>
                          <form onSubmit={logForm.handleSubmit(onSubmitLog)} className="space-y-3">
                              <FormField control={logForm.control} name="tipo_movimiento" render={({ field }) => (
                                  <FormItem>
                                      <FormLabel>Acción</FormLabel>
                                      <Select onValueChange={field.onChange} value={field.value}>
                                          <FormControl><SelectTrigger><SelectValue/></SelectTrigger></FormControl>
                                          <SelectContent>
                                              <SelectItem value="SALIDA">Salida / Consumo</SelectItem>
                                              <SelectItem value="ENTRADA">Entrada / Compra</SelectItem>
                                              <SelectItem value="AJUSTE">Ajuste Inventario</SelectItem>
                                          </SelectContent>
                                      </Select>
                                  </FormItem>
                              )}/>
                              <FormField control={logForm.control} name="cantidad" render={({ field }) => (
                                  <FormItem><FormLabel>Cantidad ({activeReagent?.unidad_almacen})</FormLabel><FormControl><Input type="number" step="0.01" {...field} /></FormControl></FormItem>
                              )}/>
                              <FormField control={logForm.control} name="fecha_movimiento" render={({ field }) => (
                                  <ManualDatePicker value={field.value} onChange={field.onChange} label="Fecha" />
                              )}/>
                              <FormField control={logForm.control} name="observaciones" render={({ field }) => (
                                  <FormItem><FormLabel>Observación</FormLabel><FormControl><Textarea className="h-20" {...field} /></FormControl></FormItem>
                              )}/>
                              <Button type="submit" className="w-full bg-slate-800">Registrar</Button>
                          </form>
                      </Form>
                  </div>

                  {/* Tabla Histórica */}
                  <div className="md:col-span-2 max-h-[400px] overflow-y-auto">
                      <Table>
                          <TableHeader>
                              <TableRow><TableHead>Fecha</TableHead><TableHead>Tipo</TableHead><TableHead>Cant.</TableHead><TableHead>Obs.</TableHead></TableRow>
                          </TableHeader>
                          <TableBody>
                              {activeReagent?.pa_eq_mo_items?.length === 0 ? (
                                  <TableRow><TableCell colSpan={4} className="text-center text-slate-400">Sin movimientos.</TableCell></TableRow>
                              ) : (
                                  [...(activeReagent?.pa_eq_mo_items || [])].reverse().map((mov: any) => (
                                      <TableRow key={mov.id}>
                                          <TableCell className="text-xs">{format(new Date(mov.fecha_movimiento), 'yyyy-MM-dd')}</TableCell>
                                          <TableCell>
                                              <Badge variant="outline" className={mov.tipo_movimiento === 'ENTRADA' ? 'text-green-600 border-green-200' : 'text-orange-600 border-orange-200'}>
                                                  {mov.tipo_movimiento === 'ENTRADA' ? <ArrowUp size={10} className="mr-1"/> : <ArrowDown size={10} className="mr-1"/>}
                                                  {mov.tipo_movimiento}
                                              </Badge>
                                          </TableCell>
                                          <TableCell className="font-mono font-bold">{mov.cantidad}</TableCell>
                                          <TableCell className="text-xs text-slate-500 truncate max-w-[100px]" title={mov.observaciones}>{mov.observaciones || '-'}</TableCell>
                                      </TableRow>
                                  ))
                              )}
                          </TableBody>
                      </Table>
                  </div>
              </div>
          </DialogContent>
      </Dialog>
      
      {/* Diálogo Eliminar */}
      <AlertDialog open={!!deleteId} onOpenChange={() => setDeleteId(null)}>
        <AlertDialogContent>
            <AlertDialogTitle>¿Eliminar Reactivo?</AlertDialogTitle>
            <AlertDialogDescription>Se eliminará el reactivo y todo su historial de forma permanente.</AlertDialogDescription>
            <AlertDialogFooter>
                <AlertDialogCancel>Cancelar</AlertDialogCancel>
                <AlertDialogAction className="bg-red-600" onClick={() => { if(deleteId) deleteReagentMutation.mutate(deleteId); setDeleteId(null); }}>Eliminar</AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
};