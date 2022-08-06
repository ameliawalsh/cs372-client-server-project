# client-server project (server)
# Date: 8/6/2022

# Citation of Sources:
# https://realpython.com/python-sockets/
# https://pythonexamples.org/python-read-string-from-console/

import socket

HOST = "127.0.0.1"  #localhost
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Server listening on localhost on port ({PORT})')
    connection, address = s.accept()
    
    with connection:
        print(f'Connected by {address}')
        print(f'Waiting for message...')
        while True:
            data = connection.recv(1024)
            if data.decode() == '/q': # if client send a /q signal, break the connection loop
                break

            print(f'>> {data.decode()}')
            message = input(f'Enter a message to send.\n') # prompt for the server to enter response to client
            if message == '/q': # if server quits, sent /q signal to client and close
                connection.sendall(str.encode(message))
                break

            connection.sendall(str.encode(message))

    s.close()

 