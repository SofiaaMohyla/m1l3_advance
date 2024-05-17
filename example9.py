def outer_function(func):
    def inner_function(*args, **kwargs):
        print("Вас вітає компанія Логіка!")
        res = func(*args, **kwargs)
        print("Гарного дня!")
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



