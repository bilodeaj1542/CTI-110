# Cti-110
# M3HW1 - Age Classifier
# Jason Bilodeau
# September 25, 2017
#

    
infant = 1
child = 13
teenager = 20
adult = 21

age = int(input('How old are you? '))
if age <= infant:
    print ('You are an infant')
else:
    if age <= child:
        print ('You are a child')
    else:
        if age <= teenager:
            print('You are a teenager')
        else:
            if age >= adult:
                print ('You are an adult')

