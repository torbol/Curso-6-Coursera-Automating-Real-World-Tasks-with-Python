#!/usr/bin/env python3


import requests
from changeImage import RUTAIMAGENESNUEVAS, listararchivos

# Se nos pide subir los archivos .jpeg de la carpeta /images donde hemos guardado los .jpeg
# para ello importamos la ruta desde changeImage para que solo haya que modificarla en un script si se cambia en un futuro,
# también se importa la función listararchivos(ruta, formato) que nos devuelve una lista con todos los archivos que hay en la carpeta en el formato
# que nos interesa.

url = "http://<external-IP-address>/upload/" # Cambiar <external-IP-address> por la IP que nos ha dado Google.

def subirarchivo(listaarchivos_f):
    """Función para hacer un post a la pagina web a partir de una lista"""
    for archivo in listaarchivos_f:
        with open(RUTAIMAGENESNUEVAS + archivo, 'rb') as opened:
            r = requests.post(url, files={'file': opened})

# main función principal
def main():
    milistadejpeg = listararchivos(ruta=RUTAIMAGENESNUEVAS, formato="jpeg")
    subirarchivo(milistadejpeg) # Llamando a esta función, subimos los archivos
if __name__ == "__main__":
    main()