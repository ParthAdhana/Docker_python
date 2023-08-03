from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 3000

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'hello')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')

if __name__ == '__main__':
    try:
        server = HTTPServer(('', PORT), SimpleHandler)
        print(f'Server listening on port {PORT}')
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')
