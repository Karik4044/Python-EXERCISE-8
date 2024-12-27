def isPrimeNumber(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
if n >= 20:
    print(n, "is too large(n<20).")
else:
    if isPrimeNumber(n):
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")