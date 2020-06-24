import PySimpleGUI as sg
import json
import time

nombre = 'clima.json'

def guardar_datos(nom,datos_guardar):
    d = {}
    dt_string = time.strftime("%a, %d %b %Y %H:%M:%S")           #Preguntar
    print('date and time =',dt_string)
    d[dt_string] = datos_guardar
    with open(nom,'w') as f:
        json.dump(d,f)

# def cargar_datos(nom):
#     with open(nom,'r') in f:
#         lista = f.read()
#     return lista

def actualizar_listado (listbox,lista):
     listbox.Update(map(lambda x: "{}: {}".format(x[0],x[1]),lista))

layout = [[sg.Text('Temperatura:'), sg.Input(key='temperatura')],
[sg.Text('Humedad:'), sg.Input(key='humedad')],
[sg.Listbox(values=[], key='Datos', size=(60,10))],
[sg.Button('Añadir'), sg.Button('Guardar')]]

window = sg.Window('Datos de la temperatura y humedad').Layout(layout)
window.Finalize()
lista = []

while True:
    event, values = window.Read()
    if event is None:
        break
    if event is 'Añadir':
        lista.append((values['temperatura'], values['humedad']))
        actualizar_listado(window.FindElement('Datos'),lista)
    if event is 'Guardar':
        print(lista)
        guardar_datos(nombre,lista)

#cargar_datos(nombre)
