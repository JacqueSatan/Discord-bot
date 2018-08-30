import json
import os
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

root = Tk()

root.title('Supprimer les salons')

all = LabelFrame(root, text='Supprimer tous les salons', padx=5, pady=5)
all.pack()

textvarr = IntVar()
text = Checkbutton(all, text='Supprimer tous les salons textuels', indicatoron=0, variable=textvarr, width=50, onvalue='1', offvalue='0')
text.pack()

vocalvarr = IntVar()
vocal = Checkbutton(all, text='Supprimer tous les salons vocaux', indicatoron=0, variable=vocalvarr, width=50, onvalue='1', offvalue='0')
vocal.pack()

catvarr = IntVar()
cat = Checkbutton(all, text='Supprimer toutes les catégories', indicatoron=0, variable=catvarr, width=50, onvalue='1', offvalue='0')
cat.pack()

vide = Label(all, text='')
vide.pack()

def launchdef(textvarr, vocalvarr, catvarr):
    with open('settings.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    data["config"]["chnlsuppr"]["text"] = textvarr.get()
    data["config"]["chnlsuppr"]["vocal"] = vocalvarr.get()
    data["config"]["chnlsuppr"]["cat"] = catvarr.get()
    with open('settings.json', 'w') as jsonFile:
        json.dump(data, jsonFile)
    os.startfile('stop.pyw')
    subprocess.run('node chnldlt.js', shell=True)

launch = Button(all, text='Valider et lancer l\'attaque', width=50, command=lambda:launchdef(textvarr, vocalvarr, catvarr))
launch.pack()

root.mainloop()
