
f = open('008_in_largestProductInASeries.txt','U')
stream = f.read()
f.closed

replacable = stream[50]
stream = stream.replace(replacable," ")
print stream
print len(stream)

itemsInProduct = 13
lengthOfStream = 1000
currentMax = 1

for i in range(0,lengthOfStream-itemsInProduct+1):
	product = 1
	for j in range(0,itemsInProduct):
		product *= int(stream[i+j])
	if product > currentMax:
		currentMax = product
		
print currentMax
