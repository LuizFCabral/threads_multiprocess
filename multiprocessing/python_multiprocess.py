import datetime
import math

import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor


def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f"Realizando o processo com {qtd_cores} cores.")

    start = datetime.datetime.now()

    pool = multiprocessing.cpu_count()

    with ProcessPoolExecutor(max_workers=qtd_cores) as executor:
        for n in range(1, qtd_cores + 1):
            beginning = 50_000_000 * (n - 1) / qtd_cores
            end = 50_000_000 * n / qtd_cores
            print(f"Core {n} processando de {beginning} ate {end}")
            executor.submit(compute, end=end, start=beginning)

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

"""Terminou em 1.74 segundos."""
