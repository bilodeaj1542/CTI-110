# CTI- 110
# M3 HW1 Software Sales
# September 25, 2017
# Write a program to set discount levels for software

quantity_1 = 9
quantity_2 = 19
quantity_3 = 49
quantity_4 = 99
quantity_5 = 100

# Determine the quantity of software and display the discount 

quantity = float(input('Enter the total number of software packages ordered: '))
if quantity <= quantity_1:
    print ('Your total is $', quantity * 99) 
    print ('You do not qualify for a volume discount')
elif quantity <= quantity_2:
    print ('Your discount is', quantity * 99 * 0.1)
    print ('Your total is $', quantity * 99 - (quantity * 99 * 0.1))
elif quantity <= quantity_3:
    print ('Your discount is', quantity * 99 * 0.2)
    print ('Your total is $', quantity * 99 - (quantity * 99 * 0.2))
elif quantity <= quantity_4:
    print ('Your discount is', quantity * 99 * 0.3)
    print ('Your total is $', quantity * 99 - (quantity * 99 * 0.3))
elif quantity >= quantity_5:
    print ('Your discount is', quantity * 99 * 0.4)
    print ('Your total is $', quantity * 99 - ((quantity * 99) * 0.4)) 

    
