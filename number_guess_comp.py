import random       #random library allows to generate random things

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Too Low!")
        elif guess > random_number:
            print("Too high")
    
    print("Congrats. Correct number guessed!")

guess(10)