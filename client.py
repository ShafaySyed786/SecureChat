import socket
import threading
import stun

def start_client():
    host = input("Enter the server IP: ")  # Enter the server's IP address
    port = 8000  # Server port

    s = socket.socket()  # Create a socket object
    s.connect((host, port))  # Connect to the server

    nat_type, external_ip, external_port = stun.get_ip_info()

    print('NAT Type:', nat_type)
    print('Public IP:', external_ip)
    print('Public Port:', external_port)

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
