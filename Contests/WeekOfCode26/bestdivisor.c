#include <stdio.h>
#include <stdlib.h>

int
SumOfDigits (
    int Number
)
{
    int LocalNumber;
    int Sum;
    
    LocalNumber = Number;
    Sum = 0;
    while (LocalNumber != 0) {
        Sum += LocalNumber % 10;
        LocalNumber /= 10;
    }
    
    return Sum;
}

int
main (
    void
)
{
    int BestDivisor;
    int Index;
    int Number; 
    
    scanf("%d",&Number);
    BestDivisor = 1;
    for (Index = 1; Index <= Number; Index++) {
        if ((Number % Index) == 0) {
            if (SumOfDigits(Index) > SumOfDigits(BestDivisor)) {
                BestDivisor = Index;
            }
        }
    }
    
    printf("%d", BestDivisor);
    return 0;
}
