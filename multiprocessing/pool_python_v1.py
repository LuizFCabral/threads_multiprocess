import multiprocessing


def calculate(data):
    return data**2


def main():
    pool_size = multiprocessing.cpu_count() * 2

    print(f"Utilizando {pool_size} processos.")

    pool = multiprocessing.Pool(processes=pool_size)

    inputs = list(range(7))
    outputs = pool.map(calculate, inputs)

    print(f"Saidas: {outputs}")

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
