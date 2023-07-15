def start_client():
    host = '<IP_OF_SERVER>'  # replace <IP_OF_SERVER> with the server machine's IP
    port = 8000  # Server port

    s = socket.socket()  # Create a socket object
    s.connect((host, port))  # Bind to the port

    while True:
        data = input(' -> ')
        s.send(data.encode())  # Send data to the server.

        data = s.recv(1024).decode()  # Receive data from the server.
        if not data:
            break
        print('Received from server: ' + data)

    s.close()  # Close the connection

if __name__ == '__main__':
    start_client()
