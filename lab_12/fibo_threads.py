import os
import threading
from time import perf_counter

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)

threads = []
print('Uruchamianie wątków...')
t0 = perf_counter()

for _ in range(os.cpu_count()):
    threads.append(threading.Thread(target=fib, args=(40,)))

for t in threads:
    t.start()   

for t in threads:
    t.join()

print(f'Czas wykonania: {perf_counter() - t0}.')