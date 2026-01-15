from fastapi import FastAPI, HTTPException, status
from models import Note, NoteCreate, NoteUpdate
from typing import Dict, List

app = FastAPI(
    title="Notes API",
    description="A simple FastAPI application for managing notes in memory",
    version="1.0.0"
)

# In-memory storage
notes_db: Dict[int, Note] = {}
note_id_counter = 1


@app.get("/")
def read_root():
    """Root endpoint"""
    return {
        "message": "WELCOME TO THE NOTES APP",
        "docs": "/docs",
        "endpoints": {
            "create_note": "POST /notes/",
            "get_all_notes": "GET /notes/",
            "get_note": "GET /notes/{note_id}",
            "update_note": "PUT /notes/{note_id}",
            "delete_note": "DELETE /notes/{note_id}"
        }
    }


@app.post("/notes/", response_model=Note, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate):
    """
    Create a new note
    
    - **title**: Title of the note
    - **content**: Content of the note
    """
    global note_id_counter
    
    new_note = Note(
        id=note_id_counter,
        title=note.title,
        content=note.content
    )
    
    notes_db[note_id_counter] = new_note
    note_id_counter += 1
    
    return new_note


@app.get("/notes/", response_model=List[Note])
def get_all_notes():
    """
    Get all notes
    
    Returns a list of all notes in the system
    """
    return list[Note](notes_db.values())


@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    """
    Get a single note by ID
    
    - **note_id**: The ID of the note to retrieve
    """
    if note_id not in notes_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found"
        )
    
    return notes_db[note_id]


@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, note_update: NoteUpdate):
    """
    Update a note
    
    - **note_id**: The ID of the note to update
    - **title**: New title (optional)
    - **content**: New content (optional)
    """
    if note_id not in notes_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found"
        )
    
    existing_note = notes_db[note_id]
    
    # Update only the fields that were provided
    update_data = note_update.model_dump(exclude_unset=True)
    
    updated_note = Note(
        id=existing_note.id,
        title=update_data.get("title", existing_note.title),
        content=update_data.get("content", existing_note.content)
    )
    
    notes_db[note_id] = updated_note
    
    return updated_note


@app.delete("/notes/{note_id}", status_code=status.HTTP_200_OK)
def delete_note(note_id: int):
    """
    Delete a note
    
    - **note_id**: The ID of the note to delete
    """
    if note_id not in notes_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found"
        )
    
    deleted_note = notes_db.pop(note_id)
    
    return {
        "message": "Note deleted successfully",
        "deleted_note": deleted_note
    }
