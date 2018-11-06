#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i;
    long long number;
    int flag;
    for(number=20; ;number+=20)
    {
        flag = 0;
        for(i=11;i<=20;i++)
        {
            if(number % i != 0)
            {
                flag = 1;
                break;
            }
        }
        if(flag == 0)
        {
            break;
        }
    }
    printf("%I64d", number);
    return 0;
}
