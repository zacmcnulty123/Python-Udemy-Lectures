#Count Primes: Write a function that returns the number of prime numbers that exist up to and including a given number
def is_prime(a):
    if a >= 2:
        for i in range(2, a):
            if not (a % i):
                return False
    else:
        return False
    return True

def count_primes(a):
    list = []
    for i in range(a):
        if is_prime(i):
            list.append(i)
    return list

print(count_primes(100))