
multiplesList = range(1,21)
primeList = [2,3,5,7,11,13,17,19]


pointer = 1
primeFactor = 1
masterPrimes = []


# Iterate backwards through the list of multiples to see if they are factors
# If so, we'll add their unique prime factors to a list
# Then, we'll take the product of that list and add it to our pointer to make our algorithm greedy
for multiple in reversed(multiplesList):
	print "Mulitple = " + str(multiple)
	while (pointer % multiple != 0):
		pointer += primeFactor
		print "Pointer = " + str(pointer)

	# Build a list to hold prime factors of the multiple
	multiplePrimes = []
	residual = multiple
	print "residual = " + str(residual)
	while (residual != 1):
		for prime in primeList:
			if residual % prime == 0:
				multiplePrimes.append(prime)
				residual /= prime
				break
	
	print "multiplePrimes: " + str(multiplePrimes)
	print "masterPrimes: " + str(masterPrimes)

					
	j = 0
	for item in multiplePrimes:
		if j == len(masterPrimes):
			masterPrimes.append(item)

		while (j<len(masterPrimes)):
			if item == masterPrimes[j]:
				j += 1
				break

			elif item >= masterPrimes[j]:
				j += 1
				if j == len(masterPrimes):
					masterPrimes.append(item)
				
			else:
				masterPrimes.insert(j,item)
				j += 1
				break
	
	print "masterPrimes: " + str(masterPrimes)
	
	# reset the primeFactor to 1 each time through
	primeFactor = 1	
	for prime in masterPrimes:
		primeFactor *= prime
		print "primeFactor = " + str(primeFactor)
			
		
print "final pointer: " + str(pointer)