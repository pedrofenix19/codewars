#include <stddef.h>
#include <stdio.h>

void count_positives_sum_negatives(
    int *values, size_t count, int *positivesCount, int *negativesSum){
    if(count == 0) return;

    for(int i = 0; i < count; i++){
        printf("value %d %d\n", i, values[i]);
        if(values[i] > 0){ 
            printf("pos\n");
            *positivesCount += 1;
        }
        else{
            printf("neg\n");
            *negativesSum += values[i];
        } 
    }

    return;
}
  // Please store the positives count in the memory, pointed to
  // by the positivesCount parameter.
  
  // Please store the negatives sum in the memory, pointed to
  // by the negativesSum parameter.

  int main(){

    int posCountReceived = 0;
    int negSumReceived = 0;

    int values[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15 };

    count_positives_sum_negatives(
        values, sizeof(values)/sizeof(values[0]),
        &posCountReceived, &negSumReceived);

    printf("%d, %d\n", posCountReceived, negSumReceived);
  }