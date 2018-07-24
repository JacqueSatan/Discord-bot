import subprocess
import sys
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Installation des dépendances')
prcnt = StringVar()
prcnt.set(0)

root1 = LabelFrame(root, text="Progression",padx=20,pady=20)
root1.pack()

p = ttk.Progressbar(root1, orient=HORIZONTAL, length=400, mode='determinate', variable=prcnt)
p.pack()
def ins():
    root.update()
    subprocess.run('npm --prefix core i discord.js', shell=True)
    prcnt.set(24.85)
    root.update()
    subprocess.run('npm --prefix core i fs', shell=True)
    prcnt.set(28.08)
    root.update()
    subprocess.run('npm --prefix core i ms', shell=True)
    prcnt.set(28.37)
    root.update()
    subprocess.run('npm --prefix core i moment', shell=True)
    prcnt.set(40)
    root.update()
    subprocess.run('npm --prefix core i chalk', shell=True)
    prcnt.set(47)
    root.update()
    subprocess.run('npm --prefix core/individuals i discord.js', shell=True)
    prcnt.set(60)
    root.update()
    subprocess.run('npm --prefix core/individuals i fs', shell=True)
    prcnt.set(65)
    root.update()
    subprocess.run('npm --prefix core/individuals i ms', shell=True)
    prcnt.set(66)
    root.update()
    subprocess.run('npm --prefix core/individuals i moment', shell=True)
    prcnt.set(90)
    root.update()
    subprocess.run('npm --prefix core/individuals i chalk', shell=True)
    prcnt.set(100)
    root.update()
    sys.exit()

ins()

root.mainloop()
