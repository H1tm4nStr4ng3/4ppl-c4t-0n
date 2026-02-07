import { useState } from 'react';
import { Outlet } from 'react-router-dom';
import { Menu } from 'lucide-react';
import { Sidebar } from './Sidebar';
import { Toaster } from "@/components/ui/sonner" // <--- Importar

export const MainLayout = () => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  return (
    <div className="flex h-screen bg-slate-50 overflow-hidden">
      
      {/* 1. Sidebar de Escritorio (Se oculta solo en móvil gracias a las clases CSS) */}
      <Sidebar />

      {/* 2. Sidebar Móvil (Overlay) */}
      {isMobileMenuOpen && (
        <div className="fixed inset-0 z-50 flex md:hidden">
          {/* Fondo oscuro transparente (Backdrop) */}
          <div 
            className="fixed inset-0 bg-black/50 backdrop-blur-sm transition-opacity"
            onClick={() => setIsMobileMenuOpen(false)}
          />
          
          {/* El Sidebar en sí mismo (reutilizamos el componente) */}
          <Sidebar 
            className="relative flex w-64 h-full shadow-2xl animate-in slide-in-from-left duration-300" 
            onClose={() => setIsMobileMenuOpen(false)} 
          />
        </div>
      )}

      {/* Área de Contenido Principal */}
      <main className="flex-1 flex flex-col h-screen overflow-hidden relative">
        
        {/* Header Superior */}
        <header className="bg-white border-b border-slate-200 h-16 flex items-center justify-between px-4 sm:px-8 shrink-0">
          <div className="flex items-center gap-3">
            {/* Botón Hamburguesa (Solo visible en Móvil) */}
            <button 
              onClick={() => setIsMobileMenuOpen(true)}
              className="md:hidden p-2 -ml-2 text-slate-600 hover:bg-slate-100 rounded-md"
            >
              <Menu size={24} />
            </button>
            
            <h2 className="text-lg font-semibold text-slate-700">
              Sistema de Gestión
            </h2>
          </div>

          {/* Acciones de Header (Derecha) */}
          <div className="flex items-center gap-4">
             {/* Aquí irán notificaciones en el futuro */}
             <span className="text-xs text-slate-400 hidden sm:inline">v2.0.0</span>
          </div>
        </header>

        {/* Contenido Scrollable */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-8 scroll-smooth">
          <div className="max-w-7xl mx-auto">
            <Outlet />
          </div>
        </div>
      </main>
    </div>
  );

  return (
    <div className="flex h-screen bg-slate-50 overflow-hidden">
      {/* ... todo tu sidebar y main ... */}
      
      {/* Agrega esto al final, antes de cerrar el último div */}
      <Toaster richColors position="top-right" /> 
    </div>
  );
};