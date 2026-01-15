from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List

from ..schemas.note import NoteCreate, NoteFetch
from ..database import get_db
from ..models import Note

router = APIRouter()


@router.post("/", response_model=NoteFetch, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    """Create a new note"""
    # Create SQLAlchemy model instance
    db_note = Note(
        title=note.title,
        content=note.content
    )
    
    # Add to database
    db.add(db_note)
    db.commit()
    db.refresh(db_note)  # Get the generated ID and timestamps
    
    return db_note


@router.get("/", response_model=List[NoteFetch])
def get_all_notes(db: Session = Depends(get_db)):
    """Get all notes"""
    notes = db.query(Note).all()
    return notes


@router.get("/{note_id}", response_model=NoteFetch)
def get_note(note_id: int, db: Session = Depends(get_db)):
    """Get a single note by ID"""
    note = db.query(Note).filter(Note.id == note_id).first()
    
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found"
        )
    
    return note


@router.put("/{note_id}", response_model=NoteFetch)
def update_note(note_id: int, note_update: NoteCreate, db: Session = Depends(get_db)):
    """Update a note"""
    note = db.query(Note).filter(Note.id == note_id).first()
    
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found"
        )
    
    # Update fields
    note.title = note_update.title
    note.content = note_update.content
    
    db.commit()
    db.refresh(note)
    
    return note


@router.delete("/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    """Delete a note"""
    note = db.query(Note).filter(Note.id == note_id).first()
    
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found"
        )
    
    db.delete(note)
    db.commit()
    
    return {"message": "Note deleted successfully"}