# -*- coding: utf-8 -*-

# Implementación de un scanner mediante la codificación de un Autómata
# Finito Determinista como una Matríz de Transiciones

import sys

# tokens
VAR = 101  # variable
CTE = 102  # constante
CNT = 104  # cuantificador
PBI = 105  # predicado binario
PUN = 106  # predicado unario
PNT = 107  # punto
LRP = 108  # Delimitador: paréntesis izquierdo
RRP = 109  # Delimitador: paréntesis derecho
CLN = 110  # coma
PYC = 111  # punto y coma
BLK = 112  # espacio
OBI = 113  # operador binario
EQU = 114  # igual (=)
NOT = 115  # negacion (~)
ERR = 200  # Error léxico: palabra desconocida
END = 999  # Final ($)

# Matriz de transiciones: codificación del AFD
# [renglón, columna] = [estado no final, transición]
# Estados > 99 son finales (ACEPTORES)
# Caso especial: Estado 200 = ERROR
E = 24;


#       min  may   @    A    E   I   D    C    T   u    b    e    t    o    d    z    q    a    r    .    $    (    )    ,    ;   " "   &    |    -    <    =    ~    >  raro
MT = [[  1,   2,   3,   2,   2,  2,  2,   2,   2,  1,   1,   1,   1,   1,   1,   1,   1,   1,   1, PNT, END, LRP, RRP, CLN, PYC, BLK,  18,  18,  21,  22,  19,  20,   E,  E], # 0 inicio
      [  1,   E,   E,   E,   E,  E,  E,   E,   E,  1,   1,   1,   1,   1,   1,   1,   1,   1,   1, VAR, VAR, VAR, VAR, VAR, VAR, VAR,   E,   E,   E,   E,   E,   E,   E,  E], # 1 variable
      [  E,   2,   E,   2,   2,  2,  2,   2,   2,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, CTE, CTE, CTE, CTE, CTE, CTE, CTE,   E,   E,   E,   E,   E,   E,   E,  E], # 2 constantes
      [  E,   E,   E,   4,   5,  6,  7,   8,   9,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E,  E], # 3 @
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   10,  E,   E,   E,   E, CNT, CNT, CNT, CNT, CNT, CNT, CNT,   E,   E,   E,   E,   E,   E,   E,  E], # 4 @A
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, CNT, CNT, CNT, CNT, CNT, CNT, CNT,   E,   E,   E,   E,   E,   E,   E,  E], # 5 @E
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,  11,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E,  E], # 6 @I
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,  12,   E,  13,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E,  E], # 7 @D
      [  E,   E,   E,   E,   E,  E,  E,   E,   E, 14,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E,  E], # 8 @C
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,  15,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E,  E], # 9 @T
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,  16,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E,  E], # 10 @Ad
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,  16,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E,  E], # 11 @Iz
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,  16,   E,   E,   E,   E,   E,  16, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E,  E], # 12 @De
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,  17,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E,  E], # 13 @Do
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,  17,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E,  E], # 14 @Cu
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,  17,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E,  E], # 15 @Te
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, PBI, PBI, PBI, PBI, PBI, PBI, PBI,   E,   E,   E,   E,   E,   E,   E,  E], # 16 binario
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, PUN, PUN, PUN, PUN, PUN, PUN, PUN,   E,   E,   E,   E,   E,   E,   E,  E], # 17 unario
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, OBI, OBI, OBI, OBI, OBI, OBI, OBI,   E,   E,   E,   E,   E,   E,   E,  E], # 18 op binario
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, EQU, EQU, EQU, EQU, EQU, EQU, EQU,   E,   E,   E,   E,   E,   E,   E,  E], # 19 =
      [NOT, NOT, NOT, NOT, NOT,NOT,NOT, NOT, NOT,NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT, NOT,   E,  E], # 20 ~
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,  18,  E], # 21 -
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,  23,   E,   E,   E,   E,  E], # 22 <
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,  18,  E], # 23 <-
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E,  E]] # 24 error

# Filtro de caracteres: regresa el número de columna de la matriz de transiciones
# de acuerdo al caracter dado
def filtro(c):
    if c == 'c' or \
       c == 'f' or \
       c == 'g' or c == 'h' or c == 'i' or \
       c == 'j' or c == 'k' or c == 'l' or c == 'm' or \
       c == 'n' or c == 'p' or \
       c == 's' or \
       c == 'v' or c == 'w' or c == 'x' or c == 'y': # minúsculas menos u,b,e,t,o,d,z,q,a,r
        return 0
    elif c == 'B' or \
        c == 'F' or \
        c == 'G' or c == 'H' or \
        c == 'J' or c == 'K' or c == 'L' or \
        c == 'M' or c == 'N' or \
        c == 'O' or c == 'P' or \
        c == 'Q' or c == 'R' or c == 'S' or \
        c == 'U' or c == 'V' or c == 'W' or \
        c == 'X' or c == 'Y' or c == 'Z': # mayúsculas menos A,C,D,E,I,T
        return 1
    elif c == '@': # delimitador (
        return 2
    elif c == 'A': # delimitador )
        return 3
    elif c == 'E': # blancos
        return 4
    elif c == 'I': # punto
        return 5
    elif c == 'D': # fin de entrada
        return 6
    elif c == 'C':
        return 7
    elif c == 'T':
        return 8
    elif c == 'u':
        return 9
    elif c == 'b':
        return 10
    elif c == 'e':
        return 11
    elif c == 't':
        return 12
    elif c == 'o':
        return 13
    elif c == 'd':
        return 14
    elif c == 'z':
        return 15
    elif c == 'q':
        return 16
    elif c == 'a':
        return 17
    elif c == 'r':
        return 18
    elif c == '.':
        return 19
    elif c == '$':
        return 20
    elif c == '(':
        return 21
    elif c == ')':
        return 22
    elif c == ',':
        return 23
    elif c == ';':
        return 24
    elif c == ' ':
        return 25
    elif c == '&':
        return 26
    elif c == '|':
        return 27
    elif c == '-':
        return 28
    elif c == '<':
        return 29
    elif c == '=':
        return 30
    elif c == '~':
        return 31
    elif c == '>':
        return 32
    else:
        return 33

_c = None    # siguiente caracter
_leer = True # indica si se requiere leer un caracter de la entrada estándar

# Función principal: implementa el análisis léxico
def obten_token():
    global _c, _leer
    edo = 0 # número de estado en el autómata
    lexema = "" # palabra que genera el token
    while (True):
        while edo < 100:    # mientras el estado no sea ACEPTOR ni ERROR
            if _leer: _c = sys.stdin.read(1)
            else: _leer = True
            edo = MT[edo][filtro(_c)]
            #print edo
            if edo < 100 and edo != 0: lexema += _c
        if edo == VAR:
            _leer = False # ya se leyó el siguiente caracter
            print "Variable", lexema
            return VAR
        elif edo == CTE:
            _leer = False # ya se leyó el siguiente caracter
            print "Constante", lexema
            return CTE
        elif edo == CNT:
            _leer = False  # ya se leyó el siguiente caracter
            print "Cuantificador", lexema
            return CNT
        elif edo == PBI:
            _leer = False  # ya se leyó el siguiente caracter
            print "Predicado Binario", lexema
            return PBI
        elif edo == PUN:
            _leer = False  # ya se leyó el siguiente caracter
            print "Predicado Unario", lexema
            return PUN
        elif edo == PNT:
            lexema += _c  # el último caracter forma el lexema
            print "Punto", lexema
            return PNT
        elif edo == LRP:
            lexema += _c  # el último caracter forma el lexema
            print "Paréntesis izquierdo", lexema
            return LRP
        elif edo == RRP:
            lexema += _c  # el último caracter forma el lexema
            print "Paréntesis izquierdo", lexema
            return RRP
        elif edo == CLN:
            lexema += _c  # el último caracter forma el lexema
            print "Coma", lexema
            return CLN
        elif edo == PYC:
            lexema += _c  # el último caracter forma el lexema
            print "Punto y coma", lexema
            return PYC
        elif edo == BLK:
            lexema += _c  # el último caracter forma el lexema
            print "Espacio", lexema
            return BLK
        elif edo == OBI:
            _leer = False  # ya se leyó el siguiente caracter
            print "Operador Binario", lexema
            return OBI
        elif edo == EQU:
            _leer = False  # ya se leyó el siguiente caracter
            print "Igualdad", lexema
            return EQU
        elif edo == NOT:
            _leer = False  # ya se leyó el siguiente caracter
            print "Negación", lexema
            return NOT
        elif edo == END:
            print "Fin", lexema
            return END
        else:
            leer = False # el último caracter no es raro
            print "ERROR! palabra ilegal", lexema
            return ERR
