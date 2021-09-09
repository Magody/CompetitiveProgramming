#include <iostream>
#include <string>
#include <list>
#include <map>
#include <algorithm>
#include <math.h>
#include<time.h>
#include <chrono>


using namespace std;

float getDistanceBetweenTwoPoints(float x1, float y1, float x2, float y2)
{
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}
bool isInsideOfEllipse(
    double x, double y,
    double fcx1, double fcy1, 
    double fcx2, double fcy2,
    double r
){
    double d1 = getDistanceBetweenTwoPoints(x, y, fcx1, fcy1);
    double d2 = getDistanceBetweenTwoPoints(x, y, fcx2, fcy2);
    return (d1 + d2) < r;
}


bool isInsideOfEllipseNoRotOptimized(double x, 
    double y, 
    float h, 
    float k, 
    float powA, 
    float powB,
    float powAB
    )
{
    
    float n1 = (x - h) * (x - h);
    float n2 = (y - k) * (y - k);

    // > for outside

    return ((n1*powB + n2*powA)/powAB) <= 1.0;
}

float getEllipseB(float powA, float c)
{
    return sqrt(powA - pow(c, 2));
}


double getDistancePow2BetweenTwoPoints(double x1, double y1, double x2, double y2)
{
    return pow(x2 - x1, 2) + pow(y2 - y1, 2);
}

bool isInsideAnyEllipse(float **matrixEllipsesData, int n, double montecarloX, double montecarloY)
{
    

    for (size_t i = 0; i < n; i++)
    {
        float h = matrixEllipsesData[i][0];
        float k = matrixEllipsesData[i][1];
        float powA = matrixEllipsesData[i][2];
        float powB = matrixEllipsesData[i][3];
        float powAB = matrixEllipsesData[i][4];
        float fcx1 = matrixEllipsesData[i][5];
        float fcy1 = matrixEllipsesData[i][6];
        float fcx2 = matrixEllipsesData[i][7];
        float fcy2 = matrixEllipsesData[i][8];
        float r = matrixEllipsesData[i][9];


        if (isInsideOfEllipse(montecarloX, montecarloY, fcx1, fcy1, fcx2, fcy2, r))
        {
            return true;
        }
    }
    return false;
}

bool debug = false;
double numberPoints = 1000000;

/*
1
2
15 -20 15 20 50
-10 10 30 30 100
*/
int main()
{

    srand(time(0));

    chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

    cout.precision(std::numeric_limits<double>::max_digits10);

    int t = 1;
    if (!debug)
        cin >> t;

    for (size_t testCase = 1; testCase <= t; testCase++)
    {
        int n = 1;

        if (!debug)
            cin >> n;

        float **matrixEllipses = new float *[n];


        for (size_t i = 0; i < n; i++)
        {
            // store h, k, a, b
            matrixEllipses[i] = new float[10];

            float fcx1 = -40, 
                   fcy1 = 0, 
                   fcx2 = 40, 
                   fcy2 = 0, 
                   r = 100;
            if (!debug)
            {
                cin >> fcx1 >> fcy1 >> fcx2 >> fcy2 >> r;
            }
            float a = r / 2;
            float c = getDistanceBetweenTwoPoints(fcx1, fcy1, fcx2, fcy2)/2;
            
            matrixEllipses[i][0] = fcx1 + (fcx2 - fcx1) / 2;
            matrixEllipses[i][1] = fcy1 + (fcy2 - fcy1) / 2;
            matrixEllipses[i][2] = pow(a, 2);
            
            float b = getEllipseB(matrixEllipses[i][2], c);
            matrixEllipses[i][3] = pow(b, 2);
            matrixEllipses[i][4] = matrixEllipses[i][2] * matrixEllipses[i][3];

            matrixEllipses[i][5] = fcx1;
            matrixEllipses[i][6] = fcy1;
            matrixEllipses[i][7] = fcx2;
            matrixEllipses[i][8] = fcy2;
            matrixEllipses[i][9] = r;
        }

        double countPointsUnpinted = 0;


        for (size_t i = 0; i < numberPoints; i++)
        {
            double x = -50 + (((double) rand()) / (double) RAND_MAX)*100;
            double y = -50 + (((double) rand()) / (double) RAND_MAX)*100;
            
            // cout << x << "," << y << endl;
            bool isInside = isInsideAnyEllipse(matrixEllipses, n, x, y);
            if(!isInside){
                countPointsUnpinted++;
            }

        }

        
        double result = (countPointsUnpinted * 100) / numberPoints;
        if (debug)
        {
            cout << result << endl;
            
        }
        cout << round(result) << "%" << endl;
    }

    chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    if (debug)
    {
        cout << "Time = " << chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() << "[ms]" << std::endl;
    }
    
    return 0;
}