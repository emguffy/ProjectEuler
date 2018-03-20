from is_prime import *

def main():
	primesPercent = 1.00
	diagonalsCount = 1
	primesCount = 0

	# We start with the counter at 3 so as to avoid the unusual pattern break at the beginning.
	counter = 1
	sideLength = 1
	currentSide = 1 # 1 is climbing on the right, 2 is traversing left on top, 3 is descending on the left, 4 is traversing right on the bottome
	
	while primesPercent >= .1:
		if currentSide == 1:
			sideLength += 2
	
		counter += sideLength - 1
		diagonalsCount += 1
		if is_prime(counter):
			primesCount += 1
		currentSide += 1
				
		if currentSide == 5:	
			primesPercent = primesCount/diagonalsCount
			#print(primesPercent)
			# Reset the current side to 1
			currentSide = 1
	
	print("Side Length: ",sideLength)


if __name__ == '__main__':
	main()