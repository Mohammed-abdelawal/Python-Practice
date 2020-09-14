# using recursion
import time


def countdown_seconds(x):
    if x == 0:
        print("We Done!")
        return
    else:
        time.sleep(1)
        print(x, "...")
        countdown_seconds(x-1)


def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)


def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)


# Test


print(factorial(7))
print(power(10, 10))
countdown_seconds(2)
