import random 
import math

upper = int(input("Enter the upper number: "))
lower = int(input("Enter the lower number: "))
x = random.randint(lower, upper)

Nog = round(math.log(upper - lower + 1, 2))
print("\nYour number of guesses are:", Nog)

count = 0

while count < Nog:
    guess = int(input("Enter your guess: "))
    count = count + 1

    if guess == x:
        print("Congratulations! You guessed it right. The number is {}.".format(x))
        break
    elif guess < x:
        print("The number you guessed is too low.")
    elif guess > x:
        print("The number you guessed is way too high.")


    