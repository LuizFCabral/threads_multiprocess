import asyncio


async def say_hi_long():
    print("Oi...")
    await asyncio.sleep(2)  # Sempre utilizar await em funcoes assincronos
    print("todos...")


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(say_hi_long())
event_loop.close()
