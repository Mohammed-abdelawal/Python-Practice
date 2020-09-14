choice = input("Input f|a|b (fibonacci, abundant or both): ")

if choice == "f" :
    num = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:\n-------------------")
    pp = 0
    p = 1
    print(pp)
    print(p)
    for i in range(num-2):
        mynum = p+pp
        print(mynum)
        pp=p
        p = mynum
elif choice == "a":
    num = int(input("Input the max number to check: "))
    print("Abundant numbers:\n-----------------")
    for i in range(num+1):
        sum_of_divs = 0

        for x in range(1,i+1):

            if (i%x==0) and (i != x):
                sum_of_divs += x
        if sum_of_divs > i :
            print(x)
elif choice == "b":
    num = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:\n-------------------")
    pp = 0
    p = 1
    print(pp)
    print(p)
    for i in range(num-2):
        mynum = p+pp
        print(mynum)
        pp=p
        p = mynum
    num = int(input("Input the max number to check: "))
    print("Abundant numbers:\n-----------------")
    for i in range(num+1):
        sum_of_divs = 0

        for x in range(1,i+1):

            if (i%x==0) and (i != x):
                sum_of_divs += x
        if sum_of_divs > i :
            print(x)