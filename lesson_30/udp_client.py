import socket

HOST = '127.0.0.1'
PORT = 65431
MESSAGE = 'Hello from client'
SIZE = 1024
attempts = 1

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while attempts <= 10:
        s.sendto(str.encode(str(attempts) + ' ' + MESSAGE), (HOST, PORT))
        msg_from_server = s.recvfrom(SIZE)
        msg = f"message from server {msg_from_server[0]}"
        print(f'Received {attempts} {msg}')
        attempts += 1
