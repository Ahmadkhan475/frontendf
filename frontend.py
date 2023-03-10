# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from datetime import datetime

hostName = "127.0.0.1"
serverPort = 8081

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        x = requests.get('http://127.0.0.1:8080')
        current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M ")
        self.wfile.write(bytes(current_datetime + x.text, "utf-8"))

webServer = HTTPServer((hostName, serverPort), MyServer)
print("Server started http://%s:%s" % (hostName, serverPort))

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()