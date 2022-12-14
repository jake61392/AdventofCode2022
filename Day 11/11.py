#################################################################################################
# Advent of Code 2022 - Day 11
#################################################################################################
from math import inf, prod

# Monkey class
class Monkey:
	def __init__(self, input):
		self.id                = input[0][-2]
		self.items             = [int(i.strip()) for i in input[1].split(":")[1].split(",")]
		self.operation, factor = input[2].split(" ")[-2:]
		self.factor            = int(factor) if factor != "old" else inf
		self.divisor           = int(input[3].split(" ")[-1])
		self.true              = int(input[4].split(" ")[-1])
		self.false             = int(input[5].split(" ")[-1])
		self.count             = 0
	def process(self, monkeyIn, modVal):
		while len(self.items) > 0:
			self.count += 1
			item = self.items.pop(0)
			num  = item if self.factor == inf else self.factor

			if self.operation == "*":
				item = item * num
			else:
				item = item + num

			# if modVal is 3, its part 1, so just // by 3
			if modVal == 3:
				item = item // 3
			# else its part 2, so lets just %= by passed in modVal
			else:
				item %= modVal

			target = self.true if item % self.divisor == 0 else self.false
			monkeyIn[target].items.append(item)

# does the stuff
def monkeyBusiness(rounds, partNum):
	input   = open("./input.txt", "r").read().splitlines()
	monkey  = []
	inspect = []

	for i in range(0, len(input), 7):
		monkey.append(Monkey(input[i:i + 6]))

	if partNum == 1:
		mod = 3
	elif partNum == 2:
		mod = prod(i.divisor for i in monkey)

	# loop through input num of rounds
	for j in range(rounds):
		for k in monkey:
			k.process(monkey, mod)
			
	for l in monkey:	
		inspect.append(l.count)
	
	inspect.sort()

	print("Part ", partNum, ": ", prod(inspect[-2:]))

######################################################
# Monkey in the Middle
######################################################
def main():
	#part 1
	monkeyBusiness(20, 1)
	
	#part 2:
	monkeyBusiness(10_000, 2)


if __name__ == "__main__":
    main()
