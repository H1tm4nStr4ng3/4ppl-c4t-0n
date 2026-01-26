import { Edit, Trash2 } from 'lucide-react';

function DataTable({ data, onEdit, onDelete }) {
  if (!data || data.length === 0) {
    return null;
  }

  // Obtener columnas del primer elemento
  const columns = Object.keys(data[0]).filter(key => key !== '__typename');

  // Función para formatear valores
  const formatValue = (value) => {
    if (value === null || value === undefined) return '-';
    if (typeof value === 'boolean') return value ? 'Sí' : 'No';
    if (typeof value === 'object' && value instanceof Date) {
      return new Date(value).toLocaleDateString();
    }
    if (typeof value === 'string' && value.match(/^\d{4}-\d{2}-\d{2}/)) {
      return new Date(value).toLocaleDateString();
    }
    if (typeof value === 'number') {
      return value.toLocaleString();
    }
    return String(value);
  };

  // Función para formatear nombres de columnas
  const formatColumnName = (columnName) => {
    return columnName
      .replace(/_/g, ' ')
      .replace(/\b\w/g, (char) => char.toUpperCase());
  };

  return (
    <div className="table-container">
      <table className="table">
        <thead>
          <tr>
            {columns.map((column) => (
              <th key={column}>{formatColumnName(column)}</th>
            ))}
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={item.id || index}>
              {columns.map((column) => (
                <td key={column}>{formatValue(item[column])}</td>
              ))}
              <td>
                <div className="table-actions">
                  <button
                    className="btn-icon"
                    onClick={() => onEdit(item)}
                    title="Editar"
                  >
                    <Edit size={18} />
                  </button>
                  <button
                    className="btn-icon danger"
                    onClick={() => onDelete(item)}
                    title="Eliminar"
                  >
                    <Trash2 size={18} />
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default DataTable;
