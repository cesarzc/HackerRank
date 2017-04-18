#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int main() {

    int *array;
    int array_size;
    int index;
    bool is_sortable;
    int queries;
    int query_index;
    int temp;

    scanf("%d", &queries);
    for(query_index = 0; query_index < queries; query_index++){
        scanf("%d", &array_size);
        array = (int *) malloc(sizeof(int) * array_size);
        for(index = 0; index < array_size; index++){
           scanf("%d",&array[index]);
        }

        // Do the possible swaps.
        for (index = 0; index < array_size - 1; index++) {
            if ((array[index] - array[index + 1]) == 1) {
                temp = array[index];
                array[index] = array[index + 1];
                array[index + 1] = temp;
            }
        }

        // Verify that the array is sorted.
        is_sortable = true;
        for (index = 0; index < array_size; index++) {
            if (index != array[index]) {
                is_sortable = false;
                break;
            }
        }

        // Print the result.
        if (is_sortable) {
            printf("Yes\n");

        } else {
            printf("No\n");
        }
    }

    return 0;
}
