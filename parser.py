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
    if token == scanner.END:
        print "Expresion bien construida"
    else:
        error("Expresion mal terminada")

def  oraciones():
    oracion()
    token == scanner.obten_token()
    if(token == scanner.PYC):
        match(token)
        print token
        oraciones()

def oracion():
    if(token == scanner.PUN):
        match(token)
        match(scanner.LRP)
        termino()
        match(scanner.RRP)
        oracion2()
    elif(token == scanner.PBI):
        match(token)
        match(scanner.LRP)
        termino()
        match(scanner.CLN)
        termino()
        match(scanner.RRP)
        oracion2()
    elif(token == scanner.LRP):
        match(token)
        oracion()
        match(scanner.RRP)
        oracion2()
    elif(token == scanner.NOT):
        match(token)
        oracion()
        oracion2()
    elif(token == scanner.CNT):
        match(token)
        match(scanner.PNT)
        match(scanner.VAR)
        match(scanner.BLK)
        oracion()
        oracion2()
    else:
        termino()
        match(scanner.BLK)
        match(scanner.EQU)
        match(scanner.BLK)
        termino()
        oracion2()

def oracion2():
    if(token == scanner.BLK):
        match(token)
        if(token == scanner.OBI):
            match(token)
            match(scanner.BLK)
            oracion()
            oracion2()

def termino():
    if(token == scanner.VAR):
        match(token)
    else:
        match(scanner.CTE)
parser()
