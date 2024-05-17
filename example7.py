
def hello_func():
    print("повідомлення: як в тебе справи")

def test_func():
    print("повідомлення: не забув виконати дз")
    print("повідомлення: це важливо!")

def outer_function(func):
    def inner_function():
        print("Вас вітає компанія Логіка!")
        func()
        print("Гарного дня!")


    return inner_function

func = outer_function(test_func)
func()
