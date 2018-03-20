from is_prime import *
	
circularsList = []	

for candidate in range(2,1000001):
	if is_prime(candidate) == True:
		rotation = str(candidate)
		isCircular = True
		i = 1
		while i < len(str(candidate)):
			rotation += rotation[0]
			rotation = rotation[1:]
			if is_prime(int(rotation)) == False:
				isCircular = False
				break
			else:
				i += 1
			
		if isCircular == True:
			print "candidate: " + str(candidate)
			circularsList.append(candidate)

print "Length of circulars list: " + str(len(circularsList))