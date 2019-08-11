#   Filename:           percent_from_two_numbers
#   Created by:         jasongreen
#   Date:               Saturday, January 12, 2019
#   Time of Creation:   12:07
#   ---

# Percent increase or decrease from two numbers

for i in range(0, 2):
    first_number = int(input("Please enter a number: "))
    second_number = int(input("Please enter a second number: "))
# number_difference = ''
# percent_increase = ''
# percent_decrease = ''

    if first_number < second_number:
        number_difference = second_number - first_number
        percent_increase = ((number_difference / first_number) * 100)
        print("The percent increase of your two numbers is: {}%".format(percent_increase))
        print("-" * 20)
    else:
        number_difference = first_number - second_number
        percent_decrease = ((number_difference / first_number) * 100)
        print("The percent decrease of your two numbers is {}%".format(percent_decrease))
        print("-" * 20)