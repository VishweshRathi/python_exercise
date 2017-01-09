"""
This is First Code in python.
"""

import datetime
__author__= 'Vishwesh'

def panvalidate():
	
	aa=datetime.date(2026,12,11)
	aa+=datetime.timedelta(hours=4)
	ab=datetime.datetime.combine(aa,datetime.time(5))	
	print ab
	
#------------------------------------------------------------------------------------------
	Pan1= raw_input("Please Enter PAN Number: ")
	Pan= Pan1.upper()
	
	fourth = Pan[3].endswith('P') or Pan[3].endswith('F') or Pan[3].endswith('C') 
	if(len(Pan)==10 and Pan[0:5].isalpha() and fourth and Pan[5:9].isdigit() and Pan[9].isalpha()):	
		print 'valid'		
	else:
		print 'notvalid'
if __name__== "__main__":
	panvalidate()
