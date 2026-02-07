import { useState } from "react";
import { useNavigate } from "react-router-dom"; // Para el botón Editar
import { MoreHorizontal, Pencil, Trash, Eye } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from "@/components/ui/alert-dialog";
import { usePersonal } from "../hooks/usePersonal";
import { Personal } from "../types/personal";

interface ActionsProps {
  personal: Personal;
}

export const PersonalActions = ({ personal }: ActionsProps) => {
  const [openAlert, setOpenAlert] = useState(false);
  const { deleteMutation } = usePersonal(); 
  const navigate = useNavigate(); // Hook de navegación

  const handleDelete = () => {
    // Llamamos a borrar usando la Abreviatura (PK)
    deleteMutation.mutate(personal.abreviatura); 
    setOpenAlert(false);
  };

  return (
    <>
      <DropdownMenu>
        <DropdownMenuTrigger asChild>
          <Button variant="ghost" className="h-8 w-8 p-0">
            <span className="sr-only">Abrir menú</span>
            <MoreHorizontal className="h-4 w-4" />
          </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent align="end">
          <DropdownMenuLabel>Acciones</DropdownMenuLabel>
          
          <DropdownMenuItem onClick={() => navigator.clipboard.writeText(personal.abreviatura)}>
            Copiar ID ({personal.abreviatura})
          </DropdownMenuItem>
          
          <DropdownMenuSeparator />
          
          {/* BOTÓN EDITAR / VER: Ahora navega a una URL real */}
          <DropdownMenuItem onClick={() => navigate(`/personal/${personal.abreviatura}`)}>
             <Pencil className="mr-2 h-4 w-4" /> Editar / Ver Ficha
          </DropdownMenuItem>
          
          <DropdownMenuSeparator />
          
          {/* BOTÓN ELIMINAR: Abre la alerta */}
          <DropdownMenuItem 
            className="text-red-600 focus:text-red-600 focus:bg-red-50" 
            onClick={() => setOpenAlert(true)}
          >
             <Trash className="mr-2 h-4 w-4" /> Eliminar
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>

      {/* ALERTA DE CONFIRMACIÓN */}
      <AlertDialog open={openAlert} onOpenChange={setOpenAlert}>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>¿Eliminar a {personal.nombre}?</AlertDialogTitle>
            <AlertDialogDescription>
              Esta acción no se puede deshacer. Se eliminará el empleado 
              <b> {personal.nombre}</b> ({personal.cargo}) y sus datos asociados.
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>Cancelar</AlertDialogCancel>
            <AlertDialogAction 
                onClick={handleDelete} 
                className="bg-red-600 hover:bg-red-700"
            >
              {deleteMutation.isPending ? "Borrando..." : "Sí, eliminar"}
            </AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </>
  );
};