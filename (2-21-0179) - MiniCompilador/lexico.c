#include <stdio.h>
#include <string.h>
#include "compilador.h"

void analisis_lexico(char *linea) {
    printf("\n[LEXICO]\n");

    char copia[MAX_LINEA];
    strcpy(copia, linea);

    char *token = strtok(copia, " ");

    while (token != NULL) {
        printf("TOKEN: %s\n", token);
        token = strtok(NULL, " ");
    }
}
