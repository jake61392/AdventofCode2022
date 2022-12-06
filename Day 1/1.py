#################################################################################################
# Advent of Code 2022 - Day 2
#################################################################################################

######################################################
# Calries carried by elves
######################################################
def main():
	# top calorie elf
	print(max(sum(map(int,i.split())) for i in open("./input.txt").read().split('\n\n')))

	# sum of calories of the top 3 elves
	print(sum(sorted(sum(map(int,i.split())) for i in open("./input.txt").read().split('\n\n'))[-3:]))


if __name__ == "__main__":
    main()