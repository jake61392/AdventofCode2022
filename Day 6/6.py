#################################################################################################
# Advent of Code 2022 - Day 6
#################################################################################################

######################################################
# comm system
######################################################
def markerFinder(uniqueCharCnt):

	input = open("./input.txt", "r").read()
		
	# grab the first uniqueCharCnt num of chars from the input stream
	chars = list(input[:uniqueCharCnt])

	# loop through the input starting at position uniqueCharCnt
	# since we already grabbed the first set of chars
	for i in range(uniqueCharCnt, len(input)):
		# convert to a set to see if there are uniqueCharCnt num of unique characters
		if (len(set(chars)) == uniqueCharCnt):
			# if so, we found our marker
			print(i)
			break
		# if not, pop off the first char and add the next
		chars.pop(0)
		chars.append(input[i])



def main():
	#part 1
	print('Part 1:')
	markerFinder(4)	
	print('Part 2:')
	#part 2:
	markerFinder(14)


if __name__ == "__main__":
    main()