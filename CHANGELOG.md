# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- PostgreSQL database integration with SQLAlchemy ORM
- Database models for Notes with automatic timestamps
- Database initialization script (`init_db.py`)
- Pydantic schemas for request/response validation
- CRUD API endpoints for notes management
- Health check endpoint
- Automatic `created_at` timestamp on note creation
- Automatic `updated_at` timestamp on note modification
- Package structure with proper `__init__.py` files
- Environment variable support for database configuration
- Sample notes for testing

### Changed
- Migrated from in-memory storage to PostgreSQL database
- Updated project structure to use Python package format
- Fixed all import statements to use relative imports
- Corrected database connection string (username: notesuser)

### Fixed
- Import errors in `main.py` with relative imports
- Import errors in `routes/note.py` with package structure
- Import errors in `models/notes.py` with relative imports
- Module resolution issues for running as a package
- Database authentication issues with correct username

### Technical Details
- **Database**: PostgreSQL with user `notesuser`, database `notesdb`
- **ORM**: SQLAlchemy 2.x
- **API Framework**: FastAPI
- **Schema Validation**: Pydantic

## [0.1.0] - 2026-01-15

### Added
- Initial FastAPI application setup
- Basic REST API structure
- In-memory note storage
- Basic CRUD operations
- Project documentation

### Endpoints
- `POST /notes/` - Create a new note
- `GET /notes/` - List all notes
- `GET /notes/{note_id}` - Get a specific note
- `PUT /notes/{note_id}` - Update a note
- `DELETE /notes/{note_id}` - Delete a note
- `GET /health` - Health check endpoint

---

## Notes

### How to Run
```bash
# Initialize database tables
python -m backend.app.init_db

# Start the server
uvicorn backend.app.main:app --reload
```

### Database Schema
**Table: notes**
- `id` (Integer, Primary Key, Auto-increment)
- `title` (String, NOT NULL)
- `content` (String, NOT NULL)
- `created_at` (Timestamp with timezone, Default: NOW())
- `updated_at` (Timestamp with timezone, Auto-updated on changes)

### Future Plans
- User authentication and authorization
- Note versioning and edit history
- Search functionality
- Tags/categories for notes
- Note sharing capabilities
