#!/usr/bin/env python3

import reportlab

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.units import inch

def generate(filename, title, additional_info, table_data, add_pie_chart=False):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,20)
  # TODO añadir un gráfico circular (pie chart) al ejercicio opcional
  if add_pie_chart == True: 
    report_chart = Drawing()
    report_pie = Pie()
    report.width = 3*inch
    report.height = 3*inch
    report_pie.data = []
    report_pie.labels = []

    # Creamos diccionario para guardar car_make (key), total_sales(value)
    diccionario = {}
    for element in table_data:
      if element == ['ID', 'Car', 'Price', 'Total Sales']: # Saltamos primera fila que contiene cabeceras de cada columna
        continue
      print(element)

      # Guardamos en diccionario
      car_make = element[1].split()[0] # Cogemos la primera palabra del string que pertenece al índice 1 de element
      total_sales = element[3]
      if car_make not in diccionario.keys():
        diccionario[car_make] = [total_sales]
      else:
        diccionario[car_make].append(total_sales)

    for every_list in list(diccionario.values()): # Cogemos cada lista de valores
      report_pie.data.append(sum(every_list)) # Hacemos la suma de los elementos de cada una de las listas y el total lo añadimos a la lista del gráfico
    report_pie.labels = list(diccionario.keys()) # Etiquetas para el gráfico que corresponden a las marcas de coches car_make
    print(type(diccionario.values()))
    report_chart.add(report_pie)
    report.build([report_title, empty_line, report_info, empty_line, report_table, report_chart])
  elif add_pie_chart == False:
    report.build([report_title, empty_line, report_info, empty_line, report_table])