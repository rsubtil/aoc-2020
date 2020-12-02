#!/usr/bin/env python3

# Get the input file
# Get the input file
with open('input', 'r') as input_file:
	input_list = [int(i) for i in input_file.readlines()]

answer_p1 = None
answer_p2 = None

# Implement the algorithm for part 1

print("-------------\nFirst part...\n-------------\n")
for i1 in range(len(input_list) - 1):
	for i2 in range(i1 + 1, len(input_list)):
		# Sum the numbers; if it's equal to 2020, we have our answer
		if input_list[i1] + input_list[i2] == 2020:
			print(f"Found the numbers! {input_list[i1]} (line {i1 + 1}) and {input_list[i2]} (line {i2 + 1})")
			answer_p1 = input_list[i1] * input_list[i2]
			break

# Implement the algorithm for part 2

print("\n--------------\nSecond part...\n--------------\n")
for i1 in range(len(input_list) - 2):
	for i2 in range(i1 + 1, len(input_list) - 1):
		for i3 in range(i2 + 1, len(input_list)):
			# Sum the numbers; if it's equal to 2020, we have our answer
			if input_list[i1] + input_list[i2] + input_list[i3] == 2020:
				print(f"Found the numbers! {input_list[i1]} (line {i1 + 1}), {input_list[i2]} (line {i2 + 1}) and {input_list[i3]} (line {i3 + 1})")
				answer_p2 = input_list[i1] * input_list[i2] * input_list[i3]
				break

# Final output
print('\n---------------')
print(f'Final answer (part 1): "{answer_p1}"')
print(f'Final answer (part 2): "{answer_p2}"')