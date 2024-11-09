#include <iostream>
#include <math.h>
#include <map>
#include <chrono>
#include <string>

#include "../utils.h"

using namespace std;

int gridTravelerGodMode(int n, int m)
{
    if (n == 0 || m == 0)
        return 0;
    if (n == 1 && m == 1)
        return 1;
    int r = m - 1;
    int d = n - 1;
    // the pattern is permutation with repetition
    return factorial(r + d) / (factorial(r) * factorial(d));
}

map<string, int> memo;

int gridTravelerDynamic(int n, int m)
{
    string key = to_string(n) + "," + to_string(m);

    if (memo.count(key) == 1)
    {
        return memo[key];
    }

    if (n == 0 || m == 0)
        return 0;
    if (n == 1 && m == 1)
        return 1;

    memo[key] = gridTravelerDynamic(n - 1, m) + gridTravelerDynamic(n, m - 1);
    return memo[key];
}

int main()
{

    int *testCases[] = {
        new int[2]{2, 3},
        new int[2]{20, 5},
        new int[2]{5, 10},
        new int[2]{11, 12},
        new int[2]{10, 4},
        new int[2]{3, 4}};

    int testCasesLength = sizeof(testCases) / sizeof(testCases[0]);

    int repetitions = 2000;

    chrono::steady_clock::time_point begin2 = std::chrono::steady_clock::now();
    for (size_t a = 0; a < repetitions; a++)
    {
        for (size_t i = 0; i < testCasesLength; i++)
        {
            int n = testCases[i][0];
            int m = testCases[i][1];
            gridTravelerDynamic(n, m);
            // cout << gridTravelerDynamic(n, m) << endl;
        }
    }
    chrono::steady_clock::time_point end2 = std::chrono::steady_clock::now();

    cout << gridTravelerDynamic(7, 11) << endl;

    chrono::steady_clock::time_point begin1 = std::chrono::steady_clock::now();
    for (size_t a = 0; a < repetitions; a++)
    {
        for (size_t i = 0; i < testCasesLength; i++)
        {
            int n = testCases[i][0];
            int m = testCases[i][1];
            gridTravelerGodMode(n, m);
            // cout << gridTravelerGodMode(n, m) << endl;
        }
    }
    chrono::steady_clock::time_point end1 = std::chrono::steady_clock::now();

    cout << gridTravelerGodMode(7, 11) << endl;

    cout << "Time 1 = " << chrono::duration_cast<std::chrono::milliseconds>(end1 - begin1).count() << "[ms]" << std::endl;
    cout << "Time 2 = " << chrono::duration_cast<std::chrono::milliseconds>(end2 - begin2).count() << "[ms]" << std::endl;

    return 0;
}