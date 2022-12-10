#################################################################################################
# Advent of Code 2022 - Day 7
#################################################################################################
from collections import defaultdict 

######################################################
# No Space Left On Device
######################################################
def main():
	#part 1
	input = open("./input.txt", "r").read().splitlines()
	
	fileDict      = defaultdict(list)
	directoryList = []
	files         = {}
	totalSize     = 0

	# iterate through the file to generate our dictionary
	for i in input:
		# check for commands input by looking for $
		if i[0] == "$":
			# is it a CD or dir command
			if i[2] == "c":
				# check if its cd up or down
				if i[5] == ".":
					directoryList.pop()
				else:
					directoryList.append(i[5:])
		# handle ls output
		else:
			# add to our dictonary
			fileDict["".join(directoryList)].append("".join(directoryList) + i.split()[1])

			# if its an ls file output rather than a dir, also add to the file size
			if i[:4] != "dir ":
				files["".join(directoryList) + i.split()[1]] = int(i.split()[0])

	# recursive funciton to iterate through the generated dictionary
	def sumSmallFiles(directory):
		# nonlocal totalSize to point to the outer functions var so it can hold its 
		# state through the recursive calls
		nonlocal totalSize
		size = 0

		# name passed in is a file, return its size
		if directory in files.keys():
			return files[directory]

		# iterate through the dictonary with the name we're looking at
		for j in fileDict[directory]:
			# recursively call to ensure we get all files and sub directories and sum all of the files inside
			size += sumSmallFiles(j)

		# if the files sum less than 100_000, then add it to our total size
		if size <= 100_000:
			totalSize += size

		# return our size to be added up
		return size

	# sum file sizes, start at root directory of "/"
	sumSmallFiles("/")
	print("Part 1: ", totalSize)
	
	#part 2:
	# constants provided in the prompt
	TOTAL_DISC_SPACE = 70_000_000
	SPACE_NEEDED     = 30_000_000

	#figure out the total amount of space used on the file system
	spaceUsed        = sum(files.values())

	freeSpace        = TOTAL_DISC_SPACE - spaceUsed
	spaceToFree      = SPACE_NEEDED - freeSpace

	# set to the total disc space so that when we use min() later it will choose the directory its 
	# compared against and not the initialized value. We know that anything chosen will be smaller than
	# the TOTAL_DISC_SPACE so this is safe to use
	totalSize        = TOTAL_DISC_SPACE

	# recursive funciton to iterate through the generated dictionary
	def findDirectoryToDelete(directory):
		# nonlocal totalSize to point to the outer functions var so it can hold its 
		# state through the recursive calls
		nonlocal totalSize
		size = 0

		# name passed in is a file, return its size
		if directory in files.keys():
			return files[directory]

		# iterate through the dictonary with the name we're looking at
		for j in fileDict[directory]:
			# recursively call to ensure we get all files and sub directories and sum all of the files inside
			size += findDirectoryToDelete(j)

		#if the size of this directory is larger than the sizeToFree, 
		# then see if its the smallest directory we can use
		if size >= spaceToFree: 
			totalSize = min(totalSize, size)

		# return our size to be added up
		return size

	# iterate through the directories to find the smalles possible one to delete
	findDirectoryToDelete("/")
	print("Part 2: ", totalSize)


if __name__ == "__main__":
    main()
