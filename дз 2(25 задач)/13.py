from time import*

class Time():
    def __enter__(self):
        self.start = perf_counter()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        end = perf_counter()
        t = end- self.start
        print(f"Время выполнения: {t:.6f} секунд")

with Time():
    sleep(2)

