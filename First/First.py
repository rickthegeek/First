#Project: CIS 177 WEEK 1 PROJECT
#Project Location: projects\cis177\first
#File: first.py
#Purpose: Request input of user's first name, favorite color, and lucky number from standard input
#         Then print the data given to standard output
#Revision: 1.0 / 22 JAN 2017
#Created: 22 JAN 2017
#Author: Rick Miller <rick@rickthegeek.com>


#First, ask for the user's name.
firstName = input('Hi! What\'s your first name? ') #NOTE: Adding a space at the end of the prompts, they are not added automatically
#... now their favorite color ...
favoriteColor = input('Great! Now, what\'s your favorite color? ')
#... and finally their lucky number. Note that we are keeping it as a string in case the user enters "seven" instead of "7"
luckyNumber = input('Thanks! Now, what\'s your lucky Number? ')
#Now build the output. Using "sep" to allow suppress the space between the end of firstName and the apostrophe
print(firstName, end='', sep='') #and using "end" to keep the output on one line
print('\'s favorite color is',favoriteColor,'and lucky number is', luckyNumber)

