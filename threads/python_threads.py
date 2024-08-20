import datetime
import math

import threading
import multiprocessing


def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f"Realizando o processo com {qtd_cores} cores.")

    start = datetime.datetime.now()

    threads = []
    for n in range(1, qtd_cores + 1):
        beginning = 50_000_000 * (n - 1) / qtd_cores
        end = 50_000_000 * n / qtd_cores
        print(f"Core {n} processando de {beginning} ate {end}")

        threads.append(
            threading.Thread(
                target=compute, kwargs={"start": beginning, "end": end}, daemon=True
            )
        )

    [th.start() for th in threads]
    [th.join() for th in threads]

    time = datetime.datetime.now() - start

    print(f"Terminou em {time.total_seconds():.2f} segundos.")


def compute(end, start=1):
    pos = start
    fator = 1000 * 1000
    while pos < end:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == "__main__":
    main()

"""Terminou em 9.9 segundos."""
