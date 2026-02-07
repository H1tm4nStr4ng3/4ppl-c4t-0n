import { createBrowserRouter, Navigate } from 'react-router-dom';
import { MainLayout } from '@/components/layout/MainLayout';

// Imports de Páginas
import { PersonalPage } from '@/modules/personal/pages/PersonalPage';
import { PersonalDetailPage } from '@/modules/personal/pages/PersonalDetailPage';
import { CargosPage } from '@/modules/personal/pages/CargosPage';
import { SelectionPage } from '@/modules/personal/pages/SelectionPage'; 
import { SelectionDetailPage } from '@/modules/personal/pages/SelectionDetailPage'; // <--- Importamos el detalle
import { RequirementsPage } from '@/modules/personal/pages/RequirementsPage';
import { CompetencyEvaluationPage } from '@/modules/personal/pages/CompetencyEvaluationPage';
import { TrainingProgramsPage } from '@/modules/personal/pages/TrainingProgramsPage';
import { TrainingPlanningPage } from '@/modules/personal/pages/TrainingPlanningPage';
import { EffectivenessPage } from '@/modules/personal/pages/EffectivenessPage';
import { SupervisionPage } from '@/modules/personal/pages/SupervisionPage';
import { EquipmentPage } from '@/modules/equipamiento/pages/EquipmentPage';
import { ReferenceMaterialsPage } from '@/modules/equipamiento/pages/ReferenceMaterialsPage';
import { ReagentsPage } from '@/modules/equipamiento/pages/ReagentsPage';

export const router = createBrowserRouter([
  {
    path: "/",
    element: <MainLayout />,
    children: [
      {
        index: true,
        element: (
          <div className="p-10 text-center">
            <h1 className="text-3xl font-bold text-slate-800 mb-2">Bienvenido al SGApp</h1>
            <p className="text-slate-500">Selecciona un módulo del menú lateral para comenzar.</p>
          </div>
        ),
      },
      // --- MÓDULO PERSONAL ---
      {
        path: "personal",
        element: <PersonalPage />,
      },
      {
        path: "personal/cargos",
        element: <CargosPage />,
      },
      
      // --- SUB-MÓDULO SELECCIÓN ---
      {
        path: "personal/seleccion", 
        element: <SelectionPage />,
      },
      {
      path: "personal/competencias/requisitos", // Nueva ruta
      element: <RequirementsPage />,
      },
      {
      path: "personal/competencias/evaluacion",
      element: <CompetencyEvaluationPage />,
      },
      {
      path: "personal/competencias/programas",
      element: <TrainingProgramsPage />,
      },
      {
      path: "personal/competencias/eficacia",
      element: <EffectivenessPage />,
      },
      {
        path: "personal/seleccion/:id", // <--- Ruta Dinámica para Detalle/Evaluación
        element: <SelectionDetailPage />,
      },
      {
        path: "personal/competencias/planificacion",
        element: <TrainingPlanningPage />,
      },
      {
      path: "personal/supervision",
      element: <SupervisionPage />,
      },
      // --- FICHA DE PERSONAL (Importante: va al final de las rutas de personal) ---
      {
        path: "personal/:id",
        element: <PersonalDetailPage />,
      },
      
      // --- OTROS MÓDULO ---
      {
      path: "equipamiento",
      element: <EquipmentPage />,
      },
      {
      path: "equipamiento/materiales",
      element: <ReferenceMaterialsPage />,
      },
      {
      path: "equipamiento/reactivos",
      element: <ReagentsPage />,
       },
      // --- OTROS MÓDULO ---
      {
        path: "planificacion",
        element: <div className="bg-white p-6 rounded-lg shadow">Módulo de Planificación</div>,
      },
      {
        path: "seguimiento",
        element: <div className="bg-white p-6 rounded-lg shadow">Módulo de Seguimiento</div>,
      },
      {
        path: "infraestructura",
        element: <div className="bg-white p-6 rounded-lg shadow">Módulo de Infraestructura</div>,
      },
      {
        path: "documentacion",
        element: <div className="bg-white p-6 rounded-lg shadow">Módulo de Documentación</div>,
      },
      {
        path: "compras",
        element: <div className="bg-white p-6 rounded-lg shadow">Módulo de Compras</div>,
      },
      {
        path: "comercial",
        element: <div className="bg-white p-6 rounded-lg shadow">Módulo Comercial</div>,
      },
      {
        path: "laboratorio",
        element: <div className="bg-white p-6 rounded-lg shadow">Módulo de Laboratorio</div>,
      },
    ],
  },
  {
    path: "*",
    element: <Navigate to="/" replace />,
  }
]);