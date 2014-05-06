#include <stdio.h>

using namespace std;

int main()
{
	int sum_square, square, sum, lim = 100;
	
	sum = lim * (lim + 1) / 2;
	sum_square = sum * sum;
	square = lim * (lim + 1) * (2 * lim + 1) / 6;
	
	printf("%d\n", sum_square - square );
	return 0;
}