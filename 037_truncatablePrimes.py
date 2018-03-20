from is_prime import *

def is_truncatable(num):
	strNum = str(num)
	isTruncatable = True
	j = len(strNum)
	while j > 0:
		if is_prime(int(strNum[:j])) == False:
			isTruncatable = False
			break
		else:
			j -= 1
	
	return isTruncatable

truncatablePrimes = []
rootList = ['1','2','3','5','7','9']

def truncatable_primes(num):
	strNum = str(num)
	for i in rootList:
		if is_prime(int(i+strNum)):
			#print i + strNum				
			if is_truncatable(int(i+strNum)):
				print "Found one: " + i + strNum
				truncatablePrimes.append(int(i+strNum))
			if i != '2':	
				truncatable_primes(int(i+strNum))			

truncatable_primes(3)
truncatable_primes(5)
truncatable_primes(7)
print truncatablePrimes
print sum(truncatablePrimes)
