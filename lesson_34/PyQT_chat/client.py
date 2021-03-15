import json
import socket

HOST = '127.0.0.1'
PORT = 65001
message = {"login": input('Enter login:'), "password": input('Enter password:')}
msg = json.dumps(message)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(msg.encode())
    data = s.recv(1024).decode()

print('Received', data)


class Client:

    def __init__(self):
        pass