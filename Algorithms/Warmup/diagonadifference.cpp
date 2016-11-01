#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int
main (
    void
)
{
    int DiagonalIndex;
    int Difference;
    int PrimarySum;
    int IndexA;
    int IndexB;
    int InverseDiagonalIndex;
    int MatrixSize;
    int SecondarySum;

    cin >> MatrixSize;
    vector< vector<int> > Matrix(MatrixSize, vector<int>(MatrixSize));
    for (IndexA = 0; IndexA < MatrixSize; IndexA++){
       for (IndexB = 0; IndexB < MatrixSize; IndexB++){
          cin >> Matrix[IndexA][IndexB];
       }
    }

    PrimarySum = 0;
    SecondarySum = 0;
    for (DiagonalIndex = 0; DiagonalIndex < MatrixSize; DiagonalIndex++) {
        PrimarySum += Matrix[DiagonalIndex][DiagonalIndex];
        InverseDiagonalIndex = (MatrixSize - 1) - DiagonalIndex;
        SecondarySum += Matrix[DiagonalIndex][InverseDiagonalIndex];
    }

    Difference = abs(PrimarySum - SecondarySum);
    cout << Difference;
    return 0;
}
