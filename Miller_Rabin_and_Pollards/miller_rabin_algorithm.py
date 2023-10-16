import random
import time

def miller_rabin(b, k):
    st = time.time()
    while True:                                      # This loop runs as long as it takes to find an odd 512-bit number AND gets "probable prime" as the result of the miller-rabin test
        randint = random.randint(2**(b-1), 2**b - 1)     # Select a random number in the 512-bit range inclusive
        if (randint % 2) != 0:                           # Test the found number for oddity
            if prime_test(randint, k):                      # Run the miller-rabin test for the found number
                et = time.time()
                elapsed_time = et - st
                return randint, elapsed_time                # Return the 512-bit number if it is a probable prime and the time it took to find it

def prime_test(n, k):

    # Find n − 1 = 2^{s}d where the exponent s > 0 and the odd multiplier d > 0 
    s = 0
    d = n - 1
    while d % 2 == 0:                   # By demanding d % 2 == 0, I am demanding that the multiplier is even. When that is no longer true, an odd multiplier has been found
        s += 1                          # Add one to the exponent. This will always happen at least once, because the input n will always be odd, so that d will always be even in the first iteration
        d //= 2                         # Divide the multiplier and drop the remainder

    # Perform testing rounds
    for _ in range(k):
        a = random.randint(2, n - 2)            # Generate a random integer from 2 to n-2 inclusive, because n will always be a probable prime for base 1 and n - 1.
        x = pow(a, d, n)                        # The pow(a,b,c)-function generates the expression a^b mod c
        y = 0

        for _ in range(s):
            y = pow(x, 2, n)
            if (y == 1) and (x != 1) and (x != (n - 1)):
                return False
            x = y

        if (y != 1):
            return False
    return True
