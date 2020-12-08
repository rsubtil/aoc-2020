#!/usr/bin/env python3

# Get the input file
with open('input', 'r') as input_file:
	input_list = [line.strip() for line in input_file.readlines()]

answer_p1 = None
answer_p2 = None

pc = 0
acc = 0

# This list contains PC values that we're run; we use this to detect a loop
pc_values = []

# Implement the algorithm for part 1

def execute():
	global pc
	global acc
	global pc_values
	while True:
		if pc >= len(input_list):
			break
		opcode, value = input_list[pc].split(' ')
		if pc in pc_values:
			break
		pc_values.append(pc)
		print("Opcode:", opcode)
		if opcode == 'nop':
			pc += 1
		elif opcode == 'acc':
			pc += 1
			acc += int(value)
		elif opcode == 'jmp':
			pc += int(value)

print("-------------\nFirst part...\n-------------\n")
execute()
answer_p1 = acc

# Implement the algorithm for part 2

def reset():
	global pc
	global acc
	global pc_values
	pc = 0
	acc = 0
	pc_values = []

print("\n--------------\nSecond part...\n--------------\n")
for idx, line in enumerate(input_list):
	# Get the current opcode
	opcode, value = line.split(' ')
	print(line)

	# Switch them
	if opcode == 'nop':
		opcode = 'jmp'
	elif opcode == 'jmp':
		opcode = 'nop'
	else:
		# If we're here, then opcode = 'acc', which we don't touch
		continue

	print("Modified to", ' '.join([opcode, value]))
	# Modify the base program, reser variables and execute
	input_list[idx] = ' '.join([opcode, value])
	reset()
	execute()

	# We only have the answer if the program has finished
	if pc >= len(input_list):
		answer_p2 = acc
		break
	else:
		# Otherwise, reset our modification to the original value
		if opcode == 'nop':
			opcode = 'jmp'
		elif opcode == 'jmp':
			opcode = 'nop'
		input_list[idx] = ' '.join([opcode, value])

# Final output
print('\n---------------')
print(f'Final answer (part 1): "{answer_p1}"')
print(f'Final answer (part 2): "{answer_p2}"')