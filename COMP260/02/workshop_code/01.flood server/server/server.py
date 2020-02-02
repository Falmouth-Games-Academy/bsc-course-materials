import socket
import time

if __name__ == '__main__':
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    mySocket.bind(("127.0.0.1",8222))
    mySocket.listen(5)

    client = mySocket.accept()[0]

    while True:
        data = client.recv(4096)
        print(data.decode('utf-8') +'\n')
        time.sleep(0.5)


        