import math

def count_divisors(num):
	# start divisorCount at 2 to account for 1 and the number itself
	divisorCount = 2
	if math.sqrt(num).is_integer() == True:
		divisorCount -= 1
	for i in range(2,int(num**0.5)+1):
		if num % i == 0:
			divisorCount += 2
	print divisorCount
	return divisorCount



foundTriangle = False
t = 0
triangleNumber = 0
divLenTarget = 500

while (foundTriangle == False):
	t += 1
	triangleNumber += t
	
	print "t:" + str(t)
	print "triangleNumber:" + str(triangleNumber)
	
	divCount = count_divisors(triangleNumber)
	if divCount > divLenTarget:
		foundTriangle = True

print triangleNumber
