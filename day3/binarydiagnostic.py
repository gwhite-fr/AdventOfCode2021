#!/usr/bin/env python3

def calc_power(data):

	rowlength = len(data[0])
	nrows = len(data)

	gamma_result = ''
	epsilon_result = ''


	for j in range(0,rowlength):

		col = []

		for i in range(0,nrows):

			col.append(data[i][j])

		print(col)
		if col.count('1') > col.count('0'):
			gamma_result += '1'
			epsilon_result += '0'
		else:
			gamma_result += '0'
			epsilon_result += '1'

	gammarate = int(gamma_result,2)
	epsilonrate = int(epsilon_result,2)
	
	print(gamma_result,epsilon_result)
	print(gammarate,epsilonrate)

	powerconsumption = gammarate*epsilonrate

	return powerconsumption

def calc_co2(data):

	#oxygen - determine most common value ( 0 or 1 )
	#keep only numbers that have that bit in that position
	#if 0 and 1 are equal, keep only values with a 1 in the position

	#co2 - determine the least common val and only keep those
	#if 0 and 1 are equal, keep the 0s

	rowlength = len(data[0])
	nrows = len(data)


	#Determine the condition bits
	data_invert = list(map(list, zip(*data)))
	targets = ''

	for d in range(0,rowlength):

		if data_invert[d].count('1') > nrows/2:

			targets += '0'

		elif data_invert[d].count('1') == nrows/2:
			
			targets += '0'

		else:

			targets += '1'

	print("targets:", targets)
	toggled_data = [(d,True) for d in data]


	for i in range(0,rowlength):

		for j in range(0, nrows):
		
			if toggled_data[j][1]:
				if not toggled_data[j][0][i] == targets[i]:
					toggled_data[j] = (toggled_data[j][0],False)

	oxygenresult = None
	for d in toggled_data:
		if d[1] == True:
			oxygenresult = d
			break

	print("Co2:", oxygenresult)
	print("Co2 #:", int(oxygenresult[0],2))



def calc_oxygen(data):

	#oxygen - determine most common value ( 0 or 1 )
	#keep only numbers that have that bit in that position
	#if 0 and 1 are equal, keep only values with a 1 in the position

	#co2 - determine the least common val and only keep those
	#if 0 and 1 are equal, keep the 0s

	rowlength = len(data[0])
	nrows = len(data)


	#Determine the condition bits
	data_invert = list(map(list, zip(*data)))
	targets = ''

	for d in range(0,rowlength):

		if data_invert[d].count('1') > nrows/2:

			targets += '1'

		elif data_invert[d].count('1') == nrows/2:
			
			targets += '1'

		else:

			targets += '0'

	print("targets:", targets)
	toggled_data = [(d,True) for d in data]


	for i in range(0,rowlength):

		for j in range(0, nrows):
		
			if toggled_data[j][1]:
				if not toggled_data[j][0][i] == targets[i]:
					toggled_data[j] = (toggled_data[j][0],False)

	oxygenresult = None
	for d in toggled_data:
		if d[1] == True:
			oxygenresult = d
			break

	print("Oxygen:", oxygenresult)
	print("Oxygen #:", int(oxygenresult[0],2))

def findoxygen(data, position, tgts):


	remaining = []

	for d in data:

		if d[position] == tgts[position]:

			remaining.append(d)

	if len(remaining) == 1:
		return remaining

	else:
		print(remaining)
		findoxygen(remaining,position+1,tgts)


def checkoxygen(binary, position):

	if binary.count('0') > binary.count('1'):
		
		return binary[position] == '0'

	elif binary.count('0') < binary.count('1'):

		return binary[position] == '1'

	else:

		print("equal", binary)
		return binary[position] == '1'		

def checkco2(binary, position):

	if binary.count('0') > binary.count('1'):
		
		return binary[position] == '1'

	elif binary.count('0') < binary.count('1'):

		return binary[position] == '0'

	else:

		return binary[position] == '0'


def find_mostcommon_value(values):
	
	if values.count('1') > values.count('0'):
		return '1'
	elif values.count('0') == values.count('1'):
		return '1'
	else:
		return '0'

def find_leastcommon_value(values):
	
	if values.count('1') > values.count('0'):
		return '0'
	elif values.count('0') == values.count('1'):
		return '0'
	else:
		return '1'

def oxygenrating(data,bitpos):

	#starting with the first bit
	filtered_data = []

	column = [d[bitpos] for d in data]
	commonval = find_mostcommon_value(column)

	for d in data:
		if d[bitpos] == commonval:
			filtered_data.append(d)

	print("OxygenFilteredData:", filtered_data, bitpos, commonval)

	if len(filtered_data) == 1:
		print("OxygenResult:", filtered_data[0], int(filtered_data[0],2))
		return filtered_data
	else:
		oxygenrating(filtered_data,bitpos+1)

def co2rating(data,bitpos):

	#starting with the first bit
	filtered_data = []

	column = [d[bitpos] for d in data]
	commonval = find_leastcommon_value(column)

	for d in data:
		if d[bitpos] == commonval:
			filtered_data.append(d)

	print("Co2FilteredData:", filtered_data, bitpos, commonval)

	if len(filtered_data) == 1:
		print("Co2Result:", filtered_data[0], int(filtered_data[0],2))
		return filtered_data
	else:
		co2rating(filtered_data,bitpos+1)

class Submarine:

	hpos = 0
	depth = 0
	aim = 0

print("Hello, World!")

# Open a file
#fo = open("input/short.txt", "r+")
fo = open("input/data.txt", "r+")
print ("Name of the file: ", fo.name)

lines = fo.readlines()
print("# of lines:", len(lines))


lines = [line.strip() for line in lines]

submarine = Submarine()

oxygenrating(lines,0)
co2rating(lines,0)


#powerconsumption = calc_power(lines)
#print(powerconsumption)

#calc_oxygen(lines)
#calc_co2(lines)

"""
for line in lines:

	#submarine.navigate(line[0],int(line[1]))
	print(line.strip(),int(line.strip(),2))
	occur_i = line.strip().split().count('1')
	occur_o = line.strip().split().count('0')
"""
	




# Close opened file
fo.close()
