# from __future__ import division
import decimal
decimalPrecision = 100000
decimal.getcontext().prec = decimalPrecision

# The maxRepeaterLength is our target variable to return at the end of the program.
maxRepeaterLength  = 1
maxRepeaterDenominator = 1

minRange = 3
maxRange = 1000

for denominator in range(minRange,maxRange,2):
	if len(str(1/(denominator * 1.0))) > 10:
		quotient = str(decimal.Decimal(1)/decimal.Decimal(denominator))
	else:
		quotient = str(1/(denominator * 1.0))
		
	# print "Denominator: " + str(denominator)
	# print "Quotient: " + str(quotient)
	# print "Quotient Length: " + str(len(quotient))

	# We will only run the following on quotients that extend infinitely (or at least to our decimal precision choice).
	if len(quotient) > decimalPrecision:
		# The first two digits are "0.", so we drop them from consideration. 
		# The last digit is rounded, so we also drop this from the string we will analyze.  But because rounding can effect more than just one digit, we remove the last 10.
		trimmedQuotient  = quotient[2:len(quotient)-10:]
		# There could be a substring at the beginning that primes the repeater.  To avoid failing our test by considering this piece, we reverse the trimmed quotient.
		reversedQuotient = trimmedQuotient[::-1]
		# print "reversedQuotient: " + reversedQuotient

		aLength = 1
		success = 0
		
		# The longest fragement we will consider oen-third the length of the reversed quotient (even though this case is trouble).
		maxALength = int(len(reversedQuotient)/3)
		# print "maxALength: " + str(maxALength)

		while aLength < maxALength:
			# print "reversedQuotient: " + reversedQuotient
 		
			testFrag = reversedQuotient[0:aLength]
			# print "testFrag: " + testFrag

			increment = 2
			incrementMax = len(reversedQuotient)/aLength - 1
			success = 1
			while increment < incrementMax:
				compareFrag = reversedQuotient[aLength*(increment - 1):aLength*increment]
				# print "compareFrag: " + compareFrag
				if testFrag != compareFrag:
					# print "testFrag != compareFrag --> success = 0"
					success = 0
					break
				# print "testFrag == compareFrag --> success = 1"
				increment += 1

			if success == 1:
				print "Repeater found!"
				print "Repeater length: " + str(aLength)

				if aLength > maxRepeaterLength:
					maxRepeaterLength = aLength	
					maxRepeaterDenominator = denominator				
					print "maxRepeaterLength: " + str(maxRepeaterLength)
					print "maxRepeaterDenominator: " + str(maxRepeaterDenominator)
				break
					
			# iterates to the next value of aLength
			aLength += 1
			
print "maxRepeaterLength: " + str(maxRepeaterLength)
print "maxRepeaterDenominator: " + str(maxRepeaterDenominator)
"""