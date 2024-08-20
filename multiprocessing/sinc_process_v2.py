import multiprocessing


def deposit(balance, lock):
    for _ in range(10_000):
        with lock:
            balance.value += 1


def withdraw(balance, lock):
    for _ in range(10_000):
        with lock:
            balance.value -= 1


def do_transaction(balance, lock):
    pc1 = multiprocessing.Process(target=deposit, args=(balance, lock))
    pc2 = multiprocessing.Process(target=withdraw, args=(balance, lock))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()


if __name__ == "__main__":
    balance = multiprocessing.Value("i", 100)
    lock = multiprocessing.RLock()

    print(f"Saldo inicial: {balance.value}")

    for _ in range(10):
        do_transaction(balance, lock)

    print(f"Saldo final: {balance.value}")
