// Author: Arvind Chembarpu
// Email: achembarpu@gmail.com

#include <iostream>

using namespace std;

int main()
{
	int giv_lim = 1000, req_sum = 0;

	for(int n=3; n<giv_lim; n+=3)
		req_sum += n;
	for(int n=5; n<giv_lim; n+=5)
		req_sum += n;
	for(int n=15; n<giv_lim; n+=15)
		req_sum -= n;

	cout << req_sum;
	return 0;
}
