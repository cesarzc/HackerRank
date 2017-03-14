#!/bin/python3

import sys

# Read the input.
number_of_candies_str, party_time_str = input().strip().split(' ')
number_of_candies, party_time = [int(number_of_candies_str), int(party_time_str)]
candies_removed_list = list(map(int, input().strip().split(' ')))

# Compute the candies added by the robot.
candies_added_by_robot = 0
candies_in_bowl = number_of_candies
for candies_removed_instance in candies_removed_list[0 : party_time - 1]:
    candies_in_bowl -= candies_removed_instance
    if candies_in_bowl < 5:
        candies_added_by_robot += number_of_candies - candies_in_bowl
        candies_in_bowl = number_of_candies

print(candies_added_by_robot)
