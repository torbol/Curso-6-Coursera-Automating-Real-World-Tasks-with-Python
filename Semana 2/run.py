#! /usr/bin/env python3

import os
import requests
import json

#Definición variables globales
rootpath = '/home/vboxuser' #BORRAR CUANDO TERMINE
feedbackpath = './data/feedback'

def list_all_txt(feedbackpath_f):
    """Lista todos los .txt en la ruta /data/feedback"""

    feedback_list_names_f = os.listdir(feedbackpath_f) #Guardamos en una lista los nombres de los archivos .txt que hay en la carpeta
    feedback_list_names_f.sort() #Ordenamos por numeración ascendente los comentarios
    print(feedback_list_names_f) #BORRAR CUANDO TERMINE
    return feedback_list_names_f
#TO DO LIST Crear función para hacer request
def read_every_single_file_to_dictionary(feedbackpath_f2, feedback_list_names_f2):
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
    #Creamos un diccionario local para la función
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
            print(dictionary.values()) #BORRAR CUANDO TERMINE
            
            
            
            
            #TO DO LIST llamar a la función para hacer request







#main()
os.chdir(rootpath) #BORRAR CUANDO TERMINE
print(os.getcwd()) #BORRAR CUANDO TERMINE
feedback_list_names = list_all_txt(feedbackpath) # 1ero obtenemos lista de archivos en carpeta feedback
read_every_single_file_to_dictionary(feedbackpath, feedback_list_names) # 2do leemos el contenido de cada uno y lo pasamos a un diccionario