import asyncio


async def say_hi():
    print("Oi...")


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(say_hi())
event_loop.close()
