# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    t = 0
    for i in list_of_numbers:
        if i > t:
            t = i
    return t


print(greatest([4, 23, 1]))