# FastAPI Notes App

![Notes App Screenshot](sample_img_1.png)

A full-stack notes application with FastAPI backend and Svelte frontend.

## 🚀 Features

- ✅ Create, read, update, and delete notes (CRUD)
- 🗄️ PostgreSQL database integration
- 🎨 Modern Svelte frontend
- 📝 RESTful API with FastAPI
- 🔍 Auto-generated API documentation
- ⚡ Fast and responsive UI

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL ORM
- **PostgreSQL** - Database
- **Pydantic** - Data validation

### Frontend
- **Svelte 4** - Reactive UI framework
- **Vite** - Fast build tool
- **Vanilla CSS** - Styling

## 📁 Project Structure

```
fast-api-notes/
├── backend/
│   └── app/
│       ├── main.py          # FastAPI app
│       ├── database.py      # Database connection
│       ├── init_db.py       # Database initialization
│       ├── models/          # SQLAlchemy models
│       ├── routes/          # API endpoints
│       └── schemas/         # Pydantic schemas
├── frontend/
│   ├── src/
│   │   ├── App.svelte      # Main component
│   │   └── main.js         # Entry point
│   └── package.json
└── requirements.txt
```

## 🚦 Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL
- Node.js 18+
- npm or yarn

### Backend Setup

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Set up PostgreSQL database:**
```bash
# Create database
createdb notesdb

# Or with custom user
sudo -u postgres psql
CREATE DATABASE notesdb;
CREATE USER notesuser WITH PASSWORD 'notes123';
GRANT ALL PRIVILEGES ON DATABASE notesdb TO notesuser;
\q
```

3. **Configure environment variables:**
Create `.env` file in the root:
```
DATABASE_URL=postgresql://notesuser:notes123@localhost:5432/notesdb
```

4. **Initialize database:**
```bash
python -m backend.app.init_db
```

5. **Run backend server:**
```bash
uvicorn backend.app.main:app --reload
```

Backend will be available at `http://localhost:8000`
- API docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Frontend Setup

1. **Navigate to frontend directory:**
```bash
cd frontend
```

2. **Install dependencies:**
```bash
npm install
```

3. **Run development server:**
```bash
npm run dev
```

Frontend will be available at `http://localhost:5173`

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/notes/` | Create a new note |
| GET | `/notes/` | Get all notes |
| GET | `/notes/{note_id}` | Get a specific note |
| PUT | `/notes/{note_id}` | Update a note |
| DELETE | `/notes/{note_id}` | Delete a note |
| GET | `/health` | Health check |

## 🗄️ Database Schema

**Table: notes**

| Column | Type | Constraints |
|--------|------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT |
| title | varchar | NOT NULL |
| content | varchar | NOT NULL |
| created_at | timestamp | DEFAULT now() |
| updated_at | timestamp | ON UPDATE |

**Default Database Credentials:**
- Database: `notesdb`
- User: `notesuser`
- Password: `notes123`

## 🧪 Testing

### Backend Tests
```bash
# Create test note
curl -X POST "http://localhost:8000/notes/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Note", "content": "This is a test"}'

# Get all notes
curl http://localhost:8000/notes/

# Get specific note
curl http://localhost:8000/notes/1
```

### Frontend
Open `http://localhost:5173` and test the UI:
- Create notes using the form
- View all notes in the grid
- Delete notes using the trash icon

## 📝 Future Additions

- [ ] User authentication & authorization
- [ ] Note versioning & history
- [ ] Search and filter functionality
- [ ] Tags/categories for notes
- [ ] Rich text editor
- [ ] Dark mode
- [ ] Note sharing
- [ ] Export notes (PDF, Markdown)

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details