import { useState, useEffect } from 'react';
import { X } from 'lucide-react';

function FormModal({ item, sampleData, onSubmit, onClose, title }) {
  const [formData, setFormData] = useState({});

  useEffect(() => {
    if (item) {
      // Modo edición: cargar datos del item
      setFormData(item);
    } else if (sampleData) {
      // Modo creación: inicializar con valores vacíos basados en la estructura
      const emptyData = {};
      Object.keys(sampleData).forEach(key => {
        if (key === 'id') return; // Skip ID field
        const value = sampleData[key];
        if (typeof value === 'boolean') {
          emptyData[key] = false;
        } else if (typeof value === 'number') {
          emptyData[key] = 0;
        } else if (typeof value === 'string') {
          emptyData[key] = '';
        } else {
          emptyData[key] = '';
        }
      });
      setFormData(emptyData);
    }
  }, [item, sampleData]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : type === 'number' ? Number(value) : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  // Función para determinar el tipo de input
  const getInputType = (key, value) => {
    if (key.toLowerCase().includes('fecha') || key.toLowerCase().includes('date')) {
      return 'date';
    }
    if (typeof value === 'boolean') {
      return 'checkbox';
    }
    if (typeof value === 'number') {
      return 'number';
    }
    if (key.toLowerCase().includes('observacion') || 
        key.toLowerCase().includes('descripcion') ||
        key.toLowerCase().includes('comentario') ||
        key.toLowerCase().includes('modificacion')) {
      return 'textarea';
    }
    return 'text';
  };

  // Función para formatear nombres de campos
  const formatFieldName = (fieldName) => {
    return fieldName
      .replace(/_/g, ' ')
      .replace(/\b\w/g, (char) => char.toUpperCase());
  };

  const fields = Object.keys(formData).filter(key => key !== 'id');

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2 className="modal-title">{title}</h2>
          <button className="modal-close" onClick={onClose}>
            <X size={24} />
          </button>
        </div>

        <form onSubmit={handleSubmit}>
          {fields.map((key) => {
            const inputType = getInputType(key, formData[key]);
            
            return (
              <div key={key} className="form-group">
                <label className="form-label" htmlFor={key}>
                  {formatFieldName(key)}
                </label>
                
                {inputType === 'textarea' ? (
                  <textarea
                    id={key}
                    name={key}
                    className="form-textarea"
                    value={formData[key] || ''}
                    onChange={handleChange}
                  />
                ) : inputType === 'checkbox' ? (
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <input
                      type="checkbox"
                      id={key}
                      name={key}
                      className="form-checkbox"
                      checked={formData[key] || false}
                      onChange={handleChange}
                    />
                    <span style={{ color: 'var(--text-secondary)' }}>
                      {formData[key] ? 'Sí' : 'No'}
                    </span>
                  </div>
                ) : (
                  <input
                    type={inputType}
                    id={key}
                    name={key}
                    className="form-input"
                    value={formData[key] || ''}
                    onChange={handleChange}
                  />
                )}
              </div>
            );
          })}

          <div className="modal-actions">
            <button type="button" className="btn btn-secondary" onClick={onClose}>
              Cancelar
            </button>
            <button type="submit" className="btn btn-success">
              {item ? 'Actualizar' : 'Crear'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default FormModal;
