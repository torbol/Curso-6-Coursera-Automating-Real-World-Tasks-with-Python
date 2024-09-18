
#!/usr/bin/env python3

# Nos piden generar el PDF desde aquí y enviar por email
from run import read_every_single_file_to_dictionary, DESCRIPTIONSPATH
from changeImage import listararchivos
from reports import generate_report
import os, datetime

# main
def main():
    listadescripciones = listararchivos(DESCRIPTIONSPATH, "txt")
    diccionario_pesos = read_every_single_file_to_dictionary(DESCRIPTIONSPATH, listadescripciones, upload=False)
    tiempo = datetime.datetime.now()
    titulo = "Processed Update on {0} {1}, {2}".format(str(tiempo.strftime("%B")), str(tiempo.day), str(tiempo.year))
    
    # Generamos un string que contenga la estructura name: key<br/>weight: value lbs<br/><br/>
    paragraph_pdf = ""
    for item in diccionario_pesos:
     paragraph_pdf += "name: " + item + "<br/>" + "weight: " + str(diccionario_pesos[item]) + "<br/><br/>"
    print(paragraph_pdf)
    generate_report(attachment="/tmp/processed.pdf", title=titulo, paragraph=paragraph_pdf)
    

if __name__=="__main__":
    main()
