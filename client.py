import socket
import threading
import stun

def start_client():
    server_ip = input("Enter the server IP: ")  # Get the server IP
    server_port = 8000  # Server port

    local_port = 9000  # Local port for UDP socket

    server_address = (server_ip, server_port)
    local_address = ('', local_port)

    # Create UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(local_address)

    print('NAT Type:', stun.get_nat_type(socket=s))
    print('Public IP:', stun.get_ip_info(socket=s)[0])

    # Send a message to the server to get the peer information
    s.sendto(b'Hello', server_address)

    # Receive the peer information from the server
    peer_data, _ = s.recvfrom(1024)
    peer_ip, peer_port = peer_data.decode().split(',')

    # Start a new thread for receiving messages from the peer
    receive_thread = threading.Thread(target=receive_messages, args=(s,))
    receive_thread.start()

    # Connect to the peer
    peer_address = (peer_ip, int(peer_port))
    s.sendto(b'Connected', peer_address)
    print('Connected to peer:', peer_ip, peer_port)

    while True:
        message = input(' -> ')
        s.sendto(message.encode(), peer_address)  # Send message to the peer.

    s.close()  # Close the socket

def receive_messages(s):
    while True:
        data, _ = s.recvfrom(1024)  # Receive data from the peer.
        if not data:
            break
        print('Received from peer:', data.decode())

if __name__ == '__main__':
    start_client()
