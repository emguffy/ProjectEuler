# champernownesConstant
dList = []
numberPointer = 1
divisor = 1
d = 1
while d < 1000001:
	strNum = str(numberPointer)
	for digit in strNum:
		if d % divisor == 0:
			dList.append(int(digit))
			divisor *= 10
		d += 1
	numberPointer += 1
	
print dList

dListProduct = 1
for multiple in dList:
	dListProduct *= multiple

print "dList Product: " + str(dListProduct)

	