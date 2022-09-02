import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text('Supply strength (A):')],
          [sg.Input(key='A')],
          [sg.Text('Supply Voltage (V):')],
          [sg.Input(key='V')],
          [sg.Text('Consumer needs (W):')],
          [sg.Input(key='W')],
          [sg.Text('Time in Hours: '), sg.Text(key='result')],
          [sg.Button('calculate', bind_return_key=True)]]

window = sg.Window('Pattern 2B', layout)

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'calculate':
        if all(values[x] for x in values):
            result = float(values['A']) * float(values['V']) / float(values['W'])
            window['result'].update(str(result))
        else:
            window['result'].update("YOU HAVE NOT FILLED ALL FIELDS")
window.close()
