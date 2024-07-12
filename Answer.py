class Gig():

    def __init__(self):
        pass

    def check(): #CHECKING IF VALID INPUT
        try:
            n=float(input())
            Gig.calculation(n) # CALLING CALCULATION FUNCTION
        except:
            print('Invalid input') # MESSAGE FOR Invalid input

    def calculation(n):
        calib_factor=1.0 # CALIBRATION FACTOR SET AT 1 mm² = 1 gram
        answer=n*calib_factor
        print('The required powder amount is',answer)


# INPUT PROMPT
print('Enter the desired area in square millimeters')
Gig.check()






