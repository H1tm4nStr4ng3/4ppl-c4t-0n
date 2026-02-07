import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { format, isValid, parseISO } from "date-fns";
import { es } from "date-fns/locale";
import { CalendarIcon, Save } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Calendar } from "@/components/ui/calendar";
import { Checkbox } from "@/components/ui/checkbox";
import {
  Form, FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage,
} from "@/components/ui/form";
import {
  Popover, PopoverContent, PopoverTrigger,
} from "@/components/ui/popover";
import {
    Select, SelectContent, SelectItem, SelectTrigger, SelectValue,
} from "@/components/ui/select";

import { personalSchema, PersonalFormValues } from "./personal-schema";
import { useCargos } from "../hooks/useCargos";

interface Props {
    defaultValues?: Partial<PersonalFormValues>;
    onSubmit: (data: PersonalFormValues) => void;
}

export const PersonalGeneralForm = ({ defaultValues, onSubmit }: Props) => {
  const { cargos, isLoading: loadingCargos } = useCargos();
  const [dateInputValue, setDateInputValue] = useState("");

  const form = useForm<PersonalFormValues>({
    resolver: zodResolver(personalSchema),
    defaultValues: defaultValues || {
      vigente: true,
      nacionalidad: "Boliviana",
    },
  });

  // Sincronizar input manual de fecha
  useEffect(() => {
    const currentDate = form.getValues("fecha_de_nacimiento");
    if (currentDate) {
        setDateInputValue(format(currentDate, "yyyy-MM-dd"));
    }
  }, [form.watch("fecha_de_nacimiento")]);

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit, (errors) => console.log("❌ Errores de validación:", errors))} 
        className="space-y-8"
        >
        
        {/* BLOQUE 1: IDENTIDAD Y CARGO */}
        <div className="space-y-4">
            <h3 className="text-lg font-bold text-slate-800 border-b border-slate-200 pb-2 mb-4">
                1. Identidad Corporativa
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-12 gap-6">
                
                {/* ID - Ancho pequeño */}
                <div className="md:col-span-2">
                    <FormField
                        control={form.control}
                        name="abreviatura"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Abreviatura (ID)</FormLabel>
                                <FormControl>
                                    <Input 
                                        placeholder="Ej: VGR" 
                                        {...field} 
                                        disabled={!!defaultValues?.abreviatura} 
                                        className="uppercase font-mono font-bold bg-slate-50"
                                        onChange={(e) => field.onChange(e.target.value.toUpperCase())}
                                        maxLength={5}
                                    /> 
                                </FormControl>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                </div>

                {/* Nombre - Ancho grande */}
                <div className="md:col-span-6">
                    <FormField
                        control={form.control}
                        name="nombre"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Nombre Completo</FormLabel>
                                <FormControl><Input placeholder="Nombres y Apellidos" {...field} value={field.value || ''}/></FormControl>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                </div>

                {/* Cargo - Ancho medio */}
                <div className="md:col-span-4">
                    <FormField
                        control={form.control}
                        name="cargo"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Cargo</FormLabel>
                                <Select onValueChange={field.onChange} value={field.value}>
                                    <FormControl>
                                    <SelectTrigger>
                                        <SelectValue placeholder={loadingCargos ? "Cargando..." : "Seleccione..."} />
                                    </SelectTrigger>
                                    </FormControl>
                                    <SelectContent>
                                        {cargos.map((c: any) => (
                                            <SelectItem key={c.abreviacion} value={c.abreviacion}>
                                                {c.cargo}
                                            </SelectItem>
                                        ))}
                                    </SelectContent>
                                </Select>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                </div>
            </div>
        </div>

        {/* BLOQUE 2: DOCUMENTACIÓN LEGAL (NUEVO) */}
        <div className="space-y-4">
            <h3 className="text-lg font-bold text-slate-800 border-b border-slate-200 pb-2 mb-4">
                2. Documentación Legal
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
                <FormField
                    control={form.control}
                    name="documento_de_identidad"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>CI / DNI / Pasaporte</FormLabel>
                            <FormControl><Input {...field} value={field.value || ''} /></FormControl>
                        </FormItem>
                    )}
                />
                
                {/* FECHA (Mantenemos la lógica arreglada) */}
                <FormField
                    control={form.control}
                    name="fecha_de_nacimiento"
                    render={({ field }) => (
                        <FormItem className="flex flex-col">
                            <FormLabel>Fecha de Nacimiento</FormLabel>
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
                                                    if (isValid(date) && val.length === 10) {
                                                        field.onChange(date);
                                                    } else if (val === "") {
                                                        field.onChange(undefined);
                                                    }
                                                }}
                                                placeholder="AAAA-MM-DD"
                                                className="pl-10 w-full"
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
                                        onSelect={(date) => field.onChange(date)}
                                        disabled={(date) => date > new Date() || date < new Date("1900-01-01")}
                                        initialFocus
                                        locale={es}
                                        captionLayout="dropdown-buttons"
                                        fromYear={1950}
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
                    name="nacionalidad"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Nacionalidad</FormLabel>
                            <FormControl><Input placeholder="Ej: Boliviana" {...field} value={field.value || ''} /></FormControl>
                        </FormItem>
                    )}
                />

                <FormField
                    control={form.control}
                    name="estado_civil"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Estado Civil</FormLabel>
                            <Select onValueChange={field.onChange} value={field.value || ""}>
                                <FormControl>
                                    <SelectTrigger><SelectValue placeholder="Seleccione..." /></SelectTrigger>
                                </FormControl>
                                <SelectContent>
                                    <SelectItem value="Soltero(a)">Soltero(a)</SelectItem>
                                    <SelectItem value="Casado(a)">Casado(a)</SelectItem>
                                    <SelectItem value="Divorciado(a)">Divorciado(a)</SelectItem>
                                    <SelectItem value="Viudo(a)">Viudo(a)</SelectItem>
                                </SelectContent>
                            </Select>
                        </FormItem>
                    )}
                />
            </div>
        </div>

        {/* BLOQUE 3: INFORMACIÓN DE CONTACTO (EXPANDIDO) */}
        <div className="space-y-4">
            <h3 className="text-lg font-bold text-slate-800 border-b border-slate-200 pb-2 mb-4">
                3. Información de Contacto
            </h3>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-4">
                {/* Columna Corporativa */}
                <div className="space-y-4 p-4 bg-slate-50 rounded-lg border border-slate-100">
                    <h4 className="font-semibold text-slate-600 text-sm uppercase">Corporativo</h4>
                    <FormField
                        control={form.control}
                        name="email_corporativo"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Email Corporativo</FormLabel>
                                <FormControl><Input placeholder="@empresa.com" {...field} value={field.value || ''} /></FormControl>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    <div className="grid grid-cols-2 gap-4">
                        <FormField
                            control={form.control}
                            name="telefono_corporativo"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Teléfono Fijo</FormLabel>
                                    <FormControl><Input {...field} value={field.value || ''} /></FormControl>
                                </FormItem>
                            )}
                        />
                        <FormField
                            control={form.control}
                            name="movil_corporativo"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Móvil Corp.</FormLabel>
                                    <FormControl><Input {...field} value={field.value || ''} /></FormControl>
                                </FormItem>
                            )}
                        />
                    </div>
                </div>

                {/* Columna Personal */}
                <div className="space-y-4 p-4 bg-white rounded-lg border border-slate-200">
                    <h4 className="font-semibold text-slate-600 text-sm uppercase">Personal</h4>
                    <FormField
                        control={form.control}
                        name="email_personal"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Email Personal</FormLabel>
                                <FormControl><Input placeholder="@gmail.com" {...field} value={field.value || ''} /></FormControl>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    <div className="grid grid-cols-2 gap-4">
                        <FormField
                            control={form.control}
                            name="telefono_personal"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Teléfono Casa</FormLabel>
                                    <FormControl><Input {...field} value={field.value || ''} /></FormControl>
                                </FormItem>
                            )}
                        />
                        <FormField
                            control={form.control}
                            name="movil_personal"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Móvil Personal</FormLabel>
                                    <FormControl><Input {...field} value={field.value || ''} /></FormControl>
                                </FormItem>
                            )}
                        />
                    </div>
                </div>

                {/* Dirección - Ocupa todo el ancho */}
                <div className="md:col-span-2">
                    <FormField
                        control={form.control}
                        name="direccion"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Dirección de Domicilio</FormLabel>
                                <FormControl><Textarea rows={2} {...field} value={field.value || ''} /></FormControl>
                            </FormItem>
                        )}
                    />
                </div>
            </div>
        </div>

        {/* BLOQUE 4: OTROS DATOS */}
        <div className="space-y-4">
            <h3 className="text-lg font-bold text-slate-800 border-b border-slate-200 pb-2 mb-4">
                4. Datos Adicionales
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <FormField
                    control={form.control}
                    name="categoria_de_licencia_de_conducir"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Licencia de Conducir (Categoría)</FormLabel>
                            <Select onValueChange={field.onChange} value={field.value || ""}>
                                <FormControl>
                                    <SelectTrigger><SelectValue placeholder="Ninguna / Seleccione" /></SelectTrigger>
                                </FormControl>
                                <SelectContent>
                                    <SelectItem value="P">Particular (P)</SelectItem>
                                    <SelectItem value="A">Motocicleta (A)</SelectItem>
                                    <SelectItem value="B">Profesional (B)</SelectItem>
                                    <SelectItem value="C">Profesional (C)</SelectItem>
                                    <SelectItem value="M">Maquinaria (M)</SelectItem>
                                    <SelectItem value="Ninguna">Ninguna</SelectItem>
                                </SelectContent>
                            </Select>
                        </FormItem>
                    )}
                />
                
                <FormField
                    control={form.control}
                    name="vigente"
                    render={({ field }) => (
                        <FormItem className="flex flex-row items-start space-x-3 space-y-0 rounded-md border p-4">
                            <FormControl>
                                <Checkbox checked={field.value} onCheckedChange={field.onChange} />
                            </FormControl>
                            <div className="space-y-1 leading-none">
                                <FormLabel>
                                    Empleado Vigente
                                </FormLabel>
                                <FormDescription>
                                    Desmarcar si el empleado ya no trabaja en la empresa.
                                </FormDescription>
                            </div>
                        </FormItem>
                    )}
                />

                <div className="md:col-span-2">
                     <FormField
                        control={form.control}
                        name="descripcion"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Observaciones / Notas del Perfil</FormLabel>
                                <FormControl><Textarea placeholder="Información extra relevante..." {...field} value={field.value || ''} /></FormControl>
                            </FormItem>
                        )}
                    />
                </div>
            </div>
        </div>

        {/* BOTÓN DE GUARDADO FLOTANTE O FINAL */}
        <div className="flex justify-end pt-6 sticky bottom-0 bg-white/80 backdrop-blur-sm p-4 border-t">
            <Button type="submit" size="lg" className="bg-blue-600 hover:bg-blue-700 shadow-lg">
                <Save className="mr-2 h-5 w-5" />
                Guardar Ficha de Personal
            </Button>
        </div>
      </form>
    </Form>
  );
};