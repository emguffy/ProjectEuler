# start on January 1, 1900
# days since January 1, 1900
dayCount = 1
months = [31,28,31,30,31,30,31,31,30,31,30,31]

SundayCount = 0

# we count Monday as 1, Tuesday as 2, ..., Sunday as 7

years = range(1900,2001,1)
for year in years:
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		months[1] = 29
	else:
		months[1] = 28
	
	for month in months:
		if dayCount % 7 == 0 and year > 1900:
			SundayCount += 1
		dayCount += month

print SundayCount