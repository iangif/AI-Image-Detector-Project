from fastapi import FastAPI
from app.controller.AnalyzerController import router

app = FastAPI()

app.include_router(router, prefix="/api")
