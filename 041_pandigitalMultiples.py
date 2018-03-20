import time
start = time.time()

pandigitalNumbers = [0]

def is_pandigital(strNum):
	if ''.join(sorted(strNum)) == '123456789':
		return True
	else:
		return False

for number in range(2,10000):
	if int(str(number)[0]) >= int(str(max(pandigitalNumbers))[0]):
		catMultiple = ''
		i = 1
		while len(catMultiple) < 9:
			catMultiple += str(number*i)
			i += 1

		if len(catMultiple) == 9:
			if is_pandigital(catMultiple):
				print "Found one: " + catMultiple
				print "number: " + str(number)
				pandigitalNumbers.append(int(catMultiple))

print "Max Pandigital: " + str(max(pandigitalNumbers))
elapsed = time.time() - start
print "Elapsed time: " + str(elapsed)