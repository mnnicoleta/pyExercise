# 1. Given the following function:
# def greet(name):
# return "Greetings {}!".format(name)
# Create a decorator called uppercase that will uppercase the result
# @uppercase
# def greet(name):
# return "Greetings {}!".format(name)
# print(greet("World"))
# >>> "GREETINGS WORLD!"

print(" First exercise______________________")


def uppercase(func):
    def wrapper(name):
        original_result = func(name)
        modified_result = original_result.upper()
        # print(f' modified_result =  {modified_result}')
        return modified_result

    return wrapper


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


pretty = uppercase(greet("world"))

print(greet("world"))

print('\n')

# 2. Given the following function:
# def divide(first_number, second_number):
# return first_number / second_number
# Create a decorator called safe_divide that will output a message if the division cannot be performed,
# othervise it will return the result.

print(" Second exercise______________________")


def safe_divide(func):
    def wrapper(a, b):
        if b == 0:
            print(" Division by zero error")
            return
        return func(a, b)

    return wrapper


@safe_divide
def divide(first_number, second_number):
    return first_number / second_number


print(divide(0, 0))
print(divide(0, 1))
print(divide(10, 2))

print('\n')

# 3. Given a set of print methods:
# print_registry = []
# def greet(name):
# return "Greetings {}!".format(name)
# def say_hello(name):
# return "Hello {}!".format(name)
# def say_goodbye(name):
# return "Goodbye {}!".format(name)

# Create a decorator called register that will update a list called print_registry with all the
# decorated functions names.
# print_registry = []
# @register
# def greet(name):
# return "Greetings {}!".format(name)
# def say_hello(name):
# return "Hello {}!".format(name)
# @register
# def say_goodbye(name):
# return "Goodbye {}!".format(name)
# print(print_registry)
# >>> ['greet', 'say_goodbye']

print(" Third exercise______________________")

print_registry = []


def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


def say_goodbye(name):
    return "Goodbye {}!".format(name)


print('\n')
