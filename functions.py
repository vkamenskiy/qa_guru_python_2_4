def print_message(message, end):
    print(message, end=end)


print_message("Hello", ", ")
print_message("World", ".")
print()

def lower_string(string: str):
    return string.lower()

print(lower_string("QWERTY"))
print(lower_string("qWeRtYuIoP"))

def upper_and_lower_string(string: str):
    return string.upper(), string.lower()

print(upper_and_lower_string("qWeRtYuIoP"))



def print_all_arguments(*args):
    print(*args)


print_all_arguments(1, 2, 3, 4, 5, 6, 7, 8, 9)


def func_with_kwargs(**kwargs):
    print(kwargs)


func_with_kwargs(first_key=123, second_key=345)


def wrapped_print(*args, **kwargs):
    print("Начинаем печать")
    print(*args, **kwargs)
    print("Заканчиваем печать")


wrapped_print("Печатаем", end="\n\n")


def by_age(d):
    return d["age"]

by_age({"name": "Oleg", "age": 32})

users = [
    {"name": "Oleg", "age": 40},
    {"name": "Vlad", "age": 30},
    {"name": "Sergey", "age": 20},
    {"name": "Maria", "age": 10},
]

print(sorted(users, key=by_age))




