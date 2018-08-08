from tkinter import *
from tkinter import ttk
import subprocess
import json
from tkinter.messagebox import *
import os

root = Tk()

root.title('Heavy spam')

conf = LabelFrame(root, text='Configuration et lancement', padx=5, pady=5)
conf.pack(side=LEFT)

e01 = IntVar()
e1 = Checkbutton(conf, text="Spammer en privé ?", variable=e01, onvalue="1", offvalue="0", width=50, indicatoron=0)
e1.pack()

e02 = IntVar()
e2 = Checkbutton(conf, text="Spammer dans tous les salons de tous les serveurs", variable=e02, onvalue="1", offvalue="0", width=50, indicatoron=0)
e2.pack()

v = Label(conf, text="")
v.pack()

def fina(e01, e02):
    with open("../settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
        
    data["config"]["spampv"] = e01.get()
    data["config"]["spamprtt"] = e02.get()
    with open('../settings.json', "w") as jsonFile:
        json.dump(data, jsonFile)
    os.startfile('..\stop.pyw')
    subprocess.run('node softspam.js', shell=True)


final = Button(conf, text='Valider et lancer l\'attaque', width=50, command=lambda:fina(e01, e02))
final.pack()

root.mainloop()