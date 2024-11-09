#include <iostream>
#include <string>
#include <list>
#include <map>
#include <math.h>

using namespace std;

bool debug = false;

int main()
{

    int n = 3, cb = 5, cp = 7;
    if (!debug)
        cin >> n >> cb >> cp;

    float sum_b = 0;
    float sum_p = 0;
    for (size_t testCase = 1; testCase <= n; testCase++)
    {
        float bi, pi;

        cin >> bi >> pi;
        sum_b += bi;
        sum_p += pi;
    }

    int cost = cb * ceil(sum_b / 10) + cp * ceil(sum_p / 10);
    cout << cost << endl;

    /*

    
    */
    return 0;
}