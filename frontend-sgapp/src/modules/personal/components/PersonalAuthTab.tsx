import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { format, isValid, parseISO } from "date-fns";
import { es } from "date-fns/locale";
import { Plus, Trash, ShieldCheck, CalendarIcon, UserCheck, Pencil } from "lucide-react"; // Pencil

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "@/components/ui/table";
import {
  Dialog, DialogContent, DialogHeader, DialogTitle,
} from "@/components/ui/dialog";
import {
  Form, FormControl, FormField, FormItem, FormLabel, FormMessage,
} from "@/components/ui/form";
import {
    Select, SelectContent, SelectItem, SelectTrigger, SelectValue,
} from "@/components/ui/select";
import {
    Popover, PopoverContent, PopoverTrigger,
} from "@/components/ui/popover";
import { Calendar } from "@/components/ui/calendar";

import { usePersonalAuth, authSchema, AuthFormValues } from "../hooks/usePersonalAuth";
import { usePersonal } from "../hooks/usePersonal";
import { useCargos } from "../hooks/useCargos";

interface Props {
    personalId: string;
}

export const PersonalAuthTab = ({ personalId }: Props) => {
  const { items, isLoading, createMutation, updateMutation, deleteMutation } = usePersonalAuth(personalId);
  const { data: allPersonal } = usePersonal();
  const { cargos } = useCargos();
  
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [dateInputValue, setDateInputValue] = useState("");

  const form = useForm<AuthFormValues>({
    resolver: zodResolver(authSchema),
    defaultValues: {
      autorizado_a: personalId,
      autorizacion_a: "",
      comentario: "",
    },
  });

  useEffect(() => {
    const currentDate = form.getValues("fecha");
    if (currentDate) {
        setDateInputValue(format(currentDate, "yyyy-MM-dd"));
    } else {
        setDateInputValue("");
    }
  }, [form.watch("fecha"), isDialogOpen]);

  // CREAR
  const handleCreate = () => {
    setEditingId(null);
    form.reset({ autorizado_a: personalId, autorizacion_a: "", comentario: "" });
    setDateInputValue("");
    setIsDialogOpen(true);
  };

  // EDITAR
  const handleEdit = (item: any) => {
    setEditingId(item.id);
    form.reset({
        id: item.id,
        autorizado_a: item.autorizado_a,
        autorizado_por: item.autorizado_por,
        autorizacion_a: item.autorizacion_a,
        comentario: item.comentario || "",
        cargo: item.cargo || undefined,
        fecha: item.fecha ? new Date(item.fecha) : undefined
    });
    setIsDialogOpen(true);
  };

  const onSubmit = async (data: AuthFormValues) => {
    if (editingId) {
        await updateMutation.mutateAsync(data);
    } else {
        await createMutation.mutateAsync(data);
    }
    setIsDialogOpen(false);
  };

  if (isLoading) return <div className="p-4 text-center text-slate-500">Cargando...</div>;

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
            <h3 className="text-lg font-bold text-slate-800">Autorizaciones y Permisos</h3>
            <p className="text-sm text-slate-500">Actividades críticas autorizadas.</p>
        </div>
        <Button onClick={handleCreate} className="bg-blue-600 hover:bg-blue-700">
            <Plus className="mr-2 h-4 w-4" /> Nueva Autorización
        </Button>
      </div>

      <div className="border rounded-lg bg-white overflow-hidden shadow-sm">
        <Table>
            <TableHeader>
                <TableRow className="bg-slate-50">
                    <TableHead>Fecha</TableHead>
                    <TableHead>Autorizado Por</TableHead>
                    <TableHead>Actividad / Alcance</TableHead>
                    <TableHead>Cargo</TableHead>
                    <TableHead className="text-right">Acciones</TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                {items.length === 0 ? (
                    <TableRow><TableCell colSpan={5} className="text-center h-24 text-slate-400">Sin autorizaciones.</TableCell></TableRow>
                ) : items.map((item: any) => (
                    <TableRow key={item.id}>
                        <TableCell className="font-mono text-slate-600">
                             {item.fecha ? format(new Date(item.fecha), 'yyyy-MM-dd') : '-'}
                        </TableCell>
                        <TableCell>
                             <div className="flex items-center gap-2">
                                <UserCheck className="h-4 w-4 text-slate-400" />
                                <span className="font-medium text-slate-800">
                                    {allPersonal?.find((p: any) => p.abreviatura === item.autorizado_por)?.nombre || item.autorizado_por}
                                </span>
                             </div>
                        </TableCell>
                        <TableCell className="italic text-slate-700">{item.autorizacion_a}</TableCell>
                        <TableCell><span className="text-xs bg-slate-100 px-2 py-1 rounded">{item.cargo || '-'}</span></TableCell>
                        <TableCell className="text-right space-x-1">
                            <Button variant="ghost" size="sm" onClick={() => handleEdit(item)}>
                                <Pencil className="h-4 w-4 text-slate-500" />
                            </Button>
                            <Button variant="ghost" size="sm" onClick={() => deleteMutation.mutate(item.id)}>
                                <Trash className="h-4 w-4 text-red-500" />
                            </Button>
                        </TableCell>
                    </TableRow>
                ))}
            </TableBody>
        </Table>
      </div>

      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
        <DialogContent className="sm:max-w-[600px]">
            <DialogHeader>
                <DialogTitle>{editingId ? "Editar Autorización" : "Otorgar Autorización"}</DialogTitle>
            </DialogHeader>
            <Form {...form}>
                <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                    <div className="grid grid-cols-2 gap-4">
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
                                                onSelect={(date) => field.onChange(date)}
                                                disabled={(date) => date > new Date()}
                                                initialFocus
                                                captionLayout="dropdown-buttons"
                                                fromYear={2010} 
                                                toYear={new Date().getFullYear()}
                                            />
                                        </PopoverContent>
                                    </Popover>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                        <FormField
                            control={form.control}
                            name="autorizado_por"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Autorizado Por</FormLabel>
                                    <Select onValueChange={field.onChange} value={field.value}>
                                        <FormControl><SelectTrigger><SelectValue placeholder="Seleccione..." /></SelectTrigger></FormControl>
                                        <SelectContent>
                                            {allPersonal?.map((p: any) => (
                                                <SelectItem key={p.abreviatura} value={p.abreviatura}>{p.nombre}</SelectItem>
                                            ))}
                                        </SelectContent>
                                    </Select>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                    </div>

                    <FormField
                        control={form.control}
                        name="autorizacion_a"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Actividad Autorizada</FormLabel>
                                <FormControl><Textarea {...field} /></FormControl>
                                <FormMessage />
                            </FormItem>
                        )}
                    />

                    <div className="grid grid-cols-2 gap-4">
                        <FormField
                            control={form.control}
                            name="cargo"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Cargo (Contexto)</FormLabel>
                                    <Select onValueChange={field.onChange} value={field.value || undefined}>
                                        <FormControl><SelectTrigger><SelectValue placeholder="Opcional" /></SelectTrigger></FormControl>
                                        <SelectContent>
                                            {cargos?.map((c: any) => (
                                                <SelectItem key={c.abreviacion} value={c.abreviacion}>{c.cargo}</SelectItem>
                                            ))}
                                        </SelectContent>
                                    </Select>
                                </FormItem>
                            )}
                        />
                         <FormField
                            control={form.control}
                            name="comentario"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Observaciones</FormLabel>
                                    <FormControl><Input placeholder="Opcional" {...field} /></FormControl>
                                </FormItem>
                            )}
                        />
                    </div>

                    <div className="flex justify-end pt-4">
                        <Button type="submit" className="bg-blue-600">
                             {editingId ? "Guardar Cambios" : "Otorgar Permiso"}
                        </Button>
                    </div>
                </form>
            </Form>
        </DialogContent>
      </Dialog>
    </div>
  );
};