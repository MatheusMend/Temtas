import queue
import keyboard
import threading
import time
from tkinter import *
from tkinter import ttk

#### Root Ui ####

root = Tk()
root.title('Temtas by Rusp v0.2')
root.iconbitmap('Soulbound.ico')
root.geometry("1200x800")
my_menu = Menu(root)
root.config(menu=my_menu)

#### Menus ####

## Funções ##

def Teste1():
    hideallframes()
    n.pack(fill='both', expand=1)


def Teste2():
    hideallframes()
    n2.pack(fill='both', expand=1)


def hideallframes():
    n2.pack_forget()
    n.pack_forget()


## Visão Geral ##

visaoGeral = Menu(my_menu)
my_menu.add_cascade(label="Visão Geral", menu=visaoGeral)
visaoGeral.add_command(label="New", command=Teste1)

## Semanais ##
weeklys = Menu(my_menu)
my_menu.add_cascade(label="Semanais", menu=weeklys)
weeklys.add_command(label="dX", command=Teste2)

## Tamers Paradise ##

weeklys = Menu(my_menu)
my_menu.add_cascade(label="Semanais", menu=weeklys)
weeklys.add_command(label="dX", command=Teste2)

## Lairs ##

weeklys = Menu(my_menu)
my_menu.add_cascade(label="Semanais", menu=weeklys)
weeklys.add_command(label="dX", command=Teste2)

## PvP ##

weeklys = Menu(my_menu)
my_menu.add_cascade(label="Semanais", menu=weeklys)
weeklys.add_command(label="dX", command=Teste2)

## Tempedia ##

weeklys = Menu(my_menu)
my_menu.add_cascade(label="Semanais", menu=weeklys)
weeklys.add_command(label="dX", command=Teste2)

## Sobre ##

weeklys = Menu(my_menu)
my_menu.add_cascade(label="Semanais", menu=weeklys)
weeklys.add_command(label="dX", command=Teste2)

n2 = Frame(root, width=400, height=400, bg='yellow')
n = Frame(root, width=400, height=400, bg='red')

#### FreeTem Counter ####

my_label = Label(n2, text="HUM?")
my_label.place(x=500, y=0)

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


main_loop_thread = threading.Thread(target=app_main_loop, args=(my_label,))
main_loop_thread.daemon = True
main_loop_thread.start()

root.mainloop()
