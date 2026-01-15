from fastapi import FastAPI
from routes import health as health_check
from routes import note as note_routes

app = FastAPI()

@app.get("/")
def root():
    return {"message": "This is my notes app backend"}

app.include_router(health_check.router, tags=["Health"])
app.include_router(note_routes.router, prefix="/notes", tags=["Notes"])