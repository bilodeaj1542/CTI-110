#CTI 110
# M6T1 Kilometer conversion program
# December 10, 2017
# Jason Bilodeau



def main(): 
    kilometers = float(input('Enter the total number of kilometers: '))

    show_miles (kilometers)


def show_miles (km): 
    miles = km * 0.6214
    print (km, 'Kilometers equals', format(miles, '.2f') , 'miles')


main () 
    



