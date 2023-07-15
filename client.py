import socket

def start_client():
    host = input("Enter the server IP: ")  # Get the server IP
    port = 8000  # Server port

    s = socket.socket()  # Create a socket object
    s.connect((host, port))  # Connect to the server

    while True:
        data = input(' -> ')
        s.send(data.encode())  # Send data to the server.

        data = s.recv(1024).decode()  # Receive data from the server.
        if not data:
            break
        print('Received from server:', data)

    s.close()  # Close the connection

if __name__ == '__main__':
    start_client()
