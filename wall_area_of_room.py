#   Filename:           wall_area_of_room
#   Created by:         jasongreen
#   Date:               Sunday, August 11, 2019
#   Time of Creation:   17:57
#   ---

# calculate wall area of a room
room_perimeter = int(input("Please enter the room's perimeter: "))
room_Height = int(input("Please enter the room height: "))

room_Wall_Area = room_perimeter * room_Height

print("The wall area of the room is: {0} square feet.".format(room_Wall_Area))