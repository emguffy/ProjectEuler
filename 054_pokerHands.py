# Poker Hands

# One method would be to create a univeral ranking, whereby a hand is evaluated, then given a rank.
# The rank might be of multiple parts, such as 10000 for a royal flush; 91200 for a straight flush with
# a king high; 813.  Because you need to evaluate potentially all 5 cards in the system, this could 
# be a 12 digit number: The first two digits for rank, then the next 10 for describing the sub-ranks.
# Each hand would get a value, then you would just need to evaluate the two numbers and select the
# highest.

# 

def score_hand(pokerHand):
	print("hello")
	# find rank (10 functions: is_&rank... - if &rank, then apply score_rank function)
	
	# score rank (10 functions score_&rank... - returns score)

	# 

def is_royal_flush(pokerHand):
	print("hello")
	
def is_straight_flush(pokerHand):
	print("hello")
	
def is_four_kind(pokerHand):
	print("hello")

def is_full_house(pokerHand):
	print("hello")
	
def is_flush(pokerHand):
	print("hello")
	
def is_straight(pokerHand):
	print("hello")
	
def is_three_kind(pokerHand):
	print("hello")

def is_two_pair(pokerHand):
	print("hello")
	
def is_pair(pokerHand):
	print("hello")


class card():
	def __init__(self,value,suit,number):
		self.suit = suit
		self.order = order
		self.value = value
		
	def displayCard(self):
		print("suit: ",self.suit)
		print("value: ",self.order)
		

class pokerHand:
	def __init__(self,c1,c2,c3,c4,c5):
		self.c1 = c1
		self.c2 = c2
		self.c3 = c3
		self.c4 = c4
		self.c5 = c5
		
	def displayHand(self):
		print("Card 1: ",self.c1)
		print("Card 2: ",self.c2)
		print("Card 3: ",self.c3)
		print("Card 4: ",self.c4)
		print("Card 5: ",self.c5)
		
	def scoreHand(self):
		rank = getHandRank(self)
		#sort hand and list from highest value to lowest.
		score = for 
		
	def getHandRank(self):
		if is_royal_flush(self) == True
			return(10)
		else if is_straigt_flush(self) == True	
			return(09)
		else if is_four_kind(self) == True
			return(08)
		else if is_straigt_flush(self) == True	
			return(07)
		else if is_full_house(self) == True
			return(06)
		else if is_flush(self) == True	
			return(05)
		else if is_straight(self) == True
			return(04)
		else if is_three_kind(self) == True	
			return(03)
		else if is_two_pair(self) == True
			return(02)
		else if is_pair(self) == True	
			return(01)


			
	
	
	def is_royal_flush(self):
		print("hello")

	def is_straight_flush(self):
		print("hello")

	def is_four_kind(self):
		print("hello")

	def is_full_house(self):
		print("hello")

	def is_flush(self):
		print("hello")

	def is_straight(self):
		print("hello")

	def is_three_kind(self):
		print("hello")

	def is_two_pair(self):
		print("hello")

	def is_pair(self):
		print("hello")
		
#firstHand = pokerHand("AH","KD","10H","9S","2D")
#firstHand.displayHand()

print("hello")