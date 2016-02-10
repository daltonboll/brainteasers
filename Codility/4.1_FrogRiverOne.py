# Brainteaser source: https://codility.com/programmers/task/frog_river_one/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
	N = len(A)

# store how many leaves we've already seen
	num_leaves_seen = 0
	leaves_seen = {}

	# rotate through each leaf time step until we've reached our destination
	for timestep in range(N):
		leaf_position = A[timestep]
		
		# check to see if this is a leaf we needed
		if leaf_position <= X and leaf_position > 0 and leaf_position not in leaves_seen:
			leaves_seen[leaf_position] = 1
			num_leaves_seen += 1

		# if the number of used leaves seen matches X, we are done
		if num_leaves_seen == X:
			return timestep

	# not all of the required leaves fell
	return -1