#include <stdio.h>
#include <stdlib.h>

int
main(
    void
)
{
    int CurrentElement;
    int ElementCount;
    int Index;
    float NegativeCount;
    float NegativeFraction;
    float PositiveCount;
    float PositiveFraction;
    float ZeroCount;
    float ZeroFraction;

    scanf("%d",&ElementCount);
    NegativeCount = 0.0f;
    PositiveCount = 0.0f;
    ZeroCount = 0.0f;
    for (int Index = 0; Index < ElementCount; Index++) {
        scanf("%d",&CurrentElement);
        if (CurrentElement < 0) {
            NegativeCount++;
        } else if (CurrentElement > 0) {
            PositiveCount++;
        } else {
            ZeroCount++;
        }
    }

    PositiveFraction = PositiveCount / ElementCount;
    NegativeFraction = NegativeCount / ElementCount;
    ZeroFraction = ZeroCount / ElementCount;

    printf("%.5f\n", PositiveFraction);
    printf("%.5f\n", NegativeFraction);
    printf("%.5f\n", ZeroFraction);
    return 0;
}
