import sys
import obten_token as scanner

def match(tokenEsperado):
    global token
    if token == tokenEsperado:
        token = scanner.obten_token()
    else:
        error("error de sinaxis")


def parser():
    global token
    token = scanner.obten_token()
    oraciones()
    if token == scaner.END:
        print "Expresion bien construida"
    else:
        error("Expresion mal terminada")

def  oraciones():
    oracion()
    token == scanner.obten_token()
    if(token == scanner.PYC):
        match(token)
        oraciones()

def oracion():
    oracion2()
    if(token == scanner.PUN):
        match(token)
        match(scanner.LRP)
        termino()
        match(scanner.RRP)
    elif(token == scanner.PBI):
        match(token)
        match(scanner.LRP)
        termino()
        match(scanner.CLN)
        match(scanner.BLK)
        termino()
        match(scanner.RRP)
    elif(token == scanner.LRP):
        match(token)
        oracion()
        match(scanner.RRP)
    elif(token == scanner.NEG):
        match(token)
        oracion()
    elif(token == scanner.CNT):
        match(token)
        match(scanner.PNT)
        match(scanner.VAR)
        match(scanner.BLK)
        oracion()
    else
        termino()
        match(scanner.BLK)
        match(scanner.EQU)
        match(scanner.BLK)
        termino()

def oracion2():
    if(token == scanner.OBI):
        match(token)
        oracion()
        oracion2()

def termino():
    if(token == scanner.VAR):
        match(token)
    else
        match(scanner.CTE)
