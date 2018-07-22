import subprocess
import sys
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Installation des dépendances')
prcnt = StringVar()
prcnt.set(0)

p = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate', variable=prcnt)
p.pack()
def ins():
    subprocess.run('npm --prefix core i discord.js', shell=True)
    prcnt.set(10)
    root.update()
    subprocess.run('npm --prefix core i fs', shell=True)
    prcnt.set(20)
    root.update()
    subprocess.run('npm --prefix core i ms', shell=True)
    prcnt.set(30)
    root.update()
    subprocess.run('npm --prefix core i moment', shell=True)
    prcnt.set(40)
    root.update()
    subprocess.run('npm --prefix core i chalk', shell=True)
    prcnt.set(50)
    root.update()
    subprocess.run('npm --prefix core/individuals i discord.js', shell=True)
    prcnt.set(60)
    root.update()
    subprocess.run('npm --prefix core/individuals i fs', shell=True)
    prcnt.set(70)
    root.update()
    subprocess.run('npm --prefix core/individuals i ms', shell=True)
    prcnt.set(80)
    root.update()
    subprocess.run('npm --prefix core/individuals i moment', shell=True)
    prcnt.set(90)
    root.update()
    subprocess.run('npm --prefix core/individuals i chalk', shell=True)
    prcnt.set(100)
    root.update()
    sys.exit()


progb = Button(root, text="Commencer l'installation", command=ins)
progb.pack()

root.mainloop()
