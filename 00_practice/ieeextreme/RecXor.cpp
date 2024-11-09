// ! https://csacademy.com/ieeextreme-practice/task/f8d68dbb0c844910797ce64354c66143/

#include <iostream>
#include <stdlib.h>

using namespace std;

long getXor(long num)
{
  switch (num % 4)
  {
  case 0:
    return num;
  case 1:
    return 1;
  case 2:
    return num + 1;
  default:
    return 0;
  }
}

long getRow(long num, long n, long l)
{
  return (num - n) / l + 1;
}

long getColumn(long num, long n, long l)
{
  return (num - n) % l + 1;
}

long solve(long l, long h, long n, long d1, long d2)
{

  long colD1 = getColumn(d1, n, l);
  long colD2 = getColumn(d2, n, l);

  long diffCol = abs(colD2 - colD1);
  long initInnerNum = colD1 > colD2 ? d1 - diffCol : d1;

  long limit = l * h + n - 1;
  long amount = getXor(limit);

  amount ^= getXor(n - 1);
  long p1 = 0;

  while (initInnerNum + p1 * l <= d2)
  {
    long before = initInnerNum + p1 * l - 1;
    long final = initInnerNum + p1 * l + diffCol;

    amount ^= getXor(before);
    amount ^= getXor(final);
    p1++;
  }

  return amount;
}

int main()
{
  int tests;
  cin >> tests;

  for (int i = 0; i < tests; i++)
  {
    long l, h, n, d1, d2;
    cin >> l;
    cin >> h;
    cin >> n;
    cin >> d1;
    cin >> d2;

    cout << solve(l, h, n, d1, d2) << endl;
  }
  return 0;
}