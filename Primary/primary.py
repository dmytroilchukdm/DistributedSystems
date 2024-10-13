from http.client import responses
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json


class PrimaryHTTPRequestHandler(BaseHTTPRequestHandler):
    messageList = ["Primary Initial"]
    def do_GET(self,content_length = None):
        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.end_headers()
        json_data = json.dumps(self.messageList)
        print("list to send from server", self.messageList)
        print("list to send from server",json_data)
        self.wfile.write(bytes(json_data, "utf-8"))
        self.wfile.write(bytes("\n", "utf-8"))
#        self.wfile.write(repr(self.messageList).encode())


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.messageList.append(post_data.decode("utf-8"))
        print("The message list",self.messageList)
        requests.post('http://secondary1:9001', data=post_data)
        requests.post('http://secondary2:9002', data=post_data)
        response = f"Data received: {post_data.decode()}"
        print(response)
        #self.wfile.write(response.encode())
        #self.wfile.write(repr(self.messageList).encode())

def run(server_class=HTTPServer, handler_class=PrimaryHTTPRequestHandler, port=9000):
    server_address = ('', port)
    primary = server_class(server_address, handler_class)
    print(f"Initiating primary on port {port}")
    primary.serve_forever()


if __name__ == "__main__":
    run()
