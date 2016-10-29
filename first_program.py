"""
This is First Code in python that takes input string and print that string again along with its length.
"""


__author__= 'Vishwesh'

def first_function():

	message = raw_input("Please Enter Some thing: ")
	print type(message)
	print("Your Message :",message)
	print("Message Lenght ",len(message))
	
if __name__== "__main__":
	first_function()
