"""
Code for finding the Factorial of number
"""


__author__= 'Vishwesh'

def factorial():
	fact=1
 	num = input("Please Enter the number: ")
	
	while num>0:
		fact = fact * num
		num = num - 1
	print fact
	
if __name__== "__main__":
	factorial()
