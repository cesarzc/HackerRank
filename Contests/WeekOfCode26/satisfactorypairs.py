#!/bin/python3

def can_sum_number(a, b, number):
    for i in range(b, number, b):
        if ((number - i) % a) == 0:
            return True

    return False

def get_number_of_satisfactory_pairs(initial_number, limit):
    satisfactory_pairs = 0
    for number in range(initial_number + 1, (limit - initial_number) + 1):
        if can_sum_number(initial_number, number, limit):
            satisfactory_pairs += 1

    return satisfactory_pairs

limit = int(input())
satisfactory_pairs = 0
for number in range(1, limit):
    satisfactory_pairs += get_number_of_satisfactory_pairs(number, limit)

print(satisfactory_pairs)
