import string
alphabetValues = dict(zip(string.ascii_lowercase, range(1,27)))

totalNameSum = 0

with open("NamesScores.txt","r") as f:
	for line in f:
		names = line.split(",")
		names.sort()
		
	for index, name in enumerate(names):
		nameScore = 0
		name = name.replace('"','').strip().lower()
		for letter in name:
			nameScore += alphabetValues.get(letter)
		
		print nameScore
		print nameScore*index
		totalNameSum += nameScore*(index+1)
		

print totalNameSum