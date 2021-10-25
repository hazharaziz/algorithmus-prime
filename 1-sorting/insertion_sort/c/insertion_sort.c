#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void insertion_sort(int length, int arr[], bool increasing) {
    int i, j, key;
    for (i = 1; i < length; i++) {
        key = arr[i];
        j = i - 1;
        while (j > -1 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1; 
        }
        arr[j + 1] = key;
    }
    for (int k = 0; k < length; k++) {
        printf("%d ", arr[k]);
    }
    printf("\n");
}

int main() {
    int arr[] = { 1, 5, 4, 2, 6 };
    int length = sizeof(arr) / sizeof(arr[0]);
    insertion_sort(length, arr, true);

    return 0;
}