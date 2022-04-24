def my_range(start=0, end=100, step=5):
    number = start
    while number < end:
        yield number
        number += step
print(list(my_range()))
