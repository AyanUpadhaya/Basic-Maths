#checks if the year is a leap year

#if year is divisible by both 4 and 400

#and checks if year is divisble by 100 but remainder not equal to 0


year_list=[1992,1993,2000,2007,2014,2022,2024]

for year in year_list:
	if ((year%400==0) or (year%4==0) and (year%100!=0)):
		print(f'{year} is a leap year')
	else:
		print(f'{year} is not a leap year')