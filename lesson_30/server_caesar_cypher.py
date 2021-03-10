import json
import socket
from json.decoder import JSONDecodeError

from caesar_cypher import encrypt_caesar

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 65000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(1024)
            try:
                received_dict = json.loads(data)
            except JSONDecodeError:
                pass
            msg, key = received_dict.get("msg"), received_dict.get("key")
            msg_to_send = encrypt_caesar(msg, key)
            if data:
                print('sending data back to the client')
                connection.sendall(msg_to_send.encode())
            else:
                print('no data from', client_address)
                break

    finally:
        connection.close()
