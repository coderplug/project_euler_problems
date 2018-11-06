#include <stdio.h>
#include <stdlib.h>
#include <math.h>

long long getPrime(long long number)
{
    long long i;
    long long j;
    long long max;
    int flag = 0;
    for(i = 3; ;i+=2)
    {
        for(j=2;j<floor(sqrt(i));j++)
        {
            if(i%j == 0)
            {
                flag = 1;
                break;
            }
        }
        if(flag == 0)
        {
            while(number % i == 0)
            {
                number = number / i;
                max = i;
            }
            if(number == 1)
            {
                break;
            }
        }
        flag = 0;
    }
    return max;
}

int main()
{
    long long number = 600851475143;
    printf("%I64d", getPrime(number));
    return 0;
}
