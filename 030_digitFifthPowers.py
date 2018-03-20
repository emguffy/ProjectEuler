digitFifthPowers = []

fifthPowers = []
for digit in range(0,10):
	fifthPowers.append(digit**5)


def fifthPowerSum(number):
	fifthPowerSum = 0
	for digit in str(number):
		fifthPowerSum += fifthPowers[int(digit)]
	return fifthPowerSum
		
for number in range(2,10000000):
	if fifthPowerSum(number) == number:
		digitFifthPowers.append(number)
		
print digitFifthPowers
print sum(digitFifthPowers)
# for number in 

print "1**5: " + str(1**5)
print "2**5: " + str(2**5)
print "3**5: " + str(3**5)
print "4**5: " + str(4**5)
print "5**5: " + str(5**5)
print "6**5: " + str(6**5)
print "7**5: " + str(7**5)
print "8**5: " + str(8**5)
print "9**5: " + str(9**5)
