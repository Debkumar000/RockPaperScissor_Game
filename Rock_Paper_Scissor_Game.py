import re
import random
print("Rock, Paper, Scissors - Shoot!")
print("_______________________________________________________________________________")
while 1<2:
    user=input("Enter your choice. R for roks, P for paper, S for scissors: ")
    if not re.match("[RrPpSs]", user):
        print("Please choose a valid charecter.")
        back=input("Press [Q] for quit the game. Otherwise press enter to continue the game.")
        if back.upper()=='Q':
            break
        else:
            continue
    else:
        print("Your choice is "+user)
    choices=['R','P','S']
    computer=random.choice(choices)
    print("Computer's choice is " +computer)
    if computer==str.upper(user):
        print("Tie")
    elif computer=='R' and user.upper()=='S':
        print("Computer win")
    elif computer=='S' and user.upper()=='P':
        print("Computer win")
    elif computer=='P' and user.upper()=='R':
        print("Computer win")
    else:
        print('You win')
    back=input("Press [Q] for quit the game. Otherwise press enter to continue the game.")
    if back.upper()=='Q':
        break
    else:
        continue