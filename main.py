from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox  # Versão? Popup de Koish? Pop up de Contador FreeTem/Luma?
import pyglet
from tkinter import ttk

# Custom Font

pyglet.font.add_file("Font/Temfont-Regular.ttf")


# Main
root = Tk()
root.title('Temtas by Rusp')
root.iconbitmap('Soulbound.ico')
root.geometry("1200x800")

# Creating Tabs
notebook = ttk.Notebook(root)  # Creating Tabs
notebook.grid(row=0, column=0)

visaoGeral = Frame(notebook, width=1200, height=800)  # Check List, foto do Koish semanal, Saipark(?), Melhor atividade/pansun?
breedProject = Frame(notebook, width=1200, height=800)  # Template para projetos, últimos projetos, lucros e etc (Temporizador?)
digiLair = Frame(notebook, width=1200, height=800)  # WinRate, e mais algumas coisas que derem vontade
freeTem = Frame(notebook, width=1200, height=800)  # Temporizador + Contador, colocar os valores só pelo roleplay
Koish = Frame(notebook, width=1200, height=800)  # Foto do Koish, prêmios, contador, temporizador?
Lairs = Frame(notebook, width=1200, height=800)  # Anak, Sacred Lake, 3rd Mythical, prêmios
lumaTempedia = Frame(notebook, width=1200, height=800)  # Radares,Penas gastas, último luma/data, db das lumas
tamersParadise = Frame(notebook, width=1200, height=800)  # Win rate, penas por atividade, melhor atividade por penas
Pvp = Frame(notebook, width=1200, height=800)  # Win rate, vídeo, talvez análise da partida?

visaoGeral.pack(fill="both", expand=1)
breedProject.pack(fill="both", expand=1)
digiLair.pack(fill="both", expand=1)
freeTem.pack(fill="both", expand=1)
Koish.pack(fill="both", expand=1)
Lairs.pack(fill="both", expand=1)
lumaTempedia.pack(fill="both", expand=1)
tamersParadise.pack(fill="both", expand=1)
Pvp.pack(fill="both", expand=1)

notebook.add(visaoGeral, text="Visão Geral")
notebook.add(breedProject, text="Breed Project")
notebook.add(digiLair, text="Digi Lair")
notebook.add(freeTem, text="FreeTem")
notebook.add(Koish, text="Koish")
notebook.add(Lairs, text="Lairs")
notebook.add(lumaTempedia, text="Luma Tempedia")
notebook.add(tamersParadise, text="Tamers Paradise")
notebook.add(Pvp, text="PvP")

# Visão Geral

#  Funções
#  Navigate*

#  Template

temtemLogo = ImageTk.PhotoImage(Image.open("Images/temtemlogo.png"))
logoCentral = Label(visaoGeral, image=temtemLogo).grid(row=0, column=0)



root.mainloop()
