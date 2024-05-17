import time


def outer_function(func):
    def inner_function(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        time.sleep(1)
        print(time.time() - start_time)
        return res

    return inner_function

@outer_function
def hello_func():
    print("повідомлення: як в тебе справи")

@outer_function
def test_func():
    print("повідомлення: не забув виконати дз")
    print("повідомлення: це важливо!")

@outer_function
def sum_func(a, b):
    return  a + b

res = sum_func(3, 4)
print(res)

test_func()



