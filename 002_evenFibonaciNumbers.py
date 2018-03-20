

num = 1
nextNum = 2
evenSum = 0


while (nextNum <= 4000000):
	if nextNum % 2 == 0:
		evenSum += nextNum 
	
	nextNum += num
	num = nextNum - num
	
	
print evenSum