import asyncio


async def a(n):
    await asyncio.sleep(n % 3)
    print(n)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([a(i) for i in range(10)]))
