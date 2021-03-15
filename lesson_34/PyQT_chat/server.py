import json
import multiprocessing
import socket
from json.decoder import JSONDecodeError

SERVER_ADDR = ('localhost', 65001)
authorised_clients = {}
current_clients = {}
names = {}


def create_socket(server_address=SERVER_ADDR, clients_quantity=5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)
    sock.listen(clients_quantity)
    return sock


def create_connection(server_address):
    server_sock = create_socket(server_address)
    while True:

        print('waiting for a connection')
        client_sock, client_address = server_sock.accept()
        # process = multiprocessing.Process(target=server_sock)
        current_clients[client_address] = client_sock

        try:
            # print('connection from', client_address)

            while True:
                data = client_sock.recv(1024).decode()
                try:
                    received_dict = json.loads(data)
                except JSONDecodeError:
                    pass
                else:
                    msg, key = received_dict.get("login"), received_dict.get("password")
                    if data:
                        client_sock.sendall(msg.encode())
                    else:
                        print('no data from', client_address)
                        break

        finally:
            client_sock.close()


def get_request():
    pass


if __name__ == '__main__':
    create_connection(SERVER_ADDR)
