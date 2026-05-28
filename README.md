**Anime & Manga Discovery Platform**  
*Author: Avaya Shrestha | Deployed: May 28, 2026 | GitHub: [@lossofcreativity](https://github.com/lossofcreativity)* |

**DEPLOYED AT**:  `Netlify`

WEBSITE: [ANILISTS](https://myanilists.netlify.app)

---

Animeflow is a sleek, single-page application (SPA) designed to help users discover, search, and track their favorite anime and manga. Powered by the AniList GraphQL API, it features modern UI elements like glassmorphism effects, 3D interactive components, and fully client-side routing.

## ✨ Features

- **🎬 Dual Search:** Separate, dedicated tabs for Anime and Manga.
- **🔖 Favorites System:** Save your top picks directly to \`localStorage\` (no backend needed).
- **🌓 Persistent Dark/Light Theme:** Matches your preference and stays saved across sessions.
- **👨‍🎨 Deep-Dive Creator Pages:** Explore dedicated profiles and works by authors and studios.
- **👥 Interactive Character Modals:** Quick-click overlays showing rich character details.
- **🎭 Advanced Filtering:** Browse content seamlessly using 9+ distinct genres.
- **📜 Infinite Scroll:** Smooth, automated content loading as you browse.
- **💀 Skeleton Loading:** Fluid, polished animations for asynchronous data fetching.
- **🎨 3D Interactive Elements:** Gorgeous gradient hover effects and tactile buttons.
- **🔗 Clean URLs:** Native history API routing without ugly hash (\`#\`) fragments.

---

## 🚀 Quick Start

1. Save \`index.html\` in your project folder.
2. Save \`server.py\` in the same folder.
3. Fire up the local routing server:
   \`\`\`bash
   python3 server.py
   \`\`\`
4. Open your browser and navigate to: **\`http://localhost:3000`**

---

## 🖥️ Server Script (\`server.py\`)

\`\`\`python
```#!/usr/bin/env python3
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

class SPAHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve the file directly if it exists, otherwise fallback to index.html for SPA routing
        if os.path.exists(self.path[1:]) and not self.path[1:] == '':
            super().do_GET()
        else:
            self.path = 'index.html'
            super().do_GET()

if __name__ == '__main__':
    port = 3000
    print(f"🚀 Serving SPA at http://localhost:{port}")
    print("Press Ctrl+C to stop")
    try:
        HTTPServer(("", port), SPAHandler).serve_forever()
    except KeyboardInterrupt:
        print("\\nServer stopped.")
```
\`\`\`

---

## 📁 Project Structure

```
animeflow/
├── index.html
├── server.py
└── README.md
```

---

## 📖 Usage Guide

### Navigation Breakdown

| Page | Description |
| :--- | :--- |
| **Home** | Trending anime spotlight (optimized without infinite scroll) |
| **Anime** | Comprehensive browse directory + Genre filters + Infinite scroll |
| **Manga** | Comprehensive manga directory + Genre filters + Infinite scroll |
| **Authors** | Profiles of popular industry creators |
| **Favorites** | Your curated collection, saved locally |
| **Search** | Universal search bar accessible from the top right |

### Rich Interactions (Detail Pages)
- **Click Genres** → Instantly discover similar content.
- **Click Studios/Authors** → Open dedicated work portfolios.
- **Click Characters** → Trigger a detailed bio modal overlay.
- **Click Heart Icon** → Toggle item in your local Favorites list.

---

## 🌐 API Integration

Animeflow is entirely client-driven, communicating directly with the official **AniList GraphQL API**.

> ⚠️ **Rate Limit Note:** The AniList API enforces a limit of **90 requests per minute**. If elements stop loading temporarily, you may have hit this threshold.

---

## 🔧 Troubleshooting

| Issue | Root Cause | Solution |
| :--- | :--- | :--- |
| **Favorites not saving** | Browser storage blocked | Ensure \`localStorage\` is enabled in browser privacy settings. |
| **404 error on page reload** | Missing SPA fallback | Do not use basic HTTP servers. Ensure you are running \`server.py\`. |
| **Images failing to load** | Network drop / API lag | Refresh the page or check your internet connection. |
| **Dark mode resets** | Stale browser cache | Clear your browser cache or site data and try again. |

---

## 🌐 Browser Support

- Chrome 90+ ✅
- Firefox 88+ ✅
- Safari 14+ ✅
- Edge 90+ ✅

---

## 🛠️ Customization

- **Change Color Palette:** Update the CSS \`:root\` design tokens inside \`index.html\`.
- **Add New Genres:** Modify the \`categories\` array structure inside the \`animeContainerPage()\` function.
- **Adjust Pagination:** Tweak the \`perPage\` variable inside the API fetch payloads to load more/fewer items at once.

---

## 🤝 Contributing

1. Fork the repository.
2. Create your feature branch: \`git checkout -b feature/AmazingFeature\`
3. Commit your changes: \`git commit -m 'Add some AmazingFeature'\`
4. Push to the branch: \`git push origin feature/AmazingFeature\`
5. Open a **Pull Request**.

💡 **Future Roadmap Ideas:** Multi-user accounts, watchlists/readlists, seasonal release calendars, native mobile wrappers.

---

## 📬 Contact & Credits

- **Author:** Avaya Shrestha
- **GitHub:** [@lossofcreativity](https://github.com/lossofcreativity)
- **Deployment Date:** May 28, 2026

<br />

<div align="center">

**Made with ❤️ by [Avaya Shrestha](https://github.com/lossofcreativity)**

</div>
