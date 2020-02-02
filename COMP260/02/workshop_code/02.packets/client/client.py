import socket
import time

if __name__ == '__main__':
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    mySocket.connect(("127.0.0.1", 8222))

    index = 0
    while True:
        tmp = 'sending ... ' + str(index)
        data = tmp.encode()

        mySocket.send (len(data).to_bytes(2,byteorder='big'))
        mySocket.send(data)

        #time.sleep(1)
        index += 1



