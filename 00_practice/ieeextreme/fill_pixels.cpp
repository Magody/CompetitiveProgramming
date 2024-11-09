#include <iostream>
#include <string>
#include <list>
#include <map>
#include <algorithm>
#include <math.h>
#include <chrono>

using namespace std;

void printMatrix(bool **matrix, int n, int m)
{
    cout << "IMPRESS" << endl;
    for (size_t i = 0; i < n; i++)
    {
        for (size_t j = 0; j < m; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

void DFSFillPlus(bool **pixels, int h, int w, int i, int j, int level){
    //  left, top, right and bottom
    if(!pixels[i][j]){
        return;
    }
    pixels[i][j] = 0;

    int left = j-1;
    int top = i-1;
    int right = j+1;
    int bottom = i+1;

    if(left >= 0){
        DFSFillPlus(pixels, h, w, i, left, level+1);
    }
    if(top >= 0){
        DFSFillPlus(pixels, h, w, top, j, level+1);
    }
    if(right < w){
        DFSFillPlus(pixels, h, w, i, right, level+1);
    }
    if(bottom < h){
        DFSFillPlus(pixels, h, w, bottom, j, level+1);
    }

}

void DFSFillCross(bool **pixels, int h, int w, int i, int j, int level){
    //  left, top, right and bottom
    if(!pixels[i][j]){
        return;
    }
    pixels[i][j] = 0;

    int top_left[2] = {i-1, j-1};
    int top_right[2] = {i-1, j+1};
    int bottom_right[2] = {i+1, j+1};
    int bottom_left[2] = {i+1, j-1};

    if(top_left[0] >= 0 && top_left[1] >= 0){
        DFSFillCross(pixels, h, w,top_left[0], top_left[1], level+1);
    }
    if(top_right[0] >= 0 && top_right[1] < w){
        DFSFillCross(pixels, h, w, top_right[0], top_right[1], level+1);
    }
    if(bottom_right[0] < h && bottom_right[1] < w){
        DFSFillCross(pixels, h, w, bottom_right[0], bottom_right[1], level+1);
    }
    if(bottom_left[0] < h && bottom_left[1] >= 0){
        DFSFillCross(pixels, h, w, bottom_left[0], bottom_left[1], level+1);
    }


}


void DFSFillStar(bool **pixels, int h, int w, int i, int j, int level){
    //  left, top, right and bottom
    if(!pixels[i][j]){
        return;
    }
    pixels[i][j] = 0;

    int left = j-1;
    int top = i-1;
    int right = j+1;
    int bottom = i+1;

    int top_left[2] = {i-1, j-1};
    int top_right[2] = {i-1, j+1};
    int bottom_right[2] = {i+1, j+1};
    int bottom_left[2] = {i+1, j-1};


    if(left >= 0){
        DFSFillStar(pixels, h, w, i, left, level+1);
    }
    if(top >= 0){
        DFSFillStar(pixels, h, w, top, j, level+1);
    }
    if(right < w){
        DFSFillStar(pixels, h, w, i, right, level+1);
    }
    if(bottom < h){
        DFSFillStar(pixels, h, w, bottom, j, level+1);
    }

    if(top_left[0] >= 0 && top_left[1] >= 0){
        DFSFillStar(pixels, h, w,top_left[0], top_left[1], level+1);
    }
    if(top_right[0] >= 0 && top_right[1] < w){
        DFSFillStar(pixels, h, w, top_right[0], top_right[1], level+1);
    }
    if(bottom_right[0] < h && bottom_right[1] < w){
        DFSFillStar(pixels, h, w, bottom_right[0], bottom_right[1], level+1);
    }
    if(bottom_left[0] < h && bottom_left[1] >= 0){
        DFSFillStar(pixels, h, w, bottom_left[0], bottom_left[1], level+1);
    }

}

bool debug = true;

int main()
{
    
    chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

    int t = 1;
    if (!debug)
        cin >> t;

    for (size_t testCase = 1; testCase <= t; testCase++)
    {
        int w = 26, 
            h = 13;

        if (!debug)
            cin >> w >> h;

        
        bool * pixelsPlus[h];
        bool * pixelsCross[h];
        bool * pixelsStar[h];

        for (size_t i = 0; i < h; i++)
        {
            pixelsPlus[i] = new bool[w];
            pixelsCross[i] = new bool[w];
            pixelsStar[i] = new bool[w];

            for (size_t j = 0; j < w; j++)
            {
                char a;
                cin >> a;
                bool value = a -'0';
                pixelsPlus[i][j] = value;
                pixelsCross[i][j] = value;
                pixelsStar[i][j] = value;
                
            }
        }

        int counterPlus = 0;
        int counterCross = 0;
        int counterStar = 0;

        for (size_t i = 0; i < h; i++)
        {
            for (size_t j = 0; j < w; j++)
            {
                if(pixelsPlus[i][j]){
                    // pixelsPlus[i][j] = 0;
                    // printMatrix(pixelsPlus, h, w);
                    DFSFillPlus(pixelsPlus, h, w, i, j, 0);
                    // printMatrix(pixelsPlus, h, w);
                    counterPlus += 1;
                }
                if(pixelsCross[i][j]){
                    // pixelsPlus[i][j] = 0;
                    // printMatrix(pixelsCross, h, w);
                    DFSFillCross(pixelsCross, h, w, i, j, 0);
                    // printMatrix(pixelsCross, h, w);
                    counterCross += 1;
                }
                if(pixelsStar[i][j]){
                    // pixelsPlus[i][j] = 0;
                    // printMatrix(pixelsStar, h, w);
                    DFSFillStar(pixelsStar, h, w, i, j, 0);
                    // printMatrix(pixelsStar, h, w);
                    counterStar += 1;
                }
            }
        }

        cout << counterPlus << " " << counterCross << " " << counterStar << endl;
    }

    chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    if (debug)
    {
        cout << "Time = " << chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() << "[ms]" << std::endl;
    }

    return 0;
}