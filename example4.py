def func(a, b, **kwargs):
    print(kwargs)


res1 = func(1, 2, c=3, d=4)

print(res1)
