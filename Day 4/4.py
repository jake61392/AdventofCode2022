#################################################################################################
# Advent of Code 2022 - Day 4
#################################################################################################

######################################################
# section ID pairings
######################################################
def main():
	#part 1
	total = 0

	input = open("./input.txt", "r").read().splitlines()

	for i in input:

		range1, range2 = i.split(",")

		firstLower, firstUpper   = [int(j) for j in range1.split("-")]
		secondLower, secondUpper = [int(j) for j in range2.split("-")]

		if (firstLower  <= secondLower and firstUpper  >= secondUpper) or \
		   (secondLower <= firstLower  and secondUpper >= firstUpper):
			total += 1

	print(total)


	# part 2
	total = 0
	for i in input:

		range1, range2 = i.split(",")

		firstLower, firstUpper   = [int(j) for j in range1.split("-")]
		secondLower, secondUpper = [int(j) for j in range2.split("-")]

		if (secondUpper >= firstLower  >= secondLower) or \
		   (firstUpper  >= secondLower >= firstLower):
			total += 1

	print(total)

if __name__ == "__main__":
    main()