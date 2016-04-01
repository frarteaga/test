def prime(N):
	i = 2
	while i * i <= N:
		if N % i == 0:
			return False
		i += 1
	return True

while 1:
	N = input()
	print prime(N)
