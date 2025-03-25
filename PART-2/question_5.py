'''Program to find simple interest from inputed values '''

principal = float(input("Enter the principal: ")) 
rate= float(input("Enter the rate of interest: ")) 
time= float(input("Enter the time period: ")) 


simpleinterest = (principal * rate * time) / 100


print("The simple interest is:", simpleinterest)
