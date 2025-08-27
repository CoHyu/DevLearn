import asyncio

clients = set()  # 保存所有连接的客户端

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"[+] 新客户端连接：{addr}")
    clients.add(writer)

    try:
        while True:
            data = await reader.readline()
            if not data:
                break
            message = data.decode().strip()
            print(f"[{addr}] {message}")

            # 广播给其他客户端
            for client in clients:
                if client != writer:
                    client.write(f"[{addr}] {message}\n".encode())
                    await client.drain()
    except ConnectionResetError:
        pass
    finally:
        print(f"[-] 客户端断开：{addr}")
        clients.remove(writer)
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    print("服务器启动，监听 8888 端口")
    async with server:
        await server.serve_forever()

asyncio.run(main())