#!/usr/bin/env python3

# Get the input file
with open('input', 'r') as input_file:
	input_list = [line.strip() for line in input_file.readlines()]

answer_p1 = 0
answer_p2 = 1

# Implement the algorithm for part 1

print("-------------\nFirst part...\n-------------\n")
# Moving pattern, Y-axis and X-axis
pattern = (1, 3)

# Get the length of a single line
line_len = len(input_list[0])
delta_x = 0
for i in range(pattern[0], len(input_list), pattern[0]):
	# Compute our movement in the X component
	delta_x = delta_x + pattern[1]
	delta_x = delta_x % line_len

	# See if there's any intersection with a tree on that position
	if input_list[i][delta_x] == '#':
		answer_p1 = answer_p1 + 1

# Implement the algorithm for part 2

print("\n--------------\nSecond part...\n--------------\n")
# Moving pattern, Y-axis and X-axis
patterns = [
	(1, 1),
	(1, 3),
	(1, 5),
	(1, 7),
	(2, 1)
]

# Get the length of a single line
line_len = len(input_list[0])
for pattern in patterns:
	delta_x = 0
	num_trees = 0
	for i in range(pattern[0], len(input_list), pattern[0]):
		# Compute our movement in the X component
		delta_x = delta_x + pattern[1]
		delta_x = delta_x % line_len

		# See if there's any intersection with a tree on that position
		if input_list[i][delta_x] == '#':
			num_trees = num_trees + 1
	
	print("Pattern:", pattern)
	print("Collisions:", num_trees)
	answer_p2 = answer_p2 * num_trees

# Final output
print('\n---------------')
print(f'Final answer (part 1): "{answer_p1}"')
print(f'Final answer (part 2): "{answer_p2}"')