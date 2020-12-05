#!/usr/bin/env python3

# Get the input file
with open('input', 'r') as input_file:
	input_list = input_file.readlines()

answer_p1 = 0
answer_p2 = None

# Const info
num_rows = 128
num_columns = 8

# Mapping of existing places
seat_map = {}
for i in range(num_rows):
	for j in range(num_columns):
		seat_map[i * num_columns + j] = True

# Implement the algorithm for part 1

print("-------------\nFirst part...\n-------------\n")

for line in input_list:
	lower_r = 0
	upper_r = num_rows - 1
	lower_c = 0
	upper_c = num_columns - 1

	r = 0
	c = 0

	# Determine row
	for ch in line[0:7]:
		if ch == 'F':
			upper_r = (upper_r + 1 - lower_r) / 2 - 1 + lower_r
			print("Char was F")
		elif ch == 'B':
			lower_r = (upper_r + 1 - lower_r) / 2 + lower_r
			print("Char was B")
		print(f"Range: {lower_r}-{upper_r}")
	
	# Ensure the ranges are equal
	if upper_r != lower_r:
		raise Exception('Upper and lower limits are different, this shouldn\'t happen!')

	r = int(upper_r)
	print("Row is", r)

	# Determine column
	for ch in line[7:10]:
		if ch == 'L':
			upper_c = (upper_c + 1 - lower_c) / 2 - 1 + lower_c
			print("Char was L")
		elif ch == 'R':
			lower_c = (upper_c + 1 - lower_c) / 2 + lower_c
			print("Char was R")
		print(f"Range: {lower_c}-{upper_c}")
	
	# Ensure the ranges are equal
	if upper_c != lower_c:
		raise Exception('Upper and lower limits are different, this shouldn\'t happen!')

	c = int(upper_c)
	print("Column is", c)

	seat_id = int(r * 8 + c)
	print("Seat ID is", seat_id)
	# Remove this from mapping, for part 2
	seat_map.pop(seat_id)
	answer_p1 = max(answer_p1, seat_id)

# Implement the algorithm for part 2

print("\n--------------\nSecond part...\n--------------\n")
# We "leeched" of on part 1, so part 2 is precalculated:
# All we need to find is the entrance on the `seat_map` that is not contiguous
# (because there are whole rows that are unoccupied)
seat_list = list(seat_map)
for i in range(1, len(seat_list) - 1):
	if seat_list[i-1] + 1 != seat_list[i] \
	and seat_list[i] != seat_list[i+1] - 1:
		answer_p2 = seat_list[i]
		break


# Final output
print('\n---------------')
print(f'Final answer (part 1): "{answer_p1}"')
print(f'Final answer (part 2): "{answer_p2}"')