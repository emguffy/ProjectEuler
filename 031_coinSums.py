### Coin Sums
poundCombos = 0

for pence200 in range(0,max(1,(200)/200 + 1)):
	for pence100 in range(0,(max(1,(200 - pence200*200)/100 + 1))):
		for pence50 in range(0,(max(1,(200 - pence200*200 - pence100*100)/50 + 1))):
			for pence20 in range(0,(max(1,(200 - pence200*200 - pence100*100 - pence50*50)/20 + 1))):
				for pence10 in range(0,(max(1,(200 - pence200*200 - pence100*100 - pence50*50 - pence20*20)/10 + 1))):
					for pence5 in range(0,(max(1,(200 - pence200*200 - pence100*100 - pence50*50 - pence20*20 - pence10*10)/5 + 1))):
						for pence2 in range(0,(max(1,(200 - pence200*200 - pence100*100 - pence50*50 - pence20*20 - pence10*10 - pence5*5)/2 + 1))):
							for pence1 in range(0,(max(1,(200 - pence200*200 - pence100*100 - pence50*50 - pence20*20 - pence10*10 - pence5*5 - pence2*2)/1 + 1))):
								cash = pence1 + 2*pence2 + 5*pence5 + 10*pence10 + 20*pence20 + 50*pence50 + 100*pence100 + 200*pence200
								if cash == 200:
									poundCombos += 1
									print "poundCombos: " + str(poundCombos)
