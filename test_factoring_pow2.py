def factor_powers_of_2(n):
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    return s, d

# Input 'n'
n = int(input("Enter a value for n: "))

# Call the function to factor powers of 2
s, d = factor_powers_of_2(n)

print(f"(n - 1) = 2^{s} * {d}")
print(f"Which gives: {2**s * d}")