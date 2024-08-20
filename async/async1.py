import datetime
import asyncio


async def generate_data(qtd: int, data: asyncio.Queue):
    print(f"Aguarde a geracao de {qtd} dados...")
    for i in range(1, qtd + 1):
        item = i * i
        await data.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.0001)
    print(f"{qtd} dados gerados com sucesso...")


async def process_data(qtd: int, dados: asyncio.Queue):
    print(f"Aguarde o processamento de {qtd} dados...")
    processed = 0
    while processed < qtd:
        item, timestamp = await dados.get()
        print(
            f"Dado processado: {item}, timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        processed += 1
        await asyncio.sleep(0.0001)
    print(f"Foram processados: {processed} itens")


if __name__ == "__main__":
    total = 5_000
    data = asyncio.Queue()
    event_loop = asyncio.get_event_loop()

    print(f"Computando {total *2:.2f} dados.")
    event_loop.run_until_complete(generate_data(total, data))
    event_loop.run_until_complete(generate_data(total, data))
    event_loop.run_until_complete(process_data(total * 2, data))

    event_loop.close()
