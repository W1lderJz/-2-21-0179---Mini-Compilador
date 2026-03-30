#include <stdio.h>
#include <string.h>
#include "compilador.h"

void analisis_semantico(char *linea);

int main() {

    FILE *entrada = fopen("entrada.txt", "r");
    FILE *salida = fopen("salida.c", "w");

    char linea[MAX_LINEA];

    while (fgets(linea, sizeof(linea), entrada)) {

        linea[strcspn(linea, "\n")] = 0;

        if (strlen(linea) == 0) continue;

        analisis_lexico(linea);

        if (!analisis_sintactico(linea)) continue;

        analisis_semantico(linea);

        generar_intermedio(linea);

        traducir_linea(linea, salida);
    }

    imprimir_tabla();

    fclose(entrada);
    fclose(salida);

    printf("\nCompilacion finalizada\n");

    return 0;
}
