#!/usr/bin/python
import sys

# Dictionary to map countries to totals
country_sales = {}
country_qnty = {}
country_avg = {}

# Get input from stdin
for line in sys.stdin:
  #Remove spaces from beginning and end of the line
  line = line.strip()

  # parse the input from mapper.py to get country, item type, year, quantity and price
  country,item_type,year,qty,tot_price = line.split('\\')

  # convert total (currently a string) to float
  try:
	qty = int(qty)  	
	tot_price = float(tot_price)  
  except ValueError:
  	pass

	#update the dictionary
  try:
  	country_sales[country,item_type,year]    = country_sales[country,item_type,year] + tot_price
    country_qnty[country,item_type,year]     = country_qnty[country,item_type,year] + qty
	country_avg[country,item_type,year]      = country_sales[country,item_type,year]/country_qnty[country,item_type,year]
  except:
  	country_sales[country,item_type,year]    = tot_price
	country_qnty[country,item_type,year]     = qty
	country_avg[country,item_type,year]      = country_sales[country,item_type,year]/country_qnty[country,item_type,year]
 
# Write the tuples to stdout
# Q1.Average unit_price by country for a given item type in a certain year
print 'Q1. Average unit_price by country for a given item type in a certain year'

for country, item_type, year in sorted( ((v,k1,k2,k3) for k1,k2,k3,v in country_sales.iteritems()), reverse=True):
  print '%s\\%s\\%s\\%s'% (country,item_type,year,((country_sales[country,item_type,year])/(country_qnty[country,item_type,year])))
