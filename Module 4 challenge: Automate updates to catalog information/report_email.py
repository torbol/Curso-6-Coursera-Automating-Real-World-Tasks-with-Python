
#!/usr/bin/env python3

# Nos piden generar el PDF desde aquí y enviar por email
from run import read_every_single_file_to_dictionary, DESCRIPTIONSPATH
from changeImage import listararchivos
from reports import generate_report
import datetime
import emails

RUTADEGUARDADOPDF = "/tmp/processed.pdf"

# main
def main():
    listadescripciones = listararchivos(DESCRIPTIONSPATH, "txt")
    diccionario_pesos = read_every_single_file_to_dictionary(DESCRIPTIONSPATH, listadescripciones, upload=False)
    tiempo = datetime.datetime.now()
    titulo = "Processed Update on {0} {1}, {2}".format(str(tiempo.strftime("%B")), str(tiempo.day), str(tiempo.year))
    
    # Generamos un string que contenga la estructura name: key<br/>weight: value lbs<br/><br/> y creamos PDF
    paragraph_pdf = ""
    for item in diccionario_pesos:
     paragraph_pdf += "name: " + item + "<br/>" + "weight: " + str(diccionario_pesos[item]) + "<br/><br/>"

    generate_report(attachment=RUTADEGUARDADOPDF, title=titulo, paragraph=paragraph_pdf)
    print("PDF frutas generado")

    # Enviamos por email el PDF que hemos generado
    sender = "automation@example.com"
    recipient = "student@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = RUTADEGUARDADOPDF

    mensaje = emails.generate_email(sender=sender, recipient=recipient, subject=subject, body=body, attachment_path=attachment_path)
    print(mensaje)

    emails.send_email(mensaje) # Finalmente se envía el mensaje
    print("Email con reporte enviado.")

if __name__=="__main__":
    main()
