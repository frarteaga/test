"""
Return True if N is a prime number, False otherwise
>>> prime(10)
False
>>> prime(2)
True
>>> prime(23)
True
>>> prime(31)
True
>>> prime(35)
False
"""
def prime(N):
	if N == 1 or N == 0:
		return False
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
