import multiprocessing

print(f"Iniciando o processo com o nome : {multiprocessing.current_process().name}")


def do_something(value):
    print(f"Fazendo algo com o valor {value}.")


def main():
    pc = multiprocessing.Process(
        target=do_something, args=("Bird",), name="Processo passaro"
    )

    print(f"Iniciando o processo com o nome {pc.name}")

    pc.start()
    pc.join()


if __name__ == "__main__":
    main()
