import http
import json
from urllib.parse import urlparse, urlencode


conn = http.client.HTTPConnection("localhost",8000)
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}

quitApp = False

while quitApp is False:

    print('\n')
    print('HTTP Client testbed')
    print('1..GET current DB')
    print('2..POST to DB')
    print('3..GET specific record')
    print('X..Quit')
    print('\n')

    key = input('>')

    if key is '1':
        conn.request("GET", "/get_all_records")
        r1 = conn.getresponse()

        data1 = r1.read()

        new_data = json.loads(data1)

        for entry in new_data['details']:
            print(entry['name'] + ' ' + str(entry['score']) )

    if key is '2':
        name = input('name')
        score = input('score')

        data_to_send = {"name": name, "score": int(score, 10) }

        json_data_to_send = json.dumps(data_to_send)

        conn.request("POST", "add_score", json_data_to_send, headers)
        response = conn.getresponse()
        data = response.read()

    if key is '3':

        name = input('Name:')

        #encode user data using urlencode.
        #put user data into a dictionary of <label><value> and encode with urlencode to address
        #spaces and other issues
        values = {'name': name}
        url = '/get_named_records'
        conn.request("GET", "/get_named_records?" + urlencode(values))
        r1 = conn.getresponse()

        #server will return package of records that match name
        #if there are none, details will be 0 length
        data1 = r1.read()

        new_data = json.loads(data1)

        if len(new_data['details']) > 0:
            for entry in new_data['details']:
                print(entry['name'] + ' ' + str(entry['score']))
        else:
            print('No entries found!')

    if key is 'x':
        quitApp = True




conn.close()