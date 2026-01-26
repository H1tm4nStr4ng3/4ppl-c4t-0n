from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cambia los datos por los de tu servidor Debian
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/SGApp"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"options": "-c search_path=SGApp"}  # 👈 Esto indica el esquema
)


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()