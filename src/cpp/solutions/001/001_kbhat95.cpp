#include<stdio.h>
using namespace std;
int main()
{
	int i, sum = 0;
	int lim = 1000;

	for(i = 3;i < lim; i++)
		if((i % 3 == 0) || (i % 5 == 0))		
			sum += i;
	
	printf("%d\n", sum);
	return 0;
}
