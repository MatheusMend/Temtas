from PIL import Image, ImageTk
import queue
import keyboard
import threading
import time
from tkinter import *
from tkinter import filedialog, ttk, messagebox  # Versão? Popup de Koish? Pop up de Contador FreeTem/Luma?



#### Root Ui ####

root = Tk()
root.title('Temtas by Rusp v0.2')
root.iconbitmap('Soulbound.ico')
root.geometry("1200x800")
my_menu = Menu(root)
root.config(menu=my_menu)

#### Menus ####


def hideallframes():
    n2.pack_forget()
    n.pack_forget()


### Visão Geral ###

def Teste1():
    hideallframes()
    n.pack(fill='both', expand=1)


visaoGeral = Menu(my_menu)
my_menu.add_cascade(label="Visão Geral", menu=visaoGeral)
visaoGeral.add_command(label="Resumo", command=Teste1)


### Semanais ###

def Teste2():
    hideallframes()
    n2.pack(fill='both', expand=1)


weeklys = Menu(my_menu)
my_menu.add_cascade(label="Semanais", menu=weeklys)
weeklys.add_command(label="Check List", command=Teste2)
weeklys.add_command(label="FreeTem", command=Teste2)
weeklys.add_command(label="Koish", command=Teste2)
weeklys.add_command(label="Postal Service", command=Teste2)


## FreeTem Counter ##

n2 = Frame(root, width=400, height=400, bg='yellow')
n = Frame(root, width=400, height=400, bg='red')

freetemcounter = Label(n2, text="HUM?")
freetemcounter.place(x=500, y=0)


def app_main_loop(my_label):
    # Create another thread that monitors the keyboard
    input_queue = queue.Queue()
    kb_input_thread = threading.Thread(target=_check_plus_pressed, args=(input_queue,))
    kb_input_thread.daemon = True
    kb_input_thread.start()

    # Main logic loop
    run_active = True
    while True:
        if not input_queue.empty():
            if run_active and (input_queue.get() == "+"):
                run_active = False
                Lap(my_label)
                Stop()
        time.sleep(0.1)  # Aparentemente não funciona sem


def _check_plus_pressed(input_queue):
    while True:
        if keyboard.is_pressed('+'):
            input_queue.put("+")
        time.sleep(0.1)  # Aparentemente não funciona sem


def Lap(my_label):
    my_label.configure(text="Lap")


def Stop():
    print("Stopped")


main_loop_thread = threading.Thread(target=app_main_loop, args=(freetemcounter,))
main_loop_thread.daemon = True
main_loop_thread.start()

## Lairs ##

lairs = Menu(my_menu)
my_menu.add_cascade(label="Lairs", menu=lairs)
lairs.add_command(label="Anak Volcano - Tyranak", command=Teste2)
lairs.add_command(label="Sacred Lake - Volgon", command=Teste2)

## PvP ##

pvp = Menu(my_menu)
my_menu.add_cascade(label="PvP", menu=pvp)
pvp.add_command(label="Dashboard", command=Teste2)

## Tamers Paradise ##

tamersparadise = Menu(my_menu)
my_menu.add_cascade(label="Tamers Paradise", menu=tamersparadise)
tamersparadise.add_command(label="Draft", command=Teste2)
tamersparadise.add_command(label="DigiLair", command=Teste2)
tamersparadise.add_command(label="Grit", command=Teste2)
tamersparadise.add_command(label="Safari", command=Teste2)
tamersparadise.add_command(label="Tower", command=Teste2)

## Tempedia ##

tempedia = Menu(my_menu)
my_menu.add_cascade(label="Tempedia", menu=tempedia)
tempedia.add_command(label="Breeding Projects", command=Teste2)
tempedia.add_command(label="Luma Tempedia", command=Teste2)

## Sobre ##

sobre = Menu(my_menu)
my_menu.add_cascade(label="Sobre", menu=sobre)
sobre.add_command(label="Versão", command=Teste2)


root.mainloop()
