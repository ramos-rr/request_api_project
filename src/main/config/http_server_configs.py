"""
SERVERCONFIG: Use to turn on your APP so that your system know what to do and what APP is operating
"""
from fastapi import FastAPI
from src.main.routes import starships_routes


app = FastAPI()

app.include_router(starships_routes)
