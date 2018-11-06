#include <stdio.h>
#include <stdlib.h>

int main()
{
    int result;
    int number1 = 3;
    int number2 = 5;
    int ceiling = 1000;
    int sum1 = 0;
    int sum2 = 0;
    int sum1and2 = 0;
    int i;
    for(i = number1; i < ceiling; i+=number1)
    {
        sum1+=i;
    }
    for(i = number2; i < ceiling; i+=number2)
    {
        sum2+=i;
    }
    for(i = number1*number2; i < ceiling; i+=(number1*number2))
    {
        sum1and2+=i;
    }
    result = sum1 + sum2 - sum1and2;
    printf("%d\n", result);
    return 0;
}
