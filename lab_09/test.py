import sys

def main():
    print('Running main...')
    for idx, arg in enumerate(sys.argv, 0):
        print(f'argv[{idx}] ma wartość {arg}')

    for idx, arg in enumerate(sys.orig_argv, 0):
        print(f'orig_argv[{idx}] ma wartość {arg}')

if __name__ == '__main__':
    main()