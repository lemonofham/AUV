import random
tests = random.randint(1, 1000)
print(f"Number of test cases : {tests}")
for i in range(tests):
	players = random.randint(3, 100000)
	print(f"\tNumber of players in test case {i+1} : {players}")
	A = [0]*players
	imposter = random.randint(1, players)
	A[imposter-1] = 2
	for j in range(players):
		if j == imposter-1:
			continue
		else:
			A[j] = random.choice([0, 1])
	returned_imposter = 0
	if players % 2 == 0:
		j = 1
		while j < players:
			if A[j-1] == A[j]:
				Janswer = 1
			elif A[j-1] == 2 and A[j] == 0:
				Janswer = 1
			elif A[j-1]*A[j] == 0:
				Janswer = 0
			elif A[j-1] == 2:
				Janswer = 0
			else:
				Janswer = 1
			if A[j] == A[j-1]:
				x = 1
			elif A[j] == 2 and A[j-1] == 0:
				x = 1
			elif A[j]*A[j-1] == 0:
				x = 0
			elif A[j] == 2:
				x = 0
			else:
				x = 1
			Janswer = Janswer*10 + x
			if Janswer != 0 and Janswer != 11:
				if j != 1:
					if A[j-2] == A[j-1]:
						afterJanswer = 1
					elif A[j-2] == 2 and A[j-1] == 0:
						afterJanswer = 1
					elif A[j-2]*A[j-1] == 0:
						afterJanswer = 0
					elif A[j-2] == 2:
						afterJanswer = 0
					else:
						afterJanswer = 1
					if A[j-1] == A[j-2]:
						y = 1
					elif A[j-1] == 2 and A[j-2] == 0:
						y = 1
					elif A[j-1]*A[j-2] == 0:
						y = 0
					elif A[j-1] == 2:
						y = 0
					else:
						y = 1
					afterJanswer = afterJanswer*10 + y
					if afterJanswer != 0 and afterJanswer != 11:
						returned_imposter = j
					else:
						returned_imposter = j + 1
					break
				else:
					if A[1] == A[2]:
						afterJanswer = 1
					elif A[1] == 2 and A[2] == 0:
						afterJanswer = 1
					elif A[1]*A[2] == 0:
						afterJanswer = 0
					elif A[1] == 2:
						afterJanswer = 0
					else:
						afterJanswer = 1
					if A[2] == A[1]:
						y = 1
					elif A[2] == 2 and A[1] == 0:
						y = 1
					elif A[2]*A[1] == 0:
						y = 0
					elif A[2] == 2:
						y = 0
					else:
						y = 1
					afterJanswer = afterJanswer*10 + y
					if afterJanswer != 0 and afterJanswer != 11:
						returned_imposter = 2
					else:
						returned_imposter = 1
					break
			j += 2
	else:
		done = False
		j = 1
		while j < players:
			if A[j-1] == A[j]:
				Janswer = 1
			elif A[j-1] == 2 and A[j] == 0:
				Janswer = 1
			elif A[j-1]*A[j] == 0:
				Janswer = 0
			elif A[j-1] == 2:
				Janswer = 0
			else:
				Janswer = 1
			if A[j] == A[j-1]:
				x = 1
			elif A[j] == 2 and A[j-1] == 0:
				x = 1
			elif A[j]*A[j-1] == 0:
				x = 0
			elif A[j] == 2:
				x = 0
			else:
				x = 1
			Janswer = Janswer*10 + x
			if Janswer != 0 and Janswer != 11:
				if j != 1:
					if A[j-2] == A[j-1]:
						afterJanswer = 1
					elif A[j-2] == 2 and A[j-1] == 0:
						afterJanswer = 1
					elif A[j-2]*A[j-1] == 0:
						afterJanswer = 0
					elif A[j-2] == 2:
						afterJanswer = 0
					else:
						afterJanswer = 1
					if A[j-1] == A[j-2]:
						y = 1
					elif A[j-1] == 2 and A[j-2] == 0:
						y = 1
					elif A[j-1]*A[j-2] == 0:
						y = 0
					elif A[j-1] == 2:
						y = 0
					else:
						y = 1
					afterJanswer = afterJanswer*10 + y
					if afterJanswer != 0 and afterJanswer != 11:
						returned_imposter = j
					else:
						returned_imposter = j + 1
					done = True
					break
				else:
					if A[1] == A[2]:
						afterJanswer = 1
					elif A[1] == 2 and A[2] == 0:
						afterJanswer = 1
					elif A[1]*A[2] == 0:
						afterJanswer = 0
					elif A[1] == 2:
						afterJanswer = 0
					else:
						afterJanswer = 1
					if A[2] == A[1]:
						y = 1
					elif A[2] == 2 and A[1] == 0:
						y = 1
					elif A[2]*A[1] == 0:
						y = 0
					elif A[2] == 2:
						y = 0
					else:
						y = 1
					afterJanswer = afterJanswer*10 + y
					if afterJanswer != 0 and afterJanswer != 11:
						returned_imposter = 2
					else:
						returned_imposter = 1
					done = True
					break
			j += 2
		if not done:
			returned_imposter = players
	if returned_imposter != imposter:
		print("Code incorrect")
		print(f"Failed at test case {i+1} out of {tests}")
		print(f"You said player number {returned_imposter} was imposter, but it was actually player number {imposter}")
		print("The distribution of player roles for the given test case is : ")
		for j in range(players):
			if A[j] == 0:
				print(f"Player {i+1} : Knave")
			elif A[j] == 1:
				print(f"Player {i+1} : Knight")
			else:
				print(f"Player {i+1} : Imposter")
		break
	else:
		print(f"\t\tImposter and Returned Imposter (same) is player number {imposter}")