# client-server project (client)
# Date: 8/6/2022

# Citation of Sources:
# https://realpython.com/python-sockets/
# https://pythonexamples.org/python-read-string-from-console/

import socket

HOST = '127.0.0.1' #localhost
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        message = input(f'Enter a message to send. Type /q to quit. \n')  #prompt user to enter a message or quit
        if message == '/q':
            s.sendall(str.encode(message)) #if user quits, send the /q signal to the server
            break

        s.sendall(str.encode(message))

        data = s.recv(1024)
        if data.decode() == '/q': #if the server send a /q signal, break connection loop
            break
        print(f'>> {data.decode()}')

    s.close()