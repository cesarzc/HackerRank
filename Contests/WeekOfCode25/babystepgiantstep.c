#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct _QUERY {
    unsigned int StepSizeA;
    unsigned int StepSizeB;
    unsigned int Point;
} QUERY, *PQUERY;

unsigned int
MinimumNumberOfSteps (
    PQUERY Query
)
{
    unsigned int StepCountA;
    unsigned int StepCountB;

    StepCountA = 0;
    StepCountB = 0;
    if (Query->Point < Query->StepSizeB) {
        if (((Query->Point / Query->StepSizeA) <= 1) && 
            ((Query->Point % Query->StepSizeA) == 0)) {
            StepCountA = Query->Point / Query->StepSizeA;
        } else {
            StepCountB = 2;
        }
    } else {
        StepCountB = Query->Point / Query->StepSizeB;
        if ((Query->Point % Query->StepSizeB) != 0) {
            StepCountB += 1;
        }
    }

    return StepCountA + StepCountB;
}

int
main(
    void
)
{

    unsigned int Index;
    unsigned int MinSteps;
    unsigned int NumberOfCases;
    PQUERY Queries;
    PQUERY Query;

    scanf("%u", &NumberOfCases);
    Queries = malloc(NumberOfCases * sizeof(QUERY));
    for (Index = 0; Index < NumberOfCases; Index++) {
        Query = &Queries[Index];
        scanf("%u %u %u", &Query->StepSizeA, &Query->StepSizeB, &Query->Point);
    }

    for (Index = 0; Index < NumberOfCases; Index++) {
        MinSteps = MinimumNumberOfSteps(&Queries[Index]);
        printf("%u\n", MinSteps);
    }

    return 0;
}
