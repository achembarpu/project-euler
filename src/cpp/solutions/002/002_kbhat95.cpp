#include <stdio.h>

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

    printf("%d\n", sum);
    return 0;
}
