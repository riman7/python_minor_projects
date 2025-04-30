import random

number = random.randrange(1,100)
guess_count = 0
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
    except ValueError:
        print("Enter a valid number")
    if not guess > 1 and guess <100:
        print("Enter a valid number")
        
    if guess == number:
        print(f"Correct! Congratulations, you guessed the number in just {guess_count} tries.")
        break

    elif guess < number:
        print("Number you guessed is low")
    else:
        print("Number you guessed is high")
    guess_count += 1