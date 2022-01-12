#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      08012
#
# Created:     02-01-2022
# Copyright:   (c) 08012 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
win_number=random.randint(1,100)
guess =-1
k=0
while win_number!= guess:

      g= int(input("Enter your guess"))
      guess =g
      k=k+1
      if guess == win_number:
          print("Won")
          print("Total number of guess",k)
      elif guess<win_number:
          print("too low")

      else:
           print("too high")
