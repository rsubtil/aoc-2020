#!/usr/bin/env python3

# Get the input file
with open('input', 'r') as input_file:
	input_list = [line.strip() for line in input_file.readlines()]

answer_p1 = 0
answer_p2 = 0

# Pre-process our input
answers_list = []
curr_line = ""
for line in input_list:
	# If we have a empty line, then the info about this answer is over
	if line == '':
		answers_list.append(curr_line)
		curr_line = ''
	else:
		# If this is the first line of info, curr_line is empty
		if curr_line == '':
			curr_line = line
		# Otherwire, append info with a space
		else:
			curr_line = f"{curr_line} {line}"

# Don't forget to add that last info, as the file doesn't end with a new-line
answers_list.append(curr_line)

print(answers_list)

# We now have a pre-formatted list of answers, where each index contains all the answers from a group, and separated by ' '.


# Implement the algorithm for both parts

print("-------------\nFirst and second part...\n-------------\n")
for group in answers_list:
	print(f"Group: '{group}'")
	answer_map = {}
	num_persons = 0
	for person in group.split(' '):
		num_persons = num_persons + 1
		print(f"Person: '{person}'")
		for question in person:
			if not question in answer_map.keys():
				answer_map[question] = 1
			else:
				answer_map[question] = answer_map[question] + 1
	
	print(answer_map)
	answer_p1 = answer_p1 + len(answer_map.keys())
	for key in answer_map.keys():
		if answer_map[key] == num_persons:
			answer_p2 = answer_p2 + 1

# Final output
print('\n---------------')
print(f'Final answer (part 1): "{answer_p1}"')
print(f'Final answer (part 2): "{answer_p2}"')