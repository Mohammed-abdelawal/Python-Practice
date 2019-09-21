# GCD Algorithm is find the greatest denominator of two nums
# using Euclid's algorithm


def gcd(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b
    return a


# test our function
print(gcd(20, 8))
print(gcd(96, 60))
