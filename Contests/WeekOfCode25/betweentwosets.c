#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define max(a,b)    (((a) > (b)) ? (a) : (b))
#define min(a,b)    (((a) < (b)) ? (a) : (b))

int
MaxInSet (
    int *Set,
    int SetSize
)
{
    int Index;
    int Max;

    Max = Set[0];
    for (Index = 1; Index < SetSize; Index++) {
        Max = max(Max, Set[Index]);
    }

    return Max;
}

int
MinInSet (
    int *Set,
    int SetSize
)
{
    int Index;
    int Min;

    Min = Set[0];
    for (Index = 1; Index < SetSize; Index++) {
        Min = min(Min, Set[Index]);
    }

    return Min;
}

bool
IsNumberFactorOfSet
(
    int Number,
    int *Set,
    int SetSize
)
{
    int Index;
    bool IsFactor;

    IsFactor = true;
    for (Index = 0; Index < SetSize; Index++) {
        if ((Set[Index] % Number) != 0) {
            IsFactor = false;
        }
    }

    return IsFactor;
}

bool
IsSetFactorOfNumber
(
    int Number,
    int *Set,
    int SetSize
)
{
    int Index;
    bool IsFactor;

    IsFactor = true;
    for (Index = 0; Index < SetSize; Index++) {
        if ((Number % Set[Index]) != 0) {
            IsFactor = false;
        }
    }

    return IsFactor;
}

int
BetweenTwoSets
(
    int *SetA,
    int SetASize,
    int *SetB,
    int SetBSize
)
{
    int Index;
    int IntegerCount;
    int RangeMin;
    int RangeMax;

    RangeMin = MaxInSet(SetA, SetASize);
    RangeMax = MinInSet(SetB, SetBSize);
    IntegerCount = 0;
    for (Index = RangeMin; Index <= RangeMax; Index++) {
        if ((IsSetFactorOfNumber(Index, SetA, SetASize)) &&
            (IsNumberFactorOfSet(Index, SetB, SetBSize))) {

            IntegerCount++;
        }
    }

    return IntegerCount;
}

int
main (
    void
)
{
    int IndexA;
    int IndexB;
    int NumberOfIntegers;
    int *SetA;
    int SetASize;
    int *SetB;
    int SetBSize;

    scanf("%d %d", &SetASize, &SetBSize);
    SetA = malloc(sizeof(int) * SetASize);
    for(IndexA = 0; IndexA < SetASize; IndexA++){
       scanf("%d",&SetA[IndexA]);
    }

    SetB = malloc(sizeof(int) * SetBSize);
    for(IndexB = 0; IndexB < SetBSize; IndexB++){
       scanf("%d",&SetB[IndexB]);
    }

    NumberOfIntegers = BetweenTwoSets(SetA, SetASize, SetB, SetBSize);
    printf("%d", NumberOfIntegers);
    return 0;
}
