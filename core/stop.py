from tkinter import *
import subprocess

root = Tk()

stopframe = LabelFrame(root, text="Arrêter l'attaque", padx=5, pady=5)
stopframe.pack()

stoplabel = Label(
    stopframe, text="Cliquez sur le bouton ci-dessous pour arrêter l'attaque")
stoplabel.pack()

vide = Label(stopframe, text='\n\n')
vide.pack()


def stopdef():
    subprocess.run('cd individuals && node stop.js',shell=True)
    sys.exit()


stopButton = Button(stopframe, text='Arrêter', command=stopdef)
stopButton.pack()

root.mainloop()
