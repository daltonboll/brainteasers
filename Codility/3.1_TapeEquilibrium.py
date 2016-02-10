# Brainteaser source: https://codility.com/programmers/task/tape_equilibrium/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import sys

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    
    # get the sum of all of the numbers in the array A
    integer_sum = 0
    for i in A:
        integer_sum += i
    
    # set up variable for keeping track of minimum differences as we go through array A
    min_difference = sys.maxsize
    
    # go through each intenger in array A, checking the differences as we go along
    left_half = 0
    for i in range(N):
        current_integer = A[i]
        
        # the first element in the array can't be used to split the array
        if i != 0:
            # calculate the differences between the left and right halves of the array at the current point
            right_half = integer_sum - left_half
            difference = abs(left_half - right_half)
            
            # find the minimum difference
            if difference < min_difference:
                min_difference = difference
                
        # keep track of the running total on the left half as we rotate through the array
        left_half += current_integer
    
    return min_difference