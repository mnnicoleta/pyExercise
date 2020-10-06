# 1. Write a python code to remove an element from a tuple.
pizza = ('peperoni', ('pepperoni', 'mozzarella'), 28, 25.5)


def del_element(tuple2, element):
    iterator = tuple2.__iter__()
    for i in range(len(tuple2) - 1):
        if next(iterator) == element:
            new_tuple = tuple2[: i] + tuple2[i + 1:]
            return new_tuple


modified_pizza = del_element(pizza, 28)
print(modified_pizza)

# 2. Replace the last element in the list with the string 'last'
# using list comprehension and tuples
tupleList = ('peperoni', ('pepperoni', 'mozzarella'), 28, 25.5)
print(tupleList)
print(type(tupleList))

tupleList = tupleList[:-1] + tuple(['last' for index, var in enumerate(tupleList) if index == len(tupleList) - 1])
print('New list is = ' + str(tupleList))

# 3. Extract only the strings from the following list using list comprehension :
list3 = ['I', 'am', 1, 'list', 'of', 5, 'strings']

stringList = [x for x in list3 if type(x) == str]
print(stringList)

# 4. Generate a 3 by 3 matrix that contains 'X' on the main diagonal and '_' in the rest.
matrix = [['X' if i == j else '_' for i in range(3)] for j in range(3)]

for i in matrix:
    print(i)
