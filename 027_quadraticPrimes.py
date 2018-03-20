### Quadratic Primes

from is_prime import *

maxPrimeCounter = 0
aStar = 0
bStar = 0

for b in range(1,1000):
	if is_prime(b) == True:
		for a in range(-999,1000):
			primeIndicator = True
			n = 0
			while primeIndicator == True:
				if is_prime(n**2 + a*n + b) == True:
					n += 1
				else:
					primeIndicator = False
			if n > maxPrimeCounter:
				maxPrimeCounter = n
				print "maxPrimeCounter: " + str(maxPrimeCounter)
				aStar = a
				print "aStar: " + str(aStar)
				bStar = b
				print "bStar: " + str(bStar)

print "product: " + str(aStar*bStar)