#################################################################################################
# Advent of Code 2022 - Day 10
#################################################################################################

######################################################
# Cathode-Ray Tube
######################################################
def main():
	#part 1
	#read file and split into instruciton pairs
	input = open("./input.txt", "r").read().splitlines()
	input = [line.split() for line in input]
	
	regX     = 1
	cycle    = 1 
	crtIndex = 0

	signalStrengths: list[int] = []
	pixels         : str       = ""

	######################################################
	# does a cycle
	######################################################
	def doCycle():
		nonlocal crtIndex
		nonlocal pixels

		if (cycle - 20) % 40 == 0:
			signalStrengths.append(cycle * regX)
	
		pixels += "#" if regX - 1 <= crtIndex <= regX + 1 else "."
	
		crtIndex += 1 if crtIndex < 39 else -39
	
		if crtIndex == 0:
			pixels += "\n"

		return 1

	for instruction in input:
		cycle += doCycle()

		if instruction[0] == "addx":
			cycle += doCycle()
			regX  += int(instruction[1])			
	

	print("Part 1: ", sum(signalStrengths))
	
	#part 2:
	print("Part 2: \n", pixels)


if __name__ == "__main__":
    main()
