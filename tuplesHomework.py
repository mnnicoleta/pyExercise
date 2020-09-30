# 1. Write a python code to remove an element from a tuple.
pizza = ('peperoni', ('pepperoni', 'motzzarella'), 28, 25.5)

def delElemFromTuple(tuple, element):
    iterator = tuple.__iter__()
    for i in range(len(tuple)-1):
        if next(iterator) == element:
            new_tuple = tuple[: i] + tuple[i + 1:]
            return new_tuple

new_tuple = delElemFromTuple(pizza, 28)
print(new_tuple)


# 2. Replace the last element in the list with the string 'last'
# using list comprehension and tuples

# 3. Extract only the strings from the following list using list comprehension :
# slist = ['I', 'am', 1, 'list', 'of', 5, 'strings']

# 4. Generate a 3 by 3 matrix that contains 'X' on the main diagonal and '_' in the rest.