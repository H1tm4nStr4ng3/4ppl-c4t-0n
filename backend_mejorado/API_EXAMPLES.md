# 📚 Ejemplos de Uso de la API

Este documento contiene ejemplos prácticos de cómo usar la API SGApp.

## 🌐 Base URL

```
http://localhost:8000
```

## 📋 Tabla de Contenidos

- [Health Check](#health-check)
- [Listar Registros](#listar-registros)
- [Obtener un Registro](#obtener-un-registro)
- [Crear Registro](#crear-registro)
- [Actualizar Registro](#actualizar-registro)
- [Eliminar Registro](#eliminar-registro)
- [Paginación Avanzada](#paginación-avanzada)

---

## Health Check

### cURL
```bash
curl -X GET "http://localhost:8000/health"
```

### Python (requests)
```python
import requests

response = requests.get("http://localhost:8000/health")
print(response.json())
```

### JavaScript (fetch)
```javascript
fetch('http://localhost:8000/health')
  .then(response => response.json())
  .then(data => console.log(data));
```

---

## Listar Registros

### cURL
```bash
# Listar primeros 50 registros (por defecto)
curl -X GET "http://localhost:8000/api/v1/pa-di-fa/"

# Listar con paginación personalizada
curl -X GET "http://localhost:8000/api/v1/pa-di-fa/?skip=0&limit=10"
```

### Python (requests)
```python
import requests

# Listar primeros 50 registros
response = requests.get("http://localhost:8000/api/v1/pa-di-fa/")
data = response.json()

print(f"Total de registros: {data['total']}")
print(f"Registros obtenidos: {len(data['items'])}")
print(f"Tiene más páginas: {data['has_next']}")

# Listar con paginación
params = {'skip': 0, 'limit': 10}
response = requests.get(
    "http://localhost:8000/api/v1/pa-di-fa/",
    params=params
)
```

### JavaScript (axios)
```javascript
const axios = require('axios');

// Listar con paginación
axios.get('http://localhost:8000/api/v1/pa-di-fa/', {
  params: {
    skip: 0,
    limit: 10
  }
})
.then(response => {
  const data = response.data;
  console.log(`Total: ${data.total}`);
  console.log(`Items: ${data.items.length}`);
})
.catch(error => console.error(error));
```

---

## Obtener un Registro

### cURL
```bash
curl -X GET "http://localhost:8000/api/v1/pa-di-fa/1"
```

### Python (requests)
```python
import requests

# Obtener registro con ID 1
response = requests.get("http://localhost:8000/api/v1/pa-di-fa/1")

if response.status_code == 200:
    registro = response.json()
    print(f"Evento: {registro['evento']}")
    print(f"Resuelto: {registro['resuelto']}")
elif response.status_code == 404:
    print("Registro no encontrado")
```

### JavaScript (fetch)
```javascript
fetch('http://localhost:8000/api/v1/pa-di-fa/1')
  .then(response => {
    if (!response.ok) throw new Error('Registro no encontrado');
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

---

## Crear Registro

### cURL
```bash
curl -X POST "http://localhost:8000/api/v1/pa-di-fa/" \
  -H "Content-Type: application/json" \
  -d '{
    "registrado_por": "Juan Pérez",
    "fecha": "2024-01-20T10:30:00",
    "evento": "Falla en el sistema de calibración",
    "resuelto": false
  }'
```

### Python (requests)
```python
import requests
from datetime import datetime

# Datos del nuevo registro
nuevo_registro = {
    "registrado_por": "Juan Pérez",
    "fecha": datetime.now().isoformat(),
    "evento": "Falla en el sistema de calibración",
    "resuelto": False
}

response = requests.post(
    "http://localhost:8000/api/v1/pa-di-fa/",
    json=nuevo_registro
)

if response.status_code == 201:
    registro_creado = response.json()
    print(f"Registro creado con ID: {registro_creado['id']}")
else:
    print(f"Error: {response.json()}")
```

### JavaScript (axios)
```javascript
const axios = require('axios');

const nuevoRegistro = {
  registrado_por: "Juan Pérez",
  fecha: new Date().toISOString(),
  evento: "Falla en el sistema de calibración",
  resuelto: false
};

axios.post('http://localhost:8000/api/v1/pa-di-fa/', nuevoRegistro)
  .then(response => {
    console.log(`Registro creado con ID: ${response.data.id}`);
  })
  .catch(error => {
    console.error('Error:', error.response.data);
  });
```

---

## Actualizar Registro

### cURL
```bash
# Actualizar parcialmente (solo los campos enviados)
curl -X PUT "http://localhost:8000/api/v1/pa-di-fa/1" \
  -H "Content-Type: application/json" \
  -d '{
    "resuelto": true
  }'
```

### Python (requests)
```python
import requests

# Actualizar solo el campo 'resuelto'
actualizacion = {
    "resuelto": True
}

response = requests.put(
    "http://localhost:8000/api/v1/pa-di-fa/1",
    json=actualizacion
)

if response.status_code == 200:
    registro_actualizado = response.json()
    print(f"Registro actualizado: {registro_actualizado}")
elif response.status_code == 404:
    print("Registro no encontrado")
```

### JavaScript (fetch)
```javascript
const actualizacion = {
  resuelto: true
};

fetch('http://localhost:8000/api/v1/pa-di-fa/1', {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(actualizacion)
})
.then(response => {
  if (!response.ok) throw new Error('Error al actualizar');
  return response.json();
})
.then(data => console.log('Actualizado:', data))
.catch(error => console.error(error));
```

---

## Eliminar Registro

### cURL
```bash
curl -X DELETE "http://localhost:8000/api/v1/pa-di-fa/1"
```

### Python (requests)
```python
import requests

response = requests.delete("http://localhost:8000/api/v1/pa-di-fa/1")

if response.status_code == 200:
    resultado = response.json()
    print(resultado['message'])
elif response.status_code == 404:
    print("Registro no encontrado")
```

### JavaScript (axios)
```javascript
axios.delete('http://localhost:8000/api/v1/pa-di-fa/1')
  .then(response => {
    console.log(response.data.message);
  })
  .catch(error => {
    if (error.response.status === 404) {
      console.log('Registro no encontrado');
    } else {
      console.error('Error:', error.response.data);
    }
  });
```

---

## Paginación Avanzada

### Python - Obtener todas las páginas
```python
import requests

def obtener_todos_los_registros(url_base, limite_por_pagina=50):
    """Obtiene todos los registros paginando automáticamente"""
    todos_los_registros = []
    skip = 0
    
    while True:
        response = requests.get(
            url_base,
            params={'skip': skip, 'limit': limite_por_pagina}
        )
        
        if response.status_code != 200:
            break
            
        data = response.json()
        todos_los_registros.extend(data['items'])
        
        # Si no hay más páginas, salir
        if not data['has_next']:
            break
            
        skip += limite_por_pagina
    
    return todos_los_registros

# Uso
registros = obtener_todos_los_registros(
    "http://localhost:8000/api/v1/pa-di-fa/"
)
print(f"Total de registros obtenidos: {len(registros)}")
```

### JavaScript - Paginación con React
```javascript
import { useState, useEffect } from 'react';

function useRegistros(endpoint, pageSize = 50) {
  const [data, setData] = useState({ items: [], total: 0 });
  const [page, setPage] = useState(0);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const response = await fetch(
          `${endpoint}?skip=${page * pageSize}&limit=${pageSize}`
        );
        const result = await response.json();
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [endpoint, page, pageSize]);

  return { data, loading, page, setPage };
}

// Uso en un componente
function ListaRegistros() {
  const { data, loading, page, setPage } = useRegistros(
    'http://localhost:8000/api/v1/pa-di-fa/'
  );

  if (loading) return <div>Cargando...</div>;

  return (
    <div>
      <ul>
        {data.items.map(item => (
          <li key={item.id}>{item.evento}</li>
        ))}
      </ul>
      
      <button 
        disabled={!data.has_prev} 
        onClick={() => setPage(page - 1)}
      >
        Anterior
      </button>
      
      <button 
        disabled={!data.has_next} 
        onClick={() => setPage(page + 1)}
      >
        Siguiente
      </button>
      
      <p>Total: {data.total} registros</p>
    </div>
  );
}
```

---

## 🔍 Ejemplos de Errores Comunes

### 404 - No Encontrado
```json
{
  "error": "Not Found",
  "message": "Registro con ID 999 no encontrado",
  "detail": null
}
```

### 422 - Error de Validación
```json
{
  "error": "Validation Error",
  "message": "Los datos proporcionados no son válidos",
  "detail": [
    {
      "loc": ["body", "fecha"],
      "msg": "invalid datetime format",
      "type": "value_error.datetime"
    }
  ]
}
```

### 500 - Error del Servidor
```json
{
  "error": "Internal Server Error",
  "message": "Ha ocurrido un error inesperado",
  "detail": null
}
```

---

## 📝 Notas

- Todos los endpoints requieren `Content-Type: application/json` para POST y PUT
- Las fechas deben estar en formato ISO 8601: `2024-01-20T10:30:00`
- La paginación está limitada a un máximo de 1000 registros por página
- Los campos opcionales pueden ser omitidos en las peticiones

---

**¿Necesitas más ayuda?** Consulta la documentación interactiva en http://localhost:8000/docs
