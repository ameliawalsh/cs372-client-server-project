# client-server project
# sources: https://realpython.com/python-sockets/
# https://pythonexamples.org/python-read-string-from-console/

import socket

HOST = '127.0.0.1' #localhost
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        message = input(f'Enter a message to send. Type /q to quit. \n')
        if message == '/q':
            s.sendall(str.encode(message))
            break

        s.sendall(str.encode(message))

        data = s.recv(1024)
        if data.decode() == '/q':
            break
        print(f'>> {data.decode()}')
        