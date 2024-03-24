import random

# User choice
user=int(input('What do you want to choose? Type 0 for rock, 1 for paper, 2 for scissors:  '))
choices=['rock','paper','scissors']
print('You chooses:', choices[user])

# Computer choice
computer=random.randint(0,2)
print('computer chooses: ',choices[computer])

# Scenerio of game
if(computer>=3 and user<=0):
    print('Invalid Number. Type a number between 0 and 2')
elif(computer==0 and user==2):
    print('You Win!')
elif(computer==2 and user==0):
    print('You Loose!')
elif(computer>user):
    print('You Loose!')
elif(computer<user):
    print('You Win!')
elif(computer==user):
    print("It's a draw")