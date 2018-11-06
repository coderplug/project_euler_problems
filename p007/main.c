#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{
	int i, j;
	int counter = 1;
	int number;
	int flag;
	for(i=3;counter!=10001;i=i+2)
	{
		flag = 0;
		if(i%2 == 0)
        {
            flag = 1;
        }
        else
        {
            for(j=3;j<=floor(sqrt(i));j+=2)
            {
                if(i % j == 0)
                {
                    flag = 1;
                    break;
                }
            }
        }

		if(flag == 0)
		{
			counter++;
			number = i;
		}
	}
	printf("%d", number);
	return 0;
}
