# SGApp Frontend

Sistema de Gestión completo desarrollado en React con diseño futurista en colores azules y negro, totalmente responsive para móviles y escritorio.

## 🚀 Características

- **Interfaz Moderna**: Diseño futurista con gradientes azules y negro
- **Totalmente Responsive**: Optimizado para móviles, tablets y escritorio
- **50+ Módulos**: Integración completa con todos los endpoints del backend
- **CRUD Completo**: Crear, Leer, Actualizar y Eliminar en todos los módulos
- **Navegación Intuitiva**: Sidebar organizado por categorías con secciones expandibles
- **Búsqueda en Tiempo Real**: Filtrado dinámico de datos
- **Formularios Dinámicos**: Generación automática de formularios basados en la estructura de datos

## 📋 Requisitos Previos

- Node.js (v16 o superior)
- npm o yarn
- Backend FastAPI ejecutándose en `http://localhost:8000`

## 🛠️ Instalación

1. **Instalar dependencias**:
```bash
npm install
```

2. **Iniciar el servidor de desarrollo**:
```bash
npm run dev
```

3. **Acceder a la aplicación**:
Abre tu navegador en `http://localhost:3000`

## 📦 Estructura del Proyecto

```
sgapp-frontend/
├── src/
│   ├── components/          # Componentes reutilizables
│   │   ├── DataTable.jsx   # Tabla de datos genérica
│   │   └── FormModal.jsx   # Modal de formulario dinámico
│   ├── pages/              # Páginas de la aplicación
│   │   ├── Dashboard.jsx   # Panel de control
│   │   └── GenericCRUD.jsx # Página CRUD genérica
│   ├── services/           # Servicios y API
│   │   └── api.js          # Configuración de Axios y endpoints
│   ├── App.jsx             # Componente principal
│   ├── App.css             # Estilos globales
│   └── main.jsx            # Punto de entrada
├── index.html              # HTML principal
├── vite.config.js          # Configuración de Vite
└── package.json            # Dependencias del proyecto
```

## 🎨 Módulos Disponibles

### Documentación (PA_DI)
- Fallas y Eventos
- Procesos
- Registro de Acciones

### Equipamiento (PA_EQ)
- Equipos
- Calibración
- Mantenimiento
- Verificación
- Y 15 módulos más...

### Instalaciones (PA_IA)
- Ambiente
- Áreas
- Limpieza
- Sanitización
- Y 6 módulos más...

### Personal (PA_PE)
- Personal
- Currículo Vitae
- Evaluaciones
- Formación
- Y 12 módulos más...

### Productos y Servicios (PA_PS)
- Productos y Servicios
- Órdenes de Servicio
- Proveedores
- Y 5 módulos más...

### Laboratorio (PC_LAB, PC_ES, PC_QR, PC_TC)
- Patrones
- Soluciones
- Especificaciones
- Técnicas
- Y 4 módulos más...

### Registros (PC_RE)
- Análisis
- Clientes
- Muestras
- Proyectos
- Y 10 módulos más...

### Planificación (PE_PL)
- Planes
- Objetivos
- Estrategias
- Actividades
- Y 4 módulos más...

### Servicios (PE_SE)
- Ensayos
- Capacitación
- Mantenimiento
- Mejoras
- Y 6 módulos más...

### Sistema (SYS, TBL)
- Factores K
- Lugares
- Posiciones del Horno

## 🎨 Diseño y Estilos

### Paleta de Colores
- **Fondo Principal**: #0a0e27 (Azul oscuro/negro)
- **Fondo Secundario**: #131829
- **Azul Primario**: #00d4ff (Cyan brillante)
- **Azul Secundario**: #0080ff
- **Azul Acento**: #4169e1
- **Éxito**: #00ff88
- **Advertencia**: #ffaa00
- **Peligro**: #ff4444

### Características del Diseño
- Gradientes suaves
- Sombras con efecto glow
- Transiciones animadas
- Bordes con color primario
- Hover effects interactivos

## 📱 Responsive Design

### Escritorio (> 768px)
- Sidebar fijo visible
- Layout a dos columnas
- Tablas con scroll horizontal si es necesario

### Tablet/Móvil (≤ 768px)
- Sidebar tipo drawer (se oculta/muestra)
- Menú hamburguesa
- Layout a una columna
- Botones y textos optimizados

### Móvil Pequeño (≤ 480px)
- Optimización de padding y fuentes
- Botones más pequeños
- Formularios adaptados

## 🔌 API Integration

El frontend se comunica con el backend FastAPI a través de Axios. La configuración del proxy en `vite.config.js` redirige las peticiones `/api/*` a `http://localhost:8000`.

### Ejemplo de uso:
```javascript
import { apiService } from './services/api';

// Obtener todos los registros
const data = await apiService.getAll('/pa-eq-eq');

// Crear nuevo registro
const newItem = await apiService.create('/pa-eq-eq', formData);

// Actualizar registro
const updated = await apiService.update('/pa-eq-eq', id, formData);

// Eliminar registro
await apiService.delete('/pa-eq-eq', id);
```

## 🚀 Scripts Disponibles

- `npm run dev` - Inicia el servidor de desarrollo
- `npm run build` - Construye la aplicación para producción
- `npm run preview` - Vista previa de la build de producción

## 🔧 Configuración del Backend

Asegúrate de que el backend FastAPI esté ejecutándose en `http://localhost:8000` con CORS habilitado:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 📝 Notas Importantes

1. **Primer Inicio**: Al iniciar por primera vez, ejecuta `npm install` para instalar todas las dependencias.
2. **Backend Requerido**: El frontend necesita que el backend FastAPI esté ejecutándose.
3. **Datos de Prueba**: Si no hay datos en la base de datos, las tablas mostrarán un estado vacío.

## 🐛 Solución de Problemas

### Error de conexión al backend
- Verifica que el backend esté ejecutándose en el puerto 8000
- Verifica la configuración de CORS en el backend
- Revisa la consola del navegador para más detalles

### Módulo no muestra datos
- Verifica que el endpoint existe en el backend
- Revisa que la tabla tenga datos en la base de datos
- Verifica la consola del navegador para errores de API

### Sidebar no se muestra en móvil
- Haz clic en el icono de menú (hamburguesa) en el header
- El sidebar debe deslizarse desde la izquierda

## 🤝 Contribuciones

Este es un proyecto privado de SGApp. Para contribuir, contacta al equipo de desarrollo.

## 📄 Licencia

Propiedad de SGApp. Todos los derechos reservados.
