"""
Name:           problem1.py
Description:    The program will use a for loop to       determind what group a team is in or if they're eleminated

Author:         Lauren M

Created:     03/03/2021
"""

print = " TOURNAMENT TRACKER "

my_string = 0

#the program will use a fro loop to allow the user to enter "W" or "L"
for i in range(6):
  w_l = str(input("Enter the wins and losses for your team: "))
  if w_l == "W":
    my_string += 1

#the program will compute and output the group 
if my_string in [5, 6]:
  print: "Your team is in group 1!"

elif my_string in [3, 4]:
  print: "Your team is in group 2!"

elif my_string in [1, 2]:
  print: "Your team is in group 3!"

else:
  print: "Your team is eleminated from the tournament"