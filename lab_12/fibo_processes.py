import os
import multiprocessing as mp
from time import perf_counter

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


if __name__ == '__main__':

    processes = []
    print('Uruchamianie procesów...')
    t0 = perf_counter()

    for _ in range(os.cpu_count()):
        processes.append(mp.Process(target=fib, args=(40,)))

    for t in processes:
        t.start()   

    for t in processes:
        t.join()

    print(f'Czas wykonania: {perf_counter() - t0}.')