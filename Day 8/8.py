#################################################################################################
# Advent of Code 2022 - Day 8
#################################################################################################
from collections import defaultdict 

######################################################
# Treetop Tree House 
######################################################
def main():
	#part 1
	input = open("./input.txt", "r").read()
	input = [[int(i) for i in j] for j in input.splitlines()]
	trees = set()

	for i in range(len(input)):
		# init these as -1 each time since 0 is a possible input
		maxTree1 = -1
		maxTree2 = -1
		maxTree3 = -1
		maxTree4 = -1

		# loop forwards
		for j in range(len(input[i])):
			if input[i][j] > maxTree1:
				trees.add((j,i))
			maxTree1 = max(maxTree1, input[i][j])
			if input[j][i] > maxTree2:
				trees.add((i,j))
			maxTree2 = max(maxTree2, input[j][i])

		# loop backwards
		for j in range(len(input[i]) -1, -1, -1):
			if input[i][j] > maxTree3:
				trees.add((j,i))
			maxTree3 = max(maxTree3, input[i][j])
			if input[j][i] > maxTree4:
				trees.add((i,j))
			maxTree4 = max(maxTree4, input[j][i])


	print("Part 1: ", len(trees))
	
	#part 2:
	maxViewDistance = 0

	for i in range(len(input)):
		for j in range(len(input[0])):
			# init as 1 since we will use it to multiply the result
			spotViewDistanceTotal = 1
			directionViewDistance = 0

			# right
			for k in range(i + 1, len(input)):
				directionViewDistance += 1
				# if the next tree is taller, break out since that's as far as we can see
				if input[k][j] >= input[i][j]:
					break
			spotViewDistanceTotal *= directionViewDistance
			directionViewDistance  = 0

			# left
			for k in range(i - 1, -1, -1):
				directionViewDistance += 1
				# if the next tree is taller, break out since that's as far as we can see
				if input[k][j] >= input[i][j]:
					break
			spotViewDistanceTotal *= directionViewDistance
			directionViewDistance  = 0

			# up
			for k in range(j + 1, len(input[0])):
				directionViewDistance += 1
				# if the next tree is taller, break out since that's as far as we can see
				if input[i][k] >= input[i][j]:
					break
			spotViewDistanceTotal *= directionViewDistance
			directionViewDistance  = 0

			# down
			for k in range(j - 1, -1, -1):
				directionViewDistance += 1
				# if the next tree is taller, break out since that's as far as we can see
				if input[i][k] >= input[i][j]:
					break
			spotViewDistanceTotal *= directionViewDistance
			directionViewDistance  = 0

			maxViewDistance = max(maxViewDistance, spotViewDistanceTotal)
	print("Part 2: ", maxViewDistance)


if __name__ == "__main__":
    main()
