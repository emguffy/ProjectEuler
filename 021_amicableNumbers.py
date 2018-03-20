def sumDivisors(number):
	divSum = 1
	for potentialDiv in range(2,number):
		if number % potentialDiv == 0:
			divSum += potentialDiv
	return divSum


maxRange = 10000
amicableNumbers =[]

for candidate in range(2,maxRange):
	if candidate not in amicableNumbers:
		divisorSumCandidate = sumDivisors(candidate)
		divisorSumSum = sumDivisors(divisorSumCandidate)
		if candidate != divisorSumCandidate and divisorSumSum == candidate:
			print candidate
			amicableNumbers.append(candidate)
			print divisorSumCandidate
			amicableNumbers.append(divisorSumCandidate)
	
amicableSum = 0			
for i in amicableNumbers:
	amicableSum += i
	
print amicableSum