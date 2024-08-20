import multiprocessing


def deposit(balance):
    for _ in range(10_000):
        balance.value += 1


def withdraw(balance):
    for _ in range(10_000):
        balance.value -= 1


def do_transaction(balance):
    pc1 = multiprocessing.Process(target=deposit, args=(balance,))
    pc2 = multiprocessing.Process(target=withdraw, args=(balance,))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()


if __name__ == "__main__":
    balance = multiprocessing.Value("i", 100)

    print(f"Saldo inicial: {balance.value}")

    for _ in range(10):
        do_transaction(balance)

    print(f"Saldo final: {balance.value}")
