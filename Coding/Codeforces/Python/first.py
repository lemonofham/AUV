n = int(input())
valid = True
lucky = 0
while n > 0:
	if n % 10 == 4 or n % 10 == 7:
		lucky += 1
	n //= 10
if lucky == 0:
	valid = False	
while lucky > 0:
	if lucky % 10 != 4 and lucky % 10 != 7:
		valid = False
	lucky //= 10
if valid:
	print("YES")
else:
	print("NO")