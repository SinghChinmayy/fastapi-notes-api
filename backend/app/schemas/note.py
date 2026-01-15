# note schemas for data validation
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NoteCreate(BaseModel):
    """Schema for creating a new note"""
    title: str
    content: str


class NoteFetch(BaseModel):
    """Schema for returning note data"""
    id: int
    title: str
    content: str
    created_at: Optional[datetime] = None