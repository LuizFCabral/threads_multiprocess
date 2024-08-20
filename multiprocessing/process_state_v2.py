import multiprocessing
import time
import ctypes


def func1(val, state):
    if state.value:
        res = val.value + 10
        state.value = False
    else:
        res = val.value + 20
        val.value = 200
        state.value = True

    print(f"O resultado da funcao 1 e {res}")
    time.sleep(0.001)


def func2(val, state):
    if state.value:
        res = val.value + 30
        state.value = False
    else:
        res = val.value + 40
        val.value = 400
        state.value = True

    print(f"O resultado da funcao 2 e {res}")
    time.sleep(0.001)


def main():
    """
    Para que os dados sejam compartilhados em memoria pelos
    processos temos que coloca-los no mesmo formato da linguagem C
    """
    value = multiprocessing.Value("i", 100)
    status = multiprocessing.Value(ctypes.c_bool, False)

    p1 = multiprocessing.Process(target=func1, args=(value, status))
    p2 = multiprocessing.Process(target=func2, args=(value, status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
