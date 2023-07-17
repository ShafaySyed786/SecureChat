import socketio

sio = socketio.Client()

@sio.on('message')
def handle_message(message):
    print('Received message:', message)

def send_message(message):
    sio.emit('message', message)

if __name__ == '__main__':
    sio.connect('http://172.28.231.231:5000')

    while True:
        message = input('Enter message (or "exit" to quit): ')
        if message == 'exit':
            break
        send_message(message)

    sio.disconnect()
