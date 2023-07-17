import socket
import threading

HOST = '16.171.162.94'  # Replace with the server's public IP address or domain name
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        data = client_socket.recv(1024).decode()
        print('Received message:', data)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input('Enter message (or "exit" to quit): ')

    if message == 'exit':
        break

    client_socket.sendall(message.encode())

client_socket.close()
