guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("WELCOME TO THE RIDDLE GAME!")

# 1st question
word = "towel"

print("What gets wet while drying?")
while guess != word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the answer: ")
        guess_count += 1
    else:
        out_of_guesses = True
        print("Out of guesses!")
        break

    if guess == word:
        print("You win!")
    else:
        print("Wrong guess!")


# ask for next question
yes_or_no = input("Press Y for next riddle and N to quit: ")

# 2nd question
if yes_or_no == "Y":
    print("What can you catch but not throw?")

    word = "cold"

    while guess != word and not(out_of_guesses):
        if guess_count <= guess_limit:
            guess = input("Enter the answer: ")
            guess_count += 1
        else:
            out_of_guesses = True
            print("Out of guesses!")

        if guess == word:
            print("You win!")
            break
        else:
            print("Wrong guess!")
            

elif yes_or_no == "N":
    print("You quit the game!")
    exit()


# ask for next question
yes_or_no = input("Press Y for next riddle and N to quit: ")

# 3rd question
if yes_or_no == "Y":
    print("What has many teeth but cannot bite?")

    word = "comb"

    while guess != word and not(out_of_guesses):
        if guess_count <= guess_limit:
            guess = input("Enter the answer: ")
            guess_count += 1
        else:
            out_of_guesses = True
            print("Out of guesses!")

        if guess == word:
            print("You win!")
            break
        else:
            print("Wrong guess!")
            

elif yes_or_no == "N":
    print("You quit the game!")
    exit()


# ask for next question
yes_or_no = input("Press Y for next riddle and N to quit: ")

# 4th question
if yes_or_no == "Y":
    print("What has lots of eyes but cannot see?")

    word = "potato"

    while guess != word and not(out_of_guesses):
        if guess_count <= guess_limit:
            guess = input("Enter the answer: ")
            guess_count += 1
        else:
            out_of_guesses = True
            print("Out of guesses!")

        if guess == word:
            print("You win!")
            break
        else:
            print("Wrong guess!")
            

elif yes_or_no == "N":
    print("You quit the game!")


print("End of the game!")
exit()