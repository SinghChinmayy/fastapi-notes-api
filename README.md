# FastAPI Notes App

A simple REST API built with FastAPI for managing notes in memory.

## Features

### Working on 

- api and backend setup 
- db setup

### Implemented:


### Future Additions:

- User auth
- keep track of when the note was edited && file versioning 


# Notes components:

id
title
content
created_at 

## API Endpoints

POST /notes -> create a note
GET /notes -> list all notes
GET /notes/{note_id} -> get a specific note

# database 

Notes:

Column      | Type                         | Default
------------|------------------------------|------------------
id          | integer (auto-increment)     | Primary Key
title       | character varying            | NOT NULL
content     | character varying            | NOT NULL
created_at  | timestamp with time zone     | now()
updated_at  | timestamp with time zone     | 


Credentials: 

name: notesdb
user: notesuser
pass: notes123

```bash
# To initialize the database, run:
python -m backend.app.init_db
```