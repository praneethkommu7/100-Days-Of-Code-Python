from logo import rock, paper, scissors
from random import randint

# print(rock)
# print(paper)
# print(scissors)

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if my_choice > 2 or my_choice < 0:
    print("Invalid")
else:
    game = [rock, paper, scissors]
    print(game[my_choice])
    print('Computer chose:\n')
    computer_choice = randint(0, len(game) - 1)
    print(game[computer_choice])
    if my_choice >= 3 or my_choice < 0:
        print('You typed an invalid number, you lose!')
    elif my_choice == 0 and computer_choice == 2:
        print('You Win!')
    elif computer_choice == 0 and my_choice == 2:
        print('You Lose!')
    elif computer_choice > my_choice:
        print("You Lose!")
    elif my_choice > computer_choice:
        print('You Win!')
    elif my_choice == computer_choice:
        print('Draw')
