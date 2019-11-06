numInput = int(input())
a = [0]
b = []
limit = 2**32 

c = 0
while(c < numInput):
	instruct = input().split(' ')
	cmd = instruct[0]

	if(cmd == "for"):
		a.append(0.0) #for some magical reason, no time limit when using 0.0
		b.append(int(instruct[1]))
	elif(cmd == "add"):
		a[-1] = a[-1] + 1
	elif(cmd == "end"):
		a[-1] = a.pop() * b.pop() + a[-1]

	c += 1

if(a[0] < limit):
	print(int(a[0]))
else:
	print("OVERFLOW!!!")