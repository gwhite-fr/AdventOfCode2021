#!/usr/bin/env python3

class BingoCard:

	gridsize = 5
	card_numbers = []
	card_markers = []
	marker_tally = 0
	winner = False

	def __init__(self,gridsize,numbers):

		self.gridsize = gridsize
		self.card_numbers = numbers
		self.card_markers = []
		
		for i in range(0,self.gridsize):
			current_row = []
			for j in range(0,self.gridsize):
				current_row.append(-1)
			self.card_markers.append(current_row)

	def calc_unmarked(self):

		total = 0
		for i in range(0,self.gridsize):
			for j in range(0, self.gridsize):
				if self.card_markers[i][j] == -1:
					total += int(self.card_numbers[i][j])
					print(total)

		return total

	def eval_number(self,num):

		if not self.winner:

			row = None
			col = None

			has_number = False

			for i in range(0,self.gridsize):
				for j in range(0, self.gridsize):
					if self.card_numbers[i][j] == num:
						row = i
						col = j
						has_number = True

			if has_number:
				winner = self.mark_number(row,col)
				if winner:
					self.winner = True
					return True

			else:
				return False

		else:
			return False

	def mark_number(self,row,col):

		self.card_markers[row][col] = 1
		self.marker_tally += 1
		
		if self.marker_tally >= self.gridsize:
			
			found_winner = self.check_for_win()
			
			if found_winner:
				return True
			else:
				return False

	def check_for_win(self):

		for i in range(0,self.gridsize):
			if self.check_row_win(i):
				return True
			elif self.check_col_win(i):	
				return True
			
		return False
		
	def check_row_win(self,i):

		row = self.card_markers[i]
		
		if sum(row) == self.gridsize:
			return True
		else:
			return False

	def check_col_win(self,i):

		col = [row[i] for row in self.card_markers]
		if sum(col) == self.gridsize:
			return True
		else:
			return False

	def check_diag_win(self):

		updiag = True
		downdiag = True

		for i in range(0,self.gridsize):

			if self.card_markers[i][i] == -1:
				downdiag = False
			
			if not all([self.card_markers[0][4],self.card_markers[1][3],self.card_markers[2][2],self.card_markers[3][1],self.card_markers[4][0]]):
				updiag = False

		if downdiag:
			return True

	def print_card(self):

		printstring = ""

		for i in range(0,self.gridsize):
			
			for j in range(0, self.gridsize):

				printstring += " " + str(self.card_numbers[i][j]) + " "

			printstring += "\n"

		print(printstring)
		print(self.card_numbers)

	def print_markers(self):

		marker_string = ""
		for i in range(0,self.gridsize):
			for j in range(0,self.gridsize):
				if self.card_markers[i][j] == 1:
					marker_string += " X "
				else:
					marker_string += " O "
			marker_string += "\n"

		print(marker_string)

def ingest_bingo_cards(lines):

	bingo_cards_data = []

	current_card = []
	for line in lines:

		if len(line) == 0:
			if len(current_card) > 0:
					bingo_cards_data.append(BingoCard(5,current_card))
					current_card = []
		else:
			current_card.append(line.split(" "))

	bingo_cards_data.append(BingoCard(5,current_card))
	return bingo_cards_data

def letsplay_bingo(numbers,cards):

	winner_list = []
	winner_indices = []
	i = 0

	indexed_cards = []
	for i in range(0,len(cards)):
			indexed_cards.append([cards[i],i])	

	#for each number
	for bingonumber in numbers:
		
		#go through all cards and mark numbers
		for card in indexed_cards:

			winner = card[0].eval_number(bingonumber)

			if winner:
				if card[1] not in winner_indices:
						print("We have a winner!")
						winner_list.append([card[0],bingonumber])
						winner_indices.append(card[1])
			
			else:
				print("no wins")


	print(len(winner_list))
	print("Cards:", len(cards))
	last_winner_card = winner_list[-1][0]
	last_winner_num = winner_list[-1][1]
	last_winner_card.print_card()
	last_winner_card.print_markers()
	unmarked_total = last_winner_card.calc_unmarked()
	final_result = unmarked_total*int(last_winner_num)
	print("Final:",final_result)



print("Hello, World!")

# Open a file
fo = open("input/data.txt", "r+")
print ("Name of the file: ", fo.name)

lines = fo.readlines()
print("# of lines:", len(lines))

lines = [line.strip() for line in lines]

bingo_numbers = lines[0].strip().split(",")
print(bingo_numbers)
bingo_cards = ingest_bingo_cards(lines[1:])

letsplay_bingo(bingo_numbers,bingo_cards)

#for card in bingo_cards:
#	card.print_card()




# Close opened file
fo.close()