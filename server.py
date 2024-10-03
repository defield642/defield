import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 16723)
server_socket.bind(server_address)

server_socket.listen(1)

print("Server is listening......")

while True:

    connection, client_address = server_socket.accept()

    try:
        print("connection from", client_address)

        while True:
            data = connection.recv(1024)
            if data:
                print("Received:", data.decode())
                connection.sendall(data)
            else:
                print("NO MORE DATA FROM ", client_address)
                break
    finally:
        connection.close()