#include <iostream>
#include <string>
#include <list>
#include <map>
#include <algorithm>

#include <boost/multiprecision/cpp_int.hpp>
using namespace boost::multiprecision;

using namespace std;

bool debug = true;

int compare(const void *a, const void *b)
{
    const int *x = (int *)a;
    const int *y = (int *)b;

    if (*x > *y)
        return 1;
    else if (*x < *y)
        return -1;

    return 0;
}

int main()
{

    int t = 20;
    if (!debug)
        cin >> t;

    for (size_t testCase = 1; testCase <= t; testCase++)
    {
        int m = 1000000, n = 1000000, k = 1000000;

        if (!debug)
            cin >> m >> n >> k;

        int *roomWired = new int[m];

        if (debug)
        {
            for (size_t i = 0; i < m; i++)
            {
                roomWired[i] = (rand() % m) + 1;
                // cout << roomWired[i] << ",";
            }
            // cout << endl;
            /*
            roomWired[0] = 3;
            roomWired[1] = 0;
            roomWired[2] = 1;
            roomWired[3] = 2;
            roomWired[4] = 2;
            */
        }
        else
        {
            for (size_t i = 0; i < m; i++)
            {
                int c;
                // 6 5 -  0 1 0 3 1 2 1 5 3 4
                // 9 12 - 0 1 0 2 0 8 1 3 3 4 4 1 4 5 5 6 6 2 6 7 7 8 2 1
                cin >> c;
                roomWired[i] = c;
            }
        }

        qsort(roomWired, m, sizeof(int), compare); // n log(n)
        
        cpp_int sum = 0;
        for (size_t indexInvert = 0; indexInvert < k; indexInvert++)
        {
            roomWired[indexInvert] = n - roomWired[indexInvert];
            sum += roomWired[indexInvert];
        }
        for (size_t indexInvert = k; indexInvert < m; indexInvert++)
        {
            sum += roomWired[indexInvert];
        }

        cout << sum << endl;
    }

    /*

    
    */
    return 0;
}