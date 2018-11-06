#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a = 0;
    int b = 1;
    int sum = 0;
    int ceiling = 4000000;
    int i = a;
    while(i<=ceiling)
    {
        if(i%2 == 0)
        {
            sum+=i;
        }
        i=a+b;
        a=b;
        b=i;
    }
    printf("%d\n", sum);
    return 0;
}
