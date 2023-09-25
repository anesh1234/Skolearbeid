import random

def miller_rabin(n, k):

    # Set n − 1 = 2^{s}d where s > 0 and odd number d > 0 
    s = 0 
    d = n - 1
    
    while d % 2 == 0:
        s += 1
        d //= 2

    # Perform testing rounds
    for _ in range(k):
        a = random.randint(2, n - 2)   #Generate a random integer from 2 to n-2 inclusive
        x = pow(a, d, n)

        for _ in range(s):
            y = pow(x, 2, n)
            if (y == 1) and (x != 1) and (x != (n - 1)):
                return False
            x = y

        if (y != 1):
            return False
    return True

# Using the algorithm:
n = 13236194115964104703902862415812148871696282343519140367937221479351974709349661452569263794914812294244750567811545456611019007622776285166768397975112867
n2 = 11558395541614906973213701641967786161216081332381300761058031206021381967945981620438995924467438386705513165559014974225617034126770238633671052125770027
k = 1000

is_prime = miller_rabin(n, k)
print(f"\nThe number \n{n} \nis {'probably prime' if is_prime else 'Composite'}")

is_prime = miller_rabin(n2, k)
print(f"\nThe number \n{n2} \nis {'probably prime' if is_prime else 'composite'}")