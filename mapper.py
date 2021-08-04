#!/usr/bin/python
import sys
import datetime

input_file = sys.stdin
next(input_file) # skip first line of input file

# Get input lines from stdin
for line in input_file:
    # strip the spaces
    line = line.strip()

    # Split tokens
    tokens = line.split(',')
    
    #Get country, price and quantity values
    try:
  	country = tokens[2]
  	item_type = tokens[3]

  	date = tokens[6]
  	dt_obj = datetime.datetime.strptime(date,'%d-%m-%Y %H:%M') 
  	year = dt_obj.year

  	tot_price = float(tokens[12])
  	qty = int(tokens[9])
  	print '%s\\%s\\%d\\%d\\%s' % (country, item_type, year, qty,tot_price)
    
    except ValueError: 
  	pass