from tkinter import *
from tkinter.messagebox import *
import json
import webbrowser
import subprocess
import os

fenetre = Tk()

#fenetre.geometry("460x205")
fenetre.title('Discord-Bot v1.3.3')

def contact():
    showinfo("Me contacter", "Discord : @Jacques#5823\nE-mail  : dsicrod@gmail.com\nTwitter : @AntiDiscord")

def git():
        webbrowser.open_new(r"https://antidiscordbot.page.link/lastversion")

def aide():
    showinfo("Aide", "Quelle est cette application ?\n    Cette application sert simplement à configurer et lancer votre bot sans avoir à éditer manuellement un fichier.\n\nPourquoi est-ce que le fichier start.bat se ferme instantanément quand je l'ouvre ?\n    Vous avez peut-être mal configuré votre bot, ou  oublié d'installer les librairies requises (discord.js, moment, etc...).\n\nSi vous avez besoin d'aide supplémentaire, veuillez me contacter.")

def installt():
    showinfo('Installation des dépendences', 'Les dépendences sont en cours d\'installation, veuillez patienter.')
    subprocess.call('npm --prefix ./core i discord.js', shell=True)
    subprocess.call('npm --prefix ./core i fs', shell=True)
    subprocess.call('npm --prefix ./core i ms', shell=True)
    subprocess.call('npm --prefix ./core i moment', shell=True)
    subprocess.call('npm --prefix ./core i chalk', shell=True)
    showinfo('Dépendences installées', 'Toutes les dépendences semblent avoir été installées.')

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_cascade(label="Installer les dépendences", command=installt)
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Aide", command=aide)
menu2.add_command(label="Page Github", command=git)
menu2.add_command(label="Me contacter", command=contact)
menubar.add_cascade(label="A propos", menu=menu2)

fenetre.config(menu=menubar)



value = StringVar() 
value.set("Token")
entree = Entry(fenetre, textvariable=value, width=30)
entree.grid(row=1, column=1)
bouton = Button(fenetre, text="Valider", command=lambda:recupere(entree))
def recupere(entree):
    text = entree.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["token"]
    data["token"] = entree.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton.grid(row=1, column=2)



value = StringVar()
value.set("Le bot est sur le serveur ? (y/n)")
entree1 = Entry(fenetre, textvariable=value, width=30)
entree1.grid(row=3, column=1)
bouton1 = Button(fenetre, text="Valider", command=lambda:recupere1(entree1))
def recupere1(entree1):
    text = entree1.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["auto"]["enabled"]
    data["auto"]["enabled"] = entree1.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton1.grid(row=3, column=2)

value = StringVar()
value.set("Id du serveur")
entree2 = Entry(fenetre, textvariable=value, width=30)
entree2.grid(row=5, column=1)
bouton2 = Button(fenetre, text="Valider", command=lambda:recupere2(entree2))
def recupere2(entree2):
    text = entree2.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["auto"]["server_id"]
    data["auto"]["server_id"] = entree2.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton2.grid(row=5, column=2)

value = StringVar()
value.set("Bannir tout le monde ? (y/n)")
entree3 = Entry(fenetre, textvariable=value, width=30)
entree3.grid(row=7, column=1)
bouton3 = Button(fenetre, text="Valider", command=lambda:recupere3(entree3))
def recupere3(entree3):
    text = entree3.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["ban"]
    data["config"]["ban"] = entree3.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton3.grid(row=7, column=2)

value = StringVar()
value.set("Changer l'image et le nom ? (y/n)")
entree4 = Entry(fenetre, textvariable=value, width=30)
entree4.grid(row=9, column=1)
bouton4 = Button(fenetre, text="Valider", command=lambda:recupere4(entree4))
def recupere4(entree4):
    text = entree4.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["imgnom"]
    data["config"]["imgnom"] = entree4.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton4.grid(row=9, column=2)

value = StringVar()
value.set("Nouveau nom")
entree5 = Entry(fenetre, textvariable=value, width=30)
entree5.grid(row=11, column=1)
bouton5 = Button(fenetre, text="Valider", command=lambda:recupere5(entree5))
def recupere5(entree5):
    text = entree5.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["name"]
    data["config"]["name"] = entree5.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton5.grid(row=11, column=2)

value = StringVar()
value.set("Chemin vers l'image")
entree6 = Entry(fenetre, textvariable=value, width=30)
entree6.grid(row=13, column=1)
bouton6 = Button(fenetre, text="Valider", command=lambda:recupere6(entree6))
def recupere6(entree6):
    text = entree6.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["img"]
    data["config"]["img"] = entree6.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton6.grid(row=13, column=2)

value = StringVar()
value.set("Supprimer tous les salons ? (y/n)")
entree8 = Entry(fenetre, textvariable=value, width=30)
entree8.grid(row=1, column=4)
bouton8 = Button(fenetre, text="Valider", command=lambda:recupere8(entree8))
def recupere8(entree8):
    text = entree8.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["chnl_dlt"]
    data["config"]["chnl_dlt"] = entree8.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton8.grid(row=1, column=5)

value = StringVar()
value.set("Rendre @everyone administrateur ? (y/n)")
entree9 = Entry(fenetre, textvariable=value, width=30)
entree9.grid(row=3, column=4)
bouton9 = Button(fenetre, text="Valider", command=lambda:recupere9(entree9))
def recupere9(entree9):
    text = entree9.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["admin"]
    data["config"]["admin"] = entree9.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton9.grid(row=3, column=5)

value = StringVar()
value.set("Supprimer tous les rôles ? (y/n)")
entree10 = Entry(fenetre, textvariable=value, width=30)
entree10.grid(row=5, column=4)
bouton10 = Button(fenetre, text="Valider", command=lambda:recupere10(entree10))
def recupere10(entree10):
    text = entree10.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["role_dlt"]
    data["config"]["role_dlt"] = entree10.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton10.grid(row=5, column=5)

value = StringVar()
value.set("Créer des rôles à l'infini ? (y/n)")
entree11 = Entry(fenetre, textvariable=value, width=30)
entree11.grid(row=7, column=4)
bouton11 = Button(fenetre, text="Valider", command=lambda:recupere11(entree11))
def recupere11(entree11):
    text = entree11.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["role_crt"]
    data["config"]["role_crt"] = entree11.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton11.grid(row=7, column=5)

value = StringVar()
value.set("Spammer ? (n/y/v/c) (voir le readme)")
entree12 = Entry(fenetre, textvariable=value, width=30)
entree12.grid(row=9, column=4)
bouton12 = Button(fenetre, text="Valider", command=lambda:recupere12(entree12))
def recupere12(entree12):
    text = entree12.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["ban"]
    data["config"]["ban"] = entree12.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton12.grid(row=9, column=5)

value = StringVar()
value.set("Nom des salons à créer (pas de maj ni d'espace ou de caractères spéciaux)")
entree13 = Entry(fenetre, textvariable=value, width=30)
entree13.grid(row=11, column=4)
bouton13 = Button(fenetre, text="Valider", command=lambda:recupere13(entree13))
def recupere13(entree13):
    text = entree13.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["chnlname"]
    data["config"]["chnlname"] = entree13.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton13.grid(row=11, column=5)

value = StringVar()
value.set("Méthode : tout/spam (1/2)")
entree14 = Entry(fenetre, textvariable=value, width=30)
entree14.grid(row=13, column=4)
bouton14 = Button(fenetre, text="Valider", command=lambda:recupere14(entree14))
def recupere14(entree14):
    text = entree14.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["auto"]["function"]
    data["auto"]["function"] = entree14.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton14.grid(row=13, column=5)

value = StringVar()
value.set("Votre Id")
entree7 = Entry(fenetre, textvariable=value, width=30)
entree7.grid(row=15, column=1)
bouton7 = Button(fenetre, text="Valider", command=lambda:recupere7(entree7))
def recupere7(entree7):
    text = entree7.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["ownerid"]
    data["ownerid"] = entree7.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
bouton7.grid(row=15, column=2)

def lancer():
    if askokcancel('Lancer l\'attaque', 'Voulez-vous vraiment lancer l\'attaque ?'):
        showinfo('Attaque lancée', 'Cette fenêtre ne répondra plus veuillez ne pas la fermer.')
        os.system('core/start.bat')
    else:
        showinfo('Attaque annulée', 'L\'attaque a bien été annulée.')
bout = Button(fenetre, text="Lancer l'attaque", command=lancer)
bout.grid(row=15, column=4)

fenetre.mainloop()
