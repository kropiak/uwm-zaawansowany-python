import multiprocessing as mp
from time import perf_counter


def open_file(filepath, sep=','):
    return f'Otwieram {filepath} używając separatora {sep}'


if __name__ == '__main__':
    
    print('Uruchamianie procesów...')
    t0 = perf_counter()
    params = [
        ('data.csv', ),
        ('names.csv', ';'),
        ('products.csv', ),
        ('other.csv', '^'),
        ('costam.csv', ',')]

    # tworzymy pulę 4 procesów
    with mp.Pool(processes=4) as pool:
        # wyniki są zbierane do listy
        results = pool.starmap(open_file, params)
        for i, result in enumerate(results):
            print(f"open_file{params[i]} = {result}")

    print(f'Czas wykonania: {perf_counter() - t0}.')