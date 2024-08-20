import threading
import time


def main():
    threads = [
        threading.Thread(target=count, args=("elephant", 10)),
        threading.Thread(target=count, args=("lion", 15)),
        threading.Thread(target=count, args=("tiger", 20)),
        threading.Thread(target=count, args=("giraffe", 25)),
    ]

    [th.start() for th in threads]

    print("Constinua rodando")
    time.sleep(2)  # espera
    print("Roda mais um pouco")

    [th.join() for th in threads]  # Espera terminar para depoiius

    print("Todas as threads terminaram de ser executadas!")


def count(thing_to_count, num):
    for i in range(1, num + 1):
        print(f"{i} {thing_to_count}(s)...")
        time.sleep(1)


if __name__ == "__main__":
    main()
