product = 600851475143


def isPrime(num):
	for i in range(2,int(num**0.5)+1):
		if num % i == 0:
			return False
	return True

def findNextPrime(currentPrime):
	# currentPrime cannot be even, so to add 1 would make it so...
	if currentPrime == 2:
		nextPrime = 3
	else:
		nextPrime = currentPrime + 2

	# We iterate from the currentPrime until we find num that is prime
	while (isPrime(nextPrime) != True):
		nextPrime += 2
	
	return nextPrime

primePointer = 2
largetstPrimeFactor = primePointer
maxPossiblePrime = int(product**0.5)
print "maxPossiblePrime: " + str(maxPossiblePrime)

while (primePointer <= maxPossiblePrime):
	if product % primePointer == 0:
		largestPrimeFactor = primePointer
		product = product / primePointer
		#print "product:" + str(product)		
	else:
		primePointer = findNextPrime(primePointer)
		#print "primePointer:" + str(primePointer)
	
print largestPrimeFactor
