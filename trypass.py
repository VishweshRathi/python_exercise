"""
Code for try except finally else block
"""


__author__= 'Vishwesh'



def divide(x,y):
	try: 
		result=x/y
	except Exception, e:
		print 'Exception is ',e
	else :
		print 'result is',result
	finally:
		print 'executing final block'

	print '--------------------------------'
def factorial():
	divide(20,1)
	divide(20,0)

if __name__== "__main__":
	factorial()

