'''
Created on Oct 21, 2020

@author: your name here
'''


#1.  write a statement that will input a persons name
#    and store it in a variable name

userNames = []
userNames.append(input("enter user name: "))
userNames.append(input("enter user name: "))
userNames.append(input("enter user name: "))

#2.  write a statement that will input a person's age as an integer

userAges = []
userAges.append(int(input("enter user age: ")))

#3.  repeat steps 1 and 2 three times total saving the input in a different
#    variable each time (a total of three names and ages).

userAges.append(int(input("enter user age: ")))
userAges.append(int(input("enter user age: ")))

#4.  find the average age of the three people and store it in a 
#    new variable.  (add all three and divide by 3)

aveAge = (userAges[0] + userAges[1] + userAges[2]) / float(len(userAges))



#5.   print the statement "the average age of _____, _____, and _____
#    is _____."  each blank should be filled with the appropriate name
#    or the average age that you calculated. Example:  The average age
#    of Jim, Dan, and Joe is 17.33333333333333

print(f" the average age of {userNames[0]}, {userNames[1]}, and {userNames[2]} is {aveAge}")


#6.  Let's try to apply the mathematical formula for calculating
#    interest.  
#    The formula for interest in math class is A=P*(1+r)**t
#    A is the amount of money that you have at the end of t years
#    P is the principle or, in other words, the starting amount
#    r is the interest rate as a decimal, so 2.4% is 0.024
#    t is the length of time of the investment.  
#    Write a series of statements that will input all necessary 
#    information(everything except A), keeping in mind they are 
#    all numbers and all values can be a decimal.
#    Calculate the amount of money (A) at the end of an investment
#    print the following statement (be sure to round the values
#    representing money to 2 decimals):
#    "After investing _p__ dollars at a rate of __r__ for __t__ years
#    you now have __A__ dollars."


P = float(input("(no $ sign)enter how much money you have: "))
R = float(input("(no % sign)enter you interest rate in percent: "))
T = float(input("enter how many years you'll be investing: "))
A = P*(1+R/100)**T
print (f"you invested ${P} at a rate of %{R} for {T} years, you now have ${A}")


#7.  input your favorite video game as a string and store
#    it into a variable called game
game = input("enter you favorite videogame: ")


#8.  input the price of that game as a float and store it into a 
#    variable called price
gamePrice = float(input("enter the price of your favorite videogame: "))

#9.    write a print statement that will say:
#        "___game___:$___price___"  there should be NO SPACES after
#      the semi-colon and price should have 2 decimal spaces
#       no matter what.  You must use the format function on price
#       and sep for print

print(f" game:  is $")