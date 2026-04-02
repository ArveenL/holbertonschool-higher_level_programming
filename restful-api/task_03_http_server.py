#!/usr/bin/python3
"""
1. Create a web server using http.server module
2. Handle different types of HTTP requests e.g GET, POST, etc
3. Serve JSON data in response to specific endpoints 
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
# BaseHTTPRequestHandler = handles GET, POST, etc
# HTTPServer = use behaviors above and pass them to HTTPServer

class MyHandler(BaseHTTPRequestHandler): # MyHandler is now a sub of parent: BaseHTTPRequestHandler
    def do_GET(self):                    # for when web server reveives a GET request, will use do_GET to handle that operation
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

server = HTTPServer(("localhost", 8000), MyHandler)
server.serve_forever()
