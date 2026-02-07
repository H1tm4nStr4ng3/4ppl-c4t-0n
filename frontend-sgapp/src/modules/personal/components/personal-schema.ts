import { z } from "zod";

// --- AYUDANTES PARA TOLERAR NULOS DE LA BD ---
// Esto convierte null, undefined o "" en undefined (que es lo que Zod prefiere para opcionales)
const nullableString = z.string().nullable().optional().transform(val => val || undefined);

// Para emails que pueden venir nulos o vacíos
const nullableEmail = z.union([z.string().email("Correo inválido"), z.literal(''), z.null()])
  .optional()
  .transform(e => (e === "" || e === null) ? undefined : e);

export const personalSchema = z.object({
  // --- Identidad (Obligatorios) ---
  abreviatura: z.string().min(2, "Mínimo 2 letras").max(5, "Máximo 5 letras"),
  nombre: z.string().min(3, "El nombre es muy corto"),
  cargo: z.string().min(1, "Debes seleccionar un cargo"),
  
  // --- Fechas ---
  // Toleramos string, Date o null
  fecha_de_nacimiento: z.preprocess((arg) => {
    if (typeof arg === "string" || arg instanceof Date) return new Date(arg);
    return arg;
  }, z.date({ required_error: "La fecha es obligatoria" })),
  
  vigente: z.boolean().default(true),

  // --- Campos Opcionales (Usamos el ayudante nullableString) ---
  // Esto arregla el error de "received null"
  documento_de_identidad: nullableString,
  nacionalidad: nullableString,
  estado_civil: nullableString,
  categoria_de_licencia_de_conducir: nullableString,

  // --- Contacto ---
  email_corporativo: nullableEmail,
  telefono_corporativo: nullableString,
  movil_corporativo: nullableString,

  direccion: nullableString,
  email_personal: nullableEmail,
  telefono_personal: nullableString,
  movil_personal: nullableString,
  
  descripcion: nullableString,
  
  // AQUÍ ESTABA EL ERROR: Ahora aceptamos null explícitamente
  fotografia: nullableString, 
});

export type PersonalFormValues = z.infer<typeof personalSchema>;