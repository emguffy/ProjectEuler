# sub-string divisibility
from is_prime import *
import itertools


digits = ['9','8','7','6','5','4','3','2','1','0']
pandigitalList = list(itertools.permutations(digits))

primeList = ['2','3','5','7','11','13','17']
panSSDivList = []

'''
1406357289
pandigital = ['1','4','0','6','3','5','7','2','8','9']
for n in range(2,9):
	print int(''.join(pandigital[n-1:n+2]))
	print int(primeList[n-2])
	print int(''.join(pandigital[n-1:n+2]))%int(primeList[n-2])
	if int(''.join(pandigital[n-1:n+2]))%int(primeList[n-2]) != 0:
		ssDivisible = False
		break
	
'''

for pandigital in pandigitalList:
	ssDivisible = True
	for n in range(2,9):
		if int(''.join(pandigital[n-1:n+2]))%int(primeList[n-2]) != 0:
			ssDivisible = False
			break
	if ssDivisible == True:
		panSSDivList.append(int(''.join(pandigital)))
		print int(''.join(pandigital))


print "sum(panSSDivList): " + str(sum(panSSDivList))

'''
	
'''