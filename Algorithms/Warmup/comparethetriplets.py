#!/bin/python3

triplet_A = [int(item) for item in input().strip().split(' ')]
triplet_B = [int(item) for item in input().strip().split(' ')]
score_A = 0
score_B = 0

for rating_A, rating_B in zip(triplet_A, triplet_B):
    if rating_A > rating_B:
        score_A += 1
    elif rating_A < rating_B:
        score_B += 1

print("{:d} {:d}".format(score_A, score_B))
