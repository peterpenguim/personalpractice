#include <stdio.h>
int main()
{
    int n1;
    int n2;
    int n3;

    printf("Valor 1: ");
    scanf("%d", &n1);
    printf("Valor 2: ");
    scanf("%d", &n2);
    printf("Valor 3: ");
    scanf("%d", &n3);

    if (n1 > n2 && n1 > n3) {
        printf("Maior: %d", n1);

    } else {
        if (n2 > n1 && n2 > n3) {
            printf("Maior: %d", n2);
        } else {
        printf("Maior: %d", n3);
    }
    } 

    return 0;
}