f = open('LargeSum.txt','U')
stream = f.read()
f.closed

replacable = stream[50]
stream = stream.replace(replacable," ")

data = []
row = []
for digit in stream:
	if digit == " ":
		data.append(row)
		row = []
	else:
		row.append(int(digit))
data.append(row)

columnSum = 0
sumDigits= []

for column in range(49,-1,-1):
	columnSum = (columnSum - columnSum % 10) / 10
	
	for index, row in enumerate(data):
		columnSum += row[column]
		if column == 49:
			print "row[" + str(column) + "]: " + str(row[column])

	if column == 0:
		for digit in reversed(str(columnSum)):
			sumDigits.insert(0,int(digit))
	else:
		sumDigits.insert(0,columnSum%10)
	

summation = ""
for i in sumDigits:
	summation += str(i)
	
print len(summation)
print summation