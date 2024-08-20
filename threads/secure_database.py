import threading
import random
import time

from typing import List


lock = threading.RLock()


class Account:
    def __init__(self, balance: float = 0):
        self.balance = balance


def main():
    accounts = create_accounts()
    with lock:
        total = sum(account.balance for account in accounts)
    print("Iniciando transferencia...")

    threads = [
        threading.Thread(target=services, args=(accounts, total)),
        threading.Thread(target=services, args=(accounts, total)),
        threading.Thread(target=services, args=(accounts, total)),
    ]

    [th.start() for th in threads]
    [th.join() for th in threads]

    print("Tranferencias completas.")

    validate_database(accounts, total)


def services(accounts, total):
    for _ in range(1, 10_000):
        c1, c2 = get_two_accounts(accounts)
        value = random.randint(1, 100)
        transfer(c1, c2, value)
        validate_database(accounts, total)


def create_accounts() -> List[Account]:
    return [Account(balance=random.randint(5000, 10000)) for _ in range(6)]


def transfer(origin: Account, destination: Account, value: int):
    if origin.balance < value:
        return

    with lock:
        origin.balance -= value
        time.sleep(0.001)
        destination.balance += value


def validate_database(accounts: List[Account], total: int):
    with lock:
        current = sum(account.balance for account in accounts)

    if current != total:
        print(
            f"ERROR: Balanco bancario inconsistente. BRL$ {current:.2f} vs {total:.2f}",
            flush=True,
        )
    else:
        print(f"OK: Balanco bancario consistente. BRL$ {total:.2f}", flush=True)


def get_two_accounts(accounts):
    c1 = random.choice(accounts)
    c2 = random.choice(accounts)

    while c1 == c2:
        c2 = random.choice(accounts)

    return c1, c2


if __name__ == "__main__":
    main()
