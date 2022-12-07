#################################################################################################
# Advent of Code 2022 - Day 3
#################################################################################################

######################################################
# Rucksack Reorganization
######################################################
def main():
	# part 1
	priorityTotal = 0
	file = open("./input.txt", "r")
	line = file.readline()
	while line:
		compartment1, compartment2 = line[:int(len(line)/2)], line[int(len(line)/2):]
		for j in compartment1:
			if j in compartment2:
				if j.islower():
					# 1-26 for a-z
					priorityTotal = priorityTotal + (ord(j) - 96)
					break
				else:
					# 64-26=38 to give 27-52 for A-Z
					priorityTotal = priorityTotal + (ord(j) - 38)
					break
		line = file.readline()

	print(priorityTotal)
	file.close()

if __name__ == "__main__":
    main()