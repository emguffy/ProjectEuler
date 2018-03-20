def sum_digits(num):
	strNumber = str(num)
	digitSum = 0
	for digit in strNumber:
		digitSum += int(digit)
	return digitSum
	

expo = 1000
print sum_digits(2**expo)