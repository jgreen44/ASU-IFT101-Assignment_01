#   Filename:           sale_price
#   Created by:         jasongreen
#   Date:               Saturday, January 12, 2019
#   Time of Creation:   12:07
#   ---

# the sale price of an item given the original amount and discount percentage

original_price = int(input("What is the original price? "))
percent_discount = int(input("What is the percent discount? "))

percent_discount = percent_discount * 0.01
amount_off = original_price * percent_discount

sale_price = original_price - amount_off

print("The sale price is ${}".format(sale_price))