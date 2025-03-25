'''program to count the number of letters and digits of inputted string'''
text = input("Enter a string: ")

num_digits = sum(char.isdigit() for char in text)
num_letters = sum(char.isalpha() for char in text)


print("Number of letters:", num_letters)
print("Number of digits:", num_digits)
