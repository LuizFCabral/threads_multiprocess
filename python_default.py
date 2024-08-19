import datetime
import math


def main():
    start = datetime.datetime.now()

    compute(end=50_000_000)

    time = datetime.datetime.now() - start

    print(f"Terminou em {time.total_seconds():.2f} segundos.")


def compute(end, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < end:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == "__main__":
    main()

"""Terminou em 14.79 segundos."""
