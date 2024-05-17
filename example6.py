def outer_function():
    message = "Привіт з зовнішньої функції!"
    def inner_function():
        print(message)

    return inner_function

func = outer_function()
func()
