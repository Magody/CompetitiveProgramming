#include <iostream>
#include <string>
#include <list>
#include <map>
#include <algorithm>
#include <math.h>
#include <chrono>

using namespace std;

bool debug = true;


int LPS(string text, int M){

    

    int lps[M];
    
    int length = 0;        
    int i = 1;
    lps[0] = 0;   

    while(i < M){
        if(text.substr(i, 1) == text.substr(length, 1)){
            length += 1;
            lps[i] = length;
            i += 1;
        }
        else{
            if(length != 0)
            {
                length = lps[length-1];
            }   
            else{
                lps[i] = 0;
                i += 1;
            }      
                
        }
    }

    
        
    return lps[M-1];
}



int isPeriodico(string stringDiff){
    


    int x = stringDiff.size();
    
    int masLargo=LPS(stringDiff, x);
    
    if(masLargo!=0 && x%(x-masLargo)==0){
        int counter = 0;
        for(size_t i=0; i<(x-masLargo); i++){
            string element = stringDiff.substr(i, 1);
            if(element == " "){
                counter += 1;
            }
        }

        

        return counter;
    }else{
        return -1;
    }
}

template <typename T> 
T reduce2(T v) {
    T k = ((v * 410) >> 12) & 0x000F000F000F000Full;
    return (((v - k * 10) << 8) + k);
}
 
template <typename T>
T reduce4(T v) {
    T k = ((v * 10486) >> 20) & 0xFF000000FFull;
    return reduce2(((v - k * 100) << 16) + (k));
}
 
typedef unsigned long long ull;
inline ull reduce8(ull v) {
    ull k = ((v * 3518437209u) >> 45);
    return reduce4(((v - k * 10000) << 32) + (k));
}
 
template <typename T>
std::string itostr(T o) {
    union {
        char str[16];
        unsigned short u2[8];
        unsigned u4[4];
        unsigned long long u8[2];
    };
 
    unsigned long long v = o < 0 ? ~o + 1 : o;
 
    u8[0] = (ull(v) * 3518437209u) >> 45;
    u8[0] = (u8[0] * 28147497672ull);
    u8[1] = v - u2[3] * 100000000;
 
    u8[1] = reduce8(u8[1]);
    char* f;
    if (u2[3]) {
        u2[3] = reduce2(u2[3]);
        f = str + 6;
    } else {
        unsigned short* k = u4[2] ? u2 + 4 : u2 + 6;
        f = *k ? (char*)k : (char*)(k + 1);
    }
    if (!*f) f++;
 
    u4[1] |= 0x30303030;
    u4[2] |= 0x30303030;
    u4[3] |= 0x30303030;
    if (o < 0) *--f = '-';
    return std::string(f, (str + 16) - f);
}

int main()
{


    chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

    
    unsigned long long n = 1000000, t = 1000000;

    if (!debug)
        cin >> n >> t;

    list<unsigned long long> diferencias;
    unsigned long long temp2 = 0;
    unsigned long long inicial = 1, temp1 = 3;

    unsigned long long valueToAppend = 0;
    string stringDiff = "";

    unsigned long long sumFull = 0;
    if (!debug)
        cin >> inicial;

    for (size_t x = 1; x < n; x++){
        if (!debug)
            cin >> temp1;
        
        if(x==1){
            valueToAppend = temp1-inicial;
        }else{
            valueToAppend = temp1-temp2;
        }

        diferencias.push_back(valueToAppend);
        sumFull += valueToAppend;

        string s = to_string(valueToAppend);

        /*
        itostr<unsigned long long>(valueToAppend);
        to_string(valueToAppend);
        */

        

        stringDiff += s + " ";
        temp2=temp1;
    }

    chrono::steady_clock::time_point middle = std::chrono::steady_clock::now();
    if (debug)
    {
        cout << "Time = " << chrono::duration_cast<std::chrono::milliseconds>(middle - begin).count() << "[ms]" << std::endl;
    }

    // 255/358

    int periodIndex = isPeriodico(stringDiff);

    

    // 260/405

    
    valueToAppend = t+inicial-temp2;
    
    diferencias.push_back(valueToAppend);
    sumFull += valueToAppend;
    stringDiff +=  to_string(valueToAppend) + " ";

    unsigned long long sum = 0;
    typename list<unsigned long long>::iterator it;

    

    
    // 331/354
    if(periodIndex == -1){
        cout << (sumFull - 1) << endl;
    }
    else{
        int index = 0;
        for (it = diferencias.begin(); it != diferencias.end(); ++it){
            sum += *it;

            index++;
            if(index == periodIndex){
                break;
            }
        }
        cout << (sum - 1) << endl;
    }
    

        

   

    chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    if (debug)
    {
        cout << "Time = " << chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() << "[ms]" << std::endl;
    }

    return 0;
}