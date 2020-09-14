from termcolor import colored

mark = '.'

width = 110
height = 30
red = int(height /3)

for i in range(1,height):
    x = 0
    if i < int((height/2))+1 :
        x = i*2
        print(colored(mark*x,'red','on_red'),end='')
    else :
        x = 2*(height - (i))
        print(colored(mark*x,'red','on_red'),end='')

    if i < red :
        print(colored(mark*(width-x),'grey','on_grey'))
    elif i < red*2 :
        print(colored(mark*(width-x),'white','on_white'))
    else :
        print(colored(mark*(width-x),'green','on_green'))

print(colored('Mohammed Abdelawal','magenta'))

