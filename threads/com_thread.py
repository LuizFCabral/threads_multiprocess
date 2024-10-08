import time
import colorama

from threading import Thread
from queue import Queue


def data_generator(queue):
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f"Dados {i} gerado", flush=True)
        time.sleep(1)
        queue.put(i)


def data_consumer(queue):
    time.sleep(
        2
    )  # espera um tempo para iniciar para que a outra funcao possa iniciar a queue
    while queue.qsize() > 0:
        value = queue.get()
        time.sleep(1.2)
        print(colorama.Fore.RED + f"Dado {value * 2} processado", flush=True)
        queue.task_done()


if __name__ == "__main__":
    print(colorama.Fore.WHITE + "Sistema iniciado", flush=True)
    queue = Queue()
    th1 = Thread(target=data_generator, args=(queue,))
    th2 = Thread(target=data_consumer, args=(queue,))

    th1.start()
    th2.start()

    th1.join()
    th2.join()
