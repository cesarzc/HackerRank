#include <stdio.h>
#include <stdlib.h>

int
SolveMeFirst (
    int a,
    int b
)
{
    return a + b;
}

int
main (
    void
)
{

    int NumA;
    int NumB;
    int Sum;

    scanf("%d %d", &NumA, &NumB);
    Sum = SolveMeFirst(NumA, NumB);
    printf("%d",Sum);
    return 0;
}
