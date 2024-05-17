def func(a, b, *args):
    return a*b+sum(args)


res1 = func(1, 2, 3, 4)

print(res1)
