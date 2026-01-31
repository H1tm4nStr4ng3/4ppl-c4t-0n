"""
Configuración central de la aplicación
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Configuración de la aplicación"""
    
    # API
    PROJECT_NAME: str = "SGApp API"
    VERSION: str = "2.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Base de datos
    DATABASE_URL: str = "postgresql://postgres:h1tm4n7793%3F@localhost:5432/SGApp"
    
    # Pool de conexiones
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20
    DB_POOL_PRE_PING: bool = True
    
    # CORS
    BACKEND_CORS_ORIGINS: list = ["*"]
    
    # Paginación
    DEFAULT_PAGE_SIZE: int = 50
    MAX_PAGE_SIZE: int = 1000
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    # Seguridad
    SECRET_KEY: str = "your-secret-key-change-in-production"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
