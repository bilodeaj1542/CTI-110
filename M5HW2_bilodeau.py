#CTI 110
# M5HW2: Running Total
# October 28, 2017
# Jason Bilodeau

running_total = 0
a = 0

while a >= 0:
    a = int(input("Enter a number: "))
    running_total = running_total + a

print ("Total: ", running_total - a) 
