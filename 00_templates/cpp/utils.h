#include <iostream>
#include <string>
#include <list>
#include <map>
#include <algorithm>
#include <chrono>

#include <boost/multiprecision/cpp_int.hpp>
using namespace boost::multiprecision;

using namespace std;


void deepCopyMatrix(int **fromMatrix, int **toMatrix, int n, int m){
     for (size_t i = 0; i < n; i++)
    {
        for (size_t j = 0; j < m; j++)
        {
            toMatrix[i][j] = fromMatrix[i][j];

        }
    }
}

list<string> splitStrings(string s, string delimiter)
{
    int textLength = s.length() + 1;

    size_t pos = 0;
    string token;
    list<string> values;
    while ((pos = s.find(delimiter)) != std::string::npos)
    {
        token = s.substr(0, pos);
        values.push_back(token);
        s.erase(0, pos + delimiter.length());
    }
    token = s.substr(0, pos);
    values.push_back(token);

    return values;
}

string readElementInString(list<string> arrayString, int n){
    typename list<string>::iterator it;
    int index = 0;
    for (it = arrayString.begin(); it != arrayString.end(); ++it)
    {
        if(index == n){
            return *it;
        }
        index++;
    }
    return "";
}


template <class T>
bool existValueInList(list<T> my_list, T my_var)
{
    return (find(my_list.begin(), my_list.end(), my_var) != my_list.end());
}

map<int, long> storedFactorialMap;

int factorial(int n)
{
    if (n == 1 || n == 0)
    {
        return 1;
    }
    if (n == 2)
        return 2;

    if (storedFactorialMap.count(n) == 1)
        return storedFactorialMap[n];

    int fn_1 = factorial(n - 1);
    if (storedFactorialMap.count(n) == 0)
    {
        storedFactorialMap[n] = n * fn_1;
    }
    return n * fn_1;
}

map<int, cpp_int> fibonacciStore;

cpp_int fibonacci(int n)
{

    if (fibonacciStore.count(n) == 1)
    {
        return fibonacciStore[n];
    }
    if (n == 0 || n == 1)
    {
        return 1;
    }

    fibonacciStore[n] = fibonacci(n - 1) + fibonacci(n - 2);
    return fibonacciStore[n];
}