#!/bin/python3

import sys

VOWELS = "aeiouy"

word = input().strip()
is_beautiful_word = True
for letter_index in range(len(word) - 1):
    current_letter = word[letter_index]
    next_letter = word[letter_index + 1]
    if (current_letter in VOWELS) and (next_letter in VOWELS):
        is_beautiful_word = False
        break

    elif current_letter == next_letter:
        is_beautiful_word = False
        break

if is_beautiful_word:
    print("Yes")

else:
    print("No")
