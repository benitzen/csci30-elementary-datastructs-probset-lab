def marshal(n):
	temp = n
	mid = []
	while True:
		init = 0
		while len(mid) > 0:
			mid.pop()
		outputValue = list(map(int, input().rstrip().split()))
		if outputValue[0] == 0:
			return None
		
		for element in outputValue:
			while init < temp and init != element:
				if len(mid) > 0 and mid[-1] == element:
					break
				init += 1
				mid.append(init)
			if mid[-1] == element:
				mid.pop()
		if len(mid) == 0:
			print("Yes")
		else:
			print("No")

def main():
	while True:
		inputValue = int(input())
		if inputValue == 0:
			break
		marshal(inputValue)
		print("")


main()


# 24148381 tomy8910

