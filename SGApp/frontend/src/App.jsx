import { BrowserRouter as Router, Routes, Route, Link, useNavigate } from 'react-router-dom';
import { useState } from 'react';
import { 
  Menu, X, Home, FileText, Package, Wrench, Users, Building2, 
  ClipboardList, Settings, ChevronDown, ChevronRight 
} from 'lucide-react';
import Dashboard from './pages/Dashboard';
import GenericCRUD from './pages/GenericCRUD';
import { endpoints } from './services/api';

function App() {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [expandedSections, setExpandedSections] = useState({});

  const toggleSection = (section) => {
    setExpandedSections(prev => ({
      ...prev,
      [section]: !prev[section]
    }));
  };

  // Organizar endpoints por categorías
  const menuStructure = {
    'Documentación': {
      icon: <FileText size={20} />,
      items: [
        { key: 'PA_DI_FA', ...endpoints.PA_DI_FA },
        { key: 'PA_DI_PR', ...endpoints.PA_DI_PR },
        { key: 'PA_DI_RA', ...endpoints.PA_DI_RA },
      ]
    },
    'Equipamiento': {
      icon: <Package size={20} />,
      items: [
        { key: 'PA_EQ_EQ', ...endpoints.PA_EQ_EQ },
        { key: 'PA_EQ_CA', ...endpoints.PA_EQ_CA },
        { key: 'PA_EQ_CI', ...endpoints.PA_EQ_CI },
        { key: 'PA_EQ_MA', ...endpoints.PA_EQ_MA },
        { key: 'PA_EQ_VE', ...endpoints.PA_EQ_VE },
        { key: 'PA_EQ_AC', ...endpoints.PA_EQ_AC },
        { key: 'PA_EQ_CB', ...endpoints.PA_EQ_CB },
        { key: 'PA_EQ_CH', ...endpoints.PA_EQ_CH },
        { key: 'PA_EQ_CV', ...endpoints.PA_EQ_CV },
        { key: 'PA_EQ_DC', ...endpoints.PA_EQ_DC },
        { key: 'PA_EQ_EX', ...endpoints.PA_EQ_EX },
        { key: 'PA_EQ_HM', ...endpoints.PA_EQ_HM },
        { key: 'PA_EQ_LE', ...endpoints.PA_EQ_LE },
        { key: 'PA_EQ_MO', ...endpoints.PA_EQ_MO },
        { key: 'PA_EQ_MR', ...endpoints.PA_EQ_MR },
        { key: 'PA_EQ_MV', ...endpoints.PA_EQ_MV },
        { key: 'PA_EQ_PA', ...endpoints.PA_EQ_PA },
        { key: 'PA_EQ_PR', ...endpoints.PA_EQ_PR },
        { key: 'PA_EQ_RE', ...endpoints.PA_EQ_RE },
        { key: 'PA_EQ_RP', ...endpoints.PA_EQ_RP },
      ]
    },
    'Instalaciones': {
      icon: <Building2 size={20} />,
      items: [
        { key: 'PA_IA_AH', ...endpoints.PA_IA_AH },
        { key: 'PA_IA_AM', ...endpoints.PA_IA_AM },
        { key: 'PA_IA_AR', ...endpoints.PA_IA_AR },
        { key: 'PA_IA_CA', ...endpoints.PA_IA_CA },
        { key: 'PA_IA_LE', ...endpoints.PA_IA_LE },
        { key: 'PA_IA_LI', ...endpoints.PA_IA_LI },
        { key: 'PA_IA_RA', ...endpoints.PA_IA_RA },
        { key: 'PA_IA_RI', ...endpoints.PA_IA_RI },
        { key: 'PA_IA_SA', ...endpoints.PA_IA_SA },
        { key: 'PA_IA_SI', ...endpoints.PA_IA_SI },
      ]
    },
    'Personal': {
      icon: <Users size={20} />,
      items: [
        { key: 'PA_PE_PE', ...endpoints.PA_PE_PE },
        { key: 'PA_PE_CV', ...endpoints.PA_PE_CV },
        { key: 'PA_PE_DE', ...endpoints.PA_PE_DE },
        { key: 'PA_PE_EC', ...endpoints.PA_PE_EC },
        { key: 'PA_PE_EF', ...endpoints.PA_PE_EF },
        { key: 'PA_PE_FG', ...endpoints.PA_PE_FG },
        { key: 'PA_PE_AU', ...endpoints.PA_PE_AU },
        { key: 'PA_PE_IE', ...endpoints.PA_PE_IE },
        { key: 'PA_PE_IS', ...endpoints.PA_PE_IS },
        { key: 'PA_PE_PL', ...endpoints.PA_PE_PL },
        { key: 'PA_PE_PO', ...endpoints.PA_PE_PO },
        { key: 'PA_PE_PR', ...endpoints.PA_PE_PR },
        { key: 'PA_PE_RQ', ...endpoints.PA_PE_RQ },
        { key: 'PA_PE_SE', ...endpoints.PA_PE_SE },
        { key: 'PA_PE_SP', ...endpoints.PA_PE_SP },
        { key: 'PA_PE_SU', ...endpoints.PA_PE_SU },
      ]
    },
    'Productos y Servicios': {
      icon: <Wrench size={20} />,
      items: [
        { key: 'PA_PS_PS', ...endpoints.PA_PS_PS },
        { key: 'PA_PS_OS', ...endpoints.PA_PS_OS },
        { key: 'PA_PS_AD', ...endpoints.PA_PS_AD },
        { key: 'PA_PS_CR', ...endpoints.PA_PS_CR },
        { key: 'PA_PS_DE', ...endpoints.PA_PS_DE },
        { key: 'PA_PS_EV', ...endpoints.PA_PS_EV },
        { key: 'PA_PS_PR', ...endpoints.PA_PS_PR },
      ]
    },
    'Laboratorio': {
      icon: <ClipboardList size={20} />,
      items: [
        { key: 'PC_LAB_PATRONES', ...endpoints.PC_LAB_PATRONES },
        { key: 'PC_LAB_SOLUCIONES', ...endpoints.PC_LAB_SOLUCIONES },
        { key: 'PC_LAB_SOLUCIONES_DET', ...endpoints.PC_LAB_SOLUCIONES_DET },
        { key: 'PC_LAB_VALIDACION', ...endpoints.PC_LAB_VALIDACION },
        { key: 'PC_ES_ES', ...endpoints.PC_ES_ES },
        { key: 'PC_QR_QU', ...endpoints.PC_QR_QU },
        { key: 'PC_TC_TC', ...endpoints.PC_TC_TC },
      ]
    },
    'Registros': {
      icon: <FileText size={20} />,
      items: [
        { key: 'PC_RE_ANALISIS', ...endpoints.PC_RE_ANALISIS },
        { key: 'PC_RE_AC', ...endpoints.PC_RE_AC },
        { key: 'PC_RE_CC', ...endpoints.PC_RE_CC },
        { key: 'PC_RE_CL', ...endpoints.PC_RE_CL },
        { key: 'PC_RE_CO', ...endpoints.PC_RE_CO },
        { key: 'PC_RE_MU', ...endpoints.PC_RE_MU },
        { key: 'PC_RE_OF', ...endpoints.PC_RE_OF },
        { key: 'PC_RE_PI', ...endpoints.PC_RE_PI },
        { key: 'PC_RE_PR', ...endpoints.PC_RE_PR },
        { key: 'PC_RE_SE', ...endpoints.PC_RE_SE },
        { key: 'PC_RE_SG', ...endpoints.PC_RE_SG },
        { key: 'PC_RE_SH', ...endpoints.PC_RE_SH },
        { key: 'PC_RE_SO', ...endpoints.PC_RE_SO },
      ]
    },
    'Planificación': {
      icon: <ClipboardList size={20} />,
      items: [
        { key: 'PE_PL_PL', ...endpoints.PE_PL_PL },
        { key: 'PE_PL_PI', ...endpoints.PE_PL_PI },
        { key: 'PE_PL_AC', ...endpoints.PE_PL_AC },
        { key: 'PE_PL_CO', ...endpoints.PE_PL_CO },
        { key: 'PE_PL_ES', ...endpoints.PE_PL_ES },
        { key: 'PE_PL_OB', ...endpoints.PE_PL_OB },
        { key: 'PE_PL_PC', ...endpoints.PE_PL_PC },
        { key: 'PE_PL_RO', ...endpoints.PE_PL_RO },
      ]
    },
    'Servicios': {
      icon: <Settings size={20} />,
      items: [
        { key: 'PE_SE_EN', ...endpoints.PE_SE_EN },
        { key: 'PE_SE_AC', ...endpoints.PE_SE_AC },
        { key: 'PE_SE_CA', ...endpoints.PE_SE_CA },
        { key: 'PE_SE_CO', ...endpoints.PE_SE_CO },
        { key: 'PE_SE_EE', ...endpoints.PE_SE_EE },
        { key: 'PE_SE_MA', ...endpoints.PE_SE_MA },
        { key: 'PE_SE_ME', ...endpoints.PE_SE_ME },
        { key: 'PE_SE_RE', ...endpoints.PE_SE_RE },
        { key: 'PE_SE_SA', ...endpoints.PE_SE_SA },
        { key: 'PE_SE_SS', ...endpoints.PE_SE_SS },
      ]
    },
    'Sistema': {
      icon: <Settings size={20} />,
      items: [
        { key: 'SYS_FACTORESK', ...endpoints.SYS_FACTORESK },
        { key: 'TBL_LUGARES', ...endpoints.TBL_LUGARES },
        { key: 'TBL_POSICIONES_HORNO', ...endpoints.TBL_POSICIONES_HORNO },
      ]
    },
  };

  return (
    <Router>
      <div className="app">
        {/* Header */}
        <header className="header">
          <button 
            className="menu-toggle"
            onClick={() => setSidebarOpen(!sidebarOpen)}
          >
            {sidebarOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
          <h1 className="header-title">
            <span className="gradient-text">SGApp</span>
          </h1>
          <div className="header-subtitle">Sistema de Gestión</div>
        </header>

        <div className="main-container">
          {/* Sidebar */}
          <aside className={`sidebar ${sidebarOpen ? 'open' : ''}`}>
            <nav className="sidebar-nav">
              <Link to="/" className="nav-item" onClick={() => setSidebarOpen(false)}>
                <Home size={20} />
                <span>Inicio</span>
              </Link>

              {Object.entries(menuStructure).map(([sectionName, section]) => (
                <div key={sectionName} className="nav-section">
                  <button
                    className="nav-section-header"
                    onClick={() => toggleSection(sectionName)}
                  >
                    {section.icon}
                    <span>{sectionName}</span>
                    {expandedSections[sectionName] ? 
                      <ChevronDown size={16} /> : 
                      <ChevronRight size={16} />
                    }
                  </button>
                  
                  {expandedSections[sectionName] && (
                    <div className="nav-section-items">
                      {section.items.map(item => (
                        <Link
                          key={item.key}
                          to={`/module/${item.key}`}
                          state={{ endpoint: item.path, name: item.name }}
                          className="nav-subitem"
                          onClick={() => setSidebarOpen(false)}
                        >
                          {item.name}
                        </Link>
                      ))}
                    </div>
                  )}
                </div>
              ))}
            </nav>
          </aside>

          {/* Overlay para cerrar sidebar en móvil */}
          {sidebarOpen && (
            <div 
              className="sidebar-overlay"
              onClick={() => setSidebarOpen(false)}
            />
          )}

          {/* Main Content */}
          <main className="content">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/module/:moduleName" element={<GenericCRUD />} />
            </Routes>
          </main>
        </div>
      </div>
    </Router>
  );
}

export default App;
