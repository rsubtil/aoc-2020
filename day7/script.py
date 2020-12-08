#!/usr/bin/env python3

# Get the input file
with open('input', 'r') as input_file:
	input_list = [line.strip() for line in input_file.readlines()]

answer_p1 = 0
answer_p2 = None

bag_list = {}

# Pre-process our input to create a list of bags
for line in input_list:
	key_bag_str, val_bag_str = line.split(' contain ')

	# key_bag_str has our main color; remove the unneeded ' bags' portion
	key_bag = key_bag_str.replace(' bags', '')

	# val_bag_str has our accepeted colors; it can be none, one, or many.
	# Handle these cases properly.

	# If this doesn't have any bags, save it prematurely
	if 'no other' in val_bag_str:
		bag_list[key_bag] = []
		continue
	
	# Iterate through the list of present bags.
	# Don't forget to remove the final dot '.' from the string
	val_bag = []
	for bag_info in val_bag_str[:-1].split(', '):
		bag_quantity = bag_info.split(' ')[0]
		bag_color = ' '.join(bag_info.split(' ')[1:3])
		val_bag.append((bag_quantity, bag_color))
	
	bag_list[key_bag] = val_bag

print("Final list of bags:", bag_list)

def visit_part1(bag_key):
	for bag_val in bag_list[bag_key]:
		if bag_val[1] == 'shiny gold':
			return 1
		else:
			if(visit_part1(bag_val[1])): return 1

	return 0

def visit_part2(bag_key):
	sum = 0
	for bag_val in bag_list[bag_key]:
		bag_quantity = int(bag_val[0])
		sum = sum + bag_quantity + bag_quantity * (visit_part2(bag_val[1]))

	return sum

# Implement the algorithm for part 1

print("-------------\nFirst part...\n-------------\n")
for bag_key in bag_list.keys():
	answer_p1 = answer_p1 + visit_part1(bag_key)

# Implement the algorithm for part 2

print("\n--------------\nSecond part...\n--------------\n")
answer_p2 = visit_part2('shiny gold')

# Final output
print('\n---------------')
print(f'Final answer (part 1): "{answer_p1}"')
print(f'Final answer (part 2): "{answer_p2}"')