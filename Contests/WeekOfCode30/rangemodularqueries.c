#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){

    int *array;
    int array_index;
    int array_item;
    int array_size;
    int divisor;
    int lower_limit;
    int max_array_value;
    int mod;
    int number_of_queries;
    int query_index;
    int satisfying_criteria_count;
    int upper_limit;

    scanf("%d %d", &array_size, &number_of_queries);

    // Get the array values.
    array = (int *) malloc(sizeof(int) * array_size);
    max_array_value = 0;
    for(array_index = 0; array_index < array_size; array_index++){
       scanf("%d", &array[array_index]);
    }

    for(query_index = 0; query_index < number_of_queries; query_index++){
        scanf("%d %d %d %d", &lower_limit, &upper_limit, &divisor, &mod);
        satisfying_criteria_count = 0;
        for (array_index = lower_limit;
             array_index <= upper_limit;
             array_index++) {

            if ((array[array_index] % divisor) == mod) {
                satisfying_criteria_count++;
            }
        }

        printf("%d\n", satisfying_criteria_count);
    }

    return 0;
}
