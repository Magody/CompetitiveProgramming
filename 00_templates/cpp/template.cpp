#include <iostream>
#include <string>
#include <list>
#include <map>
#include <algorithm>
#include <math.h>
#include <chrono>

#include <boost/multiprecision/cpp_int.hpp>

using namespace boost::multiprecision;
using namespace std;

bool debug = true;

int main()
{
    
    std::cout.precision(std::numeric_limits<cpp_int>::max_digits10);


    chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

    int t = 1;
    if (!debug)
        cin >> t;

    for (size_t testCase = 1; testCase <= t; testCase++)
    {
        int n = 6, 
            m = 5;

        if (!debug)
            cin >> n >> m;

        for (size_t i = 0; i < m; i++)
        {
            if (debug)
            {
                // (rand() % m) + 1;
                /*
                cpp_dec_float_50 x = -1 + (((float) rand()) / (float) RAND_MAX)*2;
                cpp_dec_float_50 y = -1 + (((float) rand()) / (float) RAND_MAX)*2;
        
                */
            }

            int a, 
                b;
            // 6 5 -  0 1 0 3 1 2 1 5 3 4
            // 9 12 - 0 1 0 2 0 8 1 3 3 4 4 1 4 5 5 6 6 2 6 7 7 8 2 1
            cin >> a >> b;
        }

        cout << 1 << endl;
    }

    chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    if (debug)
    {
        cout << "Time = " << chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() << "[ms]" << std::endl;
    }

    return 0;
}