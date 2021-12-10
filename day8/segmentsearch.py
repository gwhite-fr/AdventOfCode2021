from collections import defaultdict
from collections import OrderedDict

def sigma(first, last, const):
    sum = 0
    for i in range(first, last + 1):
        sum += const * i
    return sum


def determine_mapping(signal_pattern):

	"""
	we need to start with two known values
		abcdefg

	1	  c  f 
	4    bcd f
	7   a c  f
	8	abcdefg

		xxxx x 

	1+4  bcd f
	1+7 a c  f
	4+7 abcd f


	"""
	print("signal pattern:", signal_pattern)

	known_digits = OrderedDict.fromkeys('1478')
	sixlength = []
	fivelength = []

	for signal in signal_pattern:

		#Numbers Left: 9 8 7 6 5 4 3 2 1 0
		n = len(signal)
		digit = None

		if n == 7:
			#this is an 8
			digit = '8'

		#Numbers Left: 9 7 6 5 4 3 2 1 0
		elif n == 4:
			#this is a 4
			digit = '4'

		#Numbers Left: 9 7 6 5 3 2 1 0
		elif n == 2:
			#this is a 1
			digit = '1'

		#Numbers Left: 9 7 6 5 3 2 0
		elif n == 3:
			#this is a 7
			digit = '7'

		elif n == 6:
			sixlength.append(signal)
		elif n == 5:
			fivelength.append(signal)

		if not digit:

			print("not enough information")
		
		else:

			known_digits[digit] = set(signal)

	print("KnownDigits", known_digits)
	
	mapping = OrderedDict.fromkeys('abcdefg')

	#lets get started

	#first, if we have any two of these digits [1, 4, 7]
	#DETERMINE A
	a =list(known_digits['7'] - known_digits['1'])[0] #this is goood!

	##DETERMINE C and F
	cf = list(known_digits['1']) #to narrow down again, we know that 2/3 the three 6-length have c but all three have f
	#0 abc efg -- n=6
	#6 ab defg -- n=6
	#9 abcd fg -- n=6
	c = None
	f = None
	count = 0
	for signal in sixlength:
		if cf[0] in signal:
			count += 1
	if count == 3:
		f = cf[0]
		c = cf[1]
	else:
		f = cf[1]
		c = cf[0]

	#Now we know, a c f

	##DETERMINE B AND D #to narrow down again, we know that 2/3 the three 6-length have d but all three have b
	bd = list(known_digits['4'] - known_digits['7'])
	b = None
	d = None
	count = 0
	for signal in sixlength:
		if bd[0] in signal:
			count += 1
	if count == 3:
		b = bd[0]
		d = bd[1]
	else:
		b = bd[1]
		d = bd[0]


	

	x = known_digits['8'] - known_digits['4'] - known_digits['7'] - known_digits['1']

	print('cf', cf)
	print('a', a)
	print('bd', bd)
	#print('e', e)
	print('x', x)

	mapping['a'] = a
	mapping['b'] = b
	mapping['c'] = c
	mapping['d'] = d
	mapping['f'] = f

	current_known_values = [mapping[xchar] for xchar in mapping.keys() if mapping[xchar] != None]
	#print("currently known:", current_known_values)

	##
	#2 a cde g -- n=5
	#3 a cd fg -- n=5
	#5 ab d fg -- n=5
	reduced_fivelength = fivelength[:]
	#print("BEGIN FIVER STUFF")
	reduced_fiver0 = list(set([xchar for xchar in fivelength[0]]) - set(current_known_values))
	reduced_fiver1 = list(set([xchar for xchar in fivelength[1]]) - set(current_known_values))
	reduced_fiver2 = list(set([xchar for xchar in fivelength[2]]) - set(current_known_values))
	twosignal = [signal for signal in [reduced_fiver0,reduced_fiver1,reduced_fiver2] if len(signal) == 2][0]
	nottwosignal = [signal for signal in [reduced_fiver0,reduced_fiver1,reduced_fiver2] if len(signal) == 1][0]
	e = list(set(twosignal) - set(nottwosignal))[0]
	mapping['e'] = e
	#print("e:", e)
	fiver_intersect_01 = set(fivelength[0]).intersection(fivelength[1])
	fiver_intersect_02 = set(fivelength[0]).intersection(fivelength[2])
	#print(fivelength)
	#print("Intersect01:", fiver_intersect_01, "--", len(fiver_intersect_01))
	#print("Intersect02:", fiver_intersect_02, "--", len(fiver_intersect_02))
	#print("END FIVER STUFF")

	current_known_values = [mapping[xchar] for xchar in mapping.keys() if mapping[xchar] != None]
	#print("currently known:", current_known_values)

	g = list(set(known_digits['8']) - set(current_known_values))[0]
	mapping['g'] = g

	#print(mapping)

	#print("Can't solve this!! Giving Up")
	#return -1

	#we should have two chars now that will be c and f
	print("mapping complete")
	return mapping


def decode_with_mapping(entries):

	print("entries:", entries)
	results = []

	digit_codes = OrderedDict.fromkeys('0123456789')
	for digit in digit_codes.keys():
		digit_codes[digit] = 0

	#0 abc efg -- n=6
	#1   c  f  -- n=2
	#2 a cde g -- n=5
	#3 a cd fg -- n=5
	#4  bcd f  -- n=4
	#5 ab d fg -- n=5
	#6 ab defg -- n=6
	#7 a c  f  -- n=3
	#8 abcdefg -- n=7
	#9 abcd fg -- n=6
	
	for entry in entries:

		signal_patterns = entry[0].split(" ")
		signal_output = entry[1].split(" ")

		mapping = determine_mapping(signal_patterns)
		inv_mapping = {v: k for k, v in mapping.items()}
		print("mapping:", mapping)
		print("mapping:", inv_mapping)

		true_signals = []
		for signal in signal_output:
			true_signal = "".join([inv_mapping[signalchar] for signalchar in signal])
			true_signals.append(true_signal)

		print("FalseOutputSignals:", signal_output)
		print("TrueOutputSignals:", true_signals)


		result = ''
		for signal in true_signals:

			#Numbers Left: 9 8 7 6 5 4 3 2 1 0
			n = len(signal)
			print(n)
			digit = None

			if n == 7:
				#this is an 8
				digit = '8'

			#Numbers Left: 9 7 6 5 4 3 2 1 0
			elif n == 4:
				#this is a 4
				digit = '4'

			#Numbers Left: 9 7 6 5 3 2 1 0
			elif n == 2:
				#this is a 1
				digit = '1'

			#Numbers Left: 9 7 6 5 3 2 0
			elif n == 3:
				#this is a 7
				digit = '7'

			#Numbers Left: 9 6 5 3 2 0
			elif n == 5:
				#this is either a 2,3 or 5
				#2 a cde g -- n=5
				#3 a cd fg -- n=5
				#5 ab d fg -- n=5

				if 'c' in signal and 'f' in signal:
					digit = '3'
				elif 'a' in signal and 'c' in signal:
					digit = '2'
				else:
					digit = '5'
				
			#Numbers Left: 9 6 0
			else:
				#n must be 6 and that means
				#this is either a 0,6 or 9

				#0 abc efg
				#6 ab defg
				#9 abcd fg

				if 'c' in signal and 'd' not in signal:
					digit = '0'
				elif 'e' in signal and 'c' not in signal:
					digit = '6'
				else:
					digit = '9'

			print("signal:", signal, " --> ", digit)
			result += digit
			
			#digit_codes[digit] += 1
		#print("i:",i)
			print("result:", result)
		results.append(result)

	print(digit_codes)
	print("Results:",results)
	return results
	#print(sum([digit_codes['1'],digit_codes['4'],digit_codes['7'],digit_codes['8']]))
	

def decode_signal(entries):

	digit_codes = OrderedDict.fromkeys('0123456789')
	for digit in digit_codes.keys():
		digit_codes[digit] = 0

	#0 abc efg -- n=6
	#1   c  f  -- n=2
	#2 a cde g -- n=5
	#3 a cd fg -- n=5
	#4  bcd f  -- n=4
	#5 ab d fg -- n=5
	#6 ab defg -- n=6
	#7 a c  f  -- n=3
	#8 abcdefg -- n=7
	#9 abcd fg -- n=6
	i=0
	for entry in entries:

		signal_patterns = entry[0].split(" ")
		signal_output = entry[1].split(" ")

		for signal in signal_patterns:

			#Numbers Left: 9 8 7 6 5 4 3 2 1 0
			n = len(signal)
			print(n)
			digit = None

			if n == 7:
				#this is an 8
				digit = '8'

			#Numbers Left: 9 7 6 5 4 3 2 1 0
			elif n == 4:
				#this is a 4
				digit = '4'

			#Numbers Left: 9 7 6 5 3 2 1 0
			elif n == 2:
				#this is a 1
				digit = '1'

			#Numbers Left: 9 7 6 5 3 2 0
			elif n == 3:
				#this is a 7
				digit = '7'

			#Numbers Left: 9 6 5 3 2 0
			elif n == 5:
				#this is either a 2,3 or 5
				if 'c' in signal and 'f' in signal:
					digit = '2'
				elif 'a' in signal and 'c' in signal:
					digit = '3'
				else:
					digit = '5'
				
			#Numbers Left: 9 6 0
			else:
				#n must be 6 and that means
				#this is either a 0,6 or 9

				#0 abc efg
				#6 ab defg
				#9 abcd fg

				if 'c' in signal and 'd' not in signal:
					digit = '0'
				elif 'e' in signal and 'c' not in signal:
					digit = '6'
				else:
					digit = '9'

			print("DecodedDigit:", signal, "-->", digit)


		print("OutputSignals:", signal_output)
		for signal in signal_output:

			#Numbers Left: 9 8 7 6 5 4 3 2 1 0
			n = len(signal)
			print(n)
			digit = None

			if n == 7:
				#this is an 8
				digit = '8'

			#Numbers Left: 9 7 6 5 4 3 2 1 0
			elif n == 4:
				#this is a 4
				digit = '4'

			#Numbers Left: 9 7 6 5 3 2 1 0
			elif n == 2:
				#this is a 1
				digit = '1'

			#Numbers Left: 9 7 6 5 3 2 0
			elif n == 3:
				#this is a 7
				digit = '7'

			#Numbers Left: 9 6 5 3 2 0
			elif n == 5:
				#this is either a 2,3 or 5
				if 'c' in signal and 'f' in signal:
					digit = '2'
				elif 'a' in signal and 'c' in signal:
					digit = '3'
				else:
					digit = '5'
				
			#Numbers Left: 9 6 0
			else:
				#n must be 6 and that means
				#this is either a 0,6 or 9

				#0 abc efg
				#6 ab defg
				#9 abcd fg

				if 'c' in signal and 'd' not in signal:
					digit = '0'
				elif 'e' in signal and 'c' not in signal:
					digit = '6'
				else:
					digit = '9'

			
			digit_codes[digit] += 1
		print("i:",i)
		i+=1

	print(digit_codes)
	print(sum([digit_codes['1'],digit_codes['4'],digit_codes['7'],digit_codes['8']]))


fo = open("input/data.txt", "r+")
print ("Name of the file: ", fo.name)

lines = fo.readlines()
print("# of lines:", len(lines))

entries = []
for line in lines:
	pattern,output = line.split("|")
	entries.append([pattern.strip(),output.strip()])


print(entries)
#decode_signal(entries)
result = decode_with_mapping(entries)
sumtotal = sum([int(x) for x in result])
print("SumTotal:", sumtotal)

fo.close()

