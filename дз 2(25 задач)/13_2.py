from time import *
from contextlib import contextmanager

@contextmanager
def Time():
    start = perf_counter()
    try:
        yield

    finally:
        end = perf_counter()
        t = end-start
        print(f"Время работы {t:.6f} секунд")

with Time():
    sleep(2)
