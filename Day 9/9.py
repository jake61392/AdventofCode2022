#################################################################################################
# Advent of Code 2022 - Day 9
#################################################################################################

######################################################
# return vector based on passed in direction
######################################################
def getVector(direction: str):
	match direction:
		case "L":
			return [-1, 0]
		case "R":
			return [1, 0]
		case "U":
			return [0, 1]
		case "D":
			return [0, -1]

######################################################
# moves the tail
######################################################
def moveTail(head: list[int], tail: list[int]): 
		delta = [x - y for x, y in zip(head, tail)]

		if abs(delta[0]) > 1 or abs(delta[1]) > 1:
			tail[:] = [n + (1 if deltaN >= 1 else -1 if deltaN <= -1 else 0) \
			                for n, deltaN in zip(tail, delta)]


######################################################
# Rope Bridge
######################################################
def main():
	#part 1
	#read file and split into instruciton pairs
	input = open("./input.txt", "r").read().splitlines()
	input = [(line.split()[0], int(line.split()[1])) for line in input]
	
	head = [0, 0]
	tail = [0, 0]

	tailParts = [[0, 0] for i in range(9)]

	visitedPoint1 = set()
	visitedPoint2 = set()

	for direction, distance in input:
		for i in range(distance):
			head = [x + y for x, y in zip(head, getVector(direction))]

			moveTail(head, tail)

			visitedPoint1.add(tuple(tail))

			for j in range(len(tailParts)):
				moveTail(head if j == 0 else tailParts[j -1], tailParts[j])

				if j == 8:
					visitedPoint2.add(tuple(tailParts[j]))

	print("Part 1: ", len(visitedPoint1))
	
	#part 2:
	print("Part 2: ", len(visitedPoint2))


if __name__ == "__main__":
    main()
