import threading
import time


def main():
    th = threading.Thread(target=count, args=("elephant", 10))

    # Coloca a thread na poll de threads prontas para execucao
    th.start()

    print("Constinua rodando")
    time.sleep(2)  # espera
    print("Roda mais um pouco")

    th.join()  # Espera terminar para depoiius

    print("Thread terminou!")


def count(thing_to_count, num):
    for i in range(1, num + 1):
        print(f"{i} {thing_to_count}(s)...")
        time.sleep(1)


if __name__ == "__main__":
    main()
