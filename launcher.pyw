from pathlib import Path
from tkinter import *
from tkinter.messagebox import *
import json
import os
import subprocess
import webbrowser

fenetre = Tk()

#fenetre.geometry("460x205")
fenetre.title('Discord-Bot v1.3.4')

def contact():
    showinfo("Me contacter", "Discord : @Jacques#5823\nE-mail  : dsicrod@gmail.com\nTwitter : @AntiDiscord")

def git():
        webbrowser.open_new_tab(r"https://antidiscordbot.page.link/lastversionfromapp")

def dscrdc():
    webbrowser.open_new_tab(r"https://antidiscordbot.page.link/discordcreatefromapp")

def dscrdv():
    webbrowser.open_new_tab(r"https://antidiscordbot.page.link/discordappsfromapp")

def aide():
    showinfo("Aide", "Quelle est cette application ?\n    Cette application sert simplement à configurer et lancer votre bot sans avoir à éditer manuellement un fichier.\n\nPourquoi est-ce que le fichier start.bat se ferme instantanément quand je l'ouvre ?\n    Vous avez peut-être mal configuré votre bot, ou  oublié d'installer les librairies requises (discord.js, moment, etc...).\n\nSi vous avez besoin d'aide supplémentaire, veuillez me contacter.")

def installt():
    showinfo('Installation des dépendences', 'L\'installation va commencer, veuillez patienter. Si l\'application ne répond plus, c\'est normal. Attendez juste. Cela risque de prendre un peu de temps.')
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
    showinfo('Dépendences installées', 'Toutes les dépendences semblent avoir été installées.')


menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)


menu1.add_command(label="Installer les dépendences", command=installt)
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Options", menu=menu1)

def support():
    webbrowser.open_new_tab(r"https://discord.gg/ngrdmkN")

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Serveur de support", command=support)
menu3.add_command(label="Page Github", command=git)
menu3.add_command(label="Créer une application Discord", command=dscrdc)
menu3.add_command(label="Vos applications Discord", command=dscrdv)
menubar.add_cascade(label='Liens', menu=menu3)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Aide", command=aide)
menu2.add_command(label="Me contacter", command=contact)
menubar.add_cascade(label="A propos", menu=menu2)

fenetre.config(menu=menubar)

obligd = Label(fenetre, text="Obligatoire :")
obligd.grid(row=1, column=1)

value = StringVar() 
value.set("Token")
entree = Entry(fenetre, textvariable=value, width=30)
entree.grid(row=2, column=1)

value = StringVar()
value.set("Id du serveur")
entree2 = Entry(fenetre, textvariable=value, width=30)
entree2.grid(row=3, column=1)

value = StringVar()
value.set("Votre Id")
entree7 = Entry(fenetre, textvariable=value, width=30)
entree7.grid(row=4, column=1)

validb = Button(fenetre, text="Valider", cursor="pirate", command=lambda:validd(entree, entree2, entree7))
def validd(entree, entree2, entree7):
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
validb.grid(row=5, column=1)



atkl = Label(fenetre, text="Attaque automatique :")
atkl.grid(row=1, column=4)


entree1 = IntVar()
Checkbutton(fenetre, text="Le bot est sur le serveur ?", width=30, variable=entree1, onvalue="1", offvalue="0").grid(row=2, column=4)

#value = StringVar()
#value.set("Le bot est sur le serveur ? (y/n)")
#entree1 = Entry(fenetre, textvariable=value, width=30)
#entree1.grid(row=2, column=4)

entree3 = IntVar()
Checkbutton(fenetre, text="Bannir tout le monde ?", variable=entree3, onvalue="1", offvalue="0").grid(row=3, column=4)

entree4 = IntVar()
Checkbutton(fenetre, text="Changer l'image et le nom ?", variable=entree4, onvalue="1", offvalue="0").grid(row=4, column=4)


value = StringVar()
value.set("Nouveau nom")
entree5 = Entry(fenetre, textvariable=value, width=30)
entree5.grid(row=5, column=4)

value = StringVar()
value.set("Chemin ou URL de l'image")
entree6 = Entry(fenetre, textvariable=value, width=30)
entree6.grid(row=6, column=4)

entree8 = IntVar()
Checkbutton(fenetre, text="Supprimer tous les salons ?", variable=entree8, onvalue="1", offvalue="0").grid(row=7, column=4)

entree9 = IntVar()
Checkbutton(fenetre, text="Rendre  @everyone administrateur ?", variable=entree9, onvalue="1", offvalue="0").grid(row=8, column=4)

entree10 = IntVar()
Checkbutton(fenetre, text="Supprimer tous les rôles ?", variable=entree10, onvalue="1", offvalue="0").grid(row=9, column=4)

entree11 = IntVar()
Checkbutton(fenetre, text="Créer des rôles à l'infini ?", variable=entree11, onvalue="1", offvalue="0").grid(row=10, column=4)

spam = ('Créer des salons textuels à l\'infini', 'Créer des salons textuels et spammer dedans', 'Créer des salons vocaux', 'Créer des catégories')
entree12 = Spinbox(values=sorted(spam), width=len(max(spam))+2)
entree12.grid(row=11, column=4)

value = StringVar()
value.set("Nom des salons à créer (pas de maj ni d'espace ou de caractères spéciaux)")
entree13 = Entry(fenetre, textvariable=value, width=30)
entree13.grid(row=12, column=4)

value = StringVar()
value.set("Méthode : tout/spam (1/2)")
entree14 = Entry(fenetre, textvariable=value, width=30)
entree14.grid(row=13, column=4)

def lancer(entree1, entree3, entree4, entree5, entree6, entree8, entree9, entree10, entree11, entree12, entree13, entree14):
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["auto"]["enabled"]
    data["auto"]["enabled"] = entree1.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["ban"]
    data["config"]["ban"] = entree3.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["imgnom"]
    data["config"]["imgnom"] = entree4.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["name"]
    data["config"]["name"] = entree5.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["img"]
    data["config"]["img"] = entree6.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["chnl_dlt"]
    data["config"]["chnl_dlt"] = entree8.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["admin"]
    data["config"]["admin"] = entree9.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["role_dlt"]
    data["config"]["role_dlt"] = entree10.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["role_crt"]
    data["config"]["role_crt"] = entree11.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["spam"]
    data["config"]["spam"] = entree12.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["chnlname"]
    data["config"]["chnlname"] = entree13.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["auto"]["function"]
    data["auto"]["function"] = entree14.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

bout = Button(fenetre, text="Valider", cursor="pirate", command=lambda:lancer(entree1, entree3, entree4, entree5, entree6, entree8, entree9, entree10, entree11, entree12, entree13, entree14))
bout.grid(row=15, column=4)

def lancerd():
    showinfo('Attaque lancée', 'Cette fenêtre va se bloquer, veuillez ne pas la fermer.\n\nNote : Pour terminer l\'attaque, écrivez stop dans n\'importe quel salon du serveur.')
    subprocess.run('cd core && node bot.js', shell=True)
lancerb = Button(fenetre, text="Lancer l'attaque", cursor="pirate", command=lancerd)
lancerb.grid(row=16, column=4)


#boutons seuls


manu = Label(fenetre, text="Attaques manuelles :")
manu.grid(row=6, column=1)

def spambtnp():
    if askokcancel('Lancer le spam', 'Voulez-vous vraiment lancer le spam ? Vous ne pourrez plus utiliser l\'interface jusqu\'à ce que la console soit fermée. Vous pouvez la fermer à tout moment en écrivant "stop" dans un salon du serveur.'):
        subprocess.run('cd core\individuals && node spm.js', shell=True)
spambtn = Button(fenetre, text="Spam", cursor="pirate", command=spambtnp)
spambtn.grid(row=7, column=1)

def verbtn():
    subprocess.run('cd core\individuals && ver.bat', shell=True)
    path = Path(__file__).parent.joinpath('core/settings.json')
    with open(path) as fp:
        data = json.load(fp)
    tmp = data["ver"]
    if tmp == 'oui':
        showinfo('Test réussi', 'Le bot est bien administrateur sur le serveur demandé.')
    else:
        showerror('Test failli', 'Soit le bot n\est pas administrateur, soit une erreur est survenue.')
verbtnp = Button(fenetre, text="Vérifier le rôle du bot", cursor="pirate", command=verbtn)
verbtnp.grid(row=8, column=1)

def supprchnlc():
    showinfo('Suppression des salon', 'Tous les salons du serveur vont être supprimés, cela risque de prendre un peu de temps.')
    subprocess.run('cd core\individuals && node chnldlt.js', shell=True)
    showinfo('Terminé', 'Vous pouvez fermer cette fenêtre.')
supprchnl = Button(fenetre, text="Supprimer tous les salons", cursor="pirate", command=supprchnlc)
supprchnl.grid(row=9, column=1)

def banp():
    showinfo('Bannissement de tout le monde', 'Le bot va bannir tous les gens du serveur, le temps que ça prendra peut varier')
    subprocess.run('cd core\individuals && node ban.js', shell=True)
    showinfo('Terminé', 'Vous pouvez fermer cette fenêtre.')
ban = Button(fenetre, text="Bannir tous les membres", cursor="pirate", command=banp)
ban.grid(row=10, column=1)

value = StringVar()
value.set("Nouveau nom")
nouveaunom = Entry(fenetre, textvariable=value, width=30)
nouveaunom.grid(row=11, column=1)
nouveaunomb = Button(fenetre, text="Changer le nom du serveur", cursor="pirate", command=lambda:nouveaunomd(nouveaunom))
def nouveaunomd(nouveaunom):
    text = nouveaunom.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["name"]
    data["config"]["name"] = nouveaunom.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    subprocess.run("cd core\individuals && node name.js", shell=True)
nouveaunomb.grid(row=12, column=1)

def admin2d():
    subprocess.run('cd core\individuals && node admin2.js', shell=True)
    showinfo('Terminé', 'Vous êtes normalement administrateur sur le serveur indiqué.')
admin2b = Button(fenetre, text="Mettre @everyone administrateur", cursor="pirate", command=admin2d)
admin2b.grid(row=13, column=1)

value = StringVar()
value.set("Id à bannir")
bann = Entry(fenetre, textvariable=value, width=30)
bann.grid(row=14, column=1)
def bannd():
    with open("core\settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["banip"]
    data["banip"] = bann.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    subprocess.run('cd core\individuals && node bann.js', shell=True)
    showinfo('Terminé', 'Le membre en question a bien été banni.')
bannb = Button(fenetre, text="Bannir un membre", command=bannd)
bannb.grid(row=15, column=1)

def role_dlt():
    showinfo('Tous les rôles supprimables vont être supprimés.', 'Tous les rôles supprimables vont être supprimés.')
    subprocess.run('cd core\individuals && node role_dlt.js', shell=True)
    showinfo('Terminé', 'Tous les rôles supprimables semblent avoir été supprimés.')
role_dltb = Button(fenetre, text="Supprimer tous les rôles", command=role_dlt)
role_dltb.grid(row=16, column=1)

fenetre.mainloop()
