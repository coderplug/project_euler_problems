#include <stdio.h>
#include <stdlib.h>

int main()
{
    int sum1 = 0;
    int sum2 = 0;
    int i;
    int j = 0;
    sum2 = (1+100)*100/2;
    sum2*=sum2;
    for(i = 1; i <= 199;i+=2)
    {
        j = j + i;
        sum1 = sum1 + j;
    }
    printf("%d", sum2-sum1);
    return 0;
}
