secret_number = 7
attempt = 0
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number: "))
    attempt += 1
    if guess == secret_number:
        print("Congratulation! You guessed correctly.")
        print(attempt)
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")