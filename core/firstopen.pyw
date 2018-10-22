import getpass
import json
import os
import shutil
import smtplib
import sqlite3
import subprocess
import sys
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


def installv():
    lblb.pack_forget()
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
    pt.set('Installation des dépendances Discord...')
    deps.update()
    subprocess.run('cd core && npm i discord.js', shell=True)
    p.set(24.85)
    deps.update()
    subprocess.run('cd core && npm i fs', shell=True)
    p.set(28.08)
    deps.update()
    subprocess.run('cd core && npm i ms', shell=True)
    p.set(28.37)
    deps.update()
    subprocess.run('cd core && npm i moment', shell=True)
    p.set(40)
    deps.update()
    subprocess.run('cd core && npm i chalk', shell=True)
    p.set(47)
    deps.update()
    subprocess.run(
        'cd core/individuals && npm i discord.js', shell=True)
    p.set(60)
    deps.update()
    subprocess.run('cd core/individuals && npm i fs', shell=True)
    p.set(65)
    deps.update()
    subprocess.run('cd core/individuals && npm i ms', shell=True)
    p.set(66)
    deps.update()
    subprocess.run('cd core/individuals && npm i moment', shell=True)
    p.set(90)
    deps.update()
    subprocess.run('cd core/individuals && npm i chalk', shell=True)
    p.set(100)
    pt.set('Terminé.')
    deps.update()
    sys.exit()


lblb = Button(deps, text='Standard', command=installv, width=30)
lblb.pack()

deps.mainloop()
