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

    int w = 98765, 
        h = 43210, 
        a = 1, b = 1;
    cpp_int m = 777, c = 1;

    if (!debug)
        cin >> w >> h >> a >> b >> m >> c;

    cpp_int tw = cpp_int(ceil((double)w/a));
    cpp_int th = cpp_int(ceil((double)h/b));

    int modWA = (w%a);

    int rw = 0;
    if(modWA > 0){
        rw = a - modWA;
    }

    int modHB = (h%b);

    int rh = 0;
    if(modHB > 0){
        rh = b - modHB;
    }

    cpp_int partsToCut = 0;
    if(rw > 0){
        partsToCut += h;
    }
    if(rh > 0){
        partsToCut += w;
    }

    cpp_int costCut = partsToCut * c;
    cpp_int costTiles = cpp_int(ceil((double)(tw*th)/10)) * m;

    if(debug){
        cout << tw << endl;
        cout << th << endl;
        cout << (double)(tw*th)/10 << endl;
        cout << m << endl;
    }

    cout << (costCut + costTiles) << endl;

    chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    if (debug)
    {
        cout << "Time = " << chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() << "[ms]" << std::endl;
    }

    return 0;
}