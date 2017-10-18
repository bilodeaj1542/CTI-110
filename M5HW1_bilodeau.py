# M5HW1
# Distance Traveled Assignment 
# Jason Bilodeau
# October 18, 2017

speed= int(input('How fast were you going?: '))
hours_traveled = int(input('How many hours have you traveled?: '))
 
print ('Hours \t Distance Traveled')
print('---------------------------')
for currenthour in range (1, hours_traveled +1):
    distance_traveled = speed * currenthour
    print(currenthour, "\t", distance_traveled)
    



