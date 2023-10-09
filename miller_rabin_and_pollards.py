import random
import math

def miller_rabin(b, k):
    while True:                                          # This loop runs as long as it takes to find an odd 512-bit number AND gets "probable prime" as the result of the miller-rabin test
        randint = random.randint(2**(b-1), 2**b - 1)     # Select a random number in the 512-bit range inclusive
        if (randint % 2) != 0:                           # Test the found number for oddity
            if prime_test(randint, k):                   # Run the miller-rabin test for the found number
                return randint                           # Return the 512-bit number if it is a probable prime

def prime_test(n, k):

    # Find n − 1 = 2^{s}d where the exponent s > 0 and the odd multiplier d > 0 
    s = 0
    d = n - 1
    while d % 2 == 0:                   # By demanding d % 2 == 0, I am demanding that the multiplier is even. When that is no longer true, an odd multiplier has been found
        s += 1                          # Add one to the exponent. This will always happen at least once, because the input n will always be odd, so that d will always be even in the first iteration
        d //= 2                         # Divide the multiplier and drop the remainder

    # Perform testing rounds
    for _ in range(k):                     # This loop will run k times
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

def pollard_rho(n, k):

    def g(x):                     # The polynomial function g(x)
        return (x**2 + 1) % n
    
    t = k       # Setting the start values
    h = k
    d = 1

    while d == 1:          # Forming the "Rho"-sequence using the polynomial function and finding GCD for each iteration
        t = g(t)
        h = g(g(h))
        d = math.gcd(abs(t - h), n)        # Finding the GCD

    if d == n:       # Check if a non-trivial factor has been found
        return 0     # The algorithm failed to find a factor
    else:
        return d     # A factor d has been found and it is returned
    
###############################################################################################################

# Finding a 512 bit number and testing its primality
b = 512
k = 30
n = miller_rabin(b, k)

# Finding a seccond number while ensuring that the two numbers are not the same
while True:
    n2 = miller_rabin(b, k)
    if n != n2:
        break


# Printing the results to the terminal
print(f"\nThe number \n{n} \nis probably prime")
print(f"\nThe number \n{n2} \nis another probable prime\n")

###############################################################################################################

# Factoring of (p_i - 1) / 2, i = 1, 2
num1 = int((n - 1) / 2)
num2 = int((n2 - 1) / 2)

arr = [num1, num2]            # An array containing the two integers to be factorized

for x in arr:                 # Looping through the two integers
    factorBool = False                  # Verification boolean for the p_i factorization
    userBool = True                     # Boolean enabling retries if the factorization is unsuccessful
    start_val = 2                       # Standard Pollards start value

    factor_p = pollard_rho(x, start_val)    # Calls Pollards with one integer and a start value for the tortoise-and-hare-number to find the non-trivial factor p

    while userBool:
        if factor_p == 0:
            response = input("\nFailed to find a factor, would you like to try again with a new start value? 1 = yes, 0 = no")
            if response == 1:
                factor_p = pollard_rho(x, start_val + 1)
            else:
                userBool = False
        else:
            userBool = False
            factor_q = x // factor_p          # Calculates the other factor, q
            if (factor_p * factor_q) == x:    # Verifying the result of the factorization
                factorBool = True

            # Printing the results to terminal
            if x == num1:
                num1FactorBool = False               # Verification of the factorization against the probable prime root
                if (x * 2 + 1) == n:
                    num1FactorBool = True
                print(f"\nA factor of  (p_1 - 1) / 2 is: ", factor_p)
                print("Which gives p_1q_1 = ", factor_p, "*", factor_q, "=", x, "=", factorBool)
                print("\n", num1FactorBool)
            else:
                num2FactorBool = False
                if (x * 2 + 1) == n2:
                    num2FactorBool = True
                print(f"\nA factor of  (p_2 - 1) / 2 is: ", factor_p)
                print("Which gives p_2q_2 = ", factor_p, "*", factor_q, "=", x, "=", factorBool)
                print("\n", num2FactorBool)