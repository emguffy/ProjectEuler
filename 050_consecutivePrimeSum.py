from is_prime import *
primesList = []
maxPrime = 1000000

i = 2
while sum(primesList) < maxPrime:
	if is_prime(i):
		primesList.append(i)
	i += 1

maxCounter = 1
maxPrimeSum = 0		
for firstPrime in range(len(primesList)):
	#print("firstPrime: ",firstPrime)
	if sum(primesList[firstPrime:firstPrime+maxCounter]) > maxPrime:
		break
	if maxCounter > len(primesList) - firstPrime:
		break	
		
	for lastPrime in range(firstPrime+maxCounter,len(primesList)):
		#print ('lastPrime: ',lastPrime)
		primeSum = sum(primesList[firstPrime:lastPrime+1])
		#print('primeSum: ',primeSum)
		if primeSum > maxPrime:
			#print("primeSum > maxPrime")
			break
		if is_prime(primeSum):
			maxCounter = lastPrime - firstPrime + 1
			maxPrimeSum = primeSum
			print("firstPrime: ",firstPrime)
			print ('lastPrime: ',lastPrime)
			print("maxPrimeSum: ",maxPrimeSum)
			print("maxCounter: ",maxCounter)
			
print("maxPrimeSum: ",maxPrimeSum)
print("maxCounter: ",maxCounter)
