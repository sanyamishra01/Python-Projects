def guess(random_number, x):
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess any number between 1 and {x}: "))

        if guess < random_number:
            print("Too Low!")
        elif guess > random_number:
            print("Too High")
    
    print("Congrats! Correct guess.")

guess(5, 10)
