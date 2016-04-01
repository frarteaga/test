"""
Return True if N is a prime number, False otherwise
"""
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

def main():
	while 1:
		N = 1
		try:
			N = input()
		except IOError:
			break
		print prime(N)

if __name__ == '__main__':
	main()
