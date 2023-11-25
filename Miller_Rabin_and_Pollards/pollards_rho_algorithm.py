import math
import time

def pollard_rho(n, k):
    st = time.time()              # Set a start time

    def g(x):                     # The polynomial modulo function
        return (x**2 + 1) % n
    
    t = k       # Setting the start values
    h = k
    d = 1

    while d == 1:          # Forming the "Rho"-sequence using the polynomial function and finding GCD for each iteration
        t = g(t)
        h = g(g(h))
        d = math.gcd(abs(t - h), n)        # Finding the GCD

        et = time.time()            # Set end time
        elapsed_time = et - st      # Calculate elapsed time
        if elapsed_time >= 30:
            return 0, print("Pollards Timeout: The number is perhaps a prime")

    et = time.time()            # Set end time
    elapsed_time = et - st      # Calculate elapsed time

    if d == n:
        return 0, elapsed_time    # The algorithm failed to find a non-trivial factor
    else:
        return d, elapsed_time     # A non-trivial factor d has been found and is returned, along with the elapsed time
