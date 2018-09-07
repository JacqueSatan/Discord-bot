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



with open('core/options.json', 'r') as jsonFile:
    data = json.load(jsonFile)
if data['firstopen'] == 'true':
    os.startfile('core\\firstopen.bat')

# CGU


with open('core/options.json', 'r') as jsonFile:
    data = json.load(jsonFile)
if data["cgu"] == "false":
    cgu = Tk()
    cgu.title('Accepter les CGU')

    def callback(event):
        webbrowser.open_new_tab(r"https://antidiscordbot.page.link/cgu")
    accepter = LabelFrame(cgu, text='Première ouverture', pady=5, padx=5)
    accepter.pack()
    cgy = Label(
        accepter, text='En utilisant cette application, vous acceptez les conditions générales d\'utilisation.\n')
    cgy.pack()

    cgt = Label(accepter, text='Lire les CGU', cursor='hand2')
    vide = Label(accepter, text='')
    vide.pack()
    cgt.pack(anchor=W)
    cgt.bind("<Button-1>", callback)
    vide = Label(accepter, text="")
    vide.pack()
    MODES = [
        ("J'accepte les CGU", "true"),
        ("Je n'accepte pas les CGU", "false"),
    ]
    accept = StringVar()
    accept.set('false')
    for text, mode in MODES:
        b = Radiobutton(accepter, text=text, variable=accept, value=mode)
        b.pack(anchor=W)
    vide = Label(accepter, text="")
    vide.pack()
    votrepseudo = Label(accepter, text="Votre pseudo Discord : (optionnel mais recommandé)")
    votrepseudo.pack(anchor=W)
    pseudo = StringVar()
    pseudo.set('')
    oui = Entry(accepter, textvariable=pseudo, width=70)
    oui.pack(anchor=W)
    vide = Label(accepter, text='')
    vide.pack()

    def valider(accept, oui):
        with open('core/options.json', 'r') as jsonFile:
            data = json.load(jsonFile)
        data["cgu"] = accept.get()
        data["pseudo"] = oui.get()
        data["firstopen"] = 'false'
        with open('core/options.json', 'w') as jsonFile:
            json.dump(data, jsonFile)
        os.startfile('launcher.pyw')
        sys.exit()
    yess = Button(accepter, text='Valider',
                  command=lambda: valider(accept, oui))
    yess.pack(anchor=W)
    cgu.mainloop()


with open('core/options.json', 'r') as jsonFile:
    data = json.load(jsonFile)
if data["cgu"] == "true":
    fenetre = Tk()
user = getpass.getuser()

username = Path.home()

# fenetre.geometry("460x205")
with open('core/package.json', 'r') as jsonFile:
    data = json.load(jsonFile)
title = data['title']
fenetre.title(title)

"""
firebase = firebase.FirebaseApplication(
    'https://discord-bo.firebaseio.com/', None)
result = firebase.get('/version', None)
print(result)
"""


def contact():
    showinfo("Me contacter",
             "Discord : @Jacques#5823\nE-mail  : dsicrod@gmail.com\nTwitter : @AntiDiscord")


def git():
    webbrowser.open_new_tab(
        r"https://antidiscordbot.page.link/lastversionfromapp")


def dscrdc():
    webbrowser.open_new_tab(
        r"https://antidiscordbot.page.link/discordcreatefromapp")


def dscrdv():
    webbrowser.open_new_tab(
        r"https://antidiscordbot.page.link/discordappsfromapp")


def aide():
    webbrowser.open_new_tab(r"https://github.com/JacqueSatan/Discord-bot/issues")
    webbrowser.open_new_tab(r"https://github.com/JacqueSatan/Discord-bot/wiki")

def installt():
    os.startfile('core\\firstopen.bat')
    showinfo('Installation des dépendences',
             'L\'installation va commencer, veuillez patienter. Si l\'application ne répond plus, c\'est normal. Attendez juste. Cela risque de prendre un peu de temps.')
    """
    subprocess.call('npm --prefix ./core i discord.js', shell=True)
    subprocess.call('npm --prefix ./core i fs', shell=True)
    subprocess.call('npm --prefix ./core i ms', shell=True)
    subprocess.call('npm --prefix ./core i moment', shell=True)
    subprocess.call('npm --prefix ./core i chalk', shell=True)
    subprocess.call('npm --prefix ./core/individuals i discord.js', shell=True)
    subprocess.call('npm --prefix ./core/individuals i fs', shell=True)
    subprocess.call('npm --prefix ./core/individuals i ms', shell=True)
    subprocess.call('npm --prefix ./core/individuals i moment', shell=True)
    subprocess.call('npm --prefix ./core/individuals i chalk', shell=True)
    showinfo('Dépendences installées',
             'Toutes les dépendences semblent avoir été installées.')
"""


def backup():
    shutil.copy2('core\\backup\\settings.json', 'core\\settings.json')
    shutil.copy2('core\\backup\\options.json', 'core\\options.json')
    shutil.copy2('core\\backup\\conf.json', 'core\\individuals\\conf.json')
    showinfo('Terminé',
             '3 fichier ont été réparés :\n\
    core\\settings.json\n\
    core\\options.json\n\
    core\\individuals\\conf.json')


def uninstall_deps():
    showinfo('En êtes-vous sûr ?', "Si vous supprimez les dépendances, vous devrez les réinstaller pour utiliser le bot. Celà risque de prendre un peu de temps.")
    subprocess.run(
        'cd core && del /f /s /q node_modules > nul && rmdir /s /q node_modules', shell=True)
    subprocess.run(
        'cd core\individuals && del /f /s /q node_modules > nul && rmdir /s /q node_modules', shell=True)
    showinfo('Terminé', 'Toutes les dépendances ont été désinstallées.')

def serv():
    os.startfile('core/serv.pyw')

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)


menu1.add_command(label="Réparer", command=backup)
menu1.add_command(label="Confirmer votre entrée sur le serveur", command=serv)
menu1.add_command(label="Installer les dépendences", command=installt)
menu1.add_command(label="Désinstaller les dépendances", command=uninstall_deps)
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Options", menu=menu1)


def support():
    webbrowser.open_new_tab(r"https://discord.gg/DhWJNC8")


def cgu():
    webbrowser.open_new_tab(r"https://antidiscordbot.page.link/cgu")


menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Serveur de support", command=support)
menu3.add_command(label="Page Github", command=git)
menu3.add_command(label="Créer une application Discord", command=dscrdc)
menu3.add_command(label="Vos applications Discord", command=dscrdv)
menubar.add_cascade(label='Liens', menu=menu3)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Conditions d'utilisation générale", command=cgu)
menubar.add_cascade(label="A propos", menu=menu2)

fenetre.config(menu=menubar)

obligd = LabelFrame(fenetre, text="Obligatoire :", padx=5, pady=5)
obligd.pack(side=LEFT, fill=Y)


tkn = Label(obligd, text="Token :")
tkn.pack(anchor=W)
value = StringVar()
with open('core\settings.json', "r") as jsonFile:
    config = json.load(jsonFile)
value.set(config['token'])
entree = Entry(obligd, textvariable=value, width=36)
entree.pack()

servid = Label(obligd, text="Id du serveur :")
servid.pack(anchor=W)
value = StringVar()
value.set(config['auto']['server_id'])
entree2 = Entry(obligd, textvariable=value, width=36)
entree2.pack()

ownerid = Label(obligd, text="Votre Id :")
ownerid.pack(anchor=W)
value = StringVar()
value.set(config["ownerid"])
entree7 = Entry(obligd, textvariable=value, width=36)
entree7.pack()

firstopentext = StringVar()
with open('core\options.json', 'r') as jsonFile:
    options = json.load(jsonFile)
if options['firstopen'] == 'true':
    firstopentext.set('Enregistrer')
else:
    firstopentext.set('Enregistrer les modifications')
validb = Button(obligd, textvariable=firstopentext, width=30,
                command=lambda: validd(entree, entree2, entree7))


def validd(entree, entree2, entree7):
    with open('core/options.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    if data["cgu"] == "false":
        fenetre.quit()
    token = str(entree)
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["token"]
    data["token"] = entree.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["auto"]["server_id"]
    data["auto"]["server_id"] = entree2.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["ownerid"]
    data["ownerid"] = entree7.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open('core/options.json', "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["opennmbr"]

    with open('core/options.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    tmp2 = data['pseudo']




    if data["firstopen"] == "true":
        with open('core\options.json', "r") as jsonFile:
            data = json.load(jsonFile)
        openn = data["opennmbr"]
        data['opennmbr'] = openn + 1
        data['firstopen'] = 'false'
        with open('core/options.json', "w") as jsonFile:
            json.dump(data, jsonFile)

validb.pack()

l = Label(obligd, text=" ")
l.pack()


verv = StringVar()
verv.set("Appuyez pour vérifier")


def verbtn():
    subprocess.run('cd core\individuals && ver.bat', shell=True)
    with open('core/settings.json', 'r') as fp:
        data = json.load(fp)
    tmp = data["ver"]
    if tmp == 'oui':
        verv.set('Le bot est administrateur.')
    elif tmp == 'non':
        verv.set('Le bot n\'est pas administrateur')
    else:
        verv.set("Une erreur s'est produite")
    tmp = ''
    with open('core/settings.json', 'w') as fp:
        json.dump(data, fp)


verbtnp = Button(obligd, text="Vérifier le rôle du bot",
                 command=verbtn, width=30)
verbtnp.pack()
verl = Label(obligd, textvariable=verv)
verl.pack()


def errordef():
    depss.set('Recherche...')
    print('1')
    token.set('Veuillez patienter...')
    print('2')
    fenetre.update()
    print('3')
    if os.path.exists('core/node_modules') == False:
        depss.set('Dépendances : Non installées')
    if os.path.exists('core/node_modules') == True:
        depss.set('Dépendances : Bien installées')
    print('4')
    subprocess.run('cd core/individuals && node token.js',
                   shell=True)
    print('5')
    with open('core/options.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    print('6')
    print('7')
    if data["token"] == 'valid':
        token.set('Token : Valide')
        print('8')
    else:
        token.set('Token : Invalide')
        print('9')
    data["token"] = ""
    with open('core/options.json', 'w') as jsonFile:
        json.dump(data, jsonFile)
    fenetre.update()
    print('10')

vide = Label(obligd, text="")
vide.pack()
errorb = Button(obligd, text="Rechercher des erreurs",
                width=30, command=errordef)
errorb.pack()

errors = LabelFrame(obligd, text="Erreurs :", padx=5, pady=5)
errors.pack(anchor=W)

depss = StringVar()
depsver = Label(errors, textvariable=depss)
depsver.pack(anchor=W)

token = StringVar()
tokenver = Label(errors, textvariable=token)
tokenver.pack(anchor=W)

info = LabelFrame(fenetre, text="Informations :", padx=5, pady=5)
info.pack(side=LEFT, fill=Y)


def copytoken():
    with open('core\\settings.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    token = data["token"]
    fenetre.clipboard_clear()
    fenetre.clipboard_append(token)
    fenetre.update()


def copyid():
    with open('core\\settings.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    id = data["id"]
    fenetre.clipboard_clear()
    fenetre.clipboard_append(id)
    fenetre.update()


def copyinvit():
    with open('core\\settings.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    invit = "https://discordapp.com/api/oauth2/authorize?client_id=" + \
        data["id"] + "&permissions=8&scope=bot"
    fenetre.clipboard_clear()
    fenetre.clipboard_append(invit)
    fenetre.update()


tkncopy = Button(info, text="Copier le token", width=30, command=copytoken)

clientdcopy = Button(info, text="Copier l'Id du bot", width=30, command=copyid)

invitationcopy = Button(info, text="Copier l'invitation",
                        width=30, command=copyinvit)


def invitd():
    subprocess.run('cd core\\individuals && node gene.js', shell=True)
    status.set('Informations générées :')
    with open('core\\settings.json', "r") as jsonFile:
        data = json.load(jsonFile)
    token = data["token"]
    clientid = data["id"]
    invit = "https://discordapp.com/api/oauth2/authorize?client_id=" + \
        data["id"] + "&permissions=8&scope=bot"
    tknl.pack()
    tkncopy.pack()
    clientdl.pack()
    clientdcopy.pack()
    invitationl.pack()
    invitationcopy.pack()


invitb = Button(info, text="Générer les informations",
                width=30, command=invitd)
invitb.pack()

vide = Label(info, text='')
vide.pack()

status = StringVar()
status.set('Appuyez pour afficher les informations')
sttus = Label(info, textvariable=status)
sttus.pack()

tkn = StringVar()
tkn.set('')
tknl = Label(info, textvariable=tkn)


clientd = StringVar()
clientd.set('')
clientdl = Label(info, textvariable=clientd)

invitation = StringVar()
invitation.set('')
invitationl = Label(info, textvariable=invitation)

#
#
#
# attaque auto attaque auto attaque auto attaque auto attaque auto attaque auto attaque auto attaque auto attaque auto attaque auto
#
#
#

atkl = LabelFrame(fenetre, text="Attaque automatique :", padx=5, pady=5)
atkl.pack(side=RIGHT, fill=Y)

def ataque():
    os.startfile('core\pydiv\\auto.py')

atkb = Button(atkl, text='Lancer l\'attaque', command=ataque, width=30)
atkb.pack()

# boutons seuls


manu = LabelFrame(fenetre, text="Attaques manuelles :", padx=5, pady=5)
manu.pack(fill=Y)


def role_dlt():
    showinfo('Tous les rôles supprimables vont être supprimés.',
             'Tous les rôles supprimables vont être supprimés.')
    os.startfile('core\stop.pyw')
    subprocess.run('cd core\individuals && node role_dlt.js', shell=True)
    showinfo('Terminé', 'Tous les rôles supprimables semblent avoir été supprimés.')


role_dltb = Button(manu, text="Supprimer tous les rôles",
                   command=role_dlt, width=30)
role_dltb.pack()


def admin2d():
    os.startfile('core\\individuals\\roles.py')


admin2b = Button(manu, text="Gérer les rôles",
                 command=admin2d, width=30)
admin2b.pack()


def supprchnlc():
    os.startfile('core\individuals\chnldlt.pyw')


supprchnl = Button(manu, text="Supprimer les salons",
                   command=supprchnlc, width=30)
supprchnl.pack()


def banp():
    showinfo('Bannissement de tout le monde',
             'Le bot va bannir tous les gens du serveur, le temps que cela prendra peut varier')
    os.startfile('core\stop.pyw')
    subprocess.run('cd core\individuals && node ban.js', shell=True)
    showinfo('Terminé', 'Vous pouvez fermer cette fenêtre.')


ban = Button(manu, text="Bannir tous les membres",  command=banp, width=30)
ban.pack()


spam = LabelFrame(manu, text="Spam", padx=5, pady=5)
spam.pack()
value = StringVar()
value.set('Message à spammer')
spame = Entry(spam, textvariable=value, width=36)
spame.pack()
spambtn = Button(spam, text="Spam", width=30,
                 command=lambda: spambtnp(spame))


def spambtnp(spame):
    if askokcancel('Lancer le spam', 'Voulez-vous vraiment lancer le spam ? Vous ne pourrez plus utiliser l\'interface jusqu\'à ce que la console soit fermée. Vous pouvez la fermer à tout moment en écrivant "stop" dans un salon du serveur.'):
        with open("core/settings.json", "r") as jsonFile:
            data = json.load(jsonFile)
        data["config"]["msg"] = spame.get()
        data["config"]["chnlname"] = spmchnl.get()
        with open("core/settings.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        os.startfile('core\stop.pyw')
        subprocess.run('cd core\individuals && node spm.js', shell=True)


def softspam(spame):
        with open("core/settings.json", "r") as jsonFile:
            data = json.load(jsonFile)
        data["config"]["msg"] = spame.get()
        with open("core/settings.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        os.startfile('core\individuals\softspam.pyw')


def spampv(spame):
    if askokcancel('Lancer le spam privé', 'Voulez-vous vraiment lancer le spam privé ? Pendant que le bot spamme, il est impossible d\'utiliser l\'interface. Pour arrêter de spammer, envoyez "stop" au bot en privé.'):
        with open("core\settings.json", "r") as jsonFile:
            data = json.load(jsonFile)
        data["config"]["msg"] = spame.get()
        with open("core/settings.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        os.startfile('core\individuals\chnldlt.pyw')


spampvbutton = Button(spam, text='Spam Privé', width=30,
                      command=lambda: spampv(spame))
spampvbutton.pack()

softspambutton = Button(spam, text="Heavy Spam", width=30,
                        command=lambda: softspam(spame))
softspambutton.pack()

spambtn.pack()


nvnom = LabelFrame(manu, text="Modifier le serveur", padx=5, pady=5)
nvnom.pack()

value = StringVar()
value.set("Nouveau nom")
nouveaunom = Entry(nvnom, textvariable=value, width=36)
nouveaunom.pack()
nouveaunomb = Button(nvnom, text="Changer le nom du serveur",
                     command=lambda: nouveaunomd(nouveaunom), width=30)


def nouveaunomd(nouveaunom):
    text = nouveaunom.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["name"]
    data["config"]["name"] = nouveaunom.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    subprocess.run("cd core\individuals && node name.js", shell=True)


nouveaunomb.pack()

value = StringVar()
value.set("URL ou chemin vers l'image")
nouvelleimg = Entry(nvnom, text=value, width=36).pack()
nouvelleimgb = Button(nvnom, text="Changer l'icône du serveur",
                      width=30, command=lambda: nouvelleimgd(nouvelle))


def nouvelleimgd():
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data["config"]["img"] = nouvelleimg.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    subprocess.run("cd core\individuals && node img.js", shell=True)


nouvelleimgb.pack()


banip = LabelFrame(manu, text="Ban IP", padx=5, pady=5)
banip.pack()

value = StringVar()
value.set("Id à bannir")
bann = Entry(banip, textvariable=value, width=36)
bann.pack()


def bannd():
    with open("core\settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["banip"]
    data["banip"] = bann.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    subprocess.run('cd core\individuals && node bann.js', shell=True)
    showinfo('Terminé', 'Le membre en question a bien été banni.')


bannb = Button(banip, text="Bannir un membre", command=bannd, width=30)
bannb.pack()


role_crtl = LabelFrame(manu, text="Créer des rôles", padx=5, pady=5)
role_crtl.pack()

value = StringVar()
value.set("Nom du rôle")
role_crte = Entry(role_crtl, textvariable=value, width=36).pack()


def role_crt(value):
    text = value.get()
    with open("core\settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data["config"]["rolename"] = text
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    showwarning('Attention', 'Une infinité de rôles va être créée, assurez-vous d\'avoir entré votre ID, et écrivez stop dans un des salons du serveur pour arrêter.\n\nNote : Cette fenêtre sera inutilisable pendant l\'éxécution du programme.')
    os.startfile('core\stop.pyw')
    subprocess.run('cd core\individuals && node role_crt.js', shell=True)
    showinfo('Terminé', 'Vous avez choisi d\'arrêter le programme.')


role_crtb = Button(role_crtl, text="Créer une infinité de rôles",
                   command=lambda: role_crt(value), width=30).pack()


fenetre.mainloop()
