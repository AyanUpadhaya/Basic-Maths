#Python Program to Find Prime Number using For Loop
#Any natural number that is not divisible by any other number except 1 and itself 
#called Prime Number.

user_num=int(input("Enter a number:"))

def is_prime(num):

	count=0

	for i in range(2,(num//2+1)):
		if num%i==0:
			count+=1
			break
	if count==0 and num!=1:
		print(f"{num} is a prime number")
	else:
		print(f"{num} is not a prime number")

is_prime(user_num)
		
