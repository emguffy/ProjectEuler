import itertools

productList = []
panStrings = list(itertools.permutations(['1','2','3','4','5','6','7','8','9']))
print "len(panStrings): " + str(len(panStrings))

def is_pd_product(multiplicant, multiplier, product):
	if int(multiplicant) * int(multiplier) == int(product):
		return True
	else:
		return False

for perm in panStrings:
	for i_len in range(1,5):
		for j_len in range(1,6-i_len):
			m1 = ''.join(perm[0:i_len])
			m2 = ''.join(perm[i_len:i_len + j_len])
			p = ''.join(perm[i_len + j_len:])
			if is_pd_product(m1,m2,p):
				productList.append(p)
				print "m1: " + m1 + " m2: " + m2 + " p: " + p

print productList[1]

if __name__ == "__main__":
	productSum = 0
	for item in set(productList):
		productSum += int(item)
		
	print "productSum: " + str(productSum)









def is_unique(number):
	if ''.join(set(str(number))) == str(number):
		return True
	else:
		return False
		
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]		

