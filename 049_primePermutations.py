import itertools
from is_prime import *

sequence = 1234
print itertools.permutations(str(sequence))
sequenceList = []


for sequence in range(1000,10000):
	permList = sorted(int(''.join(p)) for p in itertools.permutations(str(sequence)))
		
	for perm in permList:
		if len(str(perm)) != 4 or is_prime(perm) == False:
			while permList.count(perm) > 0:
				permList.remove(perm)
				
	for perm in permList:
		if (perm + 3330) in permList and (perm + 6660) in permList:
			if is_prime(perm + 3330) and is_prime(perm + 6660):
				permCandidate = int(str(perm) + str(perm + 3330) + str(perm + 6660))
				sequenceList.append(permCandidate)
				break		

print set(sequenceList)
print is_prime(1489)
print is_prime(8149)
print is_prime(4819)
		
			
	

