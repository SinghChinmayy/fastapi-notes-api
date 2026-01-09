# FastAPI Notes App

A simple REST API built with FastAPI for managing notes in memory.

## Features

- ➕ Create a note
- 📄 Get all notes
- 🔍 Get a single note
- ✏️ Update a note
- ❌ Delete a note

## Architecture

```
Client (Postman / Browser)
        ↓ HTTP Request
FastAPI Server
        ↓
Business Logic
        ↓
In-Memory Notes Store
        ↑
     HTTP Response (JSON)
```

## Installation

1. **Clone or navigate to the project directory**

```bash
cd fast-api-notes
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

## Running the Server

Start the development server with:

```bash
uvicorn main:app --reload
```

The API will be available at: `http://localhost:8000`

## API Documentation

Once the server is running, you can access:

- **Interactive API docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative API docs (ReDoc)**: http://localhost:8000/redoc

## API Endpoints

### 1. Create a Note

**POST** `/notes/`

**Request Body:**
```json
{
  "title": "My First Note",
  "content": "This is the content of my note"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "title": "My First Note",
  "content": "This is the content of my note"
}
```

**cURL Example:**
```bash
curl -X POST "http://localhost:8000/notes/" \
  -H "Content-Type: application/json" \
  -d '{"title":"My First Note","content":"This is the content of my note"}'
```

---

### 2. Get All Notes

**GET** `/notes/`

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "title": "My First Note",
    "content": "This is the content of my note"
  },
  {
    "id": 2,
    "title": "Another Note",
    "content": "More content here"
  }
]
```

**cURL Example:**
```bash
curl -X GET "http://localhost:8000/notes/"
```

---

### 3. Get a Single Note

**GET** `/notes/{note_id}`

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "My First Note",
  "content": "This is the content of my note"
}
```

**Response (404 Not Found):**
```json
{
  "detail": "Note with id 99 not found"
}
```

**cURL Example:**
```bash
curl -X GET "http://localhost:8000/notes/1"
```

---

### 4. Update a Note

**PUT** `/notes/{note_id}`

**Request Body (partial update supported):**
```json
{
  "title": "Updated Title",
  "content": "Updated content"
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "Updated Title",
  "content": "Updated content"
}
```

**Response (404 Not Found):**
```json
{
  "detail": "Note with id 99 not found"
}
```

**cURL Example:**
```bash
curl -X PUT "http://localhost:8000/notes/1" \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated Title","content":"Updated content"}'
```

---

### 5. Delete a Note

**DELETE** `/notes/{note_id}`

**Response (200 OK):**
```json
{
  "message": "Note deleted successfully",
  "deleted_note": {
    "id": 1,
    "title": "My First Note",
    "content": "This is the content of my note"
  }
}
```

**Response (404 Not Found):**
```json
{
  "detail": "Note with id 99 not found"
}
```

**cURL Example:**
```bash
curl -X DELETE "http://localhost:8000/notes/1"
```

---

## Testing with Postman

1. Import the API into Postman by visiting `http://localhost:8000/docs` and clicking on the "Download" button
2. Or manually create requests using the endpoints documented above
3. Make sure to set `Content-Type: application/json` header for POST and PUT requests

## Project Structure

```
fast-api-notes/
├── main.py          # FastAPI app with all CRUD endpoints
├── models.py        # Pydantic models for Note
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Data Model

### Note
- `id` (int): Unique identifier (auto-generated)
- `title` (str): Title of the note
- `content` (str): Content of the note

## Notes

- All data is stored in memory and will be lost when the server restarts
- IDs are auto-incremented starting from 1
- Partial updates are supported (you can update just the title or just the content)

## License

This project is open source and available for educational purposes.
