import asyncio

async def read_from_server(reader):
    while True:
        data = await reader.readline()
        if not data:
            break
        print(data.decode().strip())

async def write_to_server(writer):
    while True:
        msg = await asyncio.to_thread(input, "")
        writer.write((msg + "\n").encode())
        await writer.drain()

async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    print("[+] 已连接到服务器")

    # 并发执行读写
    await asyncio.gather(
        read_from_server(reader),
        write_to_server(writer)
    )

asyncio.run(main())
