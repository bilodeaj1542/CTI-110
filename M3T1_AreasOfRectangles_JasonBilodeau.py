# CTI 110
# M3T1 - Areas of Rectangles
# September 25, 2017
# Determine the area of two rectangles
# Determine if the rectagles are greater or equal to each other

# Get the dimensions of rectangle 1
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangel 1: '))

# Get the dimensions of rectangel 2
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

# Calculation - set area1 and area2 values bases on input
area1 = length1 * width1
area2 = length2 * width2

# Determine which rectangle has the greater area
if area1 > area2:
   print ('Rectangel one has the greater area')
elif area2 > area1:
   print ('Rectangle two has the greater area')
else:
    print ('Both have the same area.') 

