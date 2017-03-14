#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int
main(
    void
)
{
    int Columns;
    int ColumnPackages;
    int Rows;
    int RowPackages;
    int TotalPackages;

    scanf("%d %d", &Rows, &Columns);
    ColumnPackages = ((Columns % 2) == 0) ? Columns / 2 : (int)ceil(Columns / 2.0);
    RowPackages = ((Rows % 2) == 0) ? (Rows / 2) : (int)ceil(Rows / 2.0);
    TotalPackages = ColumnPackages * RowPackages;
    printf("%d", TotalPackages);
    return 0;
}