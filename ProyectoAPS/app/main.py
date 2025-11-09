# app/main.py
from fastapi import FastAPI, Depends
from sqlmodel import Session, select

from .database import create_db_and_tables, get_session
from . import models


app = FastAPI(
    title="Food Ordering API (SQLModel)",
    description="Backend con FastAPI + SQLModel para el proyecto de puestos de comida en CU.",
    version="1.0.0",
)


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()


@app.get("/food-stands", response_model=list[models.FoodStand])
def list_food_stands(session: Session = Depends(get_session)):
    statement = select(models.FoodStand)
    results = session.exec(statement)
    return results.all()


@app.post("/food-stands", response_model=models.FoodStand)
def create_food_stand(
    food_stand: models.FoodStand,
    session: Session = Depends(get_session),
):
    session.add(food_stand)
    session.commit()
    session.refresh(food_stand)
    return food_stand
