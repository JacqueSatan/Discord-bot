from tkinter import *
from tkinter import ttk
import subprocess


deps = Tk()

deps.title('Installation de dépendances...')

def install():
    deps1 = LabelFrame(
        deps, text='Progression de l\'installation', padx=20, pady=20)
    deps1.pack()
    p = StringVar()
    p.set(0)
    pt = StringVar()
    p_l = Label(deps, textvariable=pt)
    p_l.pack()
    p_b = ttk.Progressbar(deps1, orient=HORIZONTAL,
                          length=400, mode='determinate', variable=p)
    p_b.pack()
    pt.set('Mise à jour de "pip"...')
    deps.update()
    subprocess.run(
        'py -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org requests', shell=True)
    subprocess.run(
        'py -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade requests', shell=True)
    subprocess.run(
        'py -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip', shell=True)
    p.set(15)
    pt.set('Installation de "python-firebase" (1/2)')
    deps.update()
    subprocess.run(
        'py -m pip --trusted-host pypi.org --trusted-host files.pythonhosted.org install requests==1.1.0', shell=True)
    p.set(19)
    pt.set('Installation de "python-firebase" (2/2)')
    deps.update()
    subprocess.run(
        'py -m pip --trusted-host pypi.org --trusted-host files.pythonhosted.org install python-firebase', shell=True)
    pt.set('Installation des dépendances Discord...')
    deps.update()
    subprocess.run('npm --prefix core i discord.js', shell=True)
    p.set(24.85)
    deps.update()
    subprocess.run('npm --prefix core i fs', shell=True)
    p.set(28.08)
    deps.update()
    subprocess.run('npm --prefix core i ms', shell=True)
    p.set(28.37)
    deps.update()
    subprocess.run('npm --prefix core i moment', shell=True)
    p.set(40)
    deps.update()
    subprocess.run('npm --prefix core i chalk', shell=True)
    p.set(47)
    deps.update()
    subprocess.run(
        'npm --prefix core/individuals i discord.js', shell=True)
    p.set(60)
    deps.update()
    subprocess.run('npm --prefix core/individuals i fs', shell=True)
    p.set(65)
    deps.update()
    subprocess.run('npm --prefix core/individuals i ms', shell=True)
    p.set(66)
    deps.update()
    subprocess.run('npm --prefix core/individuals i moment', shell=True)
    p.set(90)
    deps.update()
    subprocess.run('npm --prefix core/individuals i chalk', shell=True)
    p.set(100)
    deps.update()
    os.startfile('../launcher.pyw')
    sys.exit()
install()
deps.mainloop()