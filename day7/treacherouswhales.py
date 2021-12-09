from collections import defaultdict

def sigma(first, last, const):
    sum = 0
    for i in range(first, last + 1):
        sum += const * i
    return sum


def find_most_efficient_position_part2(start_positions):

	#We have a list of each starting position

	#We should calculate the cost of each position
	#Let's get all the unique positions
	start_position_range = range(min(start_positions),max(start_positions))
	position_cost = defaultdict()
	for pos in start_position_range:
		position_cost[pos] = 0	
	
	#print("UniquePositions:", position_cost)

	#We are going to sum up the cost of each crab's move to X pos
	for tgtpos in position_cost.keys():

		print(tgtpos)

		for startpos in start_positions:
			
			d = sigma(0,abs(startpos-tgtpos),1)
			cost = position_cost[tgtpos]
			position_cost[tgtpos] = cost + d

	print(position_cost)
	
	inv_cost = defaultdict()
	#invert the dict to grab the lowest cost
	for key,val in position_cost.items():
		print(key,val)
		inv_cost[val] = key

	min_key = min(inv_cost.keys())
	return (min_key,inv_cost[min_key])



def find_most_efficient_position(start_positions):

	#We have a list of each starting position

	#We should calculate the cost of each position
	#Let's get all the unique positions
	position_cost = defaultdict()
	for pos in list(set(start_positions)):
		position_cost[pos] = 0	
	
	print("UniquePositions:", position_cost)

	#We are going to sum up the cost of each crab's move to X pos
	for tgtpos in position_cost.keys():

		for startpos in start_positions:
		
			d = abs(startpos-tgtpos)
			cost = position_cost[tgtpos]
			position_cost[tgtpos] = cost + d

	print(position_cost)
	
	inv_cost = defaultdict()
	#invert the dict to grab the lowest cost
	for key,val in position_cost.items():
		print(key,val)
		inv_cost[val] = key

	min_key = min(inv_cost.keys())
	return (min_key,inv_cost[min_key])


fo = open("input/data.txt", "r+")
print ("Name of the file: ", fo.name)

lines = fo.readlines()
print("# of lines:", len(lines))

start_positions = [int(line) for line in lines[0].split(",")]
print(start_positions)
#result1 = find_most_efficient_position(start_positions)
result2 = find_most_efficient_position_part2(start_positions)

print("Lowest Cost Position:", result2[0], "-->", result2[1])


fo.close()