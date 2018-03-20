from string import maketrans

ones = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
tens = {20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
hundreds = {100:"one hundred",200:"two hundred",300:"three hundred",400:"four hundred",500:"five hundred",600:"six hundred",700:"seven hundred",800:"eight hundred",900:"nine hundred"}


def number_to_words(number):
	words = ""
	if number == 1000:
		words = "one thousand"
	else:
		if number > 99:
			words = hundreds.get((number / 100) * 100)
			if number % 100 != 0:
				words = words + " and "
				
		remainder = number % 100
		if remainder > 0 and remainder < 20:
			words = words + ones.get(remainder)
		elif remainder >= 20:
			tensDigit = (remainder / 10) * 10
			words = words + tens.get(tensDigit)
			onesDigit = remainder % 10
			if onesDigit != 0:
				words = words + "-" + ones.get(onesDigit)
	
	return words

def count_letters(stringNumber):
	stripHyphens = stringNumber.replace("-", " ")
	stripSpaces = stripHyphens.replace(" ","")
	return len(stripSpaces)

totalCount = 0
for i in range(1,1001):
	totalCount += count_letters(number_to_words(i))


print totalCount