from collections import defaultdict

class Lanternfish:

	timer = None
	initialtimer = None

	def __init__(self,timerstart):

		self.timer = timerstart
		self.initialtimer = timerstart

	def tick(self):

		if self.timer == 0:
			self.timer = 6
			return 1

		else:
			self.timer -= 1
			return 0

	def calc_offspring(self,ndays):

		#after this fish gets to 0, it will spawn a new fish every 6 days
		#256 days - 3 left on timer leaves us 253 days of spawning
		#this fish will spawn 253 % 7 times

		days_subtimer = ndays - self.initialtimer
		print("days_subtimer:", days_subtimer)
		
		#this lanternfish will spawn nspawn times
		nspawn = days_subtimer // 7
		print("# of Spawns:", nspawn)

		result = 2 ** nspawn
		print("final count:",result)


		"""
		3
		2
		1
		0	
		6	8
		5	7
		4	6
		3	5
		2	4
		1	3
		0	2
		6	1	8
		5	0	7
		4	6	6	8
		3	5	5	7
		2	4	4	6
		1	3	3	5
		0	2	2	4
		6	1	1	3	8


		"""


def fast_lanternfish(numbers, ndays):

	#init to 0
	fish = [0 for i in range(9)]

	#set each element to account for all fish of that timer #
	for timer in numbers:
		print(timer)
		fish[timer] += 1
	
	#for each day
	for n in range(ndays):
		#new fish time
		spawn = fish[0]
		fish[:] = fish[1:] + [spawn]
		fish[6] += spawn

	print(fish)
	return sum(fish)


def simulate_lanternfish(fish,ndays):

	existing_fish = []
	#Give a list of initial timers, spawn a lanternfish for each timer
	for t in fish:
		lanternfish = Lanternfish(int(t))
		existing_fish.append(lanternfish)

	#We have our initial fish in existing fish, lets simulate
	current_day = 0
	max_day = ndays

	lastday = False
	while not lastday:

		print("Day ", current_day, " Fish Count:", len(existing_fish))

		if current_day == max_day:
			lastday = True
			break

		for i in range(0,len(existing_fish)):
			spawncheck = existing_fish[i].tick()
			if spawncheck:
				existing_fish.append(Lanternfish(8))
		
		else:
			current_day += 1

	print("There are:", len(existing_fish), "after 80 days")

fo = open("input/data.txt", "r+")
print ("Name of the file: ", fo.name)

lines = fo.readlines()
print("# of lines:", len(lines))

ogfish = [line.strip().split(",") for line in lines][0]
ogfish = [int(x) for x in ogfish]
#simulate_lanternfish(ogfish)

"""
fishspawnmap = defaultdict()

for i in range(0,6):
	spawncount = simulate_lanternfish([i])
	fishspawnmap[i] = spawncount

print(fishspawnmap)
"""

#result = day_six(ogfish,256)
result = fast_lanternfish(ogfish,256)
print(result)

fo.close()