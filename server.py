import socket

HOST = '0.0.0.0'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('Server listening on {}:{}'.format(HOST, PORT))

client_sockets = []

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode()

        if not data:
            break

        print('Received message:', data)

        # Send the message to all connected clients except the sender
        for socket in client_sockets:
            if socket != client_socket:
                socket.sendall(data.encode())

    client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    print('Connected to client:', client_address)

    client_sockets.append(client_socket)

    # Start a new thread to handle the client's messages
    handle_client(client_socket)
