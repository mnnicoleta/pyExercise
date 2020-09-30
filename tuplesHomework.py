# 1. Write a python code to remove an element from a tuple.
pizza = ('peperoni', ('pepperoni', 'motzzarella'), 28, 25.5)

def del_elem_from_tuple(tuple, element):
    iterator = tuple.__iter__()
    for i in range(len(tuple) - 1):
        if next(iterator) == element:
            new_tuple = tuple[: i] + tuple[i + 1:]
            return new_tuple


new_tuple = del_elem_from_tuple(pizza, 28)
print(new_tuple)


# 2. Replace the last element in the list with the string 'last'
# using list comprehension and tuples
list2 = ['I', 'am', 1, 'list', 'of', 5, 'strings']
print(list2)
print(type(list2))

# list[len(list)-1] = 'last'
list2 = [ list2[:len(list2)-1] + ['last']]
print('New list is = ' + str(list2))


# 3. Extract only the strings from the following list using list comprehension :
slist = ['I', 'am', 1, 'list', 'of', 5, 'strings']

stringList = [x for x in slist if type(x) == str]
print(stringList)


# 4. Generate a 3 by 3 matrix that contains 'X' on the main diagonal and '_' in the rest.
matrix = [['_' for x in range(3)] for x in range(3)]

for i in range(len(matrix)):
    matrix[i][i] = "X"

for i in matrix:
    print(i)
