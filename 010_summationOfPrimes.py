def is_prime(num):
	isPrime = True
	if num == 2:
		return isPrime
	for i in range(3,int(num**0.5) + 1):
		if num % i == 0:
			isPrime = False
			break
	return isPrime
	

sumOfPrimes = 2
for i in range(3,2000000,2):
	if is_prime(i) == True:
		sumOfPrimes += i
		
print sumOfPrimes