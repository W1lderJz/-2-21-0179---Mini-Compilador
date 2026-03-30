#include <stdio.h>
#include <string.h>
#include "compilador.h"

int analisis_sintactico(char *linea) {
    printf("[SINTACTICO] ");

    if (strncmp(linea, "ENTERO", 6) == 0 ||
        strncmp(linea, "ESCRIBIR", 8) == 0 ||
        strncmp(linea, "LEER", 4) == 0 ||
        strcmp(linea, "INICIO") == 0 ||
        strcmp(linea, "FIN") == 0 ||
        strstr(linea, "=") != NULL) {

        printf("Correcto\n");
        return 1;
    }

    printf("Error de estructura\n");
    return 0;
}
