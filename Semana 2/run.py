#! /usr/bin/env python3

import os
import requests
import json

#Definición constantes globales
ROOTPATH = '/home/vboxuser' #BORRAR CUANDO TERMINE
FEEDBACKPATH = './data/feedback' #Ruta comentarios .txt
URL = "http://<corpweb-external-IP>/feedback" #URL de la página de la empresa. Reemplazar <corpweb-external-IP> con dirección IP externa de corpweb.

def list_all_txt(feedbackpath_f):
    """Lista todos los .txt en la ruta /data/feedback"""

    feedback_list_names_f = os.listdir(feedbackpath_f) #Guardamos en una lista los nombres de los archivos .txt que hay en la carpeta
    feedback_list_names_f.sort() #Ordenamos por numeración ascendente los comentarios
    print(feedback_list_names_f) #Mostramos en consola, los archivos que se van a procesar en forma de lista
    return feedback_list_names_f

def upload_dictionary_to_web(dictionary_f3, url_f3):
    """Se hace un request.post para subir el diccionario
    a la página de la empresa"""

    response = requests.post(url_f3, params=dictionary_f3)
    if response.status_code == 201: #OK HTTP status code
        print("ENVÍO EXITOSO - El requeset a la url: {0} ha dado como resultado el código de respuesta: {1}".format(url_f3, response.status_code))
    else: #ERROR HTTP status code
        print("ERROR - El requeset a la url: {0} ha dado como resultado el código de respuesta: {1}".format(url_f3, response.status_code))

def read_every_single_file_to_dictionary(feedbackpath_f2, feedback_list_names_f2, url_f2):
    """Recibe una lista de archivos por parámetro, 
    se leerá cada archivo y se procesará la información 
    como un diccionario Python con la siguiente estructura:

    {
        title:      "título"
        name:       "nombre"
        date:       "fecha"
        feedback:   "comentario"
    }

    """
    #Creamos un diccionario local para esta función
    dictionary = {
        "title": "",
        "name": "",
        "date": "",
        "feedback": ""
    }
    #Abrimos cada archivo y vamos añadiendo línea por línea a cada clave: valor (key: value)
    for element in feedback_list_names_f2:
        with open(os.path.join(feedbackpath_f2, element), 'r') as file:
            text_lines_list = file.readlines() # Guardamos las líneas del archivo en una lista de forma [title, name, date, feedback]

            #Añadimos los valores a cada key del diccionario iterando sobre cada cada elemento de la lista text_lines_list
            for index in range(0, len(text_lines_list)):
                if index == 0:                    
                    dictionary["title"] = text_lines_list[index][:-1]   # Con el [:-1] final indicamos que borre los dos últimos caracteres "\n" que son los saltos de carro del final de cada línea.
                elif index == 1:
                    dictionary["name"] = text_lines_list[index][:-1]
                elif index == 2:
                    dictionary["date"] = text_lines_list[index][:-1]
                elif index == 3:
                    dictionary["feedback"] = text_lines_list[index][:-1]

            upload_dictionary_to_web(dictionary, url_f2) #Subimos el diccionario a la web de la compañía



#Función principal main()
def main():
    print(os.getcwd()) #BORRAR CUANDO TERMINE
    feedback_list_names = list_all_txt(FEEDBACKPATH) # 1ero obtenemos lista de archivos en carpeta feedback
    read_every_single_file_to_dictionary(FEEDBACKPATH, feedback_list_names, URL) # 2do leemos el contenido de cada uno y lo pasamos a un diccionario, desde esta función se llamará tambien a la función encargada de hacer el request.post a la web (subir los comentarios)

if __name__ == "__main__":
    main()