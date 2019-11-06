def directory(a):
	indices = []
	split = a.split(' ')

	if(a == ' '):
		print('/')
		return

	for b in range(len(split)):
		if split[b] == '..':
			indices.append(b)

	if(len(indices) == 0):
		if(len(split) == 0):
			print("/")
		else:
			print("/" + '/'.join(split) + "/")
	else:
		for b in indices:
			split[b] = 'BLANK'
		for b in indices:
			count = b - 1
			while(count >= 0):
				if(split[count] != "BLANK"):
					split[count] = "BLANK"
					break

				count -= 1
		formatted = list(filter(lambda x: x != "BLANK", split))
		if(len(formatted) == 0):
			print("/")
		else:
			print("/" + "/".join(formatted) + "/")


commands = int(input())
dirs = []
outputs = []
count = 0

while(count < commands):
	command = input().split(' ')
	temp_dirs = []

	if(command[0] == 'pwd'):
		outputs.append(" " if len(dirs) == 0 else " ".join(dirs))
	elif(command[0] == 'cd'):
		if(command[1] == '/'):
			dirs = []
		else:
			if command[1].startswith("/"):
				dirs = []
				temp_dirs = command[1].split('/')[1:]
			else:
				temp_dirs = command[1].split('/')
	if(len(temp_dirs) != 0):
		dirs = dirs + temp_dirs
	count += 1

for x in outputs:
	directory(x)


