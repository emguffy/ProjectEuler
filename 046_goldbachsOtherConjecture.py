from is_prime import *

def is_square(number):
	if int(number**0.5)**2 == number:
		return True
	else:
		return False

candidate = 3 
isFalseComposite = False

# For this purpose, we can skip 2
primesList = []

while isFalseComposite == False and candidate < 100000:
	if is_prime(candidate):
		primesList.append(candidate)
	else:
		isComposite = False
		for prime in reversed(primesList):
			if is_square((candidate - prime)/2):
				isComposite = True
				break
		
		if isComposite == False:
			isFalseComposite = True
			print candidate
	
	# only need to check odds		
	candidate += 2
	
