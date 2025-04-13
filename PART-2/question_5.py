'''Program to find simple interest from inputed values '''
#taking input for the principal, rate and time
principal = float(input("Enter the principal: ")) 
rate= float(input("Enter the rate of interest: ")) 
time= float(input("Enter the time period: ")) 

#calculating using the formula
simpleinterest = (principal * rate * time) / 100


print("The simple interest is:", simpleinterest)
#final answer displayed