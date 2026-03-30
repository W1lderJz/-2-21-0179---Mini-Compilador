#ifndef COMPILADOR_H
#define COMPILADOR_H

#define MAX_LINEA 256

// Lexico
void analisis_lexico(char *linea);

// Sintactico
int analisis_sintactico(char *linea);

// Semantico
int variable_existe(char *var);
void registrar_variable(char *var);

// Tabla de símbolos
void imprimir_tabla();

// Intermedio
void generar_intermedio(char *linea);

// Generador final
void traducir_linea(char *linea, FILE *salida);

#endif
