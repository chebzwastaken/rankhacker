#include <stdio.h>

int factorial(int n){
    int i, result = 1;
    for(i = 1; i <= n; i++){
        result *= i;
    }
    return result;
}

int rfactorial(int n){
    if(n == 0) return 1;

    return n * rfactorial(n - 1);
}

int trfactorial(int n, int running_total){
    if(n == 0) return running_total;
    else if (n <= 0) return n;
    else {
        printf("%d, %d\n", n - 1, running_total*n);
        return trfactorial(n - 1, running_total*n);
    }
}

int main(void){
    printf("%d\n", factorial(5));
    printf("%d\n", rfactorial(5));
    printf("%d\n", trfactorial(5, 1));
    return 0;
}

