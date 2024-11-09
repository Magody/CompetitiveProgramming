#include <iostream>
#include <string>
#include <list>
#include <map>
#include <algorithm>

using namespace std;

// #include "utils.h"
// #include "utilsPrint.h"

template <class T>
bool existValueInList(list<T> my_list, int my_var)
{
    return (find(my_list.begin(), my_list.end(), my_var) != my_list.end());
}

template <class T>
void printMap(map<int, list<T>> m, list<int> indexes)
{
    list<T>::iterator it;
    for (it = indexes.begin(); it != indexes.end(); ++it)
    {
        int key = *it;
        cout << "Key: " << key << ", Value (list): " << endl;
        printlist(m[key]);
    }
}

bool debug = false;

int main()
{

    int t = 1;
    if (!debug)
        cin >> t;

    for (size_t testCase = 1; testCase <= t; testCase++)
    {
        int n = 6, m = 5;

        if (!debug)
            cin >> n >> m;

        list<int> indexesMap;

        map<int, list<int>> map;
        bool hasLoop = false;
        bool answerFast = false;

        for (size_t i = 0; i < m; i++)
        {
            int a, b;
            // 6 5 -  0 1 0 3 1 2 1 5 3 4
            // 9 12 - 0 1 0 2 0 8 1 3 3 4 4 1 4 5 5 6 6 2 6 7 7 8 2 1
            cin >> a >> b;

            if (a == b)
            {
                hasLoop = true;
                answerFast = true;
            }

            bool existValueInA = existValueInList(map[a], b);
            bool existValueInB = existValueInList(map[b], a);
            bool existIndexA = existValueInList(indexesMap, a);
            bool existIndexB = existValueInList(indexesMap, b);

            if (!existIndexA)
            {
                indexesMap.push_back(a);
            }
            if (!existIndexB)
            {
                indexesMap.push_back(b);
            }

            if (!existValueInA)
            {
                map[a].push_back(b);
            }
            else
            {
                hasLoop = true;
                answerFast = true;
            }
            if (!existValueInB)
            {
                map[b].push_back(a);
            }
            else
            {
                hasLoop = true;
                answerFast = true;
            }
        }

        if (answerFast)
        {
            cout << hasLoop << endl;
            continue;
        }

        bool removeLeaf = true;
        if (debug)
            cout << "Removing leaf" << endl;

        while (removeLeaf)
        {
            list<int>::iterator it;
            removeLeaf = false;
            for (it = indexesMap.begin(); it != indexesMap.end(); ++it)
            {
                list<int> l = map[*it];

                if (l.size() == 1)
                {
                    removeLeaf = true;
                    auto l_front = l.begin();
                    advance(l_front, 0);
                    map[*l_front].remove(*it);
                    map[*it].remove(*l_front);
                    if (debug)
                    {
                        cout << "Map status: " << endl;
                        printMap(map, indexesMap);
                    }
                }
            }

            continue;
        }

        list<int>::iterator it;
        for (it = indexesMap.begin(); it != indexesMap.end(); ++it)
        {
            list<int> l = map[*it];
            if (!l.empty())
            {
                hasLoop = true;
                break;
            }
        }

        cout << hasLoop << endl;
    }
    /*

    
    */
    return 0;
}