# Brainteaser source: https://codility.com/programmers/task/frog_jmp/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import math

def solution(X, Y, D):
    # Find the difference between X and Y (it's always positive or equal to 0)
    difference = float(Y - X) # convert to float in order to get non-rounding division
    
    # The number of jumps will be rounded up
    jumps = math.ceil(difference / D)
    
    # Convert jumps to an integer
    jumps = int(jumps)
    
    return jumps