#   Filename:           miles_given_a_number_of_feet
#   Created by:         jasongreen
#   Date:               Saturday, January 12, 2019
#   Time of Creation:   12:07
#   ---

# number of miles given a number of feet

number_feet = (input("Please enter a number of feet. This will be calculated into miles: "))
cleaned_number = ''

for i in range(0, len(number_feet)):
    if number_feet[i] in "0123456789":
        cleaned_number = cleaned_number + number_feet[i]

cleaned_number_feet = cleaned_number
number_miles = int(cleaned_number_feet) / 5280

print("{0} feet = {1} miles!".format(number_feet, number_miles))