import { useState, useEffect } from 'react';
import { useLocation, useParams } from 'react-router-dom';
import { Plus, Search, AlertCircle, CheckCircle } from 'lucide-react';
import { apiService } from '../services/api';
import DataTable from '../components/DataTable';
import FormModal from '../components/FormModal';

function GenericCRUD() {
  const location = useLocation();
  const { moduleName } = useParams();
  const { endpoint, name } = location.state || {};

  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [showModal, setShowModal] = useState(false);
  const [editingItem, setEditingItem] = useState(null);
  const [alert, setAlert] = useState(null);

  useEffect(() => {
    if (endpoint) {
      loadData();
    }
  }, [endpoint]);

  const loadData = async () => {
    setLoading(true);
    setError(null);
    try {
      const result = await apiService.getAll(endpoint);
      setData(result);
    } catch (err) {
      setError('Error al cargar los datos. Asegúrate de que el backend esté ejecutándose.');
      console.error('Error loading data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setEditingItem(null);
    setShowModal(true);
  };

  const handleEdit = (item) => {
    setEditingItem(item);
    setShowModal(true);
  };

  const handleDelete = async (item) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este elemento?')) {
      try {
        await apiService.delete(endpoint, item.id);
        showAlert('Elemento eliminado exitosamente', 'success');
        loadData();
      } catch (err) {
        showAlert('Error al eliminar el elemento', 'error');
        console.error('Error deleting item:', err);
      }
    }
  };

  const handleSubmit = async (formData) => {
    try {
      if (editingItem) {
        await apiService.update(endpoint, editingItem.id, formData);
        showAlert('Elemento actualizado exitosamente', 'success');
      } else {
        await apiService.create(endpoint, formData);
        showAlert('Elemento creado exitosamente', 'success');
      }
      setShowModal(false);
      loadData();
    } catch (err) {
      showAlert('Error al guardar el elemento', 'error');
      console.error('Error saving item:', err);
    }
  };

  const showAlert = (message, type) => {
    setAlert({ message, type });
    setTimeout(() => setAlert(null), 5000);
  };

  const filteredData = data.filter(item => {
    if (!searchTerm) return true;
    return Object.values(item).some(value => 
      String(value).toLowerCase().includes(searchTerm.toLowerCase())
    );
  });

  if (!endpoint) {
    return (
      <div className="empty-state">
        <AlertCircle className="empty-icon" />
        <h2>Módulo no encontrado</h2>
        <p>Por favor, selecciona un módulo del menú lateral.</p>
      </div>
    );
  }

  return (
    <div className="crud-page">
      {alert && (
        <div className={`alert alert-${alert.type}`}>
          {alert.type === 'success' ? <CheckCircle size={20} /> : <AlertCircle size={20} />}
          <span>{alert.message}</span>
        </div>
      )}

      <div className="page-header">
        <h1 className="page-title">{name || moduleName}</h1>
        
        <div className="search-bar">
          <input
            type="text"
            className="search-input"
            placeholder="Buscar..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <Search className="search-icon" size={20} />
        </div>

        <button className="btn btn-primary" onClick={handleCreate}>
          <Plus size={20} />
          Nuevo
        </button>
      </div>

      {loading ? (
        <div className="loading">
          <div className="spinner"></div>
          <p style={{ marginTop: '1rem' }}>Cargando datos...</p>
        </div>
      ) : error ? (
        <div className="alert alert-error">
          <AlertCircle size={20} />
          <span>{error}</span>
        </div>
      ) : filteredData.length === 0 ? (
        <div className="empty-state">
          <AlertCircle className="empty-icon" />
          <h2>No hay datos disponibles</h2>
          <p>Haz clic en "Nuevo" para agregar el primer elemento.</p>
        </div>
      ) : (
        <DataTable
          data={filteredData}
          onEdit={handleEdit}
          onDelete={handleDelete}
        />
      )}

      {showModal && (
        <FormModal
          item={editingItem}
          sampleData={data[0]}
          onSubmit={handleSubmit}
          onClose={() => setShowModal(false)}
          title={editingItem ? 'Editar' : 'Nuevo'}
        />
      )}
    </div>
  );
}

export default GenericCRUD;
