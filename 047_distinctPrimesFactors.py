# Two potential apporaches:
"""
One approach is start iterating from 0 numbers that are candidtates for having 4 distinct prime factors.
When one such number is found, put that number in a list and check the next number.  If that number also
fits, then stack that number in the list as well.  Keep stacking successful numbers in the list until 
reaching 4, or, if a consecutive number does not have distinct prime factors, then empty the list and
continue the iteration until 4 consecutive numbers are found.

The crux of this approach is developing a method for determining whether a number has 4 distinct primes.

The second approach is to develop a list of primes and stack products of distinct prime factors in a 
sorted list, checking for 4 consecutive entries after each iterative entry is made.

The crux of this approach is appropriately permutating through all potential products."""


# Consecutive number counter
conCounter = 0
conList = []

targetConCounter = 4
targetFactorCounter = 4

# Starting at candidate = 3
candidate = 3

# Starting with 2
primes = [2]


while conCounter < targetConCounter and candidate < 300000:	
	# Update the list of primes
	primeCandidate = candidate / 30
	if primeCandidate > primes[-1]:
		isPrime = True
		for num in range(2,primeCandidate):
			if primeCandidate % num == 0:
				isPrime = False
		
		if isPrime == True:
			primes.append(primeCandidate)

	# first problem is to figure out how to tell if a number can be divided by 4 distinct prime factors
	factorCounter = 0
	fraction = candidate	
	for prime in reversed(primes):
		if fraction == 1:
			break
		else:
			if (fraction % prime == 0):
				factorCounter += 1
			while (fraction % prime == 0):
				fraction = fraction / prime
			
	if factorCounter >= targetFactorCounter:
		conCounter += 1
		conList.append(candidate)
	else:
		conCounter = 0
		conList = []
			
	candidate += 1
	
print primes	
print conList	
	
	
	
	
	
	
	
		
		