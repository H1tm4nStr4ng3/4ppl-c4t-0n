import axios from 'axios';

const API_BASE_URL = '/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Función genérica para obtener todos los elementos de un endpoint
const getAll = async (endpoint) => {
  const response = await api.get(`${endpoint}/`);
  return response.data;
};

// Función genérica para obtener un elemento por ID
const getById = async (endpoint, id) => {
  const response = await api.get(`${endpoint}/${id}`);
  return response.data;
};

// Función genérica para crear un nuevo elemento
const create = async (endpoint, data) => {
  const response = await api.post(`${endpoint}/`, data);
  return response.data;
};

// Función genérica para actualizar un elemento
const update = async (endpoint, id, data) => {
  const response = await api.put(`${endpoint}/${id}`, data);
  return response.data;
};

// Función genérica para eliminar un elemento
const deleteItem = async (endpoint, id) => {
  const response = await api.delete(`${endpoint}/${id}`);
  return response.data;
};

// Definición de todos los endpoints del sistema
export const endpoints = {
  // PA_DI - Documentación
  PA_DI_FA: { path: '/pa-di-fa', name: 'Fallas y Eventos' },
  PA_DI_PR: { path: '/pa-di-pr', name: 'Procesos' },
  PA_DI_RA: { path: '/pa-di-ra', name: 'Registro de Acciones' },
  
  // PA_EQ - Equipamiento
  PA_EQ_AC: { path: '/pa-eq-ac', name: 'Actividades de Equipos' },
  PA_EQ_CA: { path: '/pa-eq-ca', name: 'Calibración' },
  PA_EQ_CB: { path: '/pa-eq-cb', name: 'Calibración Base' },
  PA_EQ_CH: { path: '/pa-eq-ch', name: 'Cronómetros' },
  PA_EQ_CI: { path: '/pa-eq-ci', name: 'Calibración Instrumentos' },
  PA_EQ_CV: { path: '/pa-eq-cv', name: 'Calibración Variables' },
  PA_EQ_DC: { path: '/pa-eq-dc', name: 'Documentación de Calibración' },
  PA_EQ_EQ: { path: '/pa-eq-eq', name: 'Equipos' },
  PA_EQ_EX: { path: '/pa-eq-ex', name: 'Equipos Externos' },
  PA_EQ_HM: { path: '/pa-eq-hm', name: 'Hornos y Muflas' },
  PA_EQ_LE: { path: '/pa-eq-le', name: 'Lectura de Equipos' },
  PA_EQ_MA: { path: '/pa-eq-ma', name: 'Mantenimiento' },
  PA_EQ_MO: { path: '/pa-eq-mo', name: 'Módulos' },
  PA_EQ_MR: { path: '/pa-eq-mr', name: 'Materiales de Referencia' },
  PA_EQ_MV: { path: '/pa-eq-mv', name: 'Mantenimiento Verificación' },
  PA_EQ_PA: { path: '/pa-eq-pa', name: 'Patrones' },
  PA_EQ_PR: { path: '/pa-eq-pr', name: 'Programación' },
  PA_EQ_RE: { path: '/pa-eq-re', name: 'Revisión de Equipos' },
  PA_EQ_RP: { path: '/pa-eq-rp', name: 'Reparaciones' },
  PA_EQ_VE: { path: '/pa-eq-ve', name: 'Verificación' },
  
  // PA_IA - Instalaciones
  PA_IA_AH: { path: '/pa-ia-ah', name: 'Acondicionamiento de Ambiente' },
  PA_IA_AM: { path: '/pa-ia-am', name: 'Ambiente' },
  PA_IA_AR: { path: '/pa-ia-ar', name: 'Área' },
  PA_IA_CA: { path: '/pa-ia-ca', name: 'Calibración de Ambiente' },
  PA_IA_LE: { path: '/pa-ia-le', name: 'Lectura de Ambiente' },
  PA_IA_LI: { path: '/pa-ia-li', name: 'Limpieza' },
  PA_IA_RA: { path: '/pa-ia-ra', name: 'Registro de Ambiente' },
  PA_IA_RI: { path: '/pa-ia-ri', name: 'Riesgos' },
  PA_IA_SA: { path: '/pa-ia-sa', name: 'Sanitización' },
  PA_IA_SI: { path: '/pa-ia-si', name: 'Servicios' },
  
  // PA_PE - Personal
  PA_PE_AU: { path: '/pa-pe-au', name: 'Auditorías' },
  PA_PE_CV: { path: '/pa-pe-cv', name: 'Currículo Vitae' },
  PA_PE_DE: { path: '/pa-pe-de', name: 'Desempeño' },
  PA_PE_EC: { path: '/pa-pe-ec', name: 'Evaluación de Competencias' },
  PA_PE_EF: { path: '/pa-pe-ef', name: 'Evaluación de Formación' },
  PA_PE_FG: { path: '/pa-pe-fg', name: 'Formación General' },
  PA_PE_IE: { path: '/pa-pe-ie', name: 'Informe de Evaluación' },
  PA_PE_IS: { path: '/pa-pe-is', name: 'Informe de Seguimiento' },
  PA_PE_PE: { path: '/pa-pe-pe', name: 'Personal' },
  PA_PE_PL: { path: '/pa-pe-pl', name: 'Plan de Trabajo' },
  PA_PE_PO: { path: '/pa-pe-po', name: 'Ponderación' },
  PA_PE_PR: { path: '/pa-pe-pr', name: 'Programación' },
  PA_PE_RQ: { path: '/pa-pe-rq', name: 'Requisitos' },
  PA_PE_SE: { path: '/pa-pe-se', name: 'Seguimiento' },
  PA_PE_SP: { path: '/pa-pe-sp', name: 'Supervisión' },
  PA_PE_SU: { path: '/pa-pe-su', name: 'Sustitución' },
  
  // PA_PS - Productos y Servicios
  PA_PS_AD: { path: '/pa-ps-ad', name: 'Adquisiciones' },
  PA_PS_CR: { path: '/pa-ps-cr', name: 'Control de Registros' },
  PA_PS_DE: { path: '/pa-ps-de', name: 'Desarrollo' },
  PA_PS_EV: { path: '/pa-ps-ev', name: 'Evaluación' },
  PA_PS_OS: { path: '/pa-ps-os', name: 'Orden de Servicio' },
  PA_PS_PR: { path: '/pa-ps-pr', name: 'Proveedores' },
  PA_PS_PS: { path: '/pa-ps-ps', name: 'Productos y Servicios' },
  
  // PC_ES - Especificaciones
  PC_ES_ES: { path: '/pc-es-es', name: 'Especificaciones' },
  
  // PC_LAB - Laboratorio
  PC_LAB_PATRONES: { path: '/pc-lab-patrones', name: 'Patrones' },
  PC_LAB_SOLUCIONES: { path: '/pc-lab-soluciones', name: 'Soluciones' },
  PC_LAB_SOLUCIONES_DET: { path: '/pc-lab-soluciones-det', name: 'Detalle de Soluciones' },
  PC_LAB_VALIDACION: { path: '/pc-lab-validacionmetodos', name: 'Validación de Métodos' },
  
  // PC_QR - Quality
  PC_QR_QU: { path: '/pc-qr-qu', name: 'Quejas' },
  
  // PC_RE - Registros
  PC_RE_AC: { path: '/pc-re-ac', name: 'Actas' },
  PC_RE_ANALISIS: { path: '/pc-re-analisis', name: 'Análisis' },
  PC_RE_CC: { path: '/pc-re-cc', name: 'Control de Calidad' },
  PC_RE_CL: { path: '/pc-re-cl', name: 'Clientes' },
  PC_RE_CO: { path: '/pc-re-co', name: 'Comunicaciones' },
  PC_RE_MU: { path: '/pc-re-mu', name: 'Muestras' },
  PC_RE_OF: { path: '/pc-re-of', name: 'Ofertas' },
  PC_RE_PI: { path: '/pc-re-pi', name: 'Planillas' },
  PC_RE_PR: { path: '/pc-re-pr', name: 'Proyectos' },
  PC_RE_SE: { path: '/pc-re-se', name: 'Servicios' },
  PC_RE_SG: { path: '/pc-re-sg', name: 'Seguimiento' },
  PC_RE_SH: { path: '/pc-re-sh', name: 'Historiales' },
  PC_RE_SO: { path: '/pc-re-so', name: 'Solicitudes' },
  
  // PC_TC - Técnicas
  PC_TC_TC: { path: '/pc-tc-tc', name: 'Técnicas' },
  
  // PE_PL - Planificación
  PE_PL_AC: { path: '/pe-pl-ac', name: 'Actividades' },
  PE_PL_CO: { path: '/pe-pl-co', name: 'Competencias' },
  PE_PL_ES: { path: '/pe-pl-es', name: 'Estrategias' },
  PE_PL_OB: { path: '/pe-pl-ob', name: 'Objetivos' },
  PE_PL_PC: { path: '/pe-pl-pc', name: 'Procesos' },
  PE_PL_PI: { path: '/pe-pl-pi', name: 'Plan Integral' },
  PE_PL_PL: { path: '/pe-pl-pl', name: 'Planes' },
  PE_PL_RO: { path: '/pe-pl-ro', name: 'Roles' },
  
  // PE_SE - Servicios
  PE_SE_AC: { path: '/pe-se-ac', name: 'Acciones' },
  PE_SE_CA: { path: '/pe-se-ca', name: 'Capacitación' },
  PE_SE_CO: { path: '/pe-se-co', name: 'Conformidad' },
  PE_SE_EE: { path: '/pe-se-ee', name: 'Estado de Equipos' },
  PE_SE_EN: { path: '/pe-se-en', name: 'Ensayos' },
  PE_SE_MA: { path: '/pe-se-ma', name: 'Mantenimiento' },
  PE_SE_ME: { path: '/pe-se-me', name: 'Mejoras' },
  PE_SE_RE: { path: '/pe-se-re', name: 'Revisiones' },
  PE_SE_SA: { path: '/pe-se-sa', name: 'Satisfacción' },
  PE_SE_SS: { path: '/pe-se-ss', name: 'Salidas del Sistema' },
  
  // SYS - Sistema
  SYS_FACTORESK: { path: '/sys-factoresk', name: 'Factores K' },
  
  // TBL - Tablas
  TBL_LUGARES: { path: '/tbl-lugares', name: 'Lugares' },
  TBL_POSICIONES_HORNO: { path: '/tbl-posiciones-horno', name: 'Posiciones del Horno' },
};

// Exportar funciones CRUD genéricas
export const apiService = {
  getAll,
  getById,
  create,
  update,
  delete: deleteItem,
  endpoints
};

export default api;
