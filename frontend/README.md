# Notes App - Frontend (Svelte)

A modern, responsive frontend for the Notes API built with Svelte and Vite.

## Features

- ✅ Create, read, and delete notes
- 🎨 Clean and modern UI
- ⚡ Fast and reactive with Svelte
- 📱 Responsive design
- 🔄 Real-time updates

## Tech Stack

- **Svelte 4** - Reactive UI framework
- **Vite** - Fast build tool and dev server
- **Vanilla CSS** - Simple and performant styling

## Prerequisites

- Node.js 18+ and npm/yarn
- Backend API running on `http://localhost:8000`

## Installation

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

## Development

Start the development server:

```bash
npm run dev
```

The app will be available at `http://localhost:5173`

## Build

Create a production build:

```bash
npm run build
```

Preview the production build:

```bash
npm run preview
```

## Project Structure

```
frontend/
├── public/              # Static assets
├── src/
│   ├── App.svelte      # Main application component
│   ├── main.js         # Application entry point
│   └── app.css         # Global styles
├── index.html          # HTML template
├── package.json        # Dependencies and scripts
├── vite.config.js      # Vite configuration
└── svelte.config.js    # Svelte configuration
```

## API Integration

The frontend uses a Vite proxy to connect to the FastAPI backend:

- Development: Proxies `/api/*` to `http://localhost:8000`
- All API calls use `/api/notes` as the base URL

## Features to Add

- [ ] Update/Edit notes
- [ ] Search functionality
- [ ] Note categories/tags
- [ ] Dark mode toggle
- [ ] User authentication
- [ ] Note sharing

## License

MIT
