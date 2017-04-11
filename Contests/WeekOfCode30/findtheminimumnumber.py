import sys

def get_min_functions_string(n):
    if (n == 2):
        return "min(int, int)"

    else:
        return "min(int, " + get_min_functions_string(n - 1) + ")"

number_of_integers = int(input().strip())
min_functions_string = get_min_functions_string(number_of_integers)
print(min_functions_string)

