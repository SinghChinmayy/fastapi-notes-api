from pydantic import BaseModel
from typing import Optional


class NoteCreate(BaseModel):
    """Schema for creating a new note"""
    title: str
    content: str


class NoteUpdate(BaseModel):
    """Schema for updating an existing note"""
    title: Optional[str] = None
    content: Optional[str] = None


class Note(BaseModel):
    """Schema for a complete note with ID"""
    id: int
    title: str
    content: str
