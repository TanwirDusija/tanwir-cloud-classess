from http.server import BaseHTTPRequestHandler, HTTPServer

class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
            <head><title>Docker Lab</title></head>
            <body>
                <h1>Hello from Tanwir's Docker Project!</h1>
                <p>My first web application is running inside a Docker container.</p>
            </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))

server = HTTPServer(("0.0.0.0", 8000), WebHandler)
print("Web server is running on port 8000")
server.serve_forever()
