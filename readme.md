# Animeflow

**Anime & Manga Discovery Platform** | Author: Avaya Shrestha | Deployed: May 28, 2026 | GitHub: lossofcreativity

---

## Features

- 🎬 Dual Search - Anime & Manga separate tabs
- 🔖 Favorites - Save to localStorage
- 🌓 Dark/Light Theme - Persistent
- 👨‍🎨 Author Pages - View creator works
- 👥 Character Modals - Click for details
- 🏢 Studio Pages - Browse by studio
- 🎭 Genre Filtering - 9+ genres
- 📜 Infinite Scroll - Auto-load more
- 💀 Skeleton Loading - Smooth animations
- 🎨 3D Buttons - Gradient hover effects
- 🔗 Clean URLs - No hash fragments

---

## Quick Start

1. Save `index.html` in a folder
2. Save `server.py` in same folder
3. Run: `python3 server.py`
4. Open: `http://localhost:3000`

---

## Server Script (server.py)

#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class SPAHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if os.path.exists(self.path[1:]) and not self.path[1:] == '':
            super().do_GET()
        else:
            self.path = 'index.html'
            super().do_GET()

if __name__ == '__main__':
    port = 3000
    print(f"Serving SPA at http://localhost:{port}")
    print("Press Ctrl+C to stop")
    HTTPServer(("", port), SPAHandler).serve_forever()

# Project Structure
animeflow/
├── index.html
├── server.py
└── README.md


---

## Usage Guide

| Page | Description |
|------|-------------|
| Home | Trending anime (no infinite scroll) |
| Anime | Browse by genre + infinite scroll |
| Manga | Browse manga + infinite scroll |
| Authors | Popular creators |
| Favorites | Saved items |
| Search | Search bar (top right) |

### On Detail Pages

- Click **genres** → similar anime
- Click **studios** → studio works
- Click **authors** → author profile
- Click **characters** → modal with details
- Click **heart** → add to favorites

---

## API

Powered by **AniList GraphQL API**

**Rate Limit:** 90 requests per minute

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Favorites not saving | Check localStorage enabled |
| 404 on reload | Use server.py (not basic HTTP server) |
| Images not loading | Refresh or check connection |
| Dark mode not persisting | Clear browser cache |

---

## Browser Support

Chrome 90+ ✅ | Firefox 88+ ✅ | Safari 14+ ✅ | Edge 90+ ✅

---

## Customization

- **Change colors** - Edit CSS `:root` variables
- **Add genres** - Modify `categories` array in `animeContainerPage()`
- **Change items per page** - Adjust `perPage` parameter in API calls

---

## Contributing

1. Fork repo
2. Create branch (`git checkout -b feature/Amazing`)
3. Commit changes
4. Push to branch
5. Open Pull Request

**Ideas:** User accounts, watchlist, seasonal calendar, mobile app

---

## Contact

**Author:** Avaya Shrestha
**GitHub:** lossofcreativity
**Deployed:** May 28, 2026

---

<div align="center">

**Made with ❤️ by Avaya Shrestha**

</div>