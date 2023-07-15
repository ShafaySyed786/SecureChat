import socket

def start_server():
    port = 8000  # Server port

    s = socket.socket()  # Create a socket object
    s.bind(('', port))  # Bind to the port

    s.listen(1)  # Wait for the client connection.
    print('Server is listening...')

    conn, addr = s.accept()  # Establish a connection with the client.
    print('Got connection from', addr)

    while True:
        data = conn.recv(1024).decode()  # Receive data from the client.
        if not data:
            break
        print('Received from client: ' + data)

        data = input(' -> ')
        conn.send(data.encode())  # Send data to the client.

    conn.close()  # Close the connection

if __name__ == '__main__':
    start_server()
