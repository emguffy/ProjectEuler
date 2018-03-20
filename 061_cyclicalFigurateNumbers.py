import itertools
import math
import timeit

def is_triangel(num):
	return None
	
def is_square(num):
	return math.sqrt(num) == int(math.sqrt(num))
		
def is_triangle(num):
	n = int(math.sqrt(2 * num))
	isTriangle = False
	while n < math.sqrt(2 * num):
		if int(n**2 + n) == int(2 * num):
			isTriangle = True
			break
		else:
			n += 1
	return(isTriangle)
	
list3 = []	
for n in range(1,200):
	triNum = int(n*(n+1)/2)
	if len(str(triNum)) == 4:
		list3.append(triNum)
	
	
list4 = []
for n in range(1,200):
	squareNum = int(n**2)
	if len(str(squareNum)) == 4:
		list4.append(squareNum)
		
list5 = []
for n in range(1,200):
	pentNum = int(n*(3*n-1)/2)
	if len(str(pentNum)) == 4:
		list5.append(pentNum)
		
		
list6 = []
for n in range(1,200):
	hexNum = int(n*(2*n-1))
	if len(str(hexNum)) == 4:
		list6.append(hexNum)

list7 = []
for n in range(1,200):
	hepNum = int(n*(5*n-3)/2)
	if len(str(hepNum)) == 4:
		list7.append(hepNum)


list8 = []
for n in range(1,200):
	octNum = int(n*(3*n-2))
	if len(str(octNum)) == 4:
		list8.append(octNum)

answer = set()
listList = [list3,list4,list5,list6,list7,list8]
for listPerm in itertools.permutations(listList):
	for item1 in listPerm[0]:
		for item2 in listPerm[1]:
			if str(item1)[2:] == str(item2)[:2]:
				for item3 in listPerm[2]:
					if str(item2)[2:] == str(item3)[:2]:
						for item4 in listPerm[3]:
							if str(item3)[2:] == str(item4)[:2]:
								for item5 in listPerm[4]:
									if str(item4)[2:] == str(item5)[:2]:
										for item6 in listPerm[5]:
											if str(item5)[2:] == str(item6)[:2] and str(item6)[2:] == str(item1)[:2]:
												print(item1+item2+item3+item4+item5+item6)
												break
												
												

												