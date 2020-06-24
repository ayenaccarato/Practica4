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
        datos = json.load(file)
        for coor in datos:
            coor = coor.replace('(','').replace(')','').replace('[','').replace(']','')
            x,y = coor.split(',')
            lista_coordenadas.append((int(x),int(y)))
    return lista_coordenadas

def ziprandom(lis1,lis2):
    random.shuffle(lis2)
    return zip(lis1,lis2)

def abrircolores(filename):
    lista_colores = []
    with open(filename,'r') as colores:
        color = json.load(colores)
        for c in color:
            c = c.replace('[','').replace(']','').replace('\n','').replace('"','').replace(',','')
            lista_colores.append(c)
    return lista_colores

def guardar():     #Ejercicio 5
    with open('coorCol.json','w') as file:
        json.dump(dic,file)

def dibujarGrafico(window, coord, col):
    coordenadas = abrircoordenadas(coord)
    colores = abrircolores(col)
    grafico = window.FindElement('_graph_')
    for coord,col in ziprandom(coordenadas,colores):
        grafico.DrawPoint(coord, 5, col )
        dic[str(coord)] = col
        #guardar(coord,col)

layout = [[sg.Text('Dibujar puntos de colores')],
          [sg.FileBrowse('Buscar coordenadas...', key='_file1_'), sg.Button('coord')],
          [sg.FileBrowse('Buscar colores...', key='_file2_'), sg.Button('color')],
          [sg.Graph(canvas_size=(400,400), graph_bottom_left=(-105,-105), graph_top_right=(105,105),key='_graph_')],
          [sg.Button('Dibujar'), sg.Button('Guardar'),sg.Exit()]]

window = sg.Window('Window that stays open').Layout(layout).Finalize()

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

while True:
    event, values = window.Read()
    #sg.Print(window.FindElement('_file1_'))
    if event is None or event == 'Exit':
        break
    elif event == 'coord':
        sg.Print('Abriendo archivo de coordenadas')
        if values['_file1_'] == '':
            sg.Print('No cargaste el archivo')
        else:
            sg.Print(values['_file1_'])
            print(abrircoordenadas(values['_file1_']))
    elif event == 'color':
        sg.Print('Abriendo archivo de colores')
        if values['_file2_'] == '':
            sg.Print('No cargaste el archivo')
        else:
            sg.Print(values['_file2_'])
            print(abrircolores(values['_file2_']))
    elif event == 'Dibujar':
        if values['_file1_'] == '' or values['_file2_'] == '':
            sg.Print('No cargaste los archivos')
        else:
            dibujarGrafico(window,values['_file1_'],values['_file2_'])
    elif event == 'Guardar':      #Ejercicio 5
        guardar()
    #print(event, values)

window.Close()
