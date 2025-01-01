def func(a, b, *args, **kwargs):
    return a*b+sum(args)


res1 = func(1, 2, 3, 4, c=5)

print(res1)
