import threading
import time


def process():
    print("[", end="", flush=True)
    for _ in range(10):
        print("#", end="", flush=True)
        time.sleep(1)
    print("]", end="", flush=True)


if __name__ == "__main__":
    th = threading.Thread(target=process)

    th.start()
    th.join()
