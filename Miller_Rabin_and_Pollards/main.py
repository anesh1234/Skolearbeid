import miller_rabin_algorithm as miller
import pollards_rho_algorithm as pollard

# Finding a 512 bit number and testing its primality
b = 512
k = 30
p1, p1Time = miller.miller_rabin(b, k)

# Finding a second number while ensuring that the two numbers are not the same
while True:
    p2, p2Time = miller.miller_rabin(b, k)
    if p1 != p2:
        break

# Factoring of (p_i - 1) / 2, i = 1, 2. I chose an object-oriented approach to keep it tidy

class factor:
    def __init__(self, x):
        self.prime = x
        self.part = int((x-1)/2)
        self.ntFactor, self.eTime = pollard.pollard_rho(self.part, 2)    #Running the factorization
        self.factor_q = self.part / self.ntFactor                      # Calculates the other factor, q

    def checkBasic(self):                         # Verifying the result of the factorization    
        if (self.ntFactor * self.factor_q) == self.part:
            return True
        return False
    
    def checkPrime(self):                         # Verifying the factorization against the probable prime
        if (self.part * 2 + 1) == self.prime:
            return True
        return False

pollard1 = factor(p1)    
pollard2 = factor(p2)


# Printing the results to the terminal

print(f"\nThe number \n{p1} \nis probably prime.\
      \nThis took {p1Time} seconds to calculate.")
print(f"\nThe number \n{p2} \nis another probable prime.\
      \nThis took {p2Time} seconds to calculate.")


print(f"\n\nA non-trivial factor (ntf) of p1' = (p1 - 1)/2 is: {pollard1.ntFactor}\
      \nWhich gives ntf*q1 = {pollard1.part} = {pollard1.checkBasic()}\
      \nWhen reversing p1' back to the prime, the result is: {pollard1.checkPrime()}\
      \nThe factoring took {pollard1.eTime} seconds.")

print(f"\nA non-trivial factor (ntf) of p2' = (p2 - 1)/2 is: {pollard2.ntFactor}\
      \nWhich gives ntf*q2 = {pollard2.part} = {pollard2.checkBasic()}\
      \nWhen reversing p2' back to the prime, the result is: {pollard2.checkPrime()}\
      \nThe factoring took {pollard2.eTime} seconds.")
