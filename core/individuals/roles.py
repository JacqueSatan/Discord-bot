import json
import os
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

cwd = os.getcwd()

root = Tk()

root.title('Modifier les roles')

all = LabelFrame(root, text='Options de modification', padx=5, pady=5)
all.pack()

eav = IntVar()
ea = Checkbutton(all, text='Mettre @everyone administrateur', indicatoron=0, onvalue='1', offvalue='0', width=50, variable=eav)
ea.pack()

oav = IntVar()
oa = Checkbutton(all, text='Vous mettre administrateur', indicatoron=0, onvalue='1', offvalue='0', width=50, variable=oav)
oa.pack()

env = IntVar()
en = Checkbutton(all, text='Enlever toutes les permissions à tous les rôles', indicatoron=0, offvalue='0', onvalue='1', width=50, variable=env)
en.pack()

srv = IntVar()
sr = Checkbutton(all, text='Supprimer tous les rôles', indicatoron=0, onvalue='1', offvalue='0', width=50, variable=srv)
sr.pack()

crl = LabelFrame(all, text="Création", padx=5, pady=5)
crl.pack()

crn = StringVar()
crn.set('Nom des rôles à créer')
cre = Entry(crl, textvariable=crn, width=36)

crgv = IntVar()
crg = Checkbutton(crl, text="Les donner à chaque membre (Lent)", width=30, indicatoron=0, onvalue="1", offvalue="0", variable=crgv)

def crdef(cre, crgv):
	with open(cwd + "\\core\\settings.json", "r") as jsonFile:
		data = json.load(jsonFile)
	data["roles"]["create"]["name"] = cre.get()
	data["roles"]["create"]["enabled"] = crgv.get()

validv = IntVar()
valid = Button(crl, text="Valider", width=30, command=lambda:crdef(cre, crgv))

def crd():
	cre.pack()
	crg.pack()
	valid.pack()

crv = IntVar()
cr = Checkbutton(crl, text='Créer des rôles à l\'infini', indicatoron=0, onvalue='1', offvalue='0', width=50, variable=crv, command=crd)
cr.pack()


def lancer(eav, oav, env, srv, crv):
	with open(cwd + "\\core\\settings.json", "r") as jsonFile:
		data = json.load(jsonFile)
	data["roles"]["code"]["eadmin"] = eav.get()
	data["roles"]["code"]["oadmin"] = oav.get()
	data["roles"]["code"]["e0perm"] = env.get()
	data["roles"]["code"]["esuppr"] = srv.get()
	data["roles"]["code"]["create"] = crv.get()
	with open(cwd + "\\core\\settings.json", "w") as jsonFile:
		json.dump(data, jsonFile)

vl = Button(all, text="Valider et lancer l'attaque", width=50, command=lambda:lancer(eav, oav, env, srv, crv))
vl.pack()

root.mainloop()