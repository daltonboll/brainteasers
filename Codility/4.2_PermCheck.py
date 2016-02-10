# Brainteaser source: https://codility.com/programmers/task/perm_check/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
# write your code in Python 2.7
    N = len(A)
	
    # keep track of how many integers we have seen from 1 to N
    integers_seen = {}
    integer_count = 0

    # go through each integer in A to see if we have a permutation
    for i in range(N):
        current_num = A[i]

        # if we have already seen the number or if it is <= 0 or >N, it can't be a permutation
        if current_num in integers_seen or current_num <= 0 or current_num > N:
            return 0
        else:
            integers_seen[current_num] = 1
            integer_count += 1

    if integer_count == N:
        # A contains a permutation
        return 1
    else:
        return 0