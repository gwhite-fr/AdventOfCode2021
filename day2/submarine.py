#!/usr/bin/env python3

class Submarine:

	hpos = 0
	depth = 0
	aim = 0

	def navigate(self, dir, d):

		"""
		Move the submarine in the given direction by d units
		"""

		if dir == "forward":
			self.hpos += d
			self.depth += (self.aim*d)

		elif dir == "up":
			#self.depth -= d
			self.aim -= d

		elif dir == "down":
			#self.depth += d
			self.aim += d


		print(self.hpos,self.depth,self.aim)

		return

	def current_pos(self):

		print("Horizontal Position:", self.hpos)
		print("Depth:", self.depth)
		print("Aim:", self.aim)
		print("Multiplied:", self.hpos*self.depth)

print("Hello, World!")

# Open a file
fo = open("input/data.txt", "r+")
print ("Name of the file: ", fo.name)

lines = fo.readlines()
print("# of lines:", len(lines))


lines = [line.split(" ") for line in lines]

submarine = Submarine()
for line in lines:

	submarine.navigate(line[0],int(line[1]))

submarine.current_pos()


# Close opened file
fo.close()