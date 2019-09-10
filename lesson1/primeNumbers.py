#import迭代器
import itertools

def iter_primes():
    # an iterator of all numbers between 2 and + infinity
    numbers = itertools.count(2)

    # generate primes forever
    while True:
        # get the first number from the iterator (always a prime)
        prime = next(numbers)
        yield prime

        numbers = filter(prime.__rmod__,numbers)

for p in iter_primes():
    if p > 1000:
        break
    print(p)