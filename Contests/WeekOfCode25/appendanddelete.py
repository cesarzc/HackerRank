#!/bin/python3

string_A = input().strip()
string_B = input().strip()
number_of_operations = int(input().strip())
string_A_size = len(string_A)
string_B_size = len(string_B)
min_string_size = min(string_A_size, string_B_size)
common_string_size = 0
for (char_A, char_B) in zip(string_A[0:min_string_size], string_B[0:min_string_size]):
    if char_A != char_B:
        break

    common_string_size += 1

min_deletes = string_A_size - common_string_size
min_adds = string_B_size - common_string_size
min_operations = min_deletes + min_adds
operations_when_deleted = string_A_size + string_B_size
if number_of_operations < min_operations:
    # If the number of operations is less than the minimum operations needed to
    # do the transformation, print 'No'.
    print("No")

elif number_of_operations >= operations_when_deleted:
    # If the number of operations is more than the operations needed to do the
    # transformation if the string A is completely deleted, print 'Yes' since
    # any number of deletes on an empty string is permitted.
    print("Yes")
    
else:
    # If the number of operations is between the two ranges (min_operations,
    # operations_when_deleted], return 'Yes' only when the module 2 of both the
    # number of operations and the minimum number of operations is the same.
    if (min_operations % 2) == 0:
        number_of_operations_mod_result = 0
    else:
        number_of_operations_mod_result = 1

    if (number_of_operations % 2) == number_of_operations_mod_result:
        print("Yes")
    else:
        print("No")
