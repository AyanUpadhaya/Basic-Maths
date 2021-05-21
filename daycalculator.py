# The program checks what day it was or is of the year
# The program is written on mathematical calculation
# Script wrote by Ayan, contact : ayanu881@gmail.com


#month representing values

def main():
	months={
		"jan":1,
		"feb":4,
		"mar":4,
		"apr":0,
		"may":2,
		"jun":5,
		"jul":0,
		"aug":3,
		"sep":6,
		"oct":1,
		"nov":4,
		"dec":6
	}
	days_in_week=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]

	CURRENT_YEAR=2021

	while True:
		year=int(input("year input:"))
		wmonth=input("First three letters of month:")
		day=int(input("Enter day:"))

		if len(wmonth)>3 or day>31:
			print("Wrong Input, try again")
			continue

		#get last numbers of the year, I call it year extension
		year_ext=year-1900

		#check if the year is leap year so we can perform later calculation 
		def isleap_year():
			if year_ext%4==0: 
				return True
			return False

		#default value
		leap_day_cal=0
		
		if isleap_year():
			if wmonth=="feb" or wmonth=="jan":
				leap_day_cal=(year_ext/4)-1
			else:
				leap_day_cal=year_ext/4

		else:
			leap_day_cal=year_ext/4



		total_cal=leap_day_cal+year_ext+day+months[wmonth]

		which_day_of_weak=days_in_week[int(total_cal%7)]

		if year<CURRENT_YEAR:
			print(f"It was {which_day_of_weak}")
		elif year==CURRENT_YEAR:
			print(f"It is {which_day_of_weak}")
		else:
			print(f"It is {which_day_of_weak}")


		option=input("Do you want to give nother try:(y/n)")
		
		if option.lower()=='y' or option in ['y']:
			main()
		else:
			exit()


if __name__=="__main__":
	main()
	




