from sympy.ntheory import isprime

# About the isprime() function from the sympy documentation:

# " For small numbers, a set of deterministic Miller-Rabin tests are performed with bases that are
#  known to have no counterexamples in their range. Finally if the number is larger than 2^64,
#  a strong BPSW test is performed. "

checkP1 = isprime(8971813200944627790729005543380820961152091321052943968087807768636014670984583617676861789635145781241667342899110227927586010770673425112008131181284447)
checkP2 = isprime(8057362682991974614373733847841401381709198499327808675818122518552467580870628085099116297541899564115667397725067353887060603517115502862135587738679331)

print(f"\nP1 is a strong probable prime: {checkP1}\
      \nP2 is a strong probable prime: {checkP2}\n")