#Con esta sencilla aplicacion se pueden enviar correos de manera automatica a las listas de direcciones especificadas
#con el mensaje especificado e incluso se podría configurar la direccion de correo y la contraseña para no tener que ingresarlas mediante la instruccion input
#Podria configurarse para leer un archivo de excel con las direcciones de mail y agregarlas a la lista de destinatarios.
#Un posible uso seria enviar resumenes de cuenta de clientes, faltaría la parte de adjuntar los archivos correspondientes pero eso ya es otra cosa.
#Se pueden programar los dias que queremos que se envien los correos. Particularmente hice la prueba compilando este archivo en un .exe y poniendolo como programa de inicio
#de windows. Lo cual funciona, cuando llegan las fechas en cuestion se envian los correos. Si la fecha no coincide con las especificadas (16, 18, 20) el programa
#muestra un mensaje por windows (linea final de codigo) mediante un cartel del sistema operativo gracias al modulo tkinter.

import smtplib 
import getpass
from email.message import EmailMessage
from datetime import date
from tkinter import messagebox as msgbox

fecha = date.today()

dia = fecha.strftime("%d") #Con esta instruccion obtenemos solo el día de la fecha obteninda en la instruccion anterior

if dia == "16" or dia =="18" or dia =="20":

    lista_direcciones = ["direccion1@gmail.com", "direccion2@gmail.com"]

    mensaje = "El mensaje que queramos configurar"

    configuracion = EmailMessage()

    server = smtplib.SMTP("smtp.office365.com", 587)

    server.starttls()

    email = (input("Introduce tu email por favor: "))
    password = getpass.getpass("Introduce tu contraseña por favor: ")

    configuracion['Subject'] = "Prueba de correo electronico en fecha " + dia
    configuracion['From'] = email
    configuracion['To'] = lista_direcciones
    configuracion.set_content(mensaje)

    try:

        server.login(email, password)
        server.send_message(configuracion)
        server.quit()

        msgbox.showinfo("Informacion", "Los correos han sido enviados")

    except smtplib.SMTPAuthenticationError:

         msgbox.showinfo("Error", "El usuario o la contraseña son incorrectos.")
    
else:

    msgbox.showinfo("Informacion", "Hoy no se envian correos.")