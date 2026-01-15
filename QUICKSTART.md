# Quick Start Guide

Get the Notes App running in 5 minutes!

## 1. Clone & Navigate

```bash
cd fast-api-notes
```

## 2. Backend Setup (Terminal 1)

```bash
# Install Python dependencies
pip install -r requirements.txt

# Create PostgreSQL database
createdb notesdb

# Initialize database tables
python -m backend.app.init_db

# Start backend server
uvicorn backend.app.main:app --reload
```

✅ Backend running at: `http://localhost:8000`
📚 API docs at: `http://localhost:8000/docs`

## 3. Frontend Setup (Terminal 2)

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

✅ Frontend running at: `http://localhost:5173`

## 4. Test It Out!

Open `http://localhost:5173` in your browser and:

1. Create a new note using the form
2. See your note appear in the grid
3. Delete a note using the 🗑️ icon

## Troubleshooting

### Backend won't start?

**Error: `database "notesdb" does not exist`**
```bash
createdb notesdb
```

**Error: `relation "notes" does not exist`**
```bash
python -m backend.app.init_db
```

**Error: Port 8000 already in use**
```bash
# Find and kill the process
lsof -ti:8000 | xargs kill -9

# Or use a different port
uvicorn backend.app.main:app --reload --port 8001
```

### Frontend won't start?

**Error: `Cannot find module`**
```bash
cd frontend
npm install
```

**Error: Port 5173 already in use**
```bash
# The dev server will automatically try the next available port (5174, 5175, etc.)
```

### Database connection issues?

**Create `.env` file in project root:**
```
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/notesdb
```

## Next Steps

- 📖 Read the [README.md](README.md) for detailed documentation
- 🔍 Explore the API at `http://localhost:8000/docs`
- 🎨 Customize the frontend in `frontend/src/App.svelte`
- 🗄️ Check database: `psql notesdb` → `SELECT * FROM notes;`

## Development Tips

### Hot Reload

Both backend and frontend support hot reload:
- Edit Python files → Backend reloads automatically
- Edit Svelte files → Frontend updates instantly

### API Testing

Use the Swagger UI at `http://localhost:8000/docs` to test API endpoints directly in your browser.

### Database Inspection

```bash
# Connect to database
psql notesdb

# View all notes
SELECT * FROM notes;

# Count notes
SELECT COUNT(*) FROM notes;

# Exit
\q
```

### Reset Database

```bash
# Drop and recreate database
dropdb notesdb
createdb notesdb
python -m backend.app.init_db
```

---

Happy coding! 🚀
