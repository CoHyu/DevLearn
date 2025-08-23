import asyncio

async def wget(host):
    # TCP establish
    print(f"[+] Connected to {host}")
    reader, writer = await asyncio.open_connection(host, 80)

    # HTTP request
    request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
    writer.write(request.encode("utf-8"))
    await writer.drain()

    # HTTP response
    while True:
        line = await reader.readline()
        if line == b"\r\n":
            break
        print(f"{host} HEADER > {line}")

    # TCP close
    writer.close()
    await writer.wait_closed()
    print(f"[-] Connection to {host} closed")

async def main():
    await asyncio.gather(
        wget("www.sina.com.cn"),
        wget("www.sohu.com"),
        wget("www.163.com"),
    )

if __name__ == "__main__":
    asyncio.run(main())