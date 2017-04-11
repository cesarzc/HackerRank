#!/bin/python3

import sys

# Get the info.
array_size_str, number_of_queries_str = input().strip().split(' ')
array_size, number_of_queries = [int(array_size_str), int(number_of_queries_str)]
array = list(map(int, input().strip().split(' ')))
list_of_queries = []
for query in range(number_of_queries):
    left_str, right_str, divisor_str, mod_str = input().strip().split(' ')
    query_tuple = (int(left_str), int(right_str), int(divisor_str), int(mod_str))
    list_of_queries.append(query_tuple)

for left, right, divisor, mod in list_of_queries:
    satisfying_criteria_count = 0
    for index in range(left, right + 1):
        if array[index] % divisor == mod:
            satisfying_criteria_count += 1

    print(satisfying_criteria_count)
