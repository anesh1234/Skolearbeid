import math

def pollard_rho(n, k):

    # The polynomial function g(x)
    def g(x):
        return (x**2 + 1) % n
    
    # Setting the start values
    t = k
    h = t
    d = 1

    # Forming the "Rho"-sequence using the polynomial function and finding GCD
    while d == 1:
        t = g(t)
        h = g(g(h))
        d = math.gcd(abs(t - h), n)

    if d == n:
        # The algorithm failed to find a factor, try again with a different starting point
        return pollard_rho(n, k + 1)

    # A factor has been found, returnig the factor
    return d

# Using the Algorithm:
p1 = 123456789
p2 = 123456789

factor_p11 = pollard_rho(p1, 2)   # Calls the algorithm with the prime and a start value for the tortoise-and-hare-numbers, to find the non-trivial factor p
factor_p12 = p1 // factor_p11      # Calculates the other factor, q

factor_p21 = pollard_rho(p2, 2)
factor_p22 = p2 // factor_p21

print("\nA factor of p1 is: ", factor_p11)
print("Which gives p1q1 = ", factor_p11, "*", factor_p12, "=", p1)
print("\nA factor of p2 is: ", factor_p21)
print("Which gives p2q2 = ", factor_p21, "*", factor_p22, "=", p2)