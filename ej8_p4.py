import PySimpleGUI as sg
import csv

# archivo = open('universidades.csv','r')
lista_unis = []
# leo = csv.reader(archivo)

def listado():
    archivo = open('universidades.csv','r')
    leo = csv.reader(archivo)
    for fila in leo:
        fila = fila[0].replace(';',',')
        fila = fila.split(',')
        if fila[1] != 'UNIVERSIDA':
            if not fila[1] in lista_unis:
                lista_unis.append(fila[1])
    archivo.close()

def datos(archivo,facu):
    leo = csv.reader(archivo)
    #lista = []
    dic = {}
    for fila in leo:
        fila = fila[0].replace(';',',')
        fila = fila.split(',')
        if fila[1] != 'UNIVERSIDA':
            if fila[1] == facu:
                datos = {'Regimen':fila[0],'Univ_c':fila[2],'Unac_c':fila[4],'Anexo_c':fila[5],'Unicue':fila[6],'Cui':fila[7],
                'Tel':fila[8],'Fax':fila[9],'Web':fila[10],'Direc_norm':fila[11],'Calle':fila[12],'Altura':fila[13],'Wkt_gkba':fila[14],
                'Barrio':fila[15],'Comuna':fila[16],'Cod_postal':fila[17],'Cod_postal_arg':fila[18],'Lat':fila[19],'Lng':fila[20]}
                dic[fila[3]] = datos
                #lista.extend(datos)
    #return lista
    return dic



# datos(archivo)
#print(datos(archivo,'INSTITUTO UNIVERSITARIO CEMIC'))

def actualizar_listado (listbox,dic):
    listbox.Update(map(lambda x: "{}: {}".format(x[0],x[1]),dic.items()))

listado()

layout = [
    [sg.Listbox(values=lista_unis,key='Lista',size=(60,1))],
    [sg.Listbox(values=[],key='Datos',size=(60,10))],
    [sg.Button('Imprimir datos'),sg.Button('Exit')]
]

window = sg.Window('Datos de universidades').Layout(layout).Finalize()

#lista = []
while True:
    event,values = window.Read()
    if event is None or event == 'Exit':
        break
    elif event == 'Imprimir datos':
        if values['Lista'] == []:
            sg.Popup('Error','No seleccionó ninguna universidad')
        else:
            archivo = open('universidades.csv','r')
            #valores = values['Lista'][0].replace('{','').replace('}','')
            dic = datos(archivo,values['Lista'][0])
            actualizar_listado(window.FindElement('Datos'),dic)

window.Close()
