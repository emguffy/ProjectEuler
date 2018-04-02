#! /Applications/anaconda3/bin/python

from math import sqrt


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


def is_square(n):
    return sqrt(n).is_integer()

def minSolution(D):
	y = 1
	while True:
		#print('y: ',y)
		if ((D*(y**2) + 1)**.5).is_integer():
			x = ((D*(y**2) + 1)**.5)
			print('D: ',D,' and y: ',y,' and x: ',x)
			break
		else:
			y = y + 1

	return x

minSolution(13)

def listMinSolutionX(maxD):
	minSolutionX = []
	#print('hello')
	for D in range(0,maxD):
		#print('D: ',D)
		if is_square(D):
			#print(D,' is a square')
			minSolutionX.append(0)
		#elif is_prime(D):
			#minSolutionX.append(minSolution(D))
		else:
			minSolutionX.append(minSolution(D))			
			#minSolutionX.append(0)
		
	return minSolutionX


#minSoultionList = listMinSolutionX(1000)	
#print(minSoultionList)
#print('max x: ',max(minSoultionList))
#print('D of max x: ',minSoultionList.index(max(minSoultionList)))	