# -*- coding: utf-8 -*-

# Implementación de un scanner mediante la codificación de un Autómata
# Finito Determinista como una Matríz de Transiciones

import sys

# tokens
INT = 100  # Número entero
FLT = 101  # Número de punto flotante
OPB = 102  # Operador binario
LRP = 103  # Delimitador: paréntesis izquierdo
RRP = 104  # Delimitador: paréntesis derecho
END = 105  # Fin de la entrada
VAR = 110  # Variable
FUN = 115  # Funcion
CLN = 120  # Delimitador: comma
ERR = 200  # Error léxico: palabra desconocida

# Matriz de transiciones: codificación del AFD
# [renglón, columna] = [estado no final, transición]
# Estados > 99 son finales (ACEPTORES)
# Caso especial: Estado 200 = ERROR
ERR = 200;
E = 24;


#       min  may   @    A    E   I   D    C    T   u    b    e    t    o    d    z    q    a    r    .    $    (    )    ,    ;   " "   &    |    -    <    =    ~    >
MT = [[  1,   2,   3,   2,   2,  2,  2,   2,   2,  1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 107, 999, 108, 109, 110, 111, 112,  18,  18,  21,  22,  19,  20,   E], # 0 inicio
      [  1,   E,   E,   E,   E,  E,  E,   E,   E,  1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 101, 101, 101, 101, 101, 101, 101,   E,   E,   E,   E,   E,   E,   E], # 1 variable
      [  E,   2,   E,   2,   2,  2,  2,   2,   2,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, 102, 102, 102, 102, 102, 102, 102,   E,   E,   E,   E,   E,   E,   E], # 2 constantes
      [  E,   E,   E,   4,   5,  6,  7,   8,   9,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 3 @
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   10,  E,   E,   E,   E, 104, 104, 104, 104, 104, 104, 104,   E,   E,   E,   E,   E,   E,   E], # 4 @A
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, 104, 104, 104, 104, 104, 104, 104,   E,   E,   E,   E,   E,   E,   E], # 5 @E
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,  11,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 6 @I
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,  12,   E,  13,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 7 @D
      [  E,   E,   E,   E,   E,  E,  E,   E,   E, 14,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 8 @C
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,  15,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 9 @T
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,  16,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 10 @Ad
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,  16,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 11 @Iz
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,  16,   E,   E,   E,   E,   E,  16, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 12 @De
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,  17,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 13 @Do
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,  17,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 14 @Cu
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,  17,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 15 @Te
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, 105, 105, 105, 105, 105, 105, 105,   E,   E,   E,   E,   E,   E,   E], # 16 binario
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, 106, 106, 106, 106, 106, 106, 106,   E,   E,   E,   E,   E,   E,   E], # 17 unario
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, 113, 113, 113, 113, 113, 113, 113,   E,   E,   E,   E,   E,   E,   E], # 18 op binario
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, 114, 114, 114, 114, 114, 114, 114,   E,   E,   E,   E,   E,   E,   E], # 19 =
      [115, 115, 115, 115, 115,115,115, 115, 115,115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115,   E], # 20 ~
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,  18], # 21 -
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,  23,   E,   E,   E,   E], # 22 <
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,  18], # 23 <-
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E]] # 24 error

# Filtro de caracteres: regresa el número de columna de la matriz de transiciones
# de acuerdo al caracter dado
def filtro(c):
    """Regresa el número de columna asociado al tipo de caracter dado(c)"""
    if c == '0' or c == '1' or c == '2' or \
       c == '3' or c == '4' or c == '5' or \
       c == '6' or c == '7' or c == '8' or c == '9': # dígitos
        return 0
    elif c == '+' or c == '-' or c == '*' or \
         c == '/': # operadores
        return 1
    elif c == '(': # delimitador (
        return 2
    elif c == ')': # delimitador )
        return 3
    elif c == ' ' or ord(c) == 9 or ord(c) == 10 or ord(c) == 13: # blancos
        return 5
    elif c == '.': # punto
        return 6
    elif c == '$': # fin de entrada
        return 7
    elif c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        return 8
    elif c == ',':
        return 9
    else: # caracter raro
        return 4

_c = None    # siguiente caracter
_leer = True # indica si se requiere leer un caracter de la entrada estándar

# Función principal: implementa el análisis léxico
def obten_token():
    """Implementa un analizador léxico: lee los caracteres de la entrada estándar"""
    global _c, _leer
    edo = 0 # número de estado en el autómata
    lexema = "" # palabra que genera el token
    while (True):
        while edo < 100:    # mientras el estado no sea ACEPTOR ni ERROR
            if _leer: _c = sys.stdin.read(1)
            else: _leer = True
            edo = MT[edo][filtro(_c)]
            if edo < 100 and edo != 0: lexema += _c
        if edo == INT:
            _leer = False # ya se leyó el siguiente caracter
            print "Entero", lexema
            return INT
        elif edo == FLT:
            _leer = False # ya se leyó el siguiente caracter
            print "Flotante", lexema
            return FLT
        elif edo == OPB:
            lexema += _c  # el último caracter forma el lexema
            print "Operador", lexema
            return OPB
        elif edo == LRP:
            lexema += _c  # el último caracter forma el lexema
            print "Delimitador", lexema
            return LRP
        elif edo == RRP:
            lexema += _c  # el último caracter forma el lexema
            print "Delimitador", lexema
            return RRP
        elif edo == END:
            print "Fin de expresion"
            return END
        elif edo == VAR:
            _leer = False # ya se leyó el siguiente caracter
            print "Variable", lexema
            return VAR
        elif edo == FUN:
            _leer = False # ya se leyó el siguiente caracter
            print "Funcion", lexema
            return FUN
        elif edo == CLN:
            lexema += _c  # el último caracter forma el lexema
            print "Delimitador", lexema
            return CLN
        else:
            leer = False # el último caracter no es raro
            print "ERROR! palabra ilegal", lexema
            return ERR





