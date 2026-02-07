import { ColumnDef } from "@tanstack/react-table"
import { Personal } from "../types/personal"
import { DataTableColumnHeader } from "@/components/ui/data-table-column-header"
import { Badge } from "@/components/ui/badge"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { PersonalActions } from "./PersonalActions" // Importamos el nuevo componente

export const columns: ColumnDef<Personal>[] = [
  {
    accessorKey: "abreviatura",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="ID" />
    ),
    cell: ({ row }) => <div className="font-mono font-bold">{row.getValue("abreviatura")}</div>,
    enableSorting: true,
  },
  {
    accessorKey: "nombre",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Personal" />
    ),
    cell: ({ row }) => {
        const nombre = row.getValue("nombre") as string;
        // Obtenemos iniciales para el avatar (ej: Vladimir Garcia -> VG)
        const iniciales = nombre ? nombre.split(" ").map((n) => n[0]).join("").substring(0, 2) : "NN";

        return (
            <div className="flex items-center gap-3">
                <Avatar className="h-9 w-9">
                    {/* Usamos una imagen genérica o vacía por ahora hasta arreglar el tema binario */}
                    <AvatarImage src="" alt={nombre} />
                    <AvatarFallback className="bg-blue-100 text-blue-700">{iniciales}</AvatarFallback>
                </Avatar>
                <div className="flex flex-col">
                    <span className="font-medium text-slate-900">{nombre}</span>
                    <span className="text-xs text-slate-500">{row.original.email_corporativo || "Sin email"}</span>
                </div>
            </div>
        )
    }
  },
  {
    accessorKey: "cargo",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Cargo" />
    ),
    enableHiding: false, 
  },
  {
    accessorKey: "vigente",
    header: "Estado",
    cell: ({ row }) => {
      const activo = row.getValue("vigente") as boolean
      return (
        <Badge variant={activo ? "default" : "destructive"} className={activo ? "bg-green-600 hover:bg-green-700" : ""}>
          {activo ? "Vigente" : "Inactivo"}
        </Badge>
      )
    },
  },
  // ESTA ES LA PARTE QUE DABA ERROR, AHORA ESTÁ LIMPIA:
  {
    id: "actions",
    cell: ({ row }) => <PersonalActions personal={row.original} />
  },
]