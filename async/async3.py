import datetime
import asyncio


async def generate_data(qtd: int, data: asyncio.Queue):
    print(f"Aguarde a geracao de {qtd} dados...")
    for i in range(1, qtd + 1):
        item = i * i
        await data.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.001)
    print(f"{qtd} dados gerados com sucesso...")


async def process_data(qtd: int, dados: asyncio.Queue):
    print(f"Aguarde o processamento de {qtd} dados...")
    processed = 0
    while processed < qtd:
        item, timestamp = await dados.get()
        # print(
        #     f"Dado processado: {item}, timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
        # )
        processed += 1
        await asyncio.sleep(0.001)
    print(f"Foram processados: {processed} itens")


def main():
    total = 5_000
    data = asyncio.Queue()
    print(f"Computando {total *2:.2f} daods.")

    event_loop = asyncio.get_event_loop()

    task1 = event_loop.create_task(generate_data(total, data))
    task2 = event_loop.create_task(generate_data(total, data))
    task3 = event_loop.create_task(process_data(total * 2, data))

    tasks = asyncio.gather(task1, task2, task3)

    event_loop.run_until_complete(tasks)
    event_loop.close()


if __name__ == "__main__":
    main()
