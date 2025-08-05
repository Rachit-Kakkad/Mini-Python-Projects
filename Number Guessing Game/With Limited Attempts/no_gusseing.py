import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    secret_number = random.randint(lower, upper)
    max_attempts = 7
    attempts = 0

    print(f"Guess the number between {lower} and {upper}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < lower or guess > upper:
                print(f"Please enter a number between {lower} and {upper}.")
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Correct! The number is {secret_number}. You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if attempts == max_attempts and guess != secret_number:
        print(f"Sorry! The number was {secret_number}. Better luck next time.")

number_guessing_game()
# This code implements a simple number guessing game where the user has to guess a randomly generated number within a specified range.
# The user has a limited number of attempts to guess the number correctly.
# Feedback is provided after each guess, and the game ends when the user guesses correctly or runs out of attempts.                                             