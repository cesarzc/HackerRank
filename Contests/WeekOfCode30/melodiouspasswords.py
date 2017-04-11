#!/bin/python3

import re
import sys
import string

# Get the required data for the problem.
NUMBER_OF_LETTERS = int(input().strip())
VALID_VOWELS = "aeiou"
all_vowels_rx = '[' + re.escape(VALID_VOWELS + "y") + ']'
VALID_CONSONANTS = re.sub(all_vowels_rx, "", string.ascii_lowercase)

# This function returns a string based on a combination (composed by indexes).
def get_password_string_from_combination(combination, even_letters, odd_letters):
    password_string = ""
    for index in range(len(combination)):
        letter_index = combination[index]
        if (index % 2) == 0:
            password_string += even_letters[letter_index]

        else:
            password_string += odd_letters[letter_index]

    return password_string

# This function prints all the melodious passwords given whether the first
# letter is a vowel.
def print_melodious_passwords(is_first_letter_vowel):

    # Get the even/odd letters and indexes in the password combination.
    if is_first_letter_vowel:
        first_vowel_index = 0
        even_letters = VALID_VOWELS
        odd_letters = VALID_CONSONANTS

    else:
        first_vowel_index = 1
        even_letters = VALID_CONSONANTS
        odd_letters = VALID_VOWELS

    first_consonant_index = (first_vowel_index + 1) % 2
    vowel_indexes = range(first_vowel_index, NUMBER_OF_LETTERS, 2)
    consonant_indexes = range(first_consonant_index, NUMBER_OF_LETTERS, 2)

    # Initialize the password combination indexes to the MAX.
    password_combination = [0] * NUMBER_OF_LETTERS
    for vowel_index in vowel_indexes:
        password_combination[vowel_index] = len(VALID_VOWELS) - 1

    for consonant_index in consonant_indexes:
        password_combination[consonant_index] = len(VALID_CONSONANTS) - 1

    all_passwords_printed = False
    while not all_passwords_printed:

        # Print the password currently represented by the combination.
        password_string = get_password_string_from_combination(
                              password_combination,
                              even_letters,
                              odd_letters)

        print(password_string)

        # If all passwords have been printed, halt the loop.
        if sum(password_combination) == 0:
            all_passwords_printed = True
            break

        # Substract the current combination by 1.
        for reverse_index in reversed(range(len(password_combination))):
            if (password_combination[reverse_index] > 0):
                password_combination[reverse_index] -= 1
                break

            if reverse_index in vowel_indexes:
                password_combination[reverse_index] = len(VALID_VOWELS) - 1

            else:
                password_combination[reverse_index] = len(VALID_CONSONANTS) - 1

    return

# Print the vowel-initiated passwords first and the consonant-initiated
# passwords later.
print_melodious_passwords(True)
print_melodious_passwords(False)
