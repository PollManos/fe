rom http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello depuis mon conteneur Docker !")

server = HTTPServer(("0.0.0.0", 5000), Handler)

print("Serveur demarre sur le port 5000")
server.serve_forever()

