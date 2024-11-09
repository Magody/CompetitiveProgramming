#include <iostream>
#include <string>
#include <list>
#include <map>
#include <algorithm>

using namespace std;

// #include "utils.h"
// #include "utilsPrint.h"

int mockTrollCoder(int *arr, int n)
{
    int correct[] = {0, 0, 0, 0, 1, 1};
    int sum = 0;
    for (size_t i = 0; i < n; i++)
    {
        if (arr[i] == correct[i])
        {
            sum++;
        }
    }
    return sum;
}

bool debug = true;

int main()
{

    bool continueGuess = true;

    int n = 6;
    if (!debug)
        cin >> n;

    // should begin with 0
    int *guess = new int[n];

    int index = 0;

    // initial guess
    string output = "";
    for (size_t i = 0; i < n; i++)
    {
        output += " " + to_string(guess[i]);
    }

    cout << "Q" << output << endl;

    int m = 0;
    if (debug)
        m = mockTrollCoder(guess, n);
    else
        cin >> m;

    if (m == n)
    {
        cout << "A" << output << endl;
        return 0;
    }

    while (continueGuess)
    {
        // change
        guess[index] = !guess[index];

        output = "";
        string output = "";
        for (size_t i = 0; i < n; i++)
        {
            output += " " + to_string(guess[i]);
        }

        cout << "Q" << output << endl;

        int newM = 0;
        if (debug)
            newM = mockTrollCoder(guess, n);
        else
            cin >> newM;

        if (newM > m)
        {
            // correct change
            m = newM;
        }
        else
        {
            // restore
            guess[index] = !guess[index];
        }
        index++;

        if (m == n)
        {
            cout << "A" << output << endl;
            break;
        }
    }

    /*

    
    */
    return 0;
}