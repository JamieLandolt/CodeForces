def generate_primes(n):
    for i in range(2, n):
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                break
        else:
            yield i

for i in generate_primes(20):
    print(i)