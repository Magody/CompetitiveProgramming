#include <iostream>
#include <string>
#include <list>
#include <map>
#include <algorithm>

using namespace std;



int *split(string s, string delimiter)
{
    int textLength = s.length() + 1;

    int *values = new int[textLength / 2];

    size_t pos = 0;
    string token;
    int index = 0;
    while ((pos = s.find(delimiter)) != std::string::npos)
    {
        token = s.substr(0, pos);
        values[index++] = stoi(token);
        s.erase(0, pos + delimiter.length());
        // cout << "TOKEN: " << token << ", s:" << s << endl;
    }
    token = s.substr(0, pos);
    values[index++] = stoi(token);

    return values;
}

void printVector(int *vector, int n)
{
    for (size_t i = 0; i < n; i++)
    {

        cout << vector[i] << " ";
    }
    cout << endl;
}

void printMatrix(int **matrix, int n, int m)
{
    for (size_t i = 0; i < n; i++)
    {
        for (size_t j = 0; j < m; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

template <typename T>
void printlist(list<T> g)
{
    typename list<T>::iterator it;
    for (it = g.begin(); it != g.end(); ++it)
        cout << '\t' << *it;
    cout << '\n';
}

template <typename T>
void printMap(map<int, list<T>> m, list<int> indexes)
{
    typename list<T>::iterator it;
    for (it = indexes.begin(); it != indexes.end(); ++it)
    {
        int key = *it;
        cout << "Key: " << key << ", Value (list): " << endl;
        printlist(m[key]);
    }
}