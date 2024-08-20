import multiprocessing
import time


def func1(val, state):
    if state:
        res = val + 10
        state = False
    else:
        res = val + 20
        val = 200
        state = True

    print(f"O resultado da funcao 1 e {res}")
    time.sleep(0.001)


def func2(val, state):
    if state:
        res = val + 30
        state = False
    else:
        res = val + 40
        val = 400
        state = True

    print(f"O resultado da funcao 2 e {res}")
    time.sleep(0.001)


def main():
    value = 100
    status = False

    p1 = multiprocessing.Process(target=func1, args=(value, status))
    p2 = multiprocessing.Process(target=func2, args=(value, status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
