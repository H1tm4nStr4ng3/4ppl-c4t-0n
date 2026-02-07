import { DataTable } from "@/components/ui/data-table"
import { columns } from "../components/columns"
import { usePersonal } from "../hooks/usePersonal"
import { Button } from "@/components/ui/button"
import { PlusCircle, Briefcase } from "lucide-react"
import { useNavigate } from "react-router-dom"

export const PersonalPage = () => {
  const { data, isLoading, isError } = usePersonal();
  const navigate = useNavigate();

  if (isLoading) {
    return <div className="p-10 text-center text-slate-500 animate-pulse">Cargando directorio...</div>
  }

  if (isError) {
    return <div className="p-10 text-center text-red-500 bg-red-50 rounded-lg">Error de conexión con el servidor.</div>
  }

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      {/* Encabezado */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Directorio de Personal</h1>
          <p className="text-slate-500">Administración de recursos humanos y accesos.</p>
        </div>

        <div className="flex items-center gap-2">
            {/* Botón Cargos */}
            <Button variant="outline" onClick={() => navigate('/personal/cargos')}>
                <Briefcase className="mr-2 h-4 w-4" />
                Cargos
            </Button>

            {/* Botón Nuevo Personal */}
            <Button className="bg-blue-600 hover:bg-blue-700" onClick={() => navigate('/personal/new')}>
                <PlusCircle className="mr-2 h-4 w-4" />
                Nuevo Empleado
            </Button>
        </div>
      </div>

      {/* Tabla */}
      <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
        <DataTable columns={columns} data={data || []} searchKey="nombre" />
      </div>
    </div>
  )
}