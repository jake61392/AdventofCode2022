#################################################################################################
# Advent of Code 2022 - Day 2
#################################################################################################

######################################################
# Rock - Paper - Scissors elf eddition
######################################################
def main():
	totalScore = 0

	# part 1
	for i in open("./input.txt", 'r'):
		if 'X' in i:
			totalScore = totalScore + 1
			if 'A' in i:
				totalScore = totalScore + 3
			elif 'C' in i:
				totalScore = totalScore + 6
		elif 'Y' in i:
			totalScore = totalScore + 2
			if 'A' in i:
				totalScore = totalScore + 6
			elif 'B' in i:
				totalScore = totalScore + 3
		elif 'Z' in i:
			totalScore = totalScore + 3
			if 'B' in i:
				totalScore = totalScore + 6
			elif 'C' in i:
				totalScore = totalScore + 3

	print(totalScore)
	
	# part 2
	totalScore = 0
	for i in open("./input.txt", 'r'):
		if 'X' in i: # need to lose
			if 'A' in i:
				# they chose rock (A) so we need to choose scissors (C)
				totalScore = totalScore + 3
			elif 'B' in i: 
				# they chose paper (B) so we need to choose rock (A)
				totalScore = totalScore + 1
			elif 'C' in i:
				# they chose scissors (C) so we need to choose paper (B)
				totalScore = totalScore + 2
		elif 'Y' in i: # need to draw
			totalScore = totalScore + 3
			if 'A' in i:
				# they chose rock (A) so we need to choose rock (A)
				totalScore = totalScore + 1
			elif 'B' in i: 
				# they chose paper (B) so we need to choose paper (B)
				totalScore = totalScore + 2
			elif 'C' in i:
				# they chose scissors (C) so we need to choose scissors (C)
				totalScore = totalScore + 3
		elif 'Z' in i: # need to win
			totalScore = totalScore + 6
			if 'A' in i:
				# they chose rock (A) so we need to choose paper (B)
				totalScore = totalScore + 2
			elif 'B' in i: 
				# they chose paper (B) so we need to choose scissors (C)
				totalScore = totalScore + 3
			elif 'C' in i:
				# they chose scissors (C) so we need to choose rock (A)
				totalScore = totalScore + 1

	print(totalScore)
if __name__ == "__main__":
    main()