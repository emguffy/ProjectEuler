ith_prime = 10001

def is_prime(num):
	isPrime = True
	if num == 2:
		return isPrime
	for i in range(3,int(num**0.5) + 1):
		if num % i == 0:
			isPrime = False
			break
	return isPrime

i = 1
# will skip 2, which is already accounted for since i = 1
candidate = 1
while (i < ith_prime):
	candidate += 2
	if is_prime(candidate) == True:
		i += 1
		
print candidate
	
