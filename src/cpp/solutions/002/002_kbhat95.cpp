//Author: Kishor Bhat
//Email: kishorbhat@gmail.com

#include <iostream>

using namespace std;

int main()
{
	int lim = 4000000, a = 1, b = 2, c = 3, sum = 2;

	while (c < lim)
	{
		if (c % 2 == 0)
			sum += c;
		a = b;
		b = c;
		c = a + b;
	}

	cout << sum << "\n";
	return 0;
}
