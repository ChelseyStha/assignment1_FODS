'''program to find Euclidean distance between the two points from the inputted value'''
import math
#taking input from user for the points
x1 = float(input("Enter the first point: "))
y1 = float(input("Enter the first point: "))
x2 = float(input("Enter the second point: "))
y2 = float(input("Enterthe second point: "))
#calcualting the distance using euclidean formula
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Euclidean distance between the two points is", distance)
#display the distance