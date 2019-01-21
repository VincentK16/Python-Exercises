# Python3 

import random

options = ['rock', 'paper', 'scissors']

while True:
    player = input('Your choice (rock, paper, scissors):')
    opponent = options[random.randint(0,2)]
   
    if player == options[0] and opponent == options[2]:
        print('Congrats! You won! {} {}'.format(player,opponent))
        break
    elif player == options[1] and opponent == options[0]:
        print('Congrats! You won! {} {}'.format(player,opponent))
        break
    elif player == options[2] and opponent == options[1]:
        print('Congrats! You won! {} {}'.format(player,opponent))
        break
    elif player == opponent:
        print('It is a draw! Try again in next round. {} {}'.format(player, opponent))
        break
    else:
        print("You loose :(".format(player, opponent))
        break

