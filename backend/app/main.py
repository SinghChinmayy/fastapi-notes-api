from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import health as health_check
from .routes import note as note_routes

app = FastAPI(
    title="Notes API",
    description="A REST API for managing notes with PostgreSQL",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev server
        "http://127.0.0.1:5173",  # Alternative localhost
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def root():
    return {"message": "This is my notes app backend"}

app.include_router(health_check.router, tags=["Health"])
app.include_router(note_routes.router, prefix="/notes", tags=["Notes"])