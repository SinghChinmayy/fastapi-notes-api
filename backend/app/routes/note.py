from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from typing import Dict, List

# Schemas for data validation
from schemas.note import NoteCreate, NoteFetch

router = APIRouter()

# In-memory note storage
notes_db: Dict[int, dict] = {}

# Note ID counter
note_id_counter = 1


@router.post("/", response_model=NoteFetch, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate):
    """
    Create a new note
    
    - **title**: Title of the note
    - **content**: Content of the note
    """
    global note_id_counter
    
    # Create new note dictionary
    new_note = {
        "id": note_id_counter,
        "title": note.title,
        "content": note.content,
        "created_at": datetime.now()
    }
    
    # Store in database
    notes_db[note_id_counter] = new_note
    note_id_counter += 1
    
    return new_note


@router.get("/", response_model=List[NoteFetch], status_code=status.HTTP_200_OK)
def get_all_notes():
    """
    Get all notes
    
    Returns a list of all notes stored in the system
    """
    return list(notes_db.values())


@router.get("/{note_id}", response_model=NoteFetch, status_code=status.HTTP_200_OK)
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
    