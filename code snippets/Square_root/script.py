import math

start_int = int(input("Input starting integer: "))

sq = math.sqrt(start_int)
print(round(sq,4))
while(sq>2):
    sq = math.sqrt(sq)
    print(round(sq, 4))