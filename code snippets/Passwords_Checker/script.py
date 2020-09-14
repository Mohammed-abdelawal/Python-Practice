counter_total = 0
counter_true = 0
while(choice := input('Enter a new password: ') ):
    if choice.lower() == 'q':
        break 
    if len(choice) < 6 or len(choice) > 20 :
        print('Invalid length')
        counter_total+=1
        continue

    else :
        c_upper = False
        c_lower = False
        c_num = False
        for c in choice :
            if c.islower() :
                c_lower = True
            elif c.isupper() :
                c_upper = True
            elif c.isdigit() :
                c_num = True
        
        if not c_lower :
            print('At least one lower case letter needed')
        if not c_upper :
            print('At least one upper case letter needed')
        if not c_num :
            print('At least one number needed')
        if c_upper and c_lower and c_num :
            print('Valid password of length '+str(len(choice)))
            counter_true+=1
    counter_total+=1

print('You tried '+str(counter_total)+' passwords, '+str(counter_true)+' valid, '+str(counter_total-counter_true)+' invalid')