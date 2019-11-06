test_cases = int(input())
outputs = []

for test_case in range(test_cases):
	specifications = input().rstrip().split()
	centimeters = int(specifications[0]) * 100
	num_cars = int(specifications[1])

	left = []
	right = []
	crosses = 0
	curr_sum = 0
	for car in range(num_cars):
		length_and_bank = input().rstrip().split()
		length = int(length_and_bank[0])
		bank = length_and_bank[1]

		if bank == 'left':
			left.append(length)
		elif bank == 'right':
			right.append(length)

	while len(left) != 0 or len(right) != 0:
		if crosses % 2 == 0:
			while curr_sum <= centimeters and len(left) != 0:
				if left[0] + curr_sum > centimeters:
					break
				else:
					c = left.pop(0)
					curr_sum += c
			crosses += 1
			curr_sum = 0

		elif crosses % 2 != 0:
			while curr_sum <= centimeters and len(right) != 0:
				if right[0] + curr_sum > centimeters:
					break
				else:
					c = right.pop(0)
					curr_sum += c
			crosses += 1
			curr_sum = 0

	outputs.append(crosses)




for cross in outputs:
	print(cross)

# 24156865 tomy8910













