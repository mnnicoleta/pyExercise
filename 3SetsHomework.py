# 2.1 Sets homework
# Create two sets with 10 numbers each (some of the numbers should be present in both sets). With
# these two sets, exemplify the following basic sets operations: union, intersection, difference and
# symmetric difference.
# Resources: https://docs.python.org/3.6/library/stdtypes.html#set-types-set-frozenset

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

# union
print('union = ' + str(set1 | set2))

# intersection
print('intersection = ' + str(set1 & set2))

# difference
print('difference = ' + str(set1 - set2))
print('difference = ' + str(set2 - set1))

# symmetric difference
print('symmetric difference = ' + str(set1 ^ set2))






