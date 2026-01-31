# 🔄 Guía de Migración - Backend Antiguo → Backend Nuevo

Esta guía te ayudará a migrar del backend antiguo al nuevo backend mejorado.

## 📊 Resumen de Cambios

### Cambios en URLs

| Antiguo | Nuevo | Notas |
|---------|-------|-------|
| `/pa-di-fa/` | `/api/v1/pa-di-fa/` | Agregado prefijo API versión |
| No disponible | `/api/v1/pa-di-fa/{id}` | Nuevo endpoint GET por ID |
| No disponible | DELETE endpoints | Ahora disponible para todas las entidades |

### Cambios en Respuestas

#### Antes (Lista Simple)
```json
[
  {
    "id": 1,
    "evento": "Evento 1",
    "resuelto": false
  }
]
```

#### Ahora (Paginada)
```json
{
  "items": [
    {
      "id": 1,
      "evento": "Evento 1",
      "resuelto": false
    }
  ],
  "total": 100,
  "skip": 0,
  "limit": 50,
  "has_next": true,
  "has_prev": false
}
```

---

## 🔧 Cambios Necesarios en el Frontend

### 1. Actualizar URLs Base

#### JavaScript/TypeScript
```javascript
// Antes
const API_URL = 'http://localhost:8000';

// Ahora
const API_URL = 'http://localhost:8000/api/v1';
```

### 2. Manejar Respuestas Paginadas

#### Antes
```javascript
// Fetch directo de array
fetch('/pa-di-fa/')
  .then(res => res.json())
  .then(items => {
    // items es un array directamente
    console.log(items);
  });
```

#### Ahora
```javascript
// Fetch de objeto paginado
fetch('/api/v1/pa-di-fa/')
  .then(res => res.json())
  .then(data => {
    // data.items contiene el array
    console.log(data.items);
    console.log('Total:', data.total);
  });
```

### 3. Implementar Paginación

#### React Example
```jsx
import { useState, useEffect } from 'react';

function DataTable() {
  const [data, setData] = useState({ items: [], total: 0 });
  const [page, setPage] = useState(0);
  const pageSize = 50;

  useEffect(() => {
    fetch(`/api/v1/pa-di-fa/?skip=${page * pageSize}&limit=${pageSize}`)
      .then(res => res.json())
      .then(setData);
  }, [page]);

  return (
    <div>
      <table>
        <tbody>
          {data.items.map(item => (
            <tr key={item.id}>
              <td>{item.evento}</td>
            </tr>
          ))}
        </tbody>
      </table>
      
      <div>
        <button 
          disabled={!data.has_prev}
          onClick={() => setPage(p => p - 1)}
        >
          Anterior
        </button>
        
        <span>Página {page + 1}</span>
        
        <button 
          disabled={!data.has_next}
          onClick={() => setPage(p => p + 1)}
        >
          Siguiente
        </button>
      </div>
    </div>
  );
}
```

### 4. Manejar Nuevos Errores

#### Antes
```javascript
fetch('/pa-di-fa/')
  .then(res => res.json())
  .catch(err => console.error(err));
```

#### Ahora
```javascript
fetch('/api/v1/pa-di-fa/')
  .then(res => {
    if (!res.ok) {
      return res.json().then(err => {
        throw new Error(err.message);
      });
    }
    return res.json();
  })
  .then(data => console.log(data))
  .catch(err => {
    // Manejo de error con mensaje estructurado
    console.error('Error:', err.message);
  });
```

---

## 📝 Actualizar Servicios/APIs

### Servicio Angular

#### Antes
```typescript
@Injectable()
export class DataService {
  private apiUrl = 'http://localhost:8000';

  getAll(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/pa-di-fa/`);
  }
}
```

#### Ahora
```typescript
interface PaginatedResponse<T> {
  items: T[];
  total: number;
  skip: number;
  limit: number;
  has_next: boolean;
  has_prev: boolean;
}

@Injectable()
export class DataService {
  private apiUrl = 'http://localhost:8000/api/v1';

  getAll(skip = 0, limit = 50): Observable<PaginatedResponse<any>> {
    const params = new HttpParams()
      .set('skip', skip.toString())
      .set('limit', limit.toString());
    
    return this.http.get<PaginatedResponse<any>>(
      `${this.apiUrl}/pa-di-fa/`,
      { params }
    );
  }

  getById(id: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/pa-di-fa/${id}`);
  }

  delete(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/pa-di-fa/${id}`);
  }
}
```

### API Client Python

#### Antes
```python
import requests

class SGAppClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
    
    def get_all(self):
        response = requests.get(f"{self.base_url}/pa-di-fa/")
        return response.json()
```

#### Ahora
```python
import requests
from typing import Dict, List, Optional

class SGAppClient:
    def __init__(self, base_url="http://localhost:8000/api/v1"):
        self.base_url = base_url
    
    def get_all(self, skip: int = 0, limit: int = 50) -> Dict:
        """Obtiene registros paginados"""
        response = requests.get(
            f"{self.base_url}/pa-di-fa/",
            params={'skip': skip, 'limit': limit}
        )
        response.raise_for_status()
        return response.json()
    
    def get_by_id(self, id: int) -> Dict:
        """Obtiene un registro por ID"""
        response = requests.get(f"{self.base_url}/pa-di-fa/{id}")
        response.raise_for_status()
        return response.json()
    
    def create(self, data: Dict) -> Dict:
        """Crea un nuevo registro"""
        response = requests.post(
            f"{self.base_url}/pa-di-fa/",
            json=data
        )
        response.raise_for_status()
        return response.json()
    
    def update(self, id: int, data: Dict) -> Dict:
        """Actualiza un registro"""
        response = requests.put(
            f"{self.base_url}/pa-di-fa/{id}",
            json=data
        )
        response.raise_for_status()
        return response.json()
    
    def delete(self, id: int) -> Dict:
        """Elimina un registro"""
        response = requests.delete(f"{self.base_url}/pa-di-fa/{id}")
        response.raise_for_status()
        return response.json()
    
    def get_all_items(self, endpoint: str) -> List[Dict]:
        """Obtiene todos los registros paginando automáticamente"""
        all_items = []
        skip = 0
        limit = 100
        
        while True:
            data = self.get_all(skip=skip, limit=limit)
            all_items.extend(data['items'])
            
            if not data['has_next']:
                break
            
            skip += limit
        
        return all_items

# Uso
client = SGAppClient()

# Obtener página específica
data = client.get_all(skip=0, limit=50)
print(f"Total: {data['total']}")
print(f"Items: {len(data['items'])}")

# Obtener todos los registros
all_items = client.get_all_items('/pa-di-fa/')
print(f"Total items: {len(all_items)}")
```

---

## 🔄 Migración Paso a Paso

### Fase 1: Preparación (Sin downtime)

1. **Actualizar variables de entorno**
   ```bash
   # Copiar .env.example y ajustar valores
   cp .env.example .env
   ```

2. **Verificar base de datos**
   ```bash
   # Asegurar que el schema SGApp existe
   psql -U postgres -d SGApp -c "SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'SGApp';"
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

### Fase 2: Testing Paralelo

1. **Levantar nuevo backend en puerto diferente**
   ```bash
   # Backend antiguo en 8000
   # Backend nuevo en 8001
   uvicorn app.main:app --port 8001
   ```

2. **Probar endpoints**
   ```bash
   # Health check
   curl http://localhost:8001/health
   
   # Listar registros
   curl http://localhost:8001/api/v1/pa-di-fa/
   
   # Crear registro
   curl -X POST http://localhost:8001/api/v1/pa-di-fa/ \
     -H "Content-Type: application/json" \
     -d '{"evento": "Test", "resuelto": false}'
   ```

3. **Actualizar frontend gradualmente**
   - Crear rama separada para cambios de frontend
   - Actualizar un módulo a la vez
   - Testear exhaustivamente

### Fase 3: Migración (Con downtime mínimo)

1. **Planificar ventana de mantenimiento**
   - Notificar a usuarios
   - Elegir horario de bajo uso

2. **Detener backend antiguo**
   ```bash
   # Si está corriendo con systemd
   sudo systemctl stop sgapp-api-old
   ```

3. **Iniciar nuevo backend**
   ```bash
   # Usar Docker Compose (recomendado)
   docker-compose up -d
   
   # O directamente
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

4. **Desplegar frontend actualizado**
   ```bash
   # Build production
   npm run build
   
   # Deploy
   # (tu proceso de deployment específico)
   ```

5. **Verificar funcionamiento**
   ```bash
   # Health check
   curl http://localhost:8000/health
   
   # Verificar endpoints críticos
   curl http://localhost:8000/api/v1/pa-di-fa/
   ```

---

## ✅ Checklist de Migración

### Backend
- [ ] Configurar variables de entorno (.env)
- [ ] Verificar conexión a base de datos
- [ ] Instalar dependencias
- [ ] Ejecutar tests
- [ ] Verificar logs

### Frontend
- [ ] Actualizar URLs base (agregar /api/v1)
- [ ] Modificar manejo de respuestas (items → data.items)
- [ ] Implementar paginación
- [ ] Actualizar manejo de errores
- [ ] Agregar endpoint DELETE donde sea necesario
- [ ] Agregar endpoint GET por ID donde sea necesario

### Testing
- [ ] Probar todos los endpoints CRUD
- [ ] Verificar paginación
- [ ] Probar manejo de errores
- [ ] Verificar integración con frontend
- [ ] Load testing (opcional pero recomendado)

### Deployment
- [ ] Configurar proxy reverso (nginx/traefik)
- [ ] Configurar SSL/HTTPS
- [ ] Configurar CORS para dominio productivo
- [ ] Configurar logs centralizados
- [ ] Configurar monitoreo
- [ ] Configurar backups automáticos

---

## 🚨 Problemas Comunes y Soluciones

### Problema: CORS Error
```
Access to fetch at 'http://localhost:8000/api/v1/pa-di-fa/' 
from origin 'http://localhost:3000' has been blocked by CORS policy
```

**Solución:**
```python
# En .env
BACKEND_CORS_ORIGINS=["http://localhost:3000","http://localhost:4200"]
```

### Problema: 404 Not Found
```
Error 404: Endpoint no encontrado
```

**Solución:**
Verificar que estés usando el prefijo correcto:
- ❌ `/pa-di-fa/`
- ✅ `/api/v1/pa-di-fa/`

### Problema: Datos no se muestran
```
TypeError: data.map is not a function
```

**Solución:**
```javascript
// Antes
data.map(item => ...)

// Ahora
data.items.map(item => ...)
```

---

## 📞 Soporte

Si encuentras problemas durante la migración:
1. Revisa los logs del backend: `docker-compose logs -f api`
2. Verifica la documentación interactiva: `http://localhost:8000/docs`
3. Consulta los ejemplos en `API_EXAMPLES.md`
4. Abre un issue en el repositorio

---

**¡Buena suerte con la migración!** 🚀
