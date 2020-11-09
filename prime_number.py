def is_prime(n) -> bool:
	flag = True # True means it's prime
	for i in range(2, int(n/2)+1, 1):
		if n % i == 0:
			flag = False
			break

	if n == 1: return False # 1 is neither prime nor composite
	else:
		if flag: return True
		else: return False

numbers = []
prime = 0
n = int(input("How many numbers? : "))
print("Enter ", n, "numbers :")
for i in range(0, n):
	numbers.append(int(input()))

for i in range(0, len(numbers)):
	if is_prime(numbers[i]):
		prime += 1

print("\nPrimes = ", prime)
