def prime(N):
	if N == 2:
		return True
	if N % 2 == 0:
		return False
	i = 3
	while i * i <= N:
		if N % i == 0:
			return False
		i += 2
	return True

while 1:
	N = input()
	print prime(N)
