import pattern.es
from pattern.es import conjugate, INFINITIVE
from collections import Counter
import json

archivo = 'archivo.txt'
nombre = 'verbos.json'
lista = []
lista_palabras = []

def crear (archivo,lista_palabras):
    with open (archivo,'w') as f:
        json.dump(lista_palabras,f)


def crearTexto():
    for x in pattern.es.lexicon.keys():
        if x in pattern.es.spelling.keys():
            s = (pattern.es.parse(x).split())
            for cada in s:
                for c in cada:
                    if c[1] == 'VB':
                        palabra = conjugate(x, INFINITIVE)
                        lista_palabras.append(palabra)

    #cnt = Counter(lista)
    #print(cnt)

def convertir_verbo(archivo):
    with open(archivo,'r') as f:
        arch = json.load(f)
        for x in arch:
            palabra = conjugate(x,INFINITIVE)
            lista.append(palabra)

def guardar_datos(nombre, cant):
    with open(nombre,'w') as f:
        json.dump(cant,f)

def cargar_datos (nombre):
    with open(nombre,'r') as f:
        cant = json.load(f)
    return cant

crearTexto()
crear(archivo, lista_palabras)
convertir_verbo(archivo)
cnt = Counter(lista)
guardar_datos(nombre,cnt)
cargar_datos(nombre)
