import socket

HOST = '127.0.0.1'
PORT = 65431
SIZE = 1024
MESSAGE = 'Hello from server'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f'starting up on {HOST} port {PORT}')
sock.bind((HOST, PORT))

while True:
    print('waiting for a connection')
    message, client_address = sock.recvfrom(SIZE)
    print('connection from', client_address, message)
    if message:
        sock.sendto(MESSAGE.encode(), client_address)
