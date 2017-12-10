# A program designed to convert feet to inches 
# December 10, 2017 
# CTI-110 M6T2_FeetToInches 
# Jason Bilodeau 
#

def main():
    feet = int(input('Enter total number of feet: '))
    print (feet, 'equals', feet_to_inches(feet), 'inches.') 


def feet_to_inches(feet):
    return feet * 12

main() 
