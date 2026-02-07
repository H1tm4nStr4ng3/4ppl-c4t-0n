import { useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { ArrowLeft, User, FileText, ShieldCheck, Loader2 } from "lucide-react";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";

// Imports nuestros
import { PersonalGeneralForm } from "../components/PersonalGeneralForm";
import { usePersonal } from "../hooks/usePersonal";
import { PersonalFormValues } from "../components/personal-schema";
import { PersonalCVTab } from "../components/PersonalCVTab";
import { PersonalAuthTab } from "../components/PersonalAuthTab";

export const PersonalDetailPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const isNew = id === 'new';

  // 1. Usamos el hook pasándole el ID (si no es new)
  const { 
      employee, 
      isLoadingEmployee, 
      createMutation, 
      updateMutation 
  } = usePersonal(id);

  // 2. Función que maneja el Guardado
  const handleSave = async (data: PersonalFormValues) => {
    try {
        if (isNew) {
            await createMutation.mutateAsync(data);
        } else {
            await updateMutation.mutateAsync(data);
        }
        // Si todo sale bien, volvemos a la lista
        navigate('/personal');
    } catch (error) {
        // El toast de error ya sale en el hook, aquí solo evitamos navegar
    }
  };

  // Si estamos editando y cargando, mostramos spinner
  if (!isNew && isLoadingEmployee) {
      return <div className="flex justify-center p-20"><Loader2 className="animate-spin h-8 w-8 text-blue-600"/></div>;
  }

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      
      {/* Header Fijo */}
      <div className="flex items-center gap-4 bg-white p-4 rounded-xl shadow-sm border border-slate-200">
        <Button variant="ghost" size="icon" onClick={() => navigate(-1)}>
            <ArrowLeft className="h-5 w-5 text-slate-500" />
        </Button>
        
        <Avatar className="h-16 w-16 border-2 border-slate-100">
            <AvatarImage src={employee?.fotografia || ""} />
            <AvatarFallback className="bg-blue-600 text-white text-xl">
                {isNew ? "N" : id?.substring(0,2).toUpperCase()}
            </AvatarFallback>
        </Avatar>

        <div>
            <h1 className="text-xl font-bold text-slate-800">
                {isNew ? "Nuevo Empleado" : `Editando: ${employee?.nombre || id}`}
            </h1>
            <p className="text-sm text-slate-500">
                {isNew ? "Complete los datos para dar de alta." : employee?.cargo || "Gestión de perfil."}
            </p>
        </div>
      </div>

      {/* Pestañas */}
      <Tabs defaultValue="general" className="w-full">
        <TabsList className="grid w-full grid-cols-3 lg:w-[400px]">
          <TabsTrigger value="general">
             <User className="mr-2 h-4 w-4" /> General
          </TabsTrigger>
          <TabsTrigger value="cv" disabled={isNew}>
             <FileText className="mr-2 h-4 w-4" /> CV / Formación
          </TabsTrigger>
          <TabsTrigger value="auth" disabled={isNew}>
             <ShieldCheck className="mr-2 h-4 w-4" /> Autorizaciones
          </TabsTrigger>
        </TabsList>

        <div className="mt-6 bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <TabsContent value="general">
                <PersonalGeneralForm 
                    // Si estamos editando, pasamos los datos del empleado descargado
                    // Necesitamos transformar la fecha de string a Date para el formulario
                    defaultValues={employee ? {
                        ...employee,
                        fecha_de_nacimiento: employee.fecha_de_nacimiento ? new Date(employee.fecha_de_nacimiento) : undefined
                    } : undefined}
                    
                    onSubmit={handleSave} 
                />
            </TabsContent>
            
            <TabsContent value="cv">
            {/* Solo mostramos la pestaña si NO es nuevo y tenemos ID */}
            {!isNew && id ? (
                <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
                    <PersonalCVTab personalId={id} />
                </div>
            ) : (
                <div className="text-center p-10 text-slate-500 bg-slate-50 rounded-lg border border-dashed">
                    Para agregar registros académicos, primero debe guardar la información general del empleado.
                </div>
            )}
            </TabsContent>
            
            <TabsContent value="auth">
            {!isNew && id ? (
            <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
                <PersonalAuthTab personalId={id} />
            </div>
                    ) : (
                        <div className="text-center p-10 text-slate-500 bg-slate-50 rounded-lg border border-dashed">
                            Para gestionar autorizaciones, primero guarde el empleado.
                        </div>
                    )}
            </TabsContent>
        </div>
      </Tabs>
    </div>
  );
};