from is_prime import *


# The basic form of the alogrithm is to start with the least primes and work your way up, since the problem says to find the
# smallest prime value.

# Because we are looking for the smallest of the family, we can rule out having to check certain values
# We can rule out checking anything greater than a 3, since if we didn't already check that prime as part of a smaller family,
# it could not now be a match, since 3-9 accounts for only 7 digits, which would require us to check letter digits, which would mean
# that we would have already found the match.

# So, we must therefore only check 0's, 1's and 2's
# If we start with checking 2's, if we find any non-primes, we can quit
# If we start with checking 1's, if we find any two non-primes, we can quit
# If we start with checking 3's, if we find any three non-primes, we can quit

# I use a generator function to produce primes, checking each one as I go (starting with 2)
def find_next_prime(candidate):
	while True:
		if is_prime(candidate) == True:
			yield candidate
			candidate += 1
		else:
			candidate += 1

# When primeFound = True, we stop; magicPrime holds the value
primeFound = False
magicPrime = 0

for prime in find_next_prime(2):
	# print("prime: ",prime)
	
	# Check the length of the number
	strPrime = str(prime)
	lenPrime = len(strPrime)
	
	for i in range(3):
		# Check for the existence of i within the string
		bingo = False
		for char in strPrime:
			#print("char: ",char)
			if char == str(i):
				bingo = True
				#print("bingo = True")
				break		
		
		
		if bingo == True:
			#print("i: ",i)
			# If the 0, 1, or 2 is in the 1's digit, move on.
			if strPrime[lenPrime - 1] != i:
			
				# If the notPrimeCount ever hits 0, move on.
				notPrimeCount = 2 - i
				
				# r for replacement digit
				for r in range(i + 1, 10):
					#print("r: ",r)
					#print("The replacement prime: ",strPrime.replace(str(i),str(r)))
					if is_prime(int(strPrime.replace(str(i),str(r)))) == False:
						notPrimeCount -= 1
						if notPrimeCount < 0:
							break
				else:
					#print("The code made it to here...")
					primeFound = True
					magicPrime = prime

	
	
	if primeFound == True:
		break
				
print("magicPrime: ",magicPrime)