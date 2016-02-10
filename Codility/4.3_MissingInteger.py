# Brainteaser source: https://codility.com/programmers/task/missing_integer/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    
    # keep track of the integers found in the array A
    integers_found = {}

    # go through each integer in A and add it to the hash if it is >= 1
    for num in A:
        if num >= 1:
            integers_found[num] = 1

    # starting from the number 1, go through each key in the hash to see if it was found in A
    for i in range(1, N + 1):
        if i not in integers_found:
            return i

    # every integer from 1 to N was found in the array, so N+1 is the missing integer
    return N + 1