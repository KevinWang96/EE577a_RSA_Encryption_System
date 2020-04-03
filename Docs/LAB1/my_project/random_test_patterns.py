""" 
	This program is used for generating some random binary input patterns 
	to test the functionality of circuits 
	By Yihao Wang 
"""

import os
import random
## conversion from binary to decimal, returns a string(this function is not used by random generator)
def bin_to_dec (num):
    the_num = num
    count = 0
    dec = 0
    while the_num != 0 :
		## note that **
        dec += (the_num %  10) * (2 ** count)
		
		## division of python returns a float number
        the_num = int(the_num / 10)
        count = count + 1
    return str(dec)

## conversion from decimal to binary num, returns a string
def dec_to_bin (num,width):
    the_num = num
    bin_str = ''
    if (num < 0):
            print('the parameter must be [0,255]!')
    else:
        for num in range(width):
            bin_str = str(the_num % 2) + bin_str 
            the_num = get_quotient(the_num, 2)
        return bin_str

## gets the remainder
def get_quotient (dividend, divider):
    the_dividend = dividend
    the_divider = divider
    quotient = 0
    while the_dividend >= the_divider :
        the_dividend -= the_divider
        quotient += 1
    return quotient

## Generates random input patterns based on user's configuration
## Parameters:
## 		width: the width of binary input patterns (defalt value: 8)
##		number: the number of input patterns you want to generate (default value: 30)
##		clk: clk period (default value: 10)
##      unit: time unit (default: ns)
##		slope: the slope of input signal (default value: 0.01)
##		vih: voltage of logic high (default value: 1.8V)
##		vil: voltage of logic low (default value: 0V)
def random_generator(width = 8, number = 30, clk = 10, delay  = 2, unit = 'ns', slope = 0.01, vih = 1.8, vil = 0):
	time = delay
	## gets user's work directory
	os.chdir(input('Please input your work directory: '))
	with open(input("Please enter output file name: "), "w") as the_file:
	
		count = width - 1
		print('radix', file = the_file, end = ' ')
		for i in range(width * 2) :
			print('1', file = the_file, end = ' ')
		
		print('\nio', file = the_file, end = ' ')
		for i in range(width *2) :
			print('i', file = the_file, end = ' ')
		print('\nvname', file = the_file, end = ' ')
		for i in range(width) :
			print('X' + str(count), file = the_file, end = ' ')
			count -= 1
		count = width - 1	
		for i in range(width) :
			print('Y' + str(count), file = the_file, end = ' ')
			count -= 1
			
		print('\ntunit ' + str(unit), file = the_file)
		print('slope ' + str(slope), file = the_file)
		print('vih ' + str(vih), file = the_file)
		print('vil ' + str(vil), file = the_file)

		for num in range(number) :
			print(time, end = ' ', file = the_file)
			print(dec_to_bin(int(random.random() * (2 ** width)),width), end = ' ', file = the_file)
			print(dec_to_bin(int(random.random() * (2 ** width)),width), end = '\n', file = the_file)
			time += clk
			
		print('Successfully Generated!')

