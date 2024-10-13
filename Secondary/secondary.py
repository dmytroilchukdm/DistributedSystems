from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sys
import time

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    messageList = []
    def do_GET(self, content_length=None):
        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.end_headers()
        json_data = json.dumps(self.messageList)
        print("list to send from secondary", self.messageList)
        print("list to send from secondary",json_data)
        self.wfile.write(bytes(json_data, "utf-8"))
        self.wfile.write(bytes("\n", "utf-8"))


    def do_POST(self):
        time.sleep(3)
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.messageList.append(post_data.decode("utf-8"))
        print("The message list",self.messageList)
        response = f"Data received: {post_data.decode()}"
        print(response)
        #self.wfile.write(response.encode())
        #self.wfile.write(repr(self.messageList).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=9001):
    server_address = ('', port)
    secondary = server_class(server_address, handler_class)
    print(f"Initiating secondary on port {port}")
    secondary.serve_forever()

if __name__ == "__main__":
    import sys
    run(port=int(sys.argv[1]))




