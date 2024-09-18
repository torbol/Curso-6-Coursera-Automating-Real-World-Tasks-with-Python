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
RUTAIMAGENESORIGINALES = "./supplier-data/images/"
RUTAIMAGENESNUEVAS = "./supplier-data/images/"


#Comprobamos las imágenes .tiff que hay en la carpeta /images y las guardamos en una lista llamada archivos, borramos README y LICENSE de la lista
def listararchivos(ruta, formato):
    """Lista todos los archivos del directorio especificado en el formato indicado, devuelve una lista
    
    Ej:
        ruta = "./supplier-data/images/"
        ruta = "./Desktop/"
        formato = "tiff"
        formato = "jpeg"
        ...
    """
    archivos = os.listdir(ruta)
    archivos.sort()
    listaarchivoslimpia_f = [] #Eliminaremos todo lo que no sea .tiff de la lista de archivos
    for archivo in archivos:
        if formato in archivo:
            listaarchivoslimpia_f.append(archivo)
    print(listaarchivoslimpia_f)

    return listaarchivoslimpia_f


#main
def main():
    listaarchivoslimpia = listararchivos(RUTAIMAGENESORIGINALES, ".tiff")
    #Recorremos la lista y realizamos los cambios solicitados para cada uno de los archivos
    for archivo in listaarchivoslimpia:
        print(archivo)
        img = Image.open(RUTAIMAGENESORIGINALES + archivo)
        imgprocesada = img.resize((600,400)).convert("RGB") #Cambiamos tamaño de la imagen y convertimos de RGBA (formato original de 4 canales) a RGB (3 canales)

        print("Guardando jpeg en: " + RUTAIMAGENESNUEVAS)

        #Guardamos la imagen en la ruta especificada
        imgprocesada.save(RUTAIMAGENESNUEVAS + archivo[:-5] + ".jpeg", "JPEG")

            
        #Comprobamos que se ha guardado correctamente imagen en .jpeg y 600x400
        rutacompletaaljpeg = RUTAIMAGENESNUEVAS + archivo[:-5] + ".jpeg"
        img = Image.open(rutacompletaaljpeg)
        print("Comprobación formato y resolución nueva imagen en {0}: {1}, {2}".format(rutacompletaaljpeg, img.format, img.size))

if __name__ == "__main__":
    main()
