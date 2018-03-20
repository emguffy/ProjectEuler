diagonalSum = 4

movement = 2

right = False
left = True
down = False
up = False

counter = 3
while(movement <= 1000):
	if right == True:
		counter += movement
		diagonalSum += counter
		counter += 1
		movement += 1
		right = False
		down = True
	
	elif down == True:
		counter += movement
		diagonalSum += counter
		movement += 1
		down = False
		left = True

	elif left == True:
		counter += movement
		diagonalSum += counter
		left = False
		up = True

	else:
		counter += movement
		diagonalSum += counter
		up = False
		right = True
		
	print "counter: " + str(counter)
	#print "movement: " + str(movement)
	#print "diagonalSum: " + str(diagonalSum)

print "diagonalSum: " + str(diagonalSum)
	
		
	 