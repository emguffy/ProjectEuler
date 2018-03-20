# Digit Canceling Fractions

dcfDenominatorList = []

def is_same_fraction(num,denom):
	if str(num)[0] == str(denom)[0] and float(str(num)[1])/float(str(denom)[1]) == float(num)/float(denom):
		return True
	elif str(num)[1] == str(denom)[0] and float(str(num)[0])/float(str(denom)[1]) == float(num)/float(denom):
		return True
	elif str(num)[0] == str(denom)[1] and float(str(num)[1])/float(str(denom)[0]) == float(num)/float(denom):
		return True
	elif str(num)[1] == str(denom)[1] and float(str(num)[0])/float(str(denom)[0]) == float(num)/float(denom):
		return True
	else:
		return False

print is_same_fraction(49,98)


for i in range(11,100):
	for j in range(i + 1,100):
		if i % 10 != 0 and j % 10 != 0:
			if is_same_fraction(i,j) == True:
				print "i: " + str(i)
				print "j: " + str(j)
				dcfDenominatorList.append(j)
				
print "dcfDenominatorList: "
print dcfDenominatorList
