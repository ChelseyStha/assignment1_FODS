'''Program to take two int numbers and divide the first number by second and print the divison upto two decimal places'''
import math
#taking input from the user
numberA=int(input("Enter first number:"))
numberB=int(input("Enter second number:"))
#calculating the answer
Result= numberA/numberB
#using round to show the 2nd place value
rounded=round(Result,2)
#printing the answer
print(rounded) 
