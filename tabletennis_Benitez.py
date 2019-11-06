from collections import deque

def ping_pong(wins, numPlayers):
	pongers = deque(numPlayers)
	iterateCounter = 0

	while(iterateCounter < len(pongers)):
		winsCounter = 0
		fightsCounter = 0
		pongerFought = []		

		while(True):
			fightsCounter += 1

			if(pongers[0] > pongers[1]):
				if(pongers[0] > pongers[-1] and fightsCounter == 1):
					winsCounter += 2
				else:
					winsCounter += 1

				pongerFought.append(pongers[1])

				if(winsCounter == wins or (len(pongerFought) + 1 == len(pongers) and max(pongers) == pongers[0])):			
					print(pongers[0])
					return
				else:
					temp = pongers[1]
					pongers.remove(temp)
					pongers.append(temp)
			else:
				val = pongers.popleft()
				pongers.append(val)
				break

		iterateCounter += 1

first_line = [int(a) for a in input().split(' ')]
second_line = [int(a) for a in input().split(' ')]
ping_pong(first_line[1], second_line)




