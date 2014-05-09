#include<iostream>
using namespace std;
int main()
{
	int i, sum = 0;
	int lim = 1000;

	for(i = 3;i < lim; i++)
		if((i % 3 == 0) || (i % 5 == 0))		
			sum += i;
	
	cout << sum;
	return 0;
}
