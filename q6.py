def prime_check(x):
    for i in range(2,x):
        if x % i == 0:
            return 0
            # if divisible, then not a prime
    return 1
    # otherwise it is a prime

lower = int(input("Enter the lower limit : "))
upper = int(input("Enter the upper limit : "))


if lower <= 0:
    print("Enter a positive lower limit")

else:
    print("Primes in the given range are as follows : ")
    for it in range(lower, upper+1):
        if prime_check(it) == 1:
            print(it,end = ' ')

