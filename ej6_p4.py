import PySimpleGUI as sg
import json
import random
#from os.path import isfile

dic = {}

def leerArchivo(nombre):
    with open(nombre, 'r') as archivo:
        datos = json.load(archivo)
    return datos

def abrircoordenadas(filename):
    lista_coordenadas = []
    with open(filename,'r') as file:
        datos = file.readlines()
        for coor in datos:
            coor = coor.replace('(','').replace(')','').replace('[','').replace(']','').replace('"','').replace('\n','').replace(',','')
            x,y = coor.split('/')
            lista_coordenadas.append((int(x),int(y)))
    return lista_coordenadas

def abrircolores(filename):
    lista_colores = []
    with open(filename,'r') as colores:
        color = colores.readlines()
        for c in color:
            c = c.replace('[','').replace(']','').replace('\n','').replace('"','').replace(',','')
            lista_colores.append(c)
    return lista_colores

def guardar():     #Ejercicio 5
    with open('coordCol.json','w') as file:
        json.dump(dic,file)

def dibujarGrafico(window, coord, col):
    grafico = window.FindElement('_graph_')
    grafico.DrawPoint(coord[0], 5, col[0] )
    dic[str(coord[0])] = col[0]

def actualizar_listado (listbox,lista):
     listbox.Update(map(lambda x: "Coord: {} - Color: {}".format(x[0],x[1]),lista))

layout = [[sg.Text('Seleccione la coordenada y color')],
          [sg.Text('Coord'),sg.Listbox(values = abrircoordenadas('coordenadas.json'), key='Coordenada')],
          [sg.Text('Color'),sg.Listbox(values=abrircolores('colores.json'),key='Colores')],
          [sg.Listbox(values=[], key='Valores', size=(60,10))],
          [sg.Graph(canvas_size=(400,400), graph_bottom_left=(-105,-105), graph_top_right=(105,105),key='_graph_')],
          [sg.Button('Dibujar'), sg.Button('Guardar'),sg.Button('Añadir')],
          [sg.Button('Exit')]]

window = sg.Window('Bienvenido').Layout(layout).Finalize()

graph = window.FindElement('_graph_')

# Draw axis
graph.DrawLine((-100,0), (100,0))
graph.DrawLine((0,-100), (0,100))

for x in range(-100, 101, 20):
    graph.DrawLine((x,-3), (x,3))
    if x != 0:
        graph.DrawText( x, (x,-10), color='green')

for y in range(-100, 101, 20):
    graph.DrawLine((-3,y), (3,y))
    if y != 0:
        graph.DrawText( y, (-10,y), color='blue')

lista = []
while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    elif event == 'Dibujar':
        if values['Coordenada'] == [] or values['Colores'] == []:
            sg.Print('No elegiste los datos')
        else:
            dibujarGrafico(window,values['Coordenada'],values['Colores'])
    elif event == 'Guardar':      #Ejercicio 5
        guardar()
    elif event == 'Añadir':
        lista.append((values['Coordenada'][0],values['Colores'][0]))
        actualizar_listado(window.FindElement('Valores'),lista)

window.Close()
