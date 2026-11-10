
from fastapi import FastAPI
from app.routes.look_routes import router as look_router

app = FastAPI()

app.include_router(look_router)

@app.get("/")
def root():
    return {"message": "Closetiq API running"}
