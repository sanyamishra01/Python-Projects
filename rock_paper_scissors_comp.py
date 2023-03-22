#against computer

import random

def play():
    name = input("Enter your name: ")
    
    x = int(input("How many times do you want to play: "))
    for i in range (0,x):       #for number of chances (x)
        user = input("'r' for rock, 'p' for papers, 's' for scissors': ")
        computer = random.choice(['r','p','s'])
        print(f'Computer chose: {computer}')

# r>s p>r s>p

        if user == computer:
            print('tie')
        elif (user == 'r' and computer == 'p') or (user == 's' and computer == 'r') or (user == 'p' and computer == 's'):
            print('computer wins!')
        elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or(user == 's' and computer == 'p'):
            print(f'{name} wins!')

play()