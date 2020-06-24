import PySimpleGUI as sg
import json

jugadores = {'fede': {'nivel':3,'puntaje':4,'tiempo':200},
    'belen': {'nivel':4,'puntaje':6,'tiempo':300},
    'juan': {'nivel':5,'puntaje':7,'tiempo':400}}
# jugadores = {}
# jugadores2 = {}
# def cargar(jugadores):
#     nombre=input('Ingrese el nombre del jugador')
#     while nombre != 'fin':
#         nivel = int(input('Ingrese el nivel'))
#         puntaje = int(input('Ingrese el puntaje'))
#         tiempo = int(input('Ingrese el tiempo'))
#         jugadores[nombre] = {'nivel':nivel,'puntaje':puntaje,'tiempo':tiempo}
#         nombre =input('Ingrese el nombre del jugador')
#
# def imprimir_uno():
#     print('Ingrese el nombre del jugador que desee saber los datos')
#     nombre = input()
#     print(jugadores[nombre])
#
# def imprimir():
#     print('Nombre de los jugadores que participaron')
#     print(jugadores.keys())
#
# def mi_funcion(a):
#     return a[1]['puntaje']
#
#
# def modificar():
#     print('Jugador a modificar')
#     nombre=input('Ingrese el nombre del jugador')
#     nivel = int(input('Ingrese el nivel'))
#     puntaje = int(input('Ingrese el puntaje'))
#     tiempo = int(input('Ingrese el tiempo'))
#     if (nombre in jugadores):
#         if (jugadores[nombre]['puntaje'] < puntaje):
#             jugadores[nombre] = {'nivel':nivel,'puntaje':puntaje,'tiempo':tiempo}
#     else:
#         jugadores[nombre] = {'nivel':nivel,'puntaje':puntaje,'tiempo':tiempo}
#
#

nombre_archivo = 'jugadores.json'

def guardar_datos(nombre_archivo, jugadores):
    with open(nombre_archivo, 'w') as f:
        json.dump(jugadores,f)

def cargar_jugadores(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        jugadores = json.load(f)
    return jugadores

def actualizar_listado (listbox,lista):
     listbox.Update(map(lambda x: "{} - {} - {} - {}".format(x[0],x[1],x[2],x[3]),lista))

# cargar(jugadores)
# imprimir_uno()
# imprimir()
# print('Jugador con mayor puntaje')
# print(max(jugadores.items(),key=mi_funcion))
#guardar_datos(nombre_archivo,jugadores)
#print(cargar_jugadores(nombre_archivo))

def modificoDatos(nombre_archivo,jugadores):
    with open(nombre_archivo,'a') as f:
        jugadores[values['nombre']]={'nivel': int(values['nivel']),'puntaje': int(values['puntaje']), 'tiempo': int(values['tiempo'])}

guardar_datos(nombre_archivo,jugadores)

layout = [[sg.Text('Nombre: '), sg.Input(key='nombre')],[sg.Text('Nivel: '), sg.Input(key='nivel')],
[sg.Text('Puntaje: '), sg.Input(key='puntaje')],[sg.Text('Tiempo: '),sg.Input(key='tiempo')],
[sg.Listbox(values=[], key='Datos', size=(60,10))],[sg.Button('Añadir'), sg.Button('Guardar')]]

window = sg.Window('Datos de jugador').Layout(layout)
window.Finalize()
lista = []

while True:
    event,values = window.Read()
    if event is None:
        break
    if event is 'Añadir':
        lista.append((values['nombre'], values['nivel'], values['puntaje'],values['tiempo']))
        actualizar_listado(window.FindElement('Datos'),lista)
        #jugadores[values['nombre']]={'nivel': int(values['nivel']),'puntaje': int(values['puntaje']), 'tiempo': int(values['tiempo'])}
        modificoDatos(nombre_archivo,jugadores)
        #cargar_jugadores(nombre_archivo)
    if event is 'Guardar':
        print(lista)
        guardar_datos(nombre_archivo,jugadores)


#modificar()
#juga = sorted(jugadores.items(),key=lambda jugador: jugador[1]['puntaje'],reverse=True)
#print('Ranking de los 10 mayores puntajes')
#print(juga[:10])

#Ejercicio7
#print('Los 10 primeros puntajes')
#juga1 = sorted(jugadores.items(),key=lambda j:jug[1]['puntaje'],reverse = True)
#print(juga1[:10])
#print('Ordenado por nombre')
#nom = sorted(jugadores.items(),key=lambda jug: jug[0])
#print(nom)
#print('Ordenado por nivel')
#niv = sorted(jugadores.items(),key=lambda juga: juga[1]['nivel'])
#print(niv)
