
#include <stdio.h>
#include <stdlib.h>

int main(){

    int elements_between_zero;
    int game_index;
    int games;
    int *sequence;
    int sequence_length;
    int sequence_index;

    scanf("%d",&games);
    for(int game_index = 0; game_index < games; game_index++){
        scanf("%d",&sequence_length);
        sequence = malloc(sizeof(int) * sequence_length);
        for(sequence_index = 0; sequence_index < sequence_length; sequence_index++){
           scanf("%d",&sequence[sequence_index]);
        }

        // Convert to zero all the numbers between zeros.
        for(sequence_index = 1; sequence_index < sequence_length - 1; sequence_index++){
            if ((sequence[sequence_index - 1] == 0) && 
                (sequence[sequence_index + 1] == 0)) {

                sequence[sequence_index] = 0;
            }
        }

        // Count the number of elements between zeros.
        elements_between_zero = 0;
        for(sequence_index = 1; sequence_index < sequence_length - 1; sequence_index++){
            if ((sequence[sequence_index - 1] == 0) && 
                (sequence[sequence_index + 1] == 0)) {

                elements_between_zero++;
            }
        }

        if ((elements_between_zero % 2) == 1) {
            printf("Alice\n");

        } else {
            printf("Bob\n");
        }
    }

    return 0;
}
