
maxDigitSum = 0
topRange = 100

for a in range(topRange):
	for b in range(topRange):
		digitSum = 0
		# print("Computing ",a,"**",b)
		for digit in str(a**b):
			digitSum += int(digit)
			if digitSum > maxDigitSum:
				maxDigitSum = digitSum
				
				
print("maxDigitSum: ",maxDigitSum)