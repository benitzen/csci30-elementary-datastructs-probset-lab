from collections import deque

def tabletennis(wins, players):
	p = deque(players)

	idx = 0

	while idx < len(p):
		win_count = 0
		# has_fought handles cases where wins are > 10000000
		has_fought = []
		fight_count = 0
		while True:
			fight_count += 1 # handles edge case


			if(p[0] > p[1]):
				"""
					the case is usually:
					all players lose until you reach the biggest number
					1 2 3 4 5 
					and that number is the winner, but in the case of
					1 4 3 5 2 where wins = 2
					you might expect 5 to be the expected output
					but it's 4.

					4 wins against 1 and it wins against 3.
				"""
				if fight_count == 1 and p[0] > p[-1]:
					win_count += 2
				else:
					win_count += 1
				has_fought.append(p[1])

				if win_count == wins or (len(has_fought) + 1 == len(p) and max(p) == p[0]):			
					print(p[0])
					return
				else:
					temp = p[1]
					p.remove(temp)
					p.append(temp)
			else:
				val = p.popleft()
				p.append(val)
				break

		idx += 1



first_line = [int(x) for x in input().split(' ')]
second_line = [int(x) for x in input().split(' ')]

tabletennis(first_line[1], second_line)

