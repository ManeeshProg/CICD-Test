from fastapi import FastAPI
from app.health import router as health_router

app=FastAPI(title="CICD_Demo")
app.include_router(health_router)
@app.get("/")
def welcome():
    return {"message": "FastAPI CI/CD running 🚀"}