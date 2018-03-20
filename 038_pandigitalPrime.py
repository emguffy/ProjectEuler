# pandigital prime
from is_prime import *
import itertools

maxPandigitalPrime = 1

digitList = ['9','8','7','6','5','4','3','2','1']

for digitCounter in range(1,10):
	panDigits = digitList[9-digitCounter:]
	pandigitalList = list(itertools.permutations(panDigits))	
	for pandigital in pandigitalList:
		num = int(''.join(pandigital))
		print "num: " + str(num)
		if is_prime(num):
			maxPandigitalPrime = num
			break
			
print "maxPandigitalPrime: " + str(maxPandigitalPrime)



'''






pandigitalString = '123456789'
def is_pandigital(num):
	if ''.join(sorted(str(num))) == pandigitalString[:len(str(num))]:
		return True
	else:
		return False
	
'''