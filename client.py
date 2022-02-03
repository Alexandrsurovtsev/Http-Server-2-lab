from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    words = ["1","2","3","4","5"]

    def do_GET(self):                                                #логика get запроса
       
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        print(self.words)
        for i in self.words:
            self.wfile.write(i.encode()+" ".encode())
            
    def do_POST(self):                                               #логика post запроса
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = BytesIO()
        response.write(b'Received: ')
        response.write(body)
        self.words.append(str(body.decode()))
        self.words.pop(0)
        self.wfile.write(response.getvalue()+" Измененный массив: ".encode())
        for i in self.words:
            self.wfile.write(i.encode()+" ".encode())
        print(self.words)

httpd = HTTPServer(('localhost', 5000), SimpleHTTPRequestHandler)
httpd.serve_forever()
