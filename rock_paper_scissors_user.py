#against user

def play():
    user1_name = input("Enter 1st user's name: ")
    user2_name = input("Enter 2nd user's name: ")

    x = int(input("How many times do you want to play: "))

    for i in range(0,x):
        user1 = input("'r' for rock, 'p' for papers, 's' for scissors': ")
        user2 = input("'r' for rock, 'p' for papers, 's' for scissors': ")

#r>s p>r s>p
        if user1 == user2:
            print('tie')
        elif (user1 == 'r' and user2 == 's') or (user1 == 'p' and user2 == 'r') or (user1 == 's' and user2 == 'p'):
            print(f'{user1_name} wins!')
        elif (user1 == 's' and user2 == 'r') or (user1 == 'r' and user2 == 'p') or (user1 == 'p' and user2 == 's'):
            print(f'{user2_name} wins!')

play()