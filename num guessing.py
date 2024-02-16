import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)

    attempts = 0

    while True:
        guess = int(input(f"\nEnter your guess (between {lower_bound} and {upper_bound}): "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try Once again.")
        elif guess > secret_number:
            print("Too high! Try Once again.")
        else:
            print(f"Congratulations! You guessed the correct number {secret_number} and in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
