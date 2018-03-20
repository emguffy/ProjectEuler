import itertools
from is_prime import *

prime1List = []
# prime2List, prime3List and prime4List will all be a list of lists
prime2List = []
prime3List = []
prime4List = []
prime5List = []
prime5Sum = 0

def catPrimes(p1,p2):
	if is_prime(int(str(p1)+str(p2))) and is_prime(int(str(p2)+str(p1))):
		return True
	else:
		return False
		
for newPrime in find_next_prime(2):
	# Add to prime5List
	for primeList in prime4List:
		addNewPrime = True
		for prime in primeList:
			if catPrimes(newPrime,prime) == False:
				addNewPrime = False
				break
	
		if addNewPrime == True:
			prime5Sum = sum(primeList) + newPrime
			prime5List.append(primeList + [newPrime])
			break
			
	# Add to prime4List
	for primeList in prime3List:
		addNewPrime = True
		for prime in primeList:
			if catPrimes(newPrime,prime) == False:
				addNewPrime = False
				break

		if addNewPrime == True:
			prime4List.append(primeList + [newPrime])
			
	# Add to prime3List
	for primeList in prime2List:
		addNewPrime = True
		for prime in primeList:
			if catPrimes(newPrime,prime) == False:
				addNewPrime = False
				break

		if addNewPrime == True:
			prime3List.append(primeList + [newPrime])

	# Add to prime2List
	for prime in prime1List:
		if catPrimes(newPrime,prime) == True:
			prime2List.append([prime,newPrime])

	# Add to prime1List
	prime1List.append(newPrime)
	if prime4List != []:
		print(prime4List)
	
	if prime5List != []:
		break
	

print("prime5Sum: ",prime5Sum)
print(prime1List)
print(prime2List)
print(prime3List)
print(prime4List)
print(prime5List)
print(newPrime)

		
'''
def catSets(p1,p2,p3,p4,p5):
	"""Takes 5 primes and checks all 5 select 2 combination concatenations to see if they are prime."""
	primes = [p1,p2,p3,p4,p5]
	superPrime = True
	for combo in itertools.combinations(primes,2):
		if is_prime(int(''.join(str(i) for i in combo))) == False:
			superPrime = False
			break
		
	return(superPrime)

counter = 
primesList = []
for i in range(1,674):
	if is_prime(i):
		primesList.append(i)

# It has to be a 4-prime set to become a 5-prime set
# It has to be a 3-prime set to become a 4-prime set
# It has to be a 2-prime set to become a 3-prime set




#print(catSets(3,5,7,109,673))
'''