secret_number = 42
guess = None
print(
    """**** Instructions to play the Number Guessing Game ****
>> First enter a valid number
>> The program will compare your number to a secret number
>> If it matches to the secret number, Congrats you gussed it right otherwise it'll keep asking you to guess the secret number """
)
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
print("Game over!")
