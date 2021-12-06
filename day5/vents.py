#!/usr/bin/env python3
import math

class VentLine:

	x1 = None
	y1 = None
	x2 = None
	y2 = None

	length = None
	direction = None

	def __init__(self,x1,y1,x2,y2):

		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

		if self.x1 == self.x2:
			self.direction = "horizontal"
		elif self.y1 == self.y2:
			self.direction = "vertical"
		else:
			self.direction = "diagonal"


	def get_coverage(self):

		covered_points = []

		if self.direction == "horizontal":
			for i in range(min(self.y1,self.y2),max(self.y1,self.y2)+1):
				covered_points.append((self.x1,i))

		elif self.direction == "vertical":
			for i in range(min(self.x1,self.x2),max(self.x1,self.x2)+1):
				covered_points.append((i,self.y1))

		else:
			#this line is diagonal, we need each point between the two points
			x_range = []
			y_range = []
			if self.x1 > self.x2:
				x_range = range(self.x1,self.x2-1,-1)
			else:
				x_range = range(self.x1,self.x2+1,1)

			if self.y1 > self.y2:
				y_range = range(self.y1,self.y2-1,-1)
			else:
				y_range = range(self.y1,self.y2+1,1)

			for i in range(0,len(x_range)):

				covered_points.append((x_range[i],y_range[i]))


		return covered_points

	def printVentLine(self):

		print(f"{self.x1},{self.y1} ---> {self.x2},{self.y2}")

def determine_grid_size(lines):

	max_xval = 0
	max_yval = 0

	for line in lines:

		max_xval = max(max_xval,line.x1)
		max_xval = max(max_xval,line.x2)
		max_yval = max(max_yval,line.y1)
		max_yval = max(max_yval,line.y2)


	return 1000,1000

def find_overlaps(lines,gridsize):

	#initialize empty grid
	ventgrid = []
	overlapcount = 0

	for i in range(0,gridsize[1]):

		ventrow = []
		
		for j in range(0,gridsize[0]):

			ventrow.append(0)

		ventgrid.append(ventrow)

	#increment covered points
	for line in lines:

		#get coverage points
		if line.direction != "other":
			covered_points = line.get_coverage()
			#print("coverage:", covered_points)
			for point in covered_points:
				ventgrid[point[0]][point[1]] += 1


	gridstring = ""

	for i in range(0,gridsize[1]):
		for j in range(0,gridsize[0]):
			val = ventgrid[j][i]
			if val == 0:
				gridstring += "."
			else:
				gridstring += str(val)
				if val > 1:
					overlapcount += 1

		gridstring += "\n"

	print(gridstring)

	return overlapcount

	

print("Hello, World!")

# Open a file
#fo = open("input/data.txt", "r+")
fo = open("input/data.txt", "r+")
print ("Name of the file: ", fo.name)

lines = fo.readlines()
print("# of lines:", len(lines))

lines = [line.strip() for line in lines]
print(lines)

ventlines = []

for line in lines:

	startpt, endpt = line.split("->")
	x1,y1 = [int(n) for n in startpt.split(",")]
	x2,y2 = [int(n) for n in endpt.split(",")]

	ventlines.append(VentLine(x1,y1,x2,y2))

#for ventline in ventlines:
#	ventline.printVentLine()

gridsize = determine_grid_size(ventlines)
n_ovleraps = find_overlaps(ventlines,gridsize)
print(n_ovleraps)


# Close opened file
fo.close()
