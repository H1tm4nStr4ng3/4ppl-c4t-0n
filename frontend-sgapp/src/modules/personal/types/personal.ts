export interface Personal {
  abreviatura: string; // Es la PK (ej: VGR)
  nombre: string;
  cargo: string;
  vigente: boolean;
  email_corporativo: string | null;
  telefono_corporativo: string | null;
  fotografia: string | null; // URL o nombre del archivo
  // Agrega aquí otros campos si los necesitas mostrar en la tabla
}
