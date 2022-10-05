#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int helloWorld(char * name){
    printf("Hello, %s \n", name);
    return 0;
}

int getChar(void){
    for(int i = 0; i < 10; i++){
        printf("%c", getchar());
    }
    printf("\n");
    return 0;
}

int currencyConverter(void){
    printf("UK Pounds: ");
    printf("%s", "        ");
    printf("Euros: \n");
    for ( float i; i < 11; i++){
        printf("%.2f, %.2f\n", i, i * 1.17);
    }

    return 0;
}

// write number to a file 
int writeNumber(void){
    int number;
    FILE *file;
    scanf("%d", &number);
    file = fopen("number.txt", "w");
    fprintf(file, "%d", number);
    fclose(file);

    return 0;
}

int RNG(void){
    srand(time(NULL));
    int guess;
    int number = rand() % 100; // random number between 0 and 100
    for(int i = 0; i < 7; i++){
        printf("Guess a number between 0 and 100: ");
        scanf("%d", &guess);
        if(guess == number){
            printf("You guessed the number!\n");
            return 0;
        }else if(guess > number){
            printf("Too high!\n");
        }else{
            printf("Too low!\n");
        }
    }
    printf("You ran out of guesses!\n");
    return 0;
}

int reverseRNG(void){
    int number; 
    scanf("%d", &number);

    // computer guesses
    srand(time(NULL));
    int guess;
    int low = 0;
    int high = 10000;

    for(int i = 0; i < 700; i++){
        guess = rand() % (high - low) + low; // random number between low and high
        printf("Computer guesses: %d\n", guess);
        if(guess == number){
            printf("Computer guessed the number!\n");
            return 0;
        }else if(guess > number){
            printf("Too high!\n");
            high = guess;
        }else{
            printf("Too low!\n");
            low = guess;
        }
    }

    return 0;
}

int main(int argc, char const *argv[])
{
    // helloWorld("World");
    // getChar();
    // currencyConverter();
    // writeNumber();
    // RNG();
    reverseRNG();
    return 0;
}
