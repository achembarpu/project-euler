//Author: Kishor Bhat
//Email: kishorbhat@gmail.com

#include <iostream>

using namespace std;

int main()
{
	int sum_square, square, sum, lim = 100;
	
	sum = lim * (lim + 1) / 2;
	sum_square = sum * sum;
	square = lim * (lim + 1) * (2 * lim + 1) / 6;
	
	cout << sum_square - square << "\n"; 
	return 0;
}
