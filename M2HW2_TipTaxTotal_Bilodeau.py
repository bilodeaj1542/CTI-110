# CTI-110
# M2HW2 - Tip Tax Total
# Jason Bilodeau
# September 10, 2017
# This program will calculate the total cost of a meal based upon user input of how much the meal costs.
# It will then calculate the tip, tax, and finally the total

foodcost = float(input("How much did your meal cost before tax and tip? "))
salestax = foodcost * 0.07
tip = foodcost * 0.18
totalcost = foodcost + salestax + tip
print ("Your Total Cost of Your Meal is: ", totalcost) 
