import random

def miller_rabin(n, k):

    # Set n − 1 = 2^{s}d where s > 0 and odd number d > 0 
    s = 0 
    d = n - 1
    
    while d % 2 == 0:
        s += 1
        d //= 2

    # Perform testing rounds
    for _ in range(1,k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        for _ in range(1,s):
            y = pow(x, 2, n)
            if (y == 1) and (x != 1) and (x != (n - 1)):
                return False
            x = y

        if (y != 1):
            return False
    return True

# Example usage:
n = 13
k = 5
is_prime = miller_rabin(n, k)
print(f"{n} is {'probably prime' if is_prime else 'composite'}")
