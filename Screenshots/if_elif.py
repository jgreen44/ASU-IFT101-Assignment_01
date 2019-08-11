#   Filename:           if_elif
#   Created by:         jasongreen
#   Date:               Saturday, January 12, 2019
#   Time of Creation:   12:07
#   ---

firstNumber = int(input("Please enter a number: "))
secondNumber = int(input("Please enter another number: "))
thirdNumber = int(input("Please enter your last number: "))


# this code is obviously not robust because it does not
# check to see if a user enters the same number more
# than once, and therefore the if/elif statement will
# not be entered!
if (thirdNumber > (firstNumber and secondNumber)):
    print("The largest number is: {0}".format(thirdNumber))
elif (secondNumber > (thirdNumber and firstNumber)):
    print("The largest number is: {0}".format(secondNumber))
elif (firstNumber > (secondNumber and thirdNumber)):
    print("The largest number is: {0}".format(thirdNumber))

