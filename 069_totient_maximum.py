#! /Applications/anaconda3/bin/python

# iterate n from 2 to 1M
# for each value of n, compare the value of n/phi(n) to the current maximum (initialize at 1.0)

#need a function for phi(n)
#will use a isPrime() function

def isRelativePrime(n,i):
	for f in range(2,i+1):	
		#print('f: ',f)
		if i%f == 0 and n%f == 0:
			return False
		
	return True

#print(isRelativePrime(6,5))


def phi(n):
	count = 1
	#print('count :',count)
	for k in range(2,n):
		#print('k: ',k)
		if isRelativePrime(n,k) == True:
			count += 1
			#print('count :',count)
		
	return count

#print(phi(6))
	
def phiQuotient(n):
	return n/phi(n)
	
#print(phiQuotient(2))
#print(phiQuotient(3))
#print(phiQuotient(4))
#print(phiQuotient(5))
#print(phiQuotient(6))
#print(phiQuotient(7))
#print(phiQuotient(8))

def maxPhiN(m):	
	maxPhiQuotient = 1			
	maxPhiN = 2

	for n in range(2,m):
		if phiQuotient(n) > maxPhiQuotient:
				print('n: ',n,'  phiQuotient: ',phiQuotient(n))
				maxPhiQuotient = phiQuotient(n)
				maxPhiN = n
			
	return maxPhiN

print(maxPhiN(10000))


# After building brute force functions, intuitively saw a pattern with the maximum phi values as m grew.
# These were mutiples of successive primes (i.e. 2,3,5,7,13,17,19).  By the time I multiplied by 17, I had 
# the answer, without having to brute force the solution (which is still running for m=10000 as I'm typing this...)