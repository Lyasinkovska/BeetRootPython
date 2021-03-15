import argparse
import asyncio

HOST = '127.0.0.1'


def get_port():
    parser = argparse.ArgumentParser(description='Query a port.')
    parser.add_argument('-p', type=int, help='port', default=8888)
    args = vars(parser.parse_args())
    return args['p']


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f"Received {message} from {addr}")
    data_to_send = message.upper()
    print(f"Send: {data_to_send}")
    writer.write(data_to_send.encode())
    await writer.drain()

    print("Close the client socket")
    writer.close()


if __name__ == '__main__':
    port = get_port()
    loop = asyncio.get_event_loop()
    coroutine = asyncio.start_server(handle_echo, host=HOST, port=port, loop=loop)
    server = loop.run_until_complete(coroutine)

    print(f'Serving on {server.sockets[0].getsockname()}')
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
