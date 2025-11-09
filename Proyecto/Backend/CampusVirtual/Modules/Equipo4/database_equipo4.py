# models/database_equipo4.py
from sqlmodel import SQLModel, create_engine, Session

sqlite_file_name = "equipo4_database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# echo=True para ver las queries en la terminal
engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables_equipo4() -> None:
    from . import models_equipo4  # noqa: F401

    SQLModel.metadata.create_all(engine)


def get_session_equipo4():
    """
    Dependencia para FastAPI: abre una sesión a la BD del equipo 4
    y la cierra automáticamente al finalizar la petición.
    """
    with Session(engine) as session:
        yield session
