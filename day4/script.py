#!/usr/bin/env python3

# Get the input file
with open('input', 'r') as input_file:
	input_list = [line.strip() for line in input_file.readlines()]

answer_p1 = 0
answer_p2 = 0

# Pre-process our input
passport_list = []
curr_line = ""
for line in input_list:
	# If we have a empty line, then the info about this passport is over
	if line == '':
		passport_list.append(curr_line)
		curr_line = ''
	else:
		# If this is the first line of info, curr_line is empty
		if curr_line == '':
			curr_line = line
		# Otherwire, append info with a space
		else:
			curr_line = f"{curr_line} {line}"

# Don't forget to add that last info, as the file doesn't end with a new-line
passport_list.append(curr_line)

# We now have a pre-formatted list of passports, where each index contains all the info neatly formatted for us to use

# Implement a "mapping of found keys and values"
keys = (
	'byr',
	'iyr',
	'eyr',
	'hgt',
	'hcl',
	'ecl',
	'pid',
	#'cid', (optional for part 1)
)

# Helper functions
def make_map():
	map = {}
	for key in keys:
		map[key] = False
	
	return map

def is_passport_valid(map):
	for line in map:
		if map[line] == False:
			print(f"\tMissing necessary key \"{line}\"")
			return False
	
	print("\tPassport is valid")
	return True


# Implement the algorithm for part 1

print("-------------\nFirst part...\n-------------\n")

for passport in passport_list:
	# Create an empty mapping
	print(f"Passport info: \"{passport}\"")
	map = make_map()

	# Split the info from the ' ' char
	for info in passport.split(' '):
		# Split the info through the `:` char (we're only interested in the key)
		key = info.split(':')[0]

		print(f"\tKey found: \"{key}\"")
		# Key exists, so, mark it
		map[key] = True
	
	# If passport is valid, increment the num of answer
	if is_passport_valid(map):
		answer_p1 = answer_p1 + 1


# Implement the algorithm for part 2

def validate_key(key, val):
	if key == 'byr':
		# Birth Year
		return 1920 <= int(val) <= 2002
	elif key == 'iyr':
		# Issue Year
		return 2010 <= int(val) <= 2020
	elif key == 'eyr':
		# Expiration Year
		return 2020 <= int(val) <= 2030
	elif key == 'hgt':
		# Height
		unit = val[-2:]
		if unit == 'cm':
			return 150 <= int(val[0:-2]) <= 193
		elif unit == 'in':
			return 59 <= int(val[0:-2]) <= 76
		else:
			return False
	elif key == 'hcl':
		return val[0] == '#' and len(val) == 7 and (char in "0123456789abcdef" for char in val[1:])
	elif key == 'ecl':
		return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	elif key == 'pid':
		return len(val) == 9 and val.isnumeric()

print("\n--------------\nSecond part...\n--------------\n")
for passport in passport_list:
	# Create an empty mapping
	print(f"Passport info: \"{passport}\"")
	map = make_map()

	# Split the info from the ' ' char
	for info in passport.split(' '):
		# Split the info through the `:` char
		key, val = info.split(':')

		print(f"\tKey-value pair found: \"{key}:{val}\"")
		# Key exists, so, mark it
		map[key] = validate_key(key, val)
	
	# If passport is valid, increment the num of answer
	if is_passport_valid(map):
		answer_p2 = answer_p2 + 1

# Final output
print('\n---------------')
print(f'Final answer (part 1): "{answer_p1}"')
print(f'Final answer (part 2): "{answer_p2}"')