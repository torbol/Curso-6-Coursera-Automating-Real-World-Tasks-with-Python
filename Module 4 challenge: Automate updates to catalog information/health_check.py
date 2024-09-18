#!/usr/bin/env python3

import psutil, emails, requests, time

CHECKING_STATS_INTERVAL = 60 # Tiempo en segundos para comprobación de estadísticas, se usa en el main para el bucle

def envio_email(subject_f):
    # Enviamos por email el PDF que hemos generado
    sender = "automation@example.com"
    recipient = "student@example.com"
    body = "Please check your system and resolve the issue as soon as possible."

    mensaje = emails.generate_email(sender=sender, recipient=recipient, subject=subject_f, body=body, attachment_path="")

    emails.send_email(mensaje) # Finalmente se envía el mensaje
    print("Email de error en estado del sistema enviado.")

def comprobar_estadisticas():
    # El uso de CPU está por encima del 80%?
    # El espacio en disco es menor al 20%?
    # Memoria disponible es menor a 100 mb?
    # Se puede resolver 127.0.0.1?
    
    cpu = psutil.cpu_percent() # Comprobamos porcentaje CPU
    if cpu > 80:
        envio_email("Error - CPU usage is over 80%") # Usaremos esto para identificar el asunto en el email
    disk_space = psutil.disk_usage('/').percent # Obtenemos el porcentaje usado en disco
    if 100 - disk_space < 20:
        envio_email("Error - Available disk space is less than 20%")
    available_memory = psutil.virtual_memory().available / (1024*1024) # Obtenemos la memoria ram disponible en MB antes de entrar en la swap
    if available_memory < 100:
        envio_email("Error - Available memory is less than 100MB")
    try:
        response = requests.get("http://localhost")
        print("CORRECTO - Status code: " + str(response.status_code)) #Si todo va bien, imprimimos el código de respuesta
    except:
        print("\nERROR estableciendo conexión: \n")
        envio_email("Error - localhost cannot be resolved to 127.0.0.1")

# Función principal main()
def main():
    while True:
        comprobar_estadisticas()
        time.sleep(CHECKING_STATS_INTERVAL)

if __name__ == "__main__":
    main()