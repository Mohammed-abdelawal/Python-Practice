dog_age = int(input("Input dog's age: ")) # Do not change this line

base = 24

if dog_age >1 and dog_age<17 :
    print('Human age: '+str(base + (dog_age-2)*4))
elif dog_age == 1 :
    print('Human age: 15')
else : 
    print('Invalid age')