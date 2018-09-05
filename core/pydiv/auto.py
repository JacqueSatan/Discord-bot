from tkinter import *
from tkinter import ttk
import os
import json
import subprocess

root = Tk()
root.title('Attaque automatique')

atkl = LabelFrame(root, text='Configuration de l\'attaque', padx=5, pady=5)
atkl.pack()

##########################################################################################################################################

serv = LabelFrame(
    atkl, text='Changer les informations du serveur', padx=5, pady=5)
serv.pack()


def activatedef(imgnom, guild_name, guild_icon, activate):
    activate.pack_forget()
    imgnom.pack()
    guild_name.pack()
    guild_icon.pack()
    verif.pack()
    guild_verification_level.pack()
    emoji.pack()

imgnom = LabelFrame(
    serv, text='Changer le nom et l\'icône du serveur', padx=5, pady=5)

value = StringVar()
value.set("Nouveau nom")
guild_name = Entry(imgnom, textvariable=value, width=30)

value = StringVar()
value.set("Chemin ou URL de l'image")
guild_icon = Entry(imgnom, textvariable=value, width=30)

verif = LabelFrame(
    serv, text='Changer le niveau de vérification', padx=35, pady=5)

MODES = [
    ("Aucun", 0),
    ("Mail vérifié", 1),
    ("5 minutes d'attente", 2),
    ("10 minutes d'attente", 3),
    ("Téléphone vérifié", 4),
]
accept = StringVar()
accept.set(0)
for text, mode in MODES:
    guild_verification_level = Radiobutton(verif, text=text, variable=accept, value=mode)
    guild_verification_level.pack(anchor=W)

emoji = LabelFrame(serv, text='Gérer les émojis', padx=5, pady=5)

emojidltvar = IntVar()
guild_delete_emoijs = Checkbutton(emoji, text='Supprimer tous les émojis', width=26,
                       onvalue="1", offvalue="1", indicatoron=0, variable=emojidltvar)
guild_delete_emoijs.pack()


def emojid(emojiname, emojilink):
    emojiname.pack()
    emojilink.pack()


emojinamevar = StringVar()
emojinamevar.set("Nom de l'émoji")
emojiname = Entry(emoji, textvariable=emojinamevar, width=31)

emojilinkvar = StringVar()
emojilinkvar.set("URL vers l'émoji")
emojilink = Entry(emoji, textvariable=emojilinkvar, width=31)

guild_create_emoijsvar = IntVar()
guild_create_emoijs = Checkbutton(emoji, text='Créer des émojis', width=26,
                       onvalue="1", offvalue="0", indicatoron=0, variable=guild_create_emoijsvar, command=lambda: emojid(emojiname, emojilink))
guild_create_emoijs.pack()

activate = Button(serv, text='Activer', command=lambda: activatedef(
    imgnom, guild_name, guild_icon, activate), width=28)
activate.pack()


#########################################################################################################################################################


members = LabelFrame(atkl, text="Gérer les membres", padx=5, pady=5)
members.pack()

def validef():
    validm.pack_forget()
    ban.pack()
    kick.pack()
    nick.pack()

banvar = IntVar()
ban = Checkbutton(members, text='Bannir tout le monde', width=28, indicatoron=0, onvalue="1", offvalue="0", variable=banvar)

kickvar = IntVar()
kick = Checkbutton(members, text="Expulser tout le monde", width=28, indicatoron=0, variable=kickvar, onvalue="1", offvalue="0")

def nickdef():
    nickname.pack()

nicknamevar = StringVar()
nicknamevar.set('Nouveau pseudo')
nickname = Entry(members, textvariable=nicknamevar, width=31)

nickvar = IntVar()
nick = Checkbutton(members, text='Changer les pseudos', width=28, onvalue="1", offvalue="0", indicatoron=0, variable=nickvar, command=nickdef)

validmvar = IntVar()
validm = Checkbutton(members, variable=validmvar, text='Activer', width=28, command=validef, onvalue="1", offvalue="0", indicatoron=0)
validm.pack()

##########################################################################################################################################################

roles = LabelFrame(atkl, text='Gérer les rôles', padx=5, pady=5)
roles.pack()

def activerd():
    activer.pack_forget()
    roledlt.pack()
    rc.pack()

roledltvar = IntVar()
roledlt = Checkbutton(roles, text='Supprimer tous les rôles', width=28, onvalue="1", offvalue="0", indicatoron=0,variable=roledltvar)

rc = LabelFrame(roles, text='Créer des rôles', padx=5,pady=5)

def rolesdef():
    rolename.pack()
    assign.pack()
    

rolenamev = StringVar()
rolenamev.set('Nom des rôles à créer')
rolename = Entry(rc, textvariable=rolenamev, width=31)

assignvar = IntVar()
assign = Checkbutton(rc, text='Les donner à chaque membre', width=26, onvalue="1", offvalue="0", variable=assignvar, indicatoron=0)

rolecrtvar = IntVar()
rolecrt = Checkbutton(rc, text='Créer des rôles', width=26, onvalue="1", offvalue="0", indicatoron=0,variable=rolecrtvar, command=rolesdef)
rolecrt.pack()

activer = Button(roles, text='Activer', width=28, command=activerd)
activer.pack()
"""
"auto": {
    "guild": {
        "enabled": "",
        "name": "",
        "icon": "",
        "verification_level": "",
        "delete_emojis": "",
        "create_emojis": {
            "enabled": ""
            "name": "",
            "link": ""
        }
    },
    "members": {
        "enabled": "",
        "ban_everyone": "",
        "kick_everyone": "",
        "change_nicknames": {
            "enabled": "",
            "nickname": ""
        }
    },
    "roles": {
        "enabled": "",
        "delete_roles": "",
        "create_roles": {
            "enabled": "",
            "name": ""
        }
        "assign": ""
    },
    "channels": {
        "enabled": ""
        "delete_channels": "",
        "create_channels": {
            "enabled": "",
            "name": "",
            "spam_in": "",
        }
    },
    "spam": {
        "enabled": "",
        "message": "",
        "type": "",
        "channel_id_name": ""
    }
}
"""

def attack():
    with open('..\\settings.json', 'r') as configfile:
        config = json.load(configfile)
    config["autoa"]["guild"]["enabled"] = validmvar.get()
    config["autoa"]["guild"]["name"] = guild_name.get()
    config["autoa"]["guild"]["icon"] = guild_icon.get()
    config["autoa"]["guild"]["verification_level"] = accept.get()
    config["autoa"]["guild"]["delete_emojis"] = emojidltvar.get()
    config["autoa"]["guild"]["create_emojis"]["enabled"] = guild_create_emoijsvar.get()
    config["autoa"]["guild"]["create_emojis"]["name"] = emojiname.get()
    config["autoa"]["guild"]["create_emojis"]["link"] = emojilink.get()
    with open('..\\settings.json', 'w') as configfile:
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
    with open('..\\settings.json', 'r') as configfile:
        config = json.load(configfile)
    if config["config"]["role_dlt"] == 1:
        action.set('Suppression de tous les rôles...\nDurée : 10s')
        progression.set(5)
        root.update()
        subprocess.run('cd ..\individuals && node role_dlt.js', shell=True)
        progression.set(10)
        action.set('Terminé.')
        root.update()
    if config["config"]["ban"] == 1:
        action.set('Bannissement de tous les membres...\nDurée : 15s')
        progression.set(15)
        root.update()
        subprocess.run('cd ..\individuals && node ban.js', shell=True)
        progression.set(20)
        action.set('Terminé.')
        root.update()
    if config["config"]["chnl_dlt"] == 1:
        action.set('Suppression de tous les salons...\nDurée : 15s')
        progression.set(35)
        root.update()
        subprocess.run('cd ..\individuals && node chnldlt.js', shell=True)
        progression.set(40)
        action.set('Terminé.')
        root.update()
    action.set(
        'En train de spammer...\nDurée : Envoyez stop dans un des salons du serveur')
    progression.set(75)
    root.update()
    subprocess.run('cd ../pydiv && node auto.js', shell=True)
    action.set('Terminé. Vous pouvez fermer cette fenêtre.')
    progression.set(100)
    root.update()


atk = LabelFrame(root, text='Lancer', padx=5, pady=5)
atk.pack()

valid = Button(atk, text='Valider et lancer l\'attaque',
               command=lambda: attack(), width=30)
valid.pack()

root.mainloop()
