#include <cstdio>

using namespace std;

int main()
{
	int giv_lim = 1000, req_sum = 0;

	for(int n=0; n<giv_lim; n++)
	{
		if(n%3==0 || n%5==0)
		{
			req_sum += n;
		}
	}

	printf("%d", req_sum);
	return 0;
}
