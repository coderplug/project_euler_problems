#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int getLength(int number)
{
    if(number > 100000)
        return 5;
    else if(number > 10000)
        return 4;
    return -1;
}

int main()
{
    int i;
    int j;
    int k;
    int max = 0;
    int number;
    int length;
    char numberSymbols[10];
    int flag = 0;
    for(i = 100; i < 1000; i++)
    {
        for(j = i; j < 1000; j++)
        {
            number = i*j;
            length = getLength(number);
            itoa(number, numberSymbols, 10);
            for(k = 0; k <= floor(length/2); k++)
            {
                if(numberSymbols[k]!=numberSymbols[length-k])
                {
                    flag = 1;
                }
            }
            if(flag == 0 && max<number)
            {
                max = number;
            }
            flag = 0;
        }
    }
    printf("%d", max);
    return 0;
}
