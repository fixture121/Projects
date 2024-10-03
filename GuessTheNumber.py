import random

def guess_the_number():
    print("\nGuess The Number!")
    print("\nI have a number between 1 and 100.")
    print("Try to guess the number!")
    print("\n(Enter '/' to exit game.)")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_input = input("\nEnter your guess: ")

        if user_input == '/':
            print("Exiting game. Goodbye!")
            break

        try:
            guess = int(user_input)
            attempts += 1

            if guess < secret_number:
                print("Your guess is too low, try again.")
            elif guess > secret_number:
                print("Your guess is too high, try again.")
            elif guess == "/":
                break
            else:
                print(f"Congratulations! Your guessed the correct number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number or '/' to exit game.")

if __name__ == "__main__":
    guess_the_number()
