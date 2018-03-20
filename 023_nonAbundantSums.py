
def is_abundant(candidate):
	factorSum = 1
	# print "candidate: " + str(candidate)
	# print "square of candidate (+1): " + str(int(candidate**0.5) + 1)
	for potentialFactor in range(2,int(candidate**0.5)+1):
		if candidate % potentialFactor == 0:
			if potentialFactor == candidate**0.5:
				# print "potentialFactor: " + str(potentialFactor)
				factorSum += potentialFactor
			else:
				# print "potentialFactor + opposite factor: " + str(potentialFactor) + " + " + str(candidate / potentialFactor)
				factorSum += potentialFactor + (candidate / potentialFactor)
	
	if factorSum > candidate:
		# print "factorsum:%s, candidate:%s" % (factorSum,candidate)
		return True
	else:
		return False


# Numbers 1 through 11 cannot be teh sum of two abundant numbers, so we start with their sum (84)
nonAbundantSum = 0
abundantNumbers = []


for number in range(1,28124):
	print number
	if is_abundant(number) == True:
		abundantNumbers.append(number)		
	
	canBeSummed = False
	for abundantNumber in reversed(abundantNumbers):
		remainder = number - abundantNumber
		if remainder in abundantNumbers:
			canBeSummed = True
			break
	
	if canBeSummed == False:
		nonAbundantSum += number


print abundantNumbers
print nonAbundantSum

