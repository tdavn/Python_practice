x = int(input())

def Prime_factorizer(x):
    prime_factors = []
    divisor = 2

    while divisor <= x:
        if x % divisor == 0:
            prime_factors.append(divisor)
            x = x / divisor
        else:
            divisor += 1 # divisor = divisor + 1

    return prime_factors


print(f'prime factors: {Prime_factorizer(x)}')
