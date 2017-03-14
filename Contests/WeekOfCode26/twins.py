#!/bin/python3

def create_list_of_primes(min_number, max_number):
    sieve = [True] * (max_number + 1)
    sieve[0] = sieve[1] = False
    for (number, is_prime) in enumerate(sieve):
        if not is_prime:
            continue

        for index in range(number * number, max_number, number):
            sieve[index] = False

    list_of_primes = [x for (x, is_prime) in enumerate(sieve) if is_prime and x >= min_number]
    return list_of_primes

def calculate_number_of_twins(lower_limit, upper_limit):
    list_of_primes = create_list_of_primes(lower_limit, upper_limit)
    number_of_twins = 0
    for index in range(0, len(list_of_primes) - 1, 1):
        delta = list_of_primes[index + 1] - list_of_primes[index]
        if delta == 2:
            number_of_twins += 1

    return number_of_twins

lower_limit_str, upper_limit_str = input().split(' ')
lower_limit = int(lower_limit_str)
upper_limit = int(upper_limit_str)
number_of_twins = calculate_number_of_twins(lower_limit, upper_limit)
print(number_of_twins)
