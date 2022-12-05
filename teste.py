import pandas
import PySimpleGUI as sg

headers = {'Temperatura':[], 'Tempo':[], 'C':[], 'c':[], 'C_estimado': [], 'T0_estimado': []}
table = pandas.DataFrame(headers)

headings = list(headers)
values = table.values.tolist()

sg.theme("DarkBlue3")
sg.set_options(font=("Arial", 16))

layout = [[sg.Table(values = values, headings = headings,
    # Set column widths for empty record of table
    auto_size_columns=True,
    col_widths=list(map(lambda x:len(x)+2, headings)))]]

window = sg.Window('Sample excel file',  layout)
event, value = window.read()