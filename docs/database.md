# dependencies

- sqlalchemy - ORM for database operations
- psycopg2-binary - PostgreSQL adapter for Python
- python-dotenv - For managing environment variables (optional but recommended


# db 

create db - notesdb

# schema design 

- notes app
- id, title, notes
- actions: create note, get all notes, get specific note, update a note, delete a note

attributes: 
    id
    title
    note/ content
    created_at


| Method      | Meaning      |
| ----------- | ------------ |
| `.get()`    | Read data    |
| `.post()`   | Create data  |
| `.put()`    | Replace data |
| `.patch()`  | Update data  |
| `.delete()` | Delete data  |
