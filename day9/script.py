#!/usr/bin/env python3

# Get the input file
with open('input', 'r') as input_file:
	input_list = [int(line) for line in input_file.readlines()]

answer_p1 = None
answer_p2 = None

stride = 25

# Implement the algorithm for part 1

print("-------------\nFirst part...\n-------------\n")

# We made this a function to exit immediately from three loops
def part_1():
	for idx, number in enumerate(input_list[stride:]):
		idx += stride
		# Loop on the 25 previous numbers
		print("Idx:", idx)
		print("Number:", number)
		found = False
		for i1, n1 in enumerate(input_list[idx-stride:idx-1]):
			i1 += idx - stride
			print("I1:", i1)
			print("N1:", n1)
			if found: break
			for n2 in input_list[i1+1:idx]:
				print("N2:", n2)
				if n1 + n2 == number:
					found = True
					break
		
		if not found:
			return number

answer_p1 = part_1()

# Implement the algorithm for part 2

def find_min_and_max(arr):
	min_n = arr[0]
	max_n = arr[0]
	for num in arr:
		if num < min_n:
			min_n = num
		if num > max_n:
			max_n = num
	
	print("Min:",min_n,"Max:",max_n)
	return min_n, max_n

print("\n--------------\nSecond part...\n--------------\n")
def part_2(num_total):
	for idx1, num1 in enumerate(input_list):
		print("Idx1:", idx1)
		print("Num1:", num1)
		sum = num1
		for idx2, num2 in enumerate(input_list[idx1+1:]):
			print("Idx2:", idx2)
			print("Num2:", num2)
			sum += num2
			print("Sum:", sum)
			if sum > num_total:
				break
			elif sum == num_total:
				print("Found! Idx1:", idx1, "\tIdx2:", idx1+idx2)
				min, max = find_min_and_max(input_list[idx1:idx1+idx2+1])
				return min + max

answer_p2 = part_2(answer_p1)


# Final output
print('\n---------------')
print(f'Final answer (part 1): "{answer_p1}"')
print(f'Final answer (part 2): "{answer_p2}"')