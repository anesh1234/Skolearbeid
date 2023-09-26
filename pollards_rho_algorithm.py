import math
import random

def pollard_rho(n):

    # The polynomial function g(x)
    def g(x, k):
        return (x**2 + 1) % n
    
    # Setting the start values
    #k = random.randint(2, n - 2)
    t = k
    h = t
    d = 1
    checkvar = 0

    # Forming the "Rho"-like-sequence using the polynomial function and finding GCD for each iteration
    while d == 1:
        t = g(t)
        h = g(g(h))
        d = math.gcd(abs(t - h), n)
        checkvar += 1
        print(checkvar)

    if d == n:
        # The algorithm failed to find a factor, try again with a different starting point
        return 0 #pollard_rho(n, k + 1)

    # A factor has been found, returnig the factor
    else:
        return d

# Using the Algorithm:
p1 = 13236194115964104703902862415812148871696282343519140367937221479351974709349661452569263794914812294244750567811545456611019007622776285166768397975112867
p2 = 11558395541614906973213701641967786161216081332381300761058031206021381967945981620438995924467438386705513165559014974225617034126770238633671052125770027
bool1 = False
bool2 = False

factor_p11 = pollard_rho(p1, 2)  # Calls the algorithm with the prime and a start value for the tortoise-and-hare-numbers, to find the non-trivial factor p
factor_p12 = p1 // factor_p11      # Calculates the other factor, q
if (factor_p11 * factor_p12) == p1:  # Verifying the result
    bool1 = True

factor_p21 = pollard_rho(p2, 2)
factor_p22 = p2 // factor_p21
if (factor_p21 * factor_p22) == p2:
    bool2 = True

# Printing the results to terminal
print("\nA factor of p1 is: ", factor_p11)
print("Which gives p1q1 = ", factor_p11, "*", factor_p12, "=", p1, "=", bool1)

print("\nA factor of p2 is: ", factor_p21)
print("Which gives p2q2 = ", factor_p21, "*", factor_p22, "=", p2, "=", bool2)