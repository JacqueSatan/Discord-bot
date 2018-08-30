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
    lblb.pack_forget()
    bllb.pack_forget()
    subprocess.run('cd individuals && node standard.js', shell=True)
    os.startfile('config.pyw')
    deps1 = LabelFrame(deps, text='Progression de l\'installation', padx=20, pady=20)
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
    os.startfile('launcher.pyw')
    sys.exit()


def installv():
    deps1 = LabelFrame(deps, text='Progression de l\'installation', padx=20, pady=20)
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


def mdepase(mdp):
    with open(cwd + '/individuals/conf.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    data["entry"] = mdp.get()
    data["you"] = str(user)
    with open('individuals/conf.json', "w") as jsonFile:
        json.dump(data, jsonFile)
    subprocess.run('cd individuals && node calculate.js', shell=True)
    if data['verified'] == 'true':
        installv()
    else:
        os.startfile('firstopen.pyw')
        sys.exit()


def admin():
    lblb.pack_forget()
    bllb.pack_forget()
    mdpv = StringVar()
    mdpv.set('Mot de passe')
    mdp = Entry(deps, textvariable=mdpv, width=36)
    mdp.pack()

    valid = Button(deps, text='Valider', command=lambda:mdepase(mdp), width=30)
    valid.pack()

lblb = Button(deps, text='Standard', command=install, width=30)
lblb.pack()

bllb = Button(deps, text='Administrateur', command=admin, width=30)
bllb.pack()

deps.mainloop()