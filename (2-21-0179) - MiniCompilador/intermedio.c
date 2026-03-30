#include <stdio.h>
#include <string.h>
#include "compilador.h"

void generar_intermedio(char *linea) {
    if (strchr(linea, '+')) {
        printf("[INTERMEDIO] t1 = operacion\n");
    }
}
