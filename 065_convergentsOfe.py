import math
from decimal import *
from fractions import Fraction
getcontext().prec = 200

#print(Decimal(1).exp())

# infinite continued fractions are oscillating around the target as they converge.
# As such, you should be selecting floor, then ceiling, then floor, then ceiling...
#print(math.sqrt(2))

target = Decimal(1).exp()
print("target: ",target)
topRange = 100
#convergents = []

#convergents.append(2)
#print(convergents)

#inverse = Decimal(1).exp()

def calcInfContFrac(seqIn):
	fracDecimal = 0
	# work backwards through sequence
	for s in range(len(seqIn)-1,0,-1):
		fracDecimal = Decimal(1/(fracDecimal + seqIn[s]))
		#print("seqIn[s]: ",seqIn[s])
		#print("s: ",s)
		#print("fracDecimal: ",fracDecimal)
		
	return fracDecimal + seqIn[0]
	
	
seqList = [math.floor(target)]
approx = seqList[0]
print("approx: ",approx)

for i in range(1,topRange):
	trigger = True
	j = 0
	testSeq = seqList
	while trigger:
		j = j + 1
		#print("j: ",j)	
		testSeq = seqList + [j]
		#print("testSeq: ",testSeq)	
		newApprox = calcInfContFrac(testSeq)
		#print("newApprox: ",newApprox)
		if ((newApprox > target) == (approx > target)):
			trigger = False
			#print("trigger: ",trigger)
			seqList.append(j-1)
			if abs(approx - target) < abs(newApprox - target):
				print("Stop!!!!")
		
	approx = calcInfContFrac(seqList)
print("seqList: ",seqList)


numerator = 1
print("numerator: ",numerator)

denominator = seqList[len(seqList)-1]
print("denominator: ",denominator)


for i in range(len(seqList)-2,-1,-1):
	x = seqList[i]
	numerator1 = denominator
	denominator1 = x*denominator + numerator
	
	denominator = denominator1
	numerator = numerator1

numeratorFinal = denominator
denominatorFinal = numerator
	
print("numeratorFinal: ",numeratorFinal)
print("denominatorFinal: ",denominatorFinal)

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

print("answer: ",sum_digits(numeratorFinal))
print(Decimal(numeratorFinal/denominatorFinal))

print("reduced: ",Fraction(numeratorFinal, denominatorFinal))