from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox  # Versão? Popup de Koish? Pop up de Contador FreeTem/Luma?
import pyglet
from tkinter import ttk

# Custom Font

pyglet.font.add_file("Font/Temfont-Regular.ttf")

#### Main ####

root = Tk()
root.title('Temtas by Rusp')
root.iconbitmap('Soulbound.ico')
root.geometry("1200x800")

#### Creating Tabs ####

notebook = ttk.Notebook(root)  # Creating Tabs
notebook.grid(row=0, column=0)

resumoGeral = Frame(notebook, width=1200, height=800)  # Resumo rápido de todas as atividades
Atividades = Frame(notebook, width=1200, height=800)
breedProject = Frame(notebook, width=1200, height=800)  # Template para projetos, últimos projetos, lucros e etc (Temporizador?)
digiLair = Frame(notebook, width=1200, height=800)  # WinRate, e mais algumas coisas que derem vontade
freeTem = Frame(notebook, width=1200, height=800)  # Temporizador + Contador, colocar os valores só pelo roleplay
Koish = Frame(notebook, width=1200, height=800)  # Foto do Koish, prêmios, contador, temporizador?
Lairs = Frame(notebook, width=1200, height=800)  # Anak, Sacred Lake, 3rd Mythical, prêmios
lumaTempedia = Frame(notebook, width=1200, height=800)  # Radares,Penas gastas, último luma/data, db das lumas
tamersParadise = Frame(notebook, width=1200, height=800)  # Win rate, penas por atividade, melhor atividade por penas
Pvp = Frame(notebook, width=1200, height=800)  # Win rate, vídeo, talvez análise da partida?

resumoGeral.pack(fill="both", expand=1)
Atividades.pack(fill="both", expand=1)
breedProject.pack(fill="both", expand=1)
digiLair.pack(fill="both", expand=1)
freeTem.pack(fill="both", expand=1)
Koish.pack(fill="both", expand=1)
Lairs.pack(fill="both", expand=1)
lumaTempedia.pack(fill="both", expand=1)
tamersParadise.pack(fill="both", expand=1)
Pvp.pack(fill="both", expand=1)

notebook.add(resumoGeral, text="Resumo Geral")
notebook.add(Atividades, text="Atividades Diárias/Semanais")
notebook.add(breedProject, text="Breed Project")
notebook.add(digiLair, text="Digi Lair")
notebook.add(freeTem, text="FreeTem")
notebook.add(Koish, text="Koish")
notebook.add(Lairs, text="Lairs")
notebook.add(lumaTempedia, text="Luma Tempedia")
notebook.add(tamersParadise, text="Tamers Paradise")
notebook.add(Pvp, text="PvP")

####  Resumo Geral ####
# Check List (Postal Service, Dojo Rematch, Atividades Semanais, Foto do Koish Semanal, Contador FreeTem)
# Penas e Pansuns esperados para aquela semana, resumo do radar?
# Talvez mudar para resumo, por um resumo das atividades e criar uma aba atividades para as check lists(?)

temtemLogo = ImageTk.PhotoImage(Image.open("Images/temtemlogo.png"))
logoCentral = Label(resumoGeral, image=temtemLogo, anchor=CENTER).grid(row=0, column=0, columnspan=15)

#  Funções

#  Navigate*

#### Diárias/Semanais ####
# CheckBox, Diárias/Semanais, Koish, FreeTem, Pansuns e penas espedradas para semana (marcando check box)

# Postal Service Checkboxs

postalServiceVar1 = IntVar()
postalServiceVar2 = IntVar()
postalServiceVar3 = IntVar()
postalServiceVar4 = IntVar()
postalServiceVar5 = IntVar()
postalServiceVar6 = IntVar()
postalServiceVar7 = IntVar()

postalServiceLabel = Label(Atividades, text="Postal Service", font="Temfont")
postalServiceLabel.grid(row=1, column=0)

postalDay1 = Checkbutton(Atividades, text="Segunda", variable=postalServiceVar1, anchor=W)
postalDay2 = Checkbutton(Atividades, text="Terça", variable=postalServiceVar2, anchor=W)
postalDay3 = Checkbutton(Atividades, text="Quarta", variable=postalServiceVar3, anchor=W)
postalDay4 = Checkbutton(Atividades, text="Quinta", variable=postalServiceVar4, anchor=W)
postalDay5 = Checkbutton(Atividades, text="Sexta", variable=postalServiceVar5, anchor=W)
postalDay6 = Checkbutton(Atividades, text="Sábado", variable=postalServiceVar6, anchor=W)
postalDay7 = Checkbutton(Atividades, text="Domingo", variable=postalServiceVar7, anchor=W)

postalDay1.grid(row=2, column=0)
postalDay2.grid(row=3, column=0)
postalDay3.grid(row=4, column=0)
postalDay4.grid(row=5, column=0)
postalDay5.grid(row=6, column=0)
postalDay6.grid(row=7, column=0)
postalDay7.grid(row=8, column=0)

# Dojo Rematch

DojoRematchVar1 = IntVar()
DojoRematchVar2 = IntVar()
DojoRematchVar3 = IntVar()
DojoRematchVar4 = IntVar()
DojoRematchVar5 = IntVar()
DojoRematchVar6 = IntVar()
DojoRematchVar7 = IntVar()
DojoRematchVar8 = IntVar()

DojoRematchLabel = Label(Atividades, text="Dojo Rematch", font="Temfont")
DojoRematchLabel.grid(row=9, column=0)

DojoRematch1 = Checkbutton(Atividades, text="Arissola", variable=DojoRematchVar1, anchor=W)
DojoRematch2 = Checkbutton(Atividades, text="Nanga 1", variable=DojoRematchVar1, anchor=W)
DojoRematch3 = Checkbutton(Atividades, text="Nanga 2", variable=DojoRematchVar1, anchor=W)
DojoRematch4 = Checkbutton(Atividades, text="Tucma", variable=DojoRematchVar1, anchor=W)
DojoRematch5 = Checkbutton(Atividades, text="Vumbi", variable=DojoRematchVar1, anchor=W)
DojoRematch6 = Checkbutton(Atividades, text="Neoedo", variable=DojoRematchVar1, anchor=W)
DojoRematch7 = Checkbutton(Atividades, text="Properton", variable=DojoRematchVar1, anchor=W)
DojoRematch8 = Checkbutton(Atividades, text="Lochburg", variable=DojoRematchVar1, anchor=W)

DojoRematch1.grid(row=10, column=0)
DojoRematch2.grid(row=11, column=0)
DojoRematch3.grid(row=12, column=0)
DojoRematch4.grid(row=13, column=0)
DojoRematch5.grid(row=14, column=0)
DojoRematch6.grid(row=15, column=0)
DojoRematch7.grid(row=16, column=0)
DojoRematch8.grid(row=17, column=0)

# Weekly Checklist - TemPass weeklys (Não dá pra peder novas, né?)

# Koish of the Week

# FreeTem Count

# Pansun e Penas semanais, baseados na checklist*

root.mainloop()
