# Brainteaser source: https://codility.com/programmers/task/perm_missing_elem/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
# write your code in Python 2.7
	
	# set up variables for calculations
	N = len(A) + 1
	
	# get the sum of the first N integers
	sum_of_first_N = (N * (N + 1)) / 2
	
	# keep track of the sum of all of the integers in array A
	actual_sum = 0

	# add up all of the integers in N
	for num in A:
		actual_sum += num
	
	# find the missing integer
	missing_int = sum_of_first_N - actual_sum
	
	return missing_int