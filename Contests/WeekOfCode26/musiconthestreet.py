#!/bin/python3

def is_valid_interval(start_index, end_index, time_min, time_max, miles, points):
    # Initialize important constants.
    start_section_point_tail = points[start_index + 1]
    end_section_point_head = points[end_index - 1]
    start_point_min = start_section_point_tail - time_max
    start_point_max = start_section_point_tail - time_min
    end_point_min = end_section_point_head + time_min
    end_point_max = end_section_point_head + time_max

    # Check validity and calculate the optimal start point.
    is_valid = False
    optimal_start_point = 0
    if ((end_point_min - start_point_max) <= miles) and ((end_point_max - start_point_min) >= miles):
        is_valid = True
        delta_to_optimal_point = end_point_min - (start_point_min + miles)
        if delta_to_optimal_point > 0:
            optimal_start_point = start_point_min + delta_to_optimal_point
        else:
            optimal_start_point = start_point_min

    return is_valid, optimal_start_point

# Parse input.
number_of_points = input()
input_points = [int(item) for item in input().strip().split(' ')]
miles_str, time_min_str, time_max_str = input().split(' ')
miles = int(miles_str)
time_min = int(time_min_str)
time_max = int(time_max_str)

# Include the min possible and the max possible points on the list.
all_points = [input_points[0] - time_max]
all_points.extend(input_points)
all_points.append(input_points[-1] + time_max)

# Find the interval.
interval_found = False
optimal_start_point = 0
global_index = start_index = end_index = 0
while not interval_found:
    # Get start index.
    start_index = global_index
    while (all_points[start_index + 1] - all_points[start_index]) < time_min:
        start_index += 1

    # Look for a possible interval.
    current_index = start_index + 1
    while (all_points[current_index] - all_points[start_index]) < miles:
        section_length = all_points[current_index] - all_points[current_index - 1]
        if not (time_min <= section_length <= time_max):
            break

        current_index += 1

    end_index = current_index

    # Check the validity of the possible interval.
    interval_found, optimal_start_point = is_valid_interval(start_index, end_index, time_min, time_max, miles, all_points)
    if not interval_found:
        global_index = current_index - 1

# Print the optimal start point.
print(optimal_start_point)
