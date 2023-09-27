import random

def miller_rabin(b, k):
    while True:
        print("første while")
        randint = random.randint(2**(b-1), 2**b - 1)
        if (randint % 2) != 0:
            if prime_test(randint, k):
                return randint

def prime_test(n, k):

    # Set n − 1 = 2^{s}d where s > 0 and odd number d > 0 
    s = n - 1
    d = 1
    while s % 2 == 0:
        print("andre while")
        s //= 2

    # Perform testing rounds
    for _ in range(k):

        print("range k")

        a = random.randint(2, n - 2)   #Generate a random integer from 2 to n-2 inclusive
        x = pow(a, d, n)
        y = 0
        for _ in range(s):

            print("range s")

            y = pow(x, 2, n)
            if (y == 1) and (x != 1) and (x != (n - 1)):
                return False
            x = y

        if (y != 1):
            return False
    return True


# Finding a 512 bit number and testing its primality :
b = 512
k = 1000

n = miller_rabin(b, k)

# Finding a seccond number and ensuring that the two numbers are not the same
while True:
    print("tredje while")
    n2 = miller_rabin(b,k)
    if n != n2:
        break

print(f"\nThe number \n{n} \nis probably prime")
print(f"\nThe number \n{n2} \nis another probable prime")