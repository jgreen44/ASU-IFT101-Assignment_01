#   Filename:           wall_area_of_room2
#   Created by:         jasongreen
#   Date:               Saturday, January 12, 2019
#   Time of Creation:   12:07
#   ---

# calculate wall area of room NOT
# including two windows and a door
# I'm sure I could do this in an array, but don't know how.

room_perimeter = int(input("Please enter the room's perimeter: "))
room_Height = int(input("Please enter the room height: "))
window_one_height = int(input("Please enter the height of Window #1: "))
window_one_width = int(input("Please enter the width of Window #1: "))
window_two_height = int(input("Please enter the height of Window #2: "))
window_two_width = int(input("Please enter the width of Window #2: "))
door_height = int(input("Please enter the door height: "))
door_width = int(input("Please enter the door width: "))

window_one_area = window_one_width * window_one_height
window_two_area = window_two_width * window_two_height
door_area = door_width * door_height

room_Wall_Area_noWindow_noDoor = ((room_perimeter * room_Height) -
                                  ((window_one_area +
                                    window_two_area +
                                    door_area)))
print("The wall area of the room without doors and windows is: {0} square feet.".format(room_Wall_Area_noWindow_noDoor))