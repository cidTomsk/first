#include <iostream>
#define N 10
using namespace std;
int A[N] = { 1,2,3,4,5,6,7,8,8,8 };
int quantity01A[2];
void counter01(int Ainput[], int size_A, int quantity01A[])
{
    for (int i = 0; i < size_A; i++)
    {
        int temp = A[i];
        int step;  // step это шаг
        if (A[i] < 2) step = 1;
        if (A[i] > 1 && A[i] < 4) step = 2; //количество шагов зависит 
        if (A[i] > 3 && A[i] < 8) step = 3; //размера числа
        if (A[i] > 7 && A[i] < 16) step = 4;
        for (int j = 0; j < step; j++)
        {
            if (temp % 2 == 0)
            {
                quantity01A[0]++;
            }
            else
            {
                quantity01A[1]++; // проверка 1=1, 2=01, 3=11, 4=100, 5=101
            }                    // 6=110, 7=111, 8=1000, 8=1000,8=1000
            temp = temp / 2;          // Итого 15 единиц и 14 нулей
        }
    }
   
}
int main()
{
    counter01(A, N, quantity01A);
    printf("0 count %d   ", quantity01A[0]);
    printf("1 count %d   ", quantity01A[1]);
    return 0;
}
