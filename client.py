import socket
import threading

HOST = '16.171.162.94'  # Replace with the server's public IP address or domain name

# Prompt the user for the port number
while True:
    port = input('Enter the port number (between 2500 and 5000): ')
    try:
        port = int(port)
        if 2500 <= port <= 5000:
            break
        else:
            print('Invalid port number. Please enter a value between 2500 and 5000.')
    except ValueError:
        print('Invalid port number. Please enter a valid integer value.')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, port))

def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(data)
        except:
            break

threading.Thread(target=receive_messages).start()

# Get the client's name
name = input('Enter your name: ')

while True:
    message = input()
    if message == 'exit':
        client_socket.sendall('exit'.encode())
        break
    client_socket.sendall(f'{name}: {message}'.encode())
