import random


def retry(attempts=5, desired_value=None):
    def wrapper(func):

        def inner(*args, **kwargs):
            count = attempts
            while count != 0:
                value = func(*args, **kwargs)
                if value == desired_value:
                    print("Success")
                    return desired_value
                count -= 1
            print("Failure")

        return inner

    return wrapper


@retry(desired_value=2)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2, 3])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


get_random_value()
get_random_values([1, 2, 3, 4])


def print_square(a):
    b = a - 2
    print(a * '* ')

    def inner_columns():
        nonlocal b
        if b == 0:
            return
        print('*' + ((a - 2) * '  ') + ' *')
        b -= 1
        inner_columns()

    if a > 1:
        inner_columns()
        print(a * '* ')


print_square(3)
