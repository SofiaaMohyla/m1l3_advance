def outer_function(func):
    def inner_function():
        print("Вас вітає компанія Логіка!")
        func()
        print("Гарного дня!")


    return inner_function

@outer_function
def hello_func():
    print("повідомлення: як в тебе справи")

@outer_function
def test_func():
    print("повідомлення: не забув виконати дз")
    print("повідомлення: це важливо!")


hello_func()


