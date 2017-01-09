"""
This is First Code in python.
"""


__author__= 'Vishwesh'



def divide(x,y):
	try: 
		result=x/y
	except Exception, e:
		print 'Exception is ',e
	else :
		print 'result is',result

	print '--------------------------------'
def factorial():
	divide(20,1)
	divide(20,0)

if __name__== "__main__":
	factorial()

