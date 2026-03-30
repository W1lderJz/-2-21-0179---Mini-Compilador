#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "compilador.h"

char *tabla[100];
int contador = 0;

void registrar_variable(char *var) {
    tabla[contador++] = strdup(var);
}

int variable_existe(char *var) {
    for (int i = 0; i < contador; i++) {
        if (strcmp(tabla[i], var) == 0) {
            return 1;
        }
    }
    return 0;
}

void imprimir_tabla() {
    printf("\n[TABLA DE SIMBOLOS]\n");
    for (int i = 0; i < contador; i++) {
        printf("%s\n", tabla[i]);
    }
}
