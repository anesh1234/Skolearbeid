import math
import random

def pollard_rho(n, k):

    def g(x):                     # The polynomial function g(x)
        return (x**2 + 1) % n
    
    t = k           # Setting the start values
    h = k
    d = 1
    checkvar = 0

    while d == 1:          # Forming the "Rho"-sequence using the polynomial function and finding GCD for each iteration
        t = g(t)
        h = g(g(h))
        d = math.gcd(abs(t - h), n)        # Finding the GCD

    if d == n:       # Check if a non-trivial factor has been found
        return 0     # The algorithm failed to find a factor
    else:
        return d     # A factor d has been found and it is returned

# Using the Algorithm:
p1 = 13236194115964104703902862415812148871696282343519140367937221479351974709349661452569263794914812294244750567811545456611019007622776285166768397975112866

factorBool = False
userBool = True
start_val = 2

factor_p = pollard_rho(p1, start_val)  # Calls the algorithm with the prime and a start value for the tortoise-and-hare-numbers, to find the non-trivial factor p

while userBool:
    if factor_p == 0:
        response = input("Failed to find a factor, would you like to try again with a new start value? 1 = yes, 0 = no")
        if response == 1:
            factor_p = pollard_rho(p1, start_val + 1)
        else:
            userBool = False
    else:
        userBool = False
        factor_q = p1 // factor_p      # Calculates the other factor, q
        if (factor_p * factor_q) == p1:  # Verifying the result
            factorBool = True

        # Printing the results to terminal
        print("\nA factor of p1 is: ", factor_p)
        print("Which gives p1q1 = ", factor_p, "*", factor_q, "=", p1, "=", factorBool)
