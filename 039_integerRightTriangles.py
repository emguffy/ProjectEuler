maxSolutionCount = 0
maxSolutionPerimeter = 0
for perimeter in range(3,1001):
	solutionsCount = 0
	for a in range(1,1+int(perimeter/(2+2**.5))):
		for b in reversed(range(int(perimeter/(2+2**.5)),perimeter/2)):
			c = perimeter - a - b
			if c**2 == (a**2 + b**2):
				solutionsCount += 1
				print "a: " + str(a)
				print "b: " + str(b)
				print "c: " + str(c)
		
	if solutionsCount > maxSolutionCount:
		maxSolutionCount = solutionsCount
		maxSolutionPerimeter = perimeter
		print "maxSolutionPerimeter: " + str(maxSolutionPerimeter)
		print "New maxSolutionCount: " + str(maxSolutionCount)
		
print "maxSolutionCount: " + str(maxSolutionCount)
