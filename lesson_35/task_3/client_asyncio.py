import asyncio

from server_asyncio import get_port

HOST = '127.0.0.1'


async def tcp_client(message, loop, port, host=HOST):
    reader, writer = await asyncio.open_connection(host, port,
                                                   loop=loop)
    writer.write(message.encode())

    data = await reader.read(1024)
    print(f'Received message {data.decode()}')
    writer.close()


def run_client(message, port):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tcp_client(message, loop, port))
    loop.close()


if __name__ == '__main__':
    port = get_port()

    message = input("Enter a message:")
    run_client(message, port)
