from multiprocessing import Process, Queue, Pool
import time
import os


def f(q):
    q.put(time.time())
    print(f'Aktualny rozmiar kolejki: {q.qsize()}')

if __name__ == '__main__':
    q = Queue()

    print(f'Zostanie uruchomionych {os.cpu_count()} procesów.')
    for _ in range(os.cpu_count()):
        Process(target=f, args=(q,)).start()

    while not q.empty():
        print(q.get())