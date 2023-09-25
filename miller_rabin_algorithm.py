import random

def miller_rabin(n, k):

    # Write n as 2^s * d + 1
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Perform testing rounds
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == (n - 1):
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == (n - 1):
                break
        else:
            return False  # Definitely composite

    return True  # Likely prime

# Example usage:
n = 37
k = 5
is_prime = miller_rabin(n, k)
print(f"{n} is {'probably prime' if is_prime else 'composite'}")
