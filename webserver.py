import http.server
import socketserver

PORT = 8000

class CrossOriginWebserver(http.server.SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        super().send_header("Access-Control-Allow-Origin", "*")
        return super().end_headers()

Handler = CrossOriginWebserver

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()