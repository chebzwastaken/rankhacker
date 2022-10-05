#include <stdio.h>

int linearSearch(int array[], int size, int value){
    int i;
    for(i = 0; i < size; i++){
        if(array[i] == value) return i;
    }
    return -1;
}

// recursive linearSearch
int rlinearSearch(int array[], int size, int value){
    if (array[size] == value) return size;
    return rlinearSearch(array, size-1, value);
}

// Linear Search with that uses a sentinal 
int slinearSearch(int array[], int size, int value){
    int i;
    array[size] = value; // sentinal value
    for(i = 0;; i++){
        // printf("%d %d %d\n", i, array[i], array[size]);
        if (array[i] == value) break;
        //shouldn't this be an infinite loop?
        // no becuase it sets the sentinal value to the last value
        // sentinal value is a value that we can throw away
    }
    if (i < size) return i;
    else return -1;

}

int *bubbleSort(int array[], int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < (size - 1); j++)
        {
            if (array[j] > array[j + 1])
            {
                array[j] = array[j + 1];
                array[j + 1] = array[j];
            }
        }
    }

    return array;
}

// bubble sort
int binarySearch(int array[], int size, int value){
    // sort array
    bubbleSort(array, size);

    int left = 0;
    int right = size; 
    while (left <= right){
        int pivot = left + (right - left) / 2;
        // printf("%d %d %d\n", left, pivot, right);
        if (array[pivot] == value) return pivot;
        else if (value < array[pivot]) right = pivot - 1;
        else left = pivot + 1;
    }
    return -1;
}

// recursive binary search
int rbinarySearch(int array[], int left, int right, int value){
    bubbleSort(array, right);
    if ( left >= right ) return -1;
    int pivot = left + (right - left) / 2;
    if (array[pivot] == value) return pivot;
    else if (value < array[pivot]) return rbinarySearch(array, left, pivot + 1, value);
    else return rbinarySearch(array, pivot - 1, right, value);
    
}

int main(int argc, char const *argv[])
{
    int array[] = {1, 2, 3, 3, 5, 6, 8, 9, 10};
    int size = sizeof(array)/sizeof(array[0]);
    int value = 8;
    printf("%d\n", linearSearch(array, size, value));
    printf("%d\n", rlinearSearch(array, size, value));
    printf("%d\n", slinearSearch(array, size, value));
    printf("%d\n", binarySearch(array, size, value));
    printf("%d\n", rbinarySearch(array, 0, size, value));
    return 0;
}
