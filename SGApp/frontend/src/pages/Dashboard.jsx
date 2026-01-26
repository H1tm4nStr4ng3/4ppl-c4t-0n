import { FileText, Package, Users, Settings, TrendingUp, Clock } from 'lucide-react';
import { Link } from 'react-router-dom';

function Dashboard() {
  const stats = [
    {
      icon: <FileText size={24} />,
      value: '150+',
      label: 'Documentos',
      color: '#00d4ff'
    },
    {
      icon: <Package size={24} />,
      value: '85',
      label: 'Equipos',
      color: '#0080ff'
    },
    {
      icon: <TrendingUp size={24} />,
      value: '32',
      label: 'Calibraciones',
      color: '#4169e1'
    },
    {
      icon: <Users size={24} />,
      value: '45',
      label: 'Personal',
      color: '#00ff88'
    }
  ];

  const quickAccess = [
    { name: 'Equipos', path: '/module/PA_EQ_EQ', endpoint: '/pa-eq-eq' },
    { name: 'Personal', path: '/module/PA_PE_PE', endpoint: '/pa-pe-pe' },
    { name: 'Calibración', path: '/module/PA_EQ_CA', endpoint: '/pa-eq-ca' },
    { name: 'Documentación', path: '/module/PA_DI_RA', endpoint: '/pa-di-ra' },
  ];

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h1 className="dashboard-title">Panel de Control</h1>
        <p className="dashboard-subtitle">
          Bienvenido al Sistema de Gestión SGApp
        </p>
      </div>

      <div className="stats-grid">
        {stats.map((stat, index) => (
          <div key={index} className="stat-card">
            <div className="stat-header">
              <div className="stat-icon" style={{ background: `${stat.color}15`, color: stat.color }}>
                {stat.icon}
              </div>
            </div>
            <div className="stat-value" style={{ color: stat.color }}>
              {stat.value}
            </div>
            <div className="stat-label">{stat.label}</div>
          </div>
        ))}
      </div>

      <div className="stat-card" style={{ marginBottom: '2rem' }}>
        <h2 style={{ marginBottom: '1rem', color: 'var(--primary-blue)' }}>
          Acceso Rápido
        </h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem' }}>
          {quickAccess.map((item, index) => (
            <Link
              key={index}
              to={item.path}
              state={{ endpoint: item.endpoint, name: item.name }}
              className="btn btn-secondary"
              style={{ justifyContent: 'center' }}
            >
              {item.name}
            </Link>
          ))}
        </div>
      </div>

      <div className="stat-card">
        <h2 style={{ marginBottom: '1rem', color: 'var(--primary-blue)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <Clock size={24} />
          Información del Sistema
        </h2>
        <div style={{ color: 'var(--text-secondary)', lineHeight: '1.8' }}>
          <p>• Sistema de Gestión de Calidad v1.0</p>
          <p>• Base de datos: PostgreSQL</p>
          <p>• Módulos activos: 50+</p>
          <p>• Estado del sistema: Operativo</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
