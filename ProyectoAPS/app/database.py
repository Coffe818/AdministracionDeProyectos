# app/database.py
from sqlmodel import SQLModel, create_engine, Session

# Nombre del archivo de base de datos SQLite
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# echo=True para ver en consola las consultas SQL que se ejecutan (útil en clase)
engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables() -> None:
    # Import aquí para registrar los modelos antes de crear las tablas
    from . import models  # noqa: F401

    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

