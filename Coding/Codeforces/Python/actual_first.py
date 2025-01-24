tests = int(input())
n = 0
for i in range(tests):
	Janswer = 0
	afterJanswer = 0
	n = int(input())
	if n % 2 == 0:
		j = 1
		while j < n:
			Janswer = int(input(f"? {j} {j+1}\n"))
			x = int(input(f"? {j+1} {j}\n"))
			Janswer = Janswer*10 + x
			if Janswer != 0 and Janswer != 11:
				if j != 1:
					afterJanswer = int(input(f"? {j-1} {j}\n"))
					y = int(input(f"? {j} {j-1}\n"))
					afterJanswer = afterJanswer*10 + y
					if afterJanswer != 0 and afterJanswer != 11:
						print(f"! {j}")
					else:
						print(f"! {j+1}")
					break
				else:
					afterJanswer = int(input("? 2 3\n"))
					y = int(input("? 3 2\n"))
					afterJanswer = afterJanswer*10 + y
					if afterJanswer != 0 and afterJanswer != 11:
						print("! 2")
					else:
						print("! 1")
					break
			j += 2
	else:
		done = False
		j = 1
		while j < n - 1:
			Janswer = int(input(f"? {j} {j+1}\n"))
			x = int(input(f"? {j+1} {j}\n"))
			Janswer = Janswer*10 + x
			if Janswer != 0 and Janswer != 11:
				if j != 1:
					afterJanswer = int(input(f"? {j-1} {j}\n"))
					y = int(input(f"? {j} {j-1}\n"))
					afterJanswer = afterJanswer*10 + y
					if afterJanswer != 0 and afterJanswer != 11:
						print(f"! {j}")
					else:
						print(f"! {j+1}")
					done = True
					break
				else:
					afterJanswer = int(input("? 2 3\n"))
					y = int(input("? 3 2\n"))
					afterJanswer = afterJanswer*10 + y
					if afterJanswer != 0 and afterJanswer != 11:
						print("! 2")
					else:
						print("! 1")
					done = True
					break
			j += 2
		if not done:
			print(f"! {n}")