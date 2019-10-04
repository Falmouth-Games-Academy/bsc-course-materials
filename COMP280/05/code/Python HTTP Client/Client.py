import http
import json

conn = http.client.HTTPConnection("localhost")
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}

quitApp = False

while quitApp is False:

    print('\n')
    print('HTTP Client testbed')
    print('1..GET current DB')
    print('2..POST to DB')
    print('X..Quit')
    print('\n')

    key = input('>')

    if key is '1':
        conn.request("GET", "/index.html")
        r1 = conn.getresponse()

        data1 = r1.read()

        new_data = json.loads(data1)

        for entry in new_data:
            print(entry['name'] + ' ' + str(entry['score']) )

    if key is '2':
        name = input('name')
        score = input('score')

        data_to_send = {"name": name, "score": int(score, 10) }

        json_data_to_send = json.dumps(data_to_send)

        conn.request("POST", "add_score", json_data_to_send, headers)
        response = conn.getresponse()
        data = response.read()

    if key is 'x':
        quitApp = True




conn.close()