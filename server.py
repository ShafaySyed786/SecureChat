import socket
import requests
import threading

def start_server():
    server_port = 8000  # Server port

    server_address = ('', server_port)

    # Create UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(server_address)

    print('Server is listening...')

    nat_type, external_ip, external_port = get_public_ip_info()

    print('NAT Type:', nat_type)
    print('Public IP:', external_ip)
    print('Public Port:', external_port)

    peers = {}  # Dictionary to store peer information (IP:Port)

    while True:
        data, address = s.recvfrom(1024)  # Receive data from a client.

        if data == b'Hello':
            # Get the peer's IP and port
            peer_ip, peer_port = address

            # Add the peer information to the dictionary
            peers[peer_ip] = peer_port

            # Send the peer information back to the client
            s.sendto(f'{peer_ip},{peer_port}'.encode(), address)
        elif data == b'Connected':
            # Get the peer's IP and port
            peer_ip, peer_port = address

            # Find the peer's address based on the stored information
            for ip, port in peers.items():
                if ip != peer_ip:
                    peer_address = (ip, port)
                    break

            # Start a new thread for communication with the peer
            communication_thread = threading.Thread(target=handle_communication, args=(s, peer_address, address))
            communication_thread.start()

def get_public_ip_info():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        external_ip = data['ip']
        nat_type = 'N/A'
        external_port = 'N/A'
    except:
        nat_type = 'Unknown'
        external_ip = 'Unknown'
        external_port = 'Unknown'

    return nat_type, external_ip, external_port

def handle_communication(s, peer_address, client_address):
    while True:
        data, _ = s.recvfrom(1024)  # Receive data from a peer.

        if not data:
            break

        # Send the data to the other peer
        s.sendto(data, peer_address)

    # Remove the peer's information from the dictionary
    peers.pop(client_address[0], None)

if __name__ == '__main__':
    start_server()
