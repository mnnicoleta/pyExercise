import math

# this is a comment

spam = 1  # and this is the second comment
# ... and now a third!
text = "# This is not a comment because it's inside quotes."
print(text)


""" bla bla
this is multiple line comments
"""

squares = [1, 4, 9, 16, 25]

squares[0]
print(squares[1])

items = [1, 2, 3, 4, 5, 6, 7]
for item in items:
    if item % 2 == 0:
        print(item)


print('doesn\'t')

print('"Yes," he said.')

print('C:\some\name')

print(r'C:\some\name')

print("""
Usage: thingy [OPTIONS]
-h Display this usage message
-H hostname Hostname to connect to
""")

print(3 * 'un' + 'ium')

word = 'Python'

print(word[:2])


print(word[4:])

#print(word[46])

squares = [1, 4, 9, 16, 25]

squares = squares + [36, 49, 64, 81, 100]

for sq in squares:
    print(sq, math.sqrt(sq))

# x = int(input("Please enter an integer: "))
#
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')


for i in range(5):
    print(i)

range(5, 10)


aa = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(aa)):
    print(i, aa[i])


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# Now call the function we just defined:
fib(2000)


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(1))
print(f(-5))

def my_function():
    """ la la la
    Do nothing, but document it
    bla bla
    """
    pass


print(my_function().__doc__)


print('shirts!')

all_shirts =[]

shirt_sizes = [48, 49, 50, 51, 52, 53]
smallest = min(shirt_sizes)
largest = max(shirt_sizes)
print(smallest)
print(largest)


all_shirts.append('green')
print(all_shirts)
all_shirts.append('yellow')
print(all_shirts)

all_shirts.insert(10, 'black')

all_shirts.insert(1, 'red')

all_shirts.insert(len(all_shirts), 'bla')

for all in all_shirts:
    print(all, all_shirts.index(all))

fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()
# Return the number of times the value "cherry" appears int the fruits list:
x = fruits.count("cherry")


cars = ['Ford', 'BMW', 'Volvo']
# Add the elements of cars to the fruits list:
fruits.extend(cars)

# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
x = fruits.index("cherry")

unique_grid = []
# unique_grid = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(unique_grid)

for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            unique_grid.append(tuple([x, y]))


print(unique_grid)
print(len(unique_grid))


shop2 = [(x, y) for i in range(100) for x in ['shirt', 'scarf', 'glove', 'heat'] for y in ['S', 'M', 'L', 'XL', 'XXL']]
shop2.append(['SHIRT', 's'])
print(shop2)
print('length of shop is ' + str(len(shop2)))
shop2.pop()
print(shop2)
print(' after deleting last element - length of shop is ' + str(len(shop2)))

