import random

again = input('press y to roll: ')


while again == 'y':

    x = random.randint(1, 6)
    print('Dice Get : '+ str(x) )
    again = input('press y to roll again: ')
