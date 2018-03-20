def is_prime(number):
	if number < 2:
		return False
	
	if number == 2 or number == 3:
		return True
	
	if number % 2 == 0:
		return False
	
	for factor in range(3, int(number**0.5) + 1,2):
		if number % factor == 0:
			return False
		
	return True
	
	
def find_next_prime(candidate):
	while True:
		if is_prime(candidate) == True:
			yield candidate
			candidate += 1
		else:
			candidate += 1