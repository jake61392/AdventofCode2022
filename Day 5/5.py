#################################################################################################
# Advent of Code 2022 - Day 5
#################################################################################################

######################################################
# move crates 
######################################################
def moveCrates(isCrateMover9001 = False):

	crateStacks  = []
	instructions = []
	numCrates    = 0
	src          = 0
	dest         = 0

	input = open("./input.txt", "r").readlines()

	for i in input:
		if (i[:4] == 'move'):
			# movement instruction, append instructions list
			instructions.append(i)
		elif (i[:1] == '['):
			# we have a crate, append every 4th char since that's what contains the crate leter
			crateStacks.append([i[crates * 4 + 1] for crates in range(len(i) // 4)])

	# make a list of the crates in collumns rather than rows
	crateStacks = [list("".join(column).strip()[::-1]) for column in zip(*crateStacks)]

	# parse movement instructions
	for instruction in instructions:
		# grab 2 chars after the word 'move '
		numCrates = (int(instruction.split('move ')[1][0:2]))
		# grab 2 chars after the word ' from '
		src = (int(instruction.split(' from ')[1][0:2]))
		# grab 2 chars past the word ' to '
		dest = (int(instruction.split(' to ')[1][0:2]))

		# move them crates!
		if (not isCrateMover9001):
			crateStacks[dest - 1].extend(crateStacks[src - 1][-numCrates:][::-1])
		else:
			crateStacks[dest - 1].extend(crateStacks[src - 1][-numCrates:])
		crateStacks[src - 1] = crateStacks[src - 1][:-numCrates]

	return print ("The top crates are: %a" %"".join([j[-1] for j in crateStacks]))

def main():
	#part1
	print(moveCrates())
	#part2
	print(moveCrates(True))


if __name__ == "__main__":
    main()