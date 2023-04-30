import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":      #c for correct
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low     #or high if guessed high
        
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        if feedback == "h":
            high = guess-1
        elif feedback == "l":
            low = guess+1
    
    print("Correct guess by the computer!")

computer_guess(1000)