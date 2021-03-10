import json
import socket

HOST = '127.0.0.1'
PORT = 65000
KEY = -6
message = {"msg": "Hello server", "key": 5}
msg = json.dumps(message)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(msg.encode())
    data = s.recv(1024).decode()

print('Received', data)
