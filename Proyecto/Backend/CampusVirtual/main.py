# main.py
from fastapi import FastAPI
from Modules.Equipo1.Routes.equipo1_router import router as equipo1_router
from models.database_equipo4 import create_db_and_tables_equipo4

app = FastAPI()

app.include_router(
    equipo1_router,
    prefix="/api/equipo1",
    tags=["Equipo 1 - Items"],
)

@app.on_event("startup")
def startup_event():
    create_db_and_tables_equipo4()
