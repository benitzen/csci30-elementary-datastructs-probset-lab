stringInput = input()
uniqueLetters = []

for a in stringInput:

	if(len(uniqueLetters) == 0):
		uniqueLetters.append(a)

	elif(a == uniqueLetters[-1]):
		uniqueLetters.pop()

	else:
		uniqueLetters.append(a)

print(*uniqueLetters, sep="")
