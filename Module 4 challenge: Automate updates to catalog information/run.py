#! /usr/bin/env python3

import os
import requests
from changeImage import listararchivos

#Definición constantes
DESCRIPTIONSPATH = './supplier-data/descriptions' #Ruta descripciones .txt
URL = "http://<external-IP-address>/fruits/" #URL de la página de la empresa. Reemplazar <external-IP-address> con dirección IP externa que nos ha dado Google.

def upload_dictionary_to_web(dictionary_f3, url_f3):
    """Se hace un request.post para subir el diccionario
    a la página web"""
    response = requests.post(url_f3, data=dictionary_f3)
    if response.status_code == 201: #OK HTTP status code
        print("ENVÍO EXITOSO - El request a la url: {0} ha dado como resultado el código de respuesta: {1}".format(url_f3, response.status_code))
    else: #ERROR HTTP status code
        print("ERROR - El request a la url: {0} ha dado como resultado el código de respuesta: {1}".format(url_f3, response.status_code))

def read_every_single_file_to_dictionary(feedbackpath_f2, feedback_list_names_f2, url_f2="", upload=True):
    """Recibe una lista de archivos por parámetro, 
    se leerá cada archivo y se procesará la información 
    como un diccionario Python con la siguiente estructura:

    {
        name:         "Watermelon"
        weight:       "500"
        description:  "Watermelon is good for relieving heat, eliminating..."
        image_name:   "010.jpeg"
    }

    """
    #Creamos un diccionario local para esta función
    dictionary = {
        "name": "",
        "weight": "",
        "description": "",
        "image_name": ""
    }
    diccionario_pesos = {
        #"Nombre": "Peso"
    } # Esto se usara para otro programa "report_email.py"

    #Abrimos cada archivo y vamos añadiendo línea por línea a cada clave: valor (key: value)
    for element in feedback_list_names_f2:
        with open(os.path.join(feedbackpath_f2, element), 'r') as file:
            text_lines_list = file.readlines() # Guardamos las líneas del archivo en una lista de forma [title, name, date, feedback]

            #Añadimos los valores a cada key del diccionario iterando sobre cada cada elemento de la lista text_lines_list
            for index in range(0, len(text_lines_list)):
                if index == 0:                    
                    dictionary["name"] = text_lines_list[index][:-1]   # Con el [:-1] final indicamos que borre los dos últimos caracteres "\n" que son los saltos de carro del final de cada línea.
                elif index == 1:
                    dictionary["weight"] = int(text_lines_list[index][:-5])
                elif index == 2:
                    dictionary["description"] = text_lines_list[index][:-1]
                dictionary["image_name"] = element

        # Guardamos el nombre y peso en el diccionario_pesos que se usará en otro programa llamado report_email.py (para construir PDF e email)
        diccionario_pesos[dictionary["name"]] = dictionary["weight"]

        if upload == True:
           upload_dictionary_to_web(dictionary, url_f2) #Subimos el diccionario a la web de la compañía
    return diccionario_pesos


#Función principal main()
def main():
    feedback_list_names = listararchivos(ruta = DESCRIPTIONSPATH, formato = "txt") # 1ero obtenemos lista de archivos en carpeta feedback
    read_every_single_file_to_dictionary(DESCRIPTIONSPATH, feedback_list_names, URL) # 2do leemos el contenido de cada uno y lo pasamos a un diccionario, desde esta función se llamará tambien a la función encargada de hacer el request.post a la web (subir los comentarios)

if __name__ == "__main__":
    main()