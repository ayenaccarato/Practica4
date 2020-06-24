import PySimpleGUI as sg
from random import randint

tam_celda =25
color_button = ('white','blue')
tam_button = 5,2
MAX_ROWS = MAX_COL = 10
board = [[randint(0,1) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

layout =  [[sg.Button('',size=(6, 3), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
layout.append([sg.Button('A', key=(11,1),button_color=color_button,size=tam_button), sg.Button('B', key=(11,2),button_color=color_button,size=tam_button), sg.Button('C', key=(11,3),button_color=color_button,size=tam_button),sg.Button('D', key=(11,4),button_color=color_button,size=tam_button),sg.Button('E', key=(11,5),button_color=color_button,size=tam_button)])
layout.append([sg.Button('Evaluar',button_color=color_button,size=tam_button)])

botones = [(11,1), (11,2), (11,3), (11,4), (11,5)]

window = sg.Window('Tablero', default_button_element_size=(5,2), auto_size_buttons=False).Layout(layout).Finalize()

while True:
	event, values = window.Read()
	if event in (None, 'Exit'):
		break
	else:
		if event in botones:
			valor_A = window.Element(event).GetText()
			print(event)
			keys_entered = event
			event, values = window.Read()
			valor_B = window.Element(event).GetText()
			if event not in botones:
				if valor_B == '':
					window.Element(event).Update(valor_A, button_color=('white','black'))
					window.Element(keys_entered).Update(visible=False)

			else:
				window.Element(keys_entered).Update(valor_B)
				window.Element(event).Update(valor_A)
		else:
			print (event)

window.Close()
