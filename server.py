import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('Server listening on {}:{}'.format(HOST, PORT))

client_sockets = []

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()

            if not data:
                break

            # Treat 'exit' as a special message indicating that the client wants to disconnect
            if data == 'exit':
                print('Client wants to disconnect')
                disconnect_msg = "A client has disconnected"
                notify_all_clients(disconnect_msg, client_socket)
                break

            print('Received message:', data)

            # Send the message to all connected clients except the sender
            for socket in client_sockets:
                if socket != client_socket:
                    socket.sendall(data.encode())
        except:
            # If an exception occurs, it could mean the client has abruptly disconnected
            print('Client has disconnected')
            disconnect_msg = "A client has abruptly disconnected"
            notify_all_clients(disconnect_msg, client_socket)
            break

    # Remove the client socket from the list
    client_sockets.remove(client_socket)
    client_socket.close()

def notify_all_clients(msg, sender_socket):
    """Helper function to notify all clients about some event."""
    for socket in client_sockets:
        if socket != sender_socket:
            socket.sendall(msg.encode())

while True:
    client_socket, client_address = server_socket.accept()
    print('Connected to client:', client_address)

    client_sockets.append(client_socket)

    # Start a new thread to handle the client's messages
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
