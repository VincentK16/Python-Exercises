import random

number = random.randint(0,9)

trial =0

while True:
    player = int(input("Guess one number from 0 to 9: "))
    if player == 'exit':
        break
    trial += 1

    if player == number:
        print("Congratulations! You guessed it right! The number is {} ".format(number))
        break
    elif player != number:
        if number < player:
            print ("Too high!")
        else:
            print("Too Low!") 

print("Number of trials: {}. THANK YOU!".format(trial))