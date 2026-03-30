#include <stdio.h>
#include <string.h>
#include "compilador.h"

int nivel = 0;

void traducir_linea(char *linea, FILE *salida) {

    if (strcmp(linea, "INICIO") == 0) {
        fprintf(salida, "#include <stdio.h>\n\nint main() {\n");
        nivel = 1;
    }

    else if (strcmp(linea, "FIN") == 0) {
        fprintf(salida, "return 0;\n}\n");
    }

    else if (strncmp(linea, "ENTERO ", 7) == 0) {
        registrar_variable(linea + 7);
        fprintf(salida, "int %s;\n", linea + 7);
    }

    else if (strchr(linea, '=')) {
        fprintf(salida, "%s;\n", linea);
    }

    else if (strncmp(linea, "ESCRIBIR ", 9) == 0) {
        fprintf(salida, "printf(\"%%d\\n\", %s);\n", linea + 9);
    }
}
