import random
import time


def check_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        print("До виконання")
        res =func(*args, **kwargs)
        print("Після виконання")
        print(time.time() - start_time)
        return res

    return inner


@check_time
def func1(a, b):
    print("щось важливе роблю", a + b)
    time.sleep(1)

@check_time
def func2(c):
    print("щось важливе роблю 2")
    time.sleep(2)

func1(1, b=3)

