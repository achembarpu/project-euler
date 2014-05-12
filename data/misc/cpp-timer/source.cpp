// TEST_RUNS is defined by tester script
#include <iostream>
#include <ctime>

using namespace std;

int run(void);

int main()
{
	double total_time=0.0, average_time=0.0;
	clock_t tStart;

	for(int i=0; i<TEST_RUNS; i++)
	{
		tStart = clock();
		run();
		total_time += ((double)(clock() -tStart)/CLOCKS_PER_SEC);
	}

	average_time = (total_time / TEST_RUNS);

	cout << average_time;

	return 0;
}
