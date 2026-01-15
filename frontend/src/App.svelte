<script>
  import { onMount } from 'svelte';
  
  let notes = [];
  let title = '';
  let content = '';
  let loading = false;
  let error = '';

  // API base URL
  const API_URL = '/api/notes/';

  // Fetch all notes
  async function fetchNotes() {
    loading = true;
    error = '';
    try {
      const response = await fetch(API_URL);
      if (!response.ok) throw new Error('Failed to fetch notes');
      const fetchedNotes = await response.json();
      // Sort notes by created_at in descending order (latest first)
      notes = fetchedNotes.sort((a, b) => 
        new Date(b.created_at) - new Date(a.created_at)
      );
    } catch (err) {
      error = err.message;
    } finally {
      loading = false;
    }
  }

  // Create a new note
  async function createNote() {
    if (!title.trim() || !content.trim()) {
      error = 'Title and content are required';
      return;
    }

    loading = true;
    error = '';
    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title, content }),
      });

      if (!response.ok) throw new Error('Failed to create note');
      
      const newNote = await response.json();
      // Add new note at the beginning (it's the latest)
      notes = [newNote, ...notes];
      title = '';
      content = '';
    } catch (err) {
      error = err.message;
    } finally {
      loading = false;
    }
  }

  // Delete a note
  async function deleteNote(id) {
    loading = true;
    error = '';
    try {
      const response = await fetch(`${API_URL}/${id}`, {
        method: 'DELETE',
      });

      if (!response.ok) throw new Error('Failed to delete note');
      
      notes = notes.filter(note => note.id !== id);
    } catch (err) {
      error = err.message;
    } finally {
      loading = false;
    }
  }

  onMount(() => {
    fetchNotes();
  });
</script>

<main>
  <div class="container">
    <h1>📝 Notes App</h1>
    
    <!-- Error Message -->
    {#if error}
      <div class="error">
        {error}
      </div>
    {/if}

    <!-- Create Note Form -->
    <div class="form-card">
      <h2>Create New Note</h2>
      <form on:submit|preventDefault={createNote}>
        <input
          type="text"
          placeholder="Note title..."
          bind:value={title}
          disabled={loading}
        />
        <textarea
          placeholder="Note content..."
          bind:value={content}
          rows="4"
          disabled={loading}
        ></textarea>
        <button type="submit" disabled={loading}>
          {loading ? 'Creating...' : 'Create Note'}
        </button>
      </form>
    </div>

    <!-- Notes List -->
    <div class="notes-section">
      <h2>Your Notes ({notes.length})</h2>
      
      {#if loading && notes.length === 0}
        <p class="loading">Loading notes...</p>
      {:else if notes.length === 0}
        <p class="empty">No notes yet. Create your first note above!</p>
      {:else}
        <div class="notes-grid">
          {#each notes as note (note.id)}
            <div class="note-card">
              <div class="note-header">
                <h3>{note.title}</h3>
                <button
                  class="delete-btn"
                  on:click={() => deleteNote(note.id)}
                  disabled={loading}
                  title="Delete note"
                >
                  🗑️
                </button>
              </div>
              <p>{note.content}</p>
              <div class="note-footer">
                <small>Created: {new Date(note.created_at).toLocaleDateString()}</small>
              </div>
            </div>
          {/each}
        </div>
      {/if}
    </div>
  </div>
</main>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    background: #f5f5f5;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
  }

  h1 {
    color: #333;
    text-align: center;
    margin-bottom: 2rem;
  }

  h2 {
    color: #555;
    margin-bottom: 1rem;
  }

  .error {
    background: #fee;
    color: #c33;
    padding: 1rem;
    border-radius: 8px;
    margin-bottom: 1rem;
  }

  .form-card {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 2rem;
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  input,
  textarea {
    padding: 0.75rem;
    border: 2px solid #ddd;
    border-radius: 8px;
    font-size: 1rem;
    font-family: inherit;
    transition: border-color 0.2s;
  }

  input:focus,
  textarea:focus {
    outline: none;
    border-color: #4a90e2;
  }

  button {
    padding: 0.75rem 1.5rem;
    background: #4a90e2;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
  }

  button:hover:not(:disabled) {
    background: #357abd;
  }

  button:disabled {
    background: #ccc;
    cursor: not-allowed;
  }

  .notes-section {
    margin-top: 2rem;
  }

  .loading,
  .empty {
    text-align: center;
    color: #999;
    padding: 2rem;
  }

  .notes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
  }

  .note-card {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s, box-shadow 0.2s;
  }

  .note-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
  }

  .note-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 0.75rem;
  }

  .note-header h3 {
    margin: 0;
    color: #333;
    font-size: 1.25rem;
  }

  .delete-btn {
    padding: 0.25rem 0.5rem;
    background: transparent;
    font-size: 1.25rem;
    cursor: pointer;
    transition: transform 0.2s;
  }

  .delete-btn:hover:not(:disabled) {
    transform: scale(1.2);
    background: transparent;
  }

  .note-card p {
    color: #666;
    line-height: 1.6;
    margin: 0 0 1rem 0;
  }

  .note-footer {
    border-top: 1px solid #eee;
    padding-top: 0.75rem;
  }

  .note-footer small {
    color: #999;
  }
</style>
