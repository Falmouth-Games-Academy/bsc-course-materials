from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sqlite3
import json

hostName = "localhost"
hostPort = 8000
#https://www.pythoncentral.io/introduction-to-sqlite-in-python/
#https://docs.python.org/2/library/sqlite3.html
#https://stackoverflow.com/questions/10175812/how-to-create-a-self-signed-certificate-with-openssl
conn = sqlite3.connect(':memory:')

c = conn.cursor()
c.execute("create table highscores (name varchar(20), score int)")

c.execute("insert into highscores (name, score) values ('Me', 3000)");
c.execute("insert into highscores (name, score) values ('Me', 2000)");
c.execute("insert into highscores (name, score) values ('Me', 1000)");

c.execute("insert into highscores (name, score) values ('You', 3000)");
c.execute("insert into highscores (name, score) values ('You', 2000)");
c.execute("insert into highscores (name, score) values ('You', 1000)");
conn.commit()

class MyServer(BaseHTTPRequestHandler):

	def do_GET(self):
		print("DO GET");
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()

		list = []
		for row in c.execute("select * from highscores order by score desc"):
			entry = {}
			entry['name'] = row[0]
			entry['score'] = row[1]

			list.append(entry)

		#dict = {"scores" : list}
		#result = json.dumps(dict)
		result = json.dumps(list)
		self.wfile.write(result.encode())

		new_data = json.loads(result);

		print("GET RESPONSE ", result)

	def do_POST(self):
		content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
		post_data = self.rfile.read(content_length)  # <--- Gets the data itself
		self.send_response(200)
		self.end_headers()

		print( "POST: ", post_data)

		command = json.loads(post_data)
		c.execute('insert into highscores(name, score) values(?,?)', (command['name'], command['score'] ))
		conn.commit()






myServer = HTTPServer((hostName, hostPort), MyServer)

print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))