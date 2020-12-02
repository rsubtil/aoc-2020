#!/usr/bin/env python3

# Get the input file
with open('input', 'r') as input_file:
	input_list = input_file.readlines()

answer_p1 = 0
answer_p2 = 0

# Implement the algorithm for part 1

print("-------------\nFirst part...\n-------------\n")
for line in input_list:
	# Pre-processing the words
	range, character, password = line.strip().split(' ')

	# Range is in the form "1-3"; separate by the '-'
	min, max = [int(i) for i in range.split('-')]

	# Character is in the form 'v:'; cut the unneeded ':'
	character = character.replace(':', '')

	# Password needs no processing; it's ready to go
	# And we're ready to process
	if min <= password.count(character) <= max:
		answer_p1 = answer_p1 + 1

# Implement the algorithm for part 2

print("\n--------------\nSecond part...\n--------------\n")
for line in input_list:
	# Pre-processing the words
	positions, character, password = line.strip().split(' ')

	# Positions is in the form "1-3"; separate by the '-', and decrement already for later usage
	idx1, idx2 = [int(i) - 1 for i in positions.split('-')]

	# Character is in the form 'v:;, cut the unneeded ':'
	character = character.replace(':', '')

	# Password needs no processing; it's ready to go
	# And we're ready to process
	if bool(password[idx1] == character) ^ bool(password[idx2] == character):
		answer_p2 = answer_p2 + 1

# Final output
print('\n---------------')
print(f'Final answer (part 1): "{answer_p1}"')
print(f'Final answer (part 2): "{answer_p2}"')