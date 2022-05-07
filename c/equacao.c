#include <stdio.h>
#include <math.h>
int main()
{
    printf("Informe A: ");
    int a;
    scanf("%d", &a);
    printf("Informe B: ");
    int b;
    scanf("%d", &b);
    printf("Informe C: ");
    int c;
    scanf("%d", &c);

    int delta = (pow(b, 2)) - (4 * a * c);

    if (delta > 0) 
    {
        float x1;
        x1 = (-b + sqrt(delta)) / 2 * a;
        printf("x1 = %.2f\n", x1);
        float x2;
        x2 = (-b - sqrt(delta)) / 2 * a;
        printf("x2 = %.2f\n", x2);
    } else {
        printf("Nao possui raiz.");
    }
}