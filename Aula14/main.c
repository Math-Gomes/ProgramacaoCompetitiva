#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define TAM 5

int main(){
    int vetor[TAM] = {5,4,3,2,1};

    for(int i = 0; i < (1 << TAM); i++){
        printf("{ ");
        for(int j = 0; j < TAM; j++){
            if((i >> j) & 1){
                printf("%d ", vetor[j]);
            }
        }
        printf("}\n");
    }

    return 0;
}