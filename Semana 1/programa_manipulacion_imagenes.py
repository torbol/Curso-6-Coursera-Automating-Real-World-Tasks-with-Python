#!/usr/bin/python3

#Tenemos
# formatos .tiff
# Resolución 192x192 pixel
# Posición: Rotado 90 grados sentido antihorario

#Necesitamos
# formatos .jpeg
# Resolución 128x128 pixel
# Posición: Rectas
# Guardar archivos buenos en ruta /opt/icons/

from PIL import Image
import os

#Rutas a usar
rutaimagenesoriginales = "./images/"
rutaimagenesnuevas = "/opt/icons/"


#Comprobamos las imágenes que hay en la carpeta /images y las guardamos en una lista llamada archivos
archivos = os.listdir(rutaimagenesoriginales)
archivos.remove(".DS_Store")

#Comprobamos que exista directorio /opt/icons en caso de que no, o no esté vacío se creará

if os.path.exists(rutaimagenesnuevas):
    print("Existe /opt/icons")
else:
    print("No existe /opt/icons")
    #Creamos la carpeta /opt/icons
    os.mkdir(rutaimagenesnuevas)

#Recorremos la lista y realizamos los cambios solicitados para cada uno de los archivos
for archivo in archivos:
    print(archivo)
    img = Image.open(rutaimagenesoriginales + archivo)
    imgprocesada = img.rotate(-90).resize((128,128)).convert("L") #Convertimos a RGB porque LA no es compatible con JPEG https://pillow.readthedocs.io/en/stable/handbook/concepts.html y https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
    print("Guardando jpeg en: " + rutaimagenesnuevas + archivo)
    imgprocesada.save(rutaimagenesnuevas + archivo, "JPEG")
    #Comprobamos que se ha guardado correctamente imagen en .jpeg y 128x128
    img = Image.open(rutaimagenesnuevas + archivo)
    print("Comprobación formato y resolución nueva imagen en /opt/icons: {0}, {1}".format(img.format, img.size))
