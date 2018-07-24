from tkinter import *
from tkinter import ttk
import os
import json
import subprocess

root = Tk()
root.title('Attaque automatique')

a = LabelFrame(root, text='Progression de l\'attaque', padx=20, pady=20)
a.pack()

action = StringVar()
action.set('')

progression = StringVar()
progression.set(0)

actionlabel = Label(a, textvariable=action)
actionlabel.pack()

p = ttk.Progressbar(a, orient=HORIZONTAL, length=400,
                    mode='determinate', variable=progression)
p.pack()


def detect():
    os.startfile('..\stop.pyw')
    with open('..\settings.json', 'r') as configfile:
        config = json.load(configfile)
    if config["config"]["role_dlt"] == 1:
        action.set('Suppression de tous les rôles...')
        progression.set(5)
        root.update()
        subprocess.run('cd ..\individuals && node role_dlt.js', shell=True)
        progression.set(10)
        action.set('Terminé.')
        root.update()


detect()

root.mainloop()

"""
    "config": {
        "msg": "https://discord.gg/ngrdmkN @everyone",
        "ban": "",
        "imgnom": "",
        "img": "",
        "name": "",
        "chnl_dlt": "",
        "admin": "",
        "role_dlt": "",
        "role_crt": "",
        "spam": "",
        "chnlname": "",
        "rolename": ""
    },
"""
