from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sqlite3
import json
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
hostPort = 8000
#https://www.pythoncentral.io/introduction-to-sqlite-in-python/
#https://docs.python.org/2/library/sqlite3.html
#https://pythonexamples.org/python-sqlite3-tutorial/

#if you want to create a temporary memory-based database:
#conn = sqlite3.connect(':memory:')

#if you want to make a persisent file-based database, or open an existing one
conn = sqlite3.connect('db.sqlite')

c = conn.cursor()

#does the table already exist in the database, i.e. has it been created before?
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='highscores' ''')

#if the count is 1, then table exists
if c.fetchone()[0] == 1:
	print('Table exists.')
else:
	print('Creating high-score table')
	c.execute("create table highscores (name varchar(20), score int)")


#see how many highscores are currently in the table
#select all the rows from the highscores table
c.execute('select * from highscores ')
rows = c.fetchall()

#if it's 0, add some to start things off
if(len(rows) == 0):
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

		result = urlparse(self.path)

		if 'get_all_records' in result.path:
			list = []
			for row in c.execute("select * from highscores order by score desc"):
				entry = {}
				entry['name'] = row[0]
				entry['score'] = row[1]

				list.append(entry)

			#annoyingly, the stupid json parser in Unreal can't parse annoynmous containers
			#so we need to put the list into a tuple and give it a name. The Unreal and Unity
			#parsers will have objects of List<entry> or TArray<entry> to reflect the data.

			result = json.dumps({"details": list})
			self.wfile.write(result.encode())

			new_data = json.loads(result);

			print("GET RESPONSE ", result)

		if 'get_named_records' in result.path:
			args = parse_qs(result.query)

			list = []
			for row in c.execute("select * from highscores where name=? order by score desc", (args['name'][0],)):
				entry = {}
				entry['name'] = row[0]
				entry['score'] = row[1]

				list.append(entry)

			# annoyingly, the stupid json parser in Unreal can't parse annoynmous containers
			# so we need to put the list into a tuple and give it a name. The Unreal and Unity
			# parsers will have objects of List<entry> or TArray<entry> to reflect the data.

			result = json.dumps({"details": list})
			self.wfile.write(result.encode())

			new_data = json.loads(result);

			print("GET RESPONSE ", result)

	def do_POST(self):

		print( "POST")
		content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
		post_data = self.rfile.read(content_length)  # <--- Gets the data itself
		self.send_response(200)
		self.end_headers()

		print( "POST: ", post_data)
		print(json.loads(post_data))

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