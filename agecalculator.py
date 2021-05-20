#Age calculator a beginners python project script by Ayan Upadhaya
#the program will launch and first will show current date and then will ask for
#birth year, month and day and will calculate your age.

#30 days has September, April, June and November.
#31 days in a year are January, March, May, July, August, October, December

#contact Ayan : ayanU881@gmail.com

from datetime import datetime

current=datetime.date(datetime.now())

data=str(current).split('-')

print(f"Current Date:{current}")

current_year=int(data[0])
current_month=int(data[1])
current_day=int(data[2])


thirty_first_days_month=[1,3,5,7,8,10,12]
thirty_days_month=[9,4,6,11]
twenty_days_month=[2]


def ageCalCulator(year,month,day):


	if (year<current_year and month<current_month and day<current_day):
		total_year=current_year-year
		total_month=current_month-month
		total_day=current_day-day
		print(f"you are {total_year} years {total_month} months and {total_day} days old")
	
	if (year<current_year and month<current_month and day>current_day):
		total_year=current_year-year
		total_month=(current_month-1)-month
		

		if month in thirty_days_month:
			total_day=(current_day+30)-day
		if month in thirty_first_days_month:
			total_day=(current_day+31)-day
		if month in twenty_days_month:
			total_day=(current_day+30)-day

		print(f"you are {total_year} years {total_month} months and {total_day} days old")


	if (year<current_year and month<current_month and day==current_day):
		total_year=current_year-year
		total_month=(current_month-1)-month
		total_day=current_day-day
		
		print(f"you are {total_year} years {total_month} months and {total_day} days old")
	
	if (year<current_year and month>=current_month and day>current_day):
		total_year=(current_year-1)-year
		total_month=(current_month+12)-(month+1)


		if month in thirty_days_month:
			total_day=(current_day+30)-day
		if month in thirty_first_days_month:
			total_day=(current_day+31)-day
		if month in twenty_days_month:
			total_day=(current_day+30)-day
		
		print(f"you are {total_year} years {total_month} months and {total_day} days old")
				

def main():
	try:
		birth_year=int(input("Enter Birth Year:"))
		birth_month=int(input("Enter Birth Month:"))
		birth_day=int(input("Enter Birth Day:"))
		ageCalCulator(birth_year,birth_month,birth_day)
	except ValueError:
		print("Wrong input start again?(y/n)")
		op=input()
		if op.lower()=='y':
			main()
		else:
			exit()


if __name__=="__main__":
	main()