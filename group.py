import math
import unittest
# The following function takes a list of integers as the input and splits the
# list into three groups, the first group containing the first three integers in the list,
# the second containing the next three, and the last containing the rest of the numbers,
# from zero numbers to three numbers depending on how many numbers the list contains.
# If the list has fewer than 6 integers or more than 9, None is returned. The output is
# The list of lists that group the original list into groups of three.
def groups_of_3(lists):
    if len(lists) < 6 or len(lists) > 9:
        return None
    elif len(lists) == 6:
        lista = [lists[0], lists[1], lists[2]]
        listb = [lists[3], lists[4], lists[5]]
        listc = []
    elif len(lists) == 7:
        lista = [lists[0], lists[1], lists[2]]
        listb = [lists[3], lists[4], lists[5]]
        listc = [lists[6]]
    elif len(lists) == 8:
        lista = [lists[0], lists[1], lists[2]]
        listb = [lists[3], lists[4], lists[5]]
        listc = [lists[6], lists[7]]
    else:
        lista = [lists[0], lists[1], lists[2]]
        listb = [lists[3], lists[4], lists[5]]
        listc = [lists[6], lists[7], lists[8]]
    return [lista, listb, listc]
print(groups_of_3([1, 2, 3, 4, 5, 6, 7]))
