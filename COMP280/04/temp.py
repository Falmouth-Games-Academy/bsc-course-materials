
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):

	def do_GET(self):
		print("DO GET:" + self.path);
        #boilerplate HTML code
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()

        #send response back to client
		response_data = "The server has sent you this reply"
		self.wfile.write(response_data.encode())

	def do_POST(self):
		print("DO POST:" + self.path);

        #extract client data
		content_length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(content_length)

        #boilerplate HTML code
		self.send_response(200)
		self.end_headers()

		print( "POST: ", post_data.decode())


hostName = "localhost"
hostPort = 8000

myServer = HTTPServer((hostName, hostPort), MyServer)

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
