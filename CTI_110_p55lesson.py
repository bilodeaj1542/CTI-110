# CTI-110
# Calculating a Percentage p55
# Jason Bilodeau
# September 10, 2017
# This program will calculate a percentage off of an item that is on sale and then output the final price to the user

original_price = float(input("Enter the item's original price "))
discount = original_price * 0.20
sale_price = original_price - discount
print ("The sale price is ", sale_price) 
