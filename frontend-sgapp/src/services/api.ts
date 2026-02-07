import axios from 'axios';

// Si estás en local con la VM, usa la IP de tu VM o localhost.
// Para producción, esto se cambiará por una variable de entorno.
const API_URL = 'http://192.168.100.200:8000/api/v1'; 

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para manejo de errores global (útil para el futuro login)
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      // Aquí manejaremos errores 401 (No autorizado) más adelante
      console.error('Error de API:', error.response.data);
    }
    return Promise.reject(error);
  }
);