import { useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { 
  // Iconos Generales
  LayoutDashboard, Users, Microscope, FileText, Building2, 
  ShoppingCart, Briefcase, TrendingUp, X, 
  ChevronDown, ChevronRight,
  
  // Iconos Personal
  Contact,      // Directorio
  UserPlus,     // Selección
  GraduationCap,// Icono para el Grupo de Competencias
  
  // Iconos Fases Competencias
  Ruler,        // Fase 1
  ClipboardList,// Fase 2
  BookOpen,     // Fase 3
  ClipboardCheck,// Fase 4
  Award,         // Fase 5
  Eye,
  FlaskConical,
  FlaskRound
} from 'lucide-react';
import { cn } from '@/lib/utils';

// --- 1. DEFINICIÓN DE TIPOS RECURSIVA ---
interface MenuItem {
  label: string;
  icon?: any;
  to?: string;
  // El submenú ahora es del mismo tipo MenuItem, permitiendo anidamiento infinito
  submenu?: MenuItem[]; 
}

// --- 2. CONFIGURACIÓN DEL MENÚ ---
export const menuItems: MenuItem[] = [
  { icon: LayoutDashboard, label: 'Dashboard', to: '/' },
  
  // MÓDULO PERSONAL
  { 
    icon: Users, 
    label: 'Personal', 
    submenu: [
      { label: 'Directorio', to: '/personal', icon: Contact },
      // "Cargos" ELIMINADO según solicitud
      { label: 'Selección', to: '/personal/seleccion', icon: UserPlus },
      { label: 'Supervisión', to: '/personal/supervision', icon: Eye },
      
      // NUEVO GRUPO: GESTIÓN DE COMPETENCIAS (Nivel 2)
      { 
        label: 'Gestión Competencias',
        icon: GraduationCap,
        submenu: [
          // NIVEL 3: LAS 5 FASES
          { label: '1. Requisitos', to: '/personal/competencias/requisitos', icon: Ruler }, 
          { label: '2. Evaluación', to: '/personal/competencias/evaluacion', icon: ClipboardList },
          { label: '3. Necesidades', to: '/personal/competencias/programas', icon: BookOpen },
          { label: '4. Ejecución', to: '/personal/competencias/planificacion', icon: ClipboardCheck },
          { label: '5. Eficacia', to: '/personal/competencias/eficacia', icon: Award },
        ]
      },
    ]
  },

  { 
  icon: Microscope, 
  label: 'Equipamiento', 
  submenu: [ // Convertimos Equipamiento en un menú desplegable
     { label: 'Inventario', to: '/equipamiento', icon: Microscope },
     { label: 'Mat. Referencia', to: '/equipamiento/materiales', icon: FlaskConical },
     { 
        label: 'Reactivos', 
        to: '/equipamiento/reactivos', 
        icon: FlaskRound 
      },
  ]
  },
  { icon: ClipboardCheck, label: 'Planificación', to: '/planificacion' },
  { icon: TrendingUp, label: 'Seguimiento SG', to: '/seguimiento' },
  { icon: Building2, label: 'Infraestructura', to: '/infraestructura' },
  { icon: FileText, label: 'Documentación', to: '/documentacion' },
  { icon: ShoppingCart, label: 'Compras', to: '/compras' },
  { icon: Briefcase, label: 'Comercial', to: '/comercial' },
  { icon: FlaskConical, label: 'Laboratorio', to: '/laboratorio' },
];

// --- 3. COMPONENTE RECURSIVO PARA RENDERIZAR ITEMS ---
const SidebarItem = ({ 
  item, 
  level = 0, 
  expanded, 
  onToggle, 
  onClose 
}: { 
  item: MenuItem, 
  level?: number, 
  expanded: Record<string, boolean>, 
  onToggle: (label: string) => void,
  onClose?: () => void
}) => {
  const location = useLocation();
  const hasSubmenu = item.submenu && item.submenu.length > 0;
  const isOpen = expanded[item.label];

  // Cálculo de indentación dinámica según el nivel
  const paddingLeft = level === 0 ? '12px' : `${(level * 12) + 12}px`;

  // Renderizado de Ítem con Submenú (Botón Acordeón)
  if (hasSubmenu) {
    // Verificamos si algún hijo está activo para colorear el padre
    const isChildActive = (items: MenuItem[]): boolean => {
      return items.some(child => 
        (child.to && location.pathname === child.to) || 
        (child.submenu && isChildActive(child.submenu))
      );
    };
    const isActive = isChildActive(item.submenu!);

    return (
      <li>
        <button
          onClick={() => onToggle(item.label)}
          className={cn(
            "w-full flex items-center justify-between py-2.5 rounded-lg text-sm font-medium transition-colors hover:bg-slate-800 hover:text-white pr-3",
            isActive ? "text-blue-400" : "text-slate-400"
          )}
          style={{ paddingLeft }}
        >
          <div className="flex items-center gap-3">
            {item.icon && <item.icon size={20} />}
            <span>{item.label}</span>
          </div>
          {isOpen ? <ChevronDown size={16} /> : <ChevronRight size={16} />}
        </button>

        {/* Renderizado Recursivo de Hijos */}
        {isOpen && (
          <ul className="mt-1 space-y-1 border-l border-slate-800 ml-4">
            {item.submenu!.map((subItem) => (
              <SidebarItem 
                key={subItem.label} 
                item={subItem} 
                level={level + 1} 
                expanded={expanded} 
                onToggle={onToggle}
                onClose={onClose}
              />
            ))}
          </ul>
        )}
      </li>
    );
  }

  // Renderizado de Ítem Normal (Enlace)
  return (
    <li>
      <NavLink
        to={item.to!}
        onClick={onClose}
        className={({ isActive }) =>
          cn(
            "flex items-center gap-3 py-2.5 rounded-lg text-sm font-medium transition-colors pr-3",
            isActive 
              ? "bg-blue-600 text-white shadow-md" 
              : "text-slate-400 hover:bg-slate-800 hover:text-white"
          )
        }
        style={{ paddingLeft }}
      >
        {item.icon && <item.icon size={20} />}
        <span>{item.label}</span>
      </NavLink>
    </li>
  );
};

// --- 4. COMPONENTE PRINCIPAL SIDEBAR ---
interface SidebarProps {
  className?: string;
  onClose?: () => void;
}

export const Sidebar = ({ className, onClose }: SidebarProps) => {
  const location = useLocation();
  
  // Estado para controlar qué menús están expandidos
  // Inicializamos abierto si la ruta actual coincide
  const [expanded, setExpanded] = useState<Record<string, boolean>>(() => {
    const initialState: Record<string, boolean> = {};
    
    // Función auxiliar para pre-abrir menús según la URL actual
    const checkOpen = (items: MenuItem[]) => {
      items.forEach(item => {
        if (item.submenu) {
          // Si un hijo coincide con la URL, abrimos este padre
          const shouldOpen = item.submenu.some(sub => 
            (sub.to && location.pathname.includes(sub.to)) ||
            (sub.submenu && sub.submenu.some(deep => deep.to && location.pathname.includes(deep.to)))
          );
          if (shouldOpen || location.pathname.includes('/personal')) { 
             // Lógica específica: Mantener Personal abierto si estamos en ese módulo
             if (item.label === 'Personal' && location.pathname.includes('/personal')) initialState[item.label] = true;
             if (item.label === 'Gestión Competencias' && location.pathname.includes('/personal/competencias')) initialState[item.label] = true;
          }
          checkOpen(item.submenu);
        }
      });
    };
    checkOpen(menuItems);
    return initialState;
  });

  const toggleMenu = (label: string) => {
    setExpanded(prev => ({
      ...prev,
      [label]: !prev[label]
    }));
  };

  return (
    <aside className={cn(
      "bg-slate-900 text-slate-100 flex-col w-64 h-screen transition-all duration-300",
      "hidden md:flex", 
      className
    )}>
      {/* Header */}
      <div className="h-16 flex items-center justify-between px-6 border-b border-slate-700 bg-slate-950">
        <h1 className="text-xl font-bold tracking-wider text-white">SGApp <span className="text-blue-500">v2</span></h1>
        {onClose && (
          <button onClick={onClose} className="md:hidden text-slate-400 hover:text-white">
            <X size={24} />
          </button>
        )}
      </div>

      {/* Navegación */}
      <nav className="flex-1 overflow-y-auto py-4 scrollbar-thin scrollbar-thumb-slate-700">
        <ul className="space-y-1 px-2">
          {menuItems.map((item) => (
            <SidebarItem 
              key={item.label} 
              item={item} 
              expanded={expanded} 
              onToggle={toggleMenu}
              onClose={onClose}
            />
          ))}
        </ul>
      </nav>

      {/* Footer */}
      <div className="p-4 border-t border-slate-700 bg-slate-950">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center text-xs font-bold text-white">
            AD
          </div>
          <div>
            <p className="text-sm font-medium text-white">Admin</p>
            <p className="text-xs text-slate-400">admin@sgapp.com</p>
          </div>
        </div>
      </div>
    </aside>
  );
};