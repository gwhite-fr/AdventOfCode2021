#!/usr/bin/env python3

print("Hello, World!")

# Open a file
fo = open("input/data.txt", "r+")
print ("Name of the file: ", fo.name)

lines = fo.readlines()
print("# of lines:", len(lines))


lines = [int(line) for line in lines]


increasecount = 0
slidingincreasecount = 0
previousdepth = lines[0]
previousdepthA = lines[0]
previousdepthB = lines[1]
previousdepthC = lines[2]

for line in lines:

	currentdepth = line
	currentsum = currentdepth + previousdepthC + previousdepthB
	previoussum = previousdepthA + previousdepthB + previousdepthC

	if previousdepth < 0:

		previousdepth == currentdepth

	if currentdepth > previousdepth:

		increasecount += 1
		print("increase")

	if currentsum > previoussum:

		slidingincreasecount += 1
		print("slidingincrease")

	previousdepth = currentdepth
	previousdepthA = previousdepthB
	previousdepthB = previousdepthC		
	previousdepthC = currentdepth

print("The answer is:", increasecount)
print("The sliding answer is:", slidingincreasecount)

# Close opened file
fo.close()