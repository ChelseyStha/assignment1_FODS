'''Program to take two int numbers and divide the first number by second and print the divison upto two decimal places'''
import math

numberA=int(input("Enter first number:"))
numberB=int(input("Enter second number:"))
Result= numberA/numberB
rounded=round(Result,2)
print(rounded) 
