import string

def is_triangle_number(candidate):
	if candidate == int((candidate*2)**.5)*(int((candidate*2)**.5)+1)/2:
		return True
	else:
		return False

wordList = []
f = open('codedTriangleNumbers.txt')
for line in f:
	splitLine = line.split(",")
	for word in splitLine:
		wordList.append(word.strip('"'))

print len(wordList)
print wordList[1]

alphabet = dict(zip(string.ascii_lowercase, range(1,27)))
print alphabet
triangleWords = []

for word in wordList:
	wordSum = 0
	for letter in word:
		wordSum += alphabet.get(letter.lower())
	if is_triangle_number(wordSum):
		triangleWords.append(word)	
		print word

print len(triangleWords)

'''	
	
for i in range(1,100):
	if is_triangle_number(i):
		print "Triangle Number: " + str(i)
	else:
		print "Not triangle number: " + str(i)
'''