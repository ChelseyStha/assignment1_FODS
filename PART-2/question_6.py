'''program to find numbers divisible by 7 and multiples of 5 from 1500 to 2000'''

numbers = []

for num in range(1500, 2001):
   if num % 7 == 0 and num % 5 == 0:
       numbers.append(num)
print("Numbers divisible by 7 and multiples of 5 between 1500 and 2000 are:")
print(numbers)