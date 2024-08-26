#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

/// @brief 
void main(){    
    srand(time(NULL));
    char senha[16] = "";
    int i, numero1;
    char letras_maius[26] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char letras_minus[26] = "abcdefghijklmnopqrstuvwxyz";
    char numeros[10] = "1234567890";
    for (i = 0; i < 15; i++){
        numero1 = rand() % 3;
        int numero2;
        if (numero1 == 0){
            numero2 = rand() % 26;
            senha[i] = letras_maius[numero2];
        }
        if (numero1 == 1){
            numero2 = rand() % 26;
            senha[i] = letras_minus[numero2];
        }
        if (numero1 == 2){
            numero2 = rand() % 10;
            senha[i] = numeros[numero2];
        }    
    }
    senha[16] = "\n";
    printf("Senha criada: %s", senha);
    return;
}