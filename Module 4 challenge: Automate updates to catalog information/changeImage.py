#!/usr/bin/env python3

#Tenemos
# formatos .tiff
# Resolución 3000x2000 pixel

#Necesitamos
# formatos .jpeg
# Resolución 600x400 pixel
# Guardar archivos buenos en misma ruta /supplier-data/images/

from PIL import Image
import os

#Rutas a usar (son la misma ruta)
rutaimagenesoriginales = "./supplier-data/images/"
rutaimagenesnuevas = "./supplier-data/images/"


#Comprobamos las imágenes .tiff que hay en la carpeta /images y las guardamos en una lista llamada archivos, borramos README y LICENSE de la lista
archivos = os.listdir(rutaimagenesoriginales)
archivos.sort()
listaarchivostiff = [] #Eliminaremos todo lo que no sea .tiff de la lista de archivos
for archivo in archivos:
    if ".tiff" in archivo:
        listaarchivostiff.append(archivo)
print(listaarchivostiff)

#Recorremos la lista y realizamos los cambios solicitados para cada uno de los archivos
for archivo in listaarchivostiff:
    print(archivo)
    img = Image.open(rutaimagenesoriginales + archivo)
    imgprocesada = img.resize((600,400)).convert("RGB") #Cambiamos tamaño de la imagen y convertimos de RGBA (formato original de 4 canales) a RGB (3 canales)

    print("Guardando jpeg en: " + rutaimagenesnuevas)

    #Guardamos la imagen en la ruta especificada
    imgprocesada.save(rutaimagenesnuevas + archivo[:-5] + ".jpeg", "JPEG")

        
    #Comprobamos que se ha guardado correctamente imagen en .jpeg y 600x400
    img = Image.open(rutaimagenesnuevas + archivo[:-5] + ".jpeg")
    print("Comprobación formato y resolución nueva imagen en {0}: {1}, {2}".format(rutaimagenesnuevas, img.format, img.size))
