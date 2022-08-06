
# sources: https://realpython.com/python-sockets/



import socket

HOST = '127.0.0.1'  #localhost
PORT = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.getsockname()[1]
    s.listen
    print(f'server listening on localhost on port: {PORT}')
    connection, address = s.accept()

    with connection:
        print(f'connected by : {address}')
        while True:
            data = connection.recv(1024)
            print(f'data received (server): {data}')
            if data == '/q':
                break
            connection.sendall(data)