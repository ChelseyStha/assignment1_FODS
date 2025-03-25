'''Program to generate a random number and be able to guess the number 5 times, then make it end after 5 tries'''
import random

# Generate a random number 
answer = random.randint(1, 100)
for attempt in range(1, 6):

    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

   
    if guess > answer:
        print("Too high!")
    elif guess < answer:
        print("Too low!")
    else:
        print("Correct number! You win!")
        break
else:
    
    print("Game Over! The correct number was:", answer)