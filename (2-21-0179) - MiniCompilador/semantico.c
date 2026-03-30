#include <stdio.h>
#include <string.h>
#include "compilador.h"

int variable_existe(char *var);

void analisis_semantico(char *linea) {
    printf("[SEMANTICO] ");

    if (strchr(linea, '=') != NULL) {
        char var[50];
        sscanf(linea, "%s =", var);

        if (!variable_existe(var)) {
            printf("Error: variable no declarada (%s)\n", var);
        } else {
            printf("Correcto\n");
        }
    } else {
        printf("OK\n");
    }
}
