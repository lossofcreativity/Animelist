#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class SPAHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # If path exists as a file, serve it
        if os.path.exists(self.path[1:]) and not self.path[1:] == '':
            super().do_GET()
        else:
            # Otherwise serve index.html
            self.path = 'index.html'
            super().do_GET()

if __name__ == '__main__':
    port = 3000
    print(f"Serving SPA at http://localhost:{port}")
    print("Press Ctrl+C to stop")
    HTTPServer(("", port), SPAHandler).serve_forever()