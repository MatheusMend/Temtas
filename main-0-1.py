from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, ttk, messagebox  # Versão? Popup de Koish? Pop up de Contador FreeTem/Luma?
import pyglet


#### Custom Font ####

pyglet.font.add_file("Font/Temfont-Regular.ttf")

#### Tkinter Root ####

root = Tk()
root.title('Temtas by Rusp v0.1')
root.iconbitmap('Soulbound.ico')
root.geometry("1200x800")

#### Ttk Notebook and Tabs ####

notebook = ttk.Notebook(root)  # Creating Tabs
notebook.grid(row=0, column=0)

resumoGeral = Frame(notebook)  # Resumo rápido de todas as atividades
Atividades = Frame(notebook, width=1200, height=800)
breedProject = Frame(notebook, width=1200, height=800)  # Template para projetos, últimos projetos, lucros e etc (Temporizador?)
digiLair = Frame(notebook, width=1200, height=800)  # WinRate, e mais algumas coisas que derem vontade
freeTem = Frame(notebook, width=1200, height=800)  # Temporizador + Contador, colocar os valores só pelo roleplay
Koish = Frame(notebook, width=1200, height=800)  # Foto do Koish, prêmios, contador, temporizador?
Lairs = Frame(notebook, width=1200, height=800)  # Anak, Sacred Lake, 3rd Mythical, prêmios
lumaTempedia = Frame(notebook, width=1200, height=800)  # Radares,Penas gastas, último luma/data, db das lumas
postalService = Frame(notebook, width=1200, height=800)  # Simulador de Sedex
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
postalService.pack(fill="both", expand=1)
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
notebook.add(postalService, text="Postal Service")
notebook.add(tamersParadise, text="Tamers Paradise")
notebook.add(Pvp, text="PvP")

####  Resumo Geral ####
# Check List (Postal Service, Dojo Rematch, Atividades Semanais, Foto do Koish Semanal, Contador FreeTem)
# Penas e Pansuns esperados para aquela semana, resumo do radar?
# Talvez mudar para resumo, por um resumo das atividades e criar uma aba atividades para as check lists(?)

temtemLogo = ImageTk.PhotoImage(Image.open("Images/temtemlogo.png"))
logoCentral = Label(resumoGeral, image=temtemLogo)
logoCentral.place(x=500, y=30)

Feathericon = ImageTk.PhotoImage(Image.open("Images/Feather.png"))
Novaicon = ImageTk.PhotoImage(Image.open("Images/Nova.png"))
Pansunicon = ImageTk.PhotoImage(Image.open("Images/Pansun.png"))

#  Funções

#  Navigate*

#### Diárias/Semanais ####
# Postal Service, Dojo Rematch, ArchTamers, Free Token Tamers Paradise, Free Tem, Weekly Koish
# Battle pass weekly missions, Mythical Lairs, Pansuns e Penas esperadas para a semana (baseado na média das atividades)

## Postal Service

PostalFeather = Label(Atividades, image=Feathericon)
PostalPansun = Label(Atividades, image=Pansunicon)
PackagesPostalService = Label(Atividades, image="")

PostalFeather.place(x=50, y=260)
PostalPansun.place(x=50, y=305)

postalServiceVar1 = IntVar()
postalServiceVar2 = IntVar()
postalServiceVar3 = IntVar()
postalServiceVar4 = IntVar()
postalServiceVar5 = IntVar()
postalServiceVar6 = IntVar()
postalServiceVar7 = IntVar()

postalServiceLabel = Label(Atividades, text="Postal Service", font=("Temfont", 25))
postalServiceLabel.place(x=0, y=0)

postalDay1 = Checkbutton(Atividades, text="Segunda", variable=postalServiceVar1, font=("Arial", 12))
postalDay2 = Checkbutton(Atividades, text="Terça", variable=postalServiceVar2, font=("Arial", 12))
postalDay3 = Checkbutton(Atividades, text="Quarta", variable=postalServiceVar3, font=("Arial", 12))
postalDay4 = Checkbutton(Atividades, text="Quinta", variable=postalServiceVar4, font=("Arial", 12))
postalDay5 = Checkbutton(Atividades, text="Sexta", variable=postalServiceVar5, font=("Arial", 12))
postalDay6 = Checkbutton(Atividades, text="Sábado", variable=postalServiceVar6, font=("Arial", 12))
postalDay7 = Checkbutton(Atividades, text="Domingo", variable=postalServiceVar7, font=("Arial", 12))

postalDay1.place(x=50, y=50)
postalDay2.place(x=50, y=80)
postalDay3.place(x=50, y=110)
postalDay4.place(x=50, y=140)
postalDay5.place(x=50, y=170)
postalDay6.place(x=50, y=200)
postalDay7.place(x=50, y=230)

## Dojo Rematch

FeathersDojoRematch = Label(Atividades, image=Pansunicon)
PansunsDojoRematch = Label(Atividades, image=Feathericon)

FeathersDojoRematch.place(x=50, y=650)
PansunsDojoRematch.place(x=50, y=695)

DojoRematchVar1 = IntVar()
DojoRematchVar2 = IntVar()
DojoRematchVar3 = IntVar()
DojoRematchVar4 = IntVar()
DojoRematchVar5 = IntVar()
DojoRematchVar6 = IntVar()
DojoRematchVar7 = IntVar()
DojoRematchVar8 = IntVar()

DojoRematchLabel = Label(Atividades, text="Dojo Rematch", font=("Temfont", 25))
DojoRematchLabel.place(x=0, y=360)

DojoRematch1 = Checkbutton(Atividades, text="Arissola", variable=DojoRematchVar1, font=("Arial", 12))
DojoRematch2 = Checkbutton(Atividades, text="Nanga 1", variable=DojoRematchVar1, font=("Arial", 12))
DojoRematch3 = Checkbutton(Atividades, text="Nanga 2", variable=DojoRematchVar1, font=("Arial", 12))
DojoRematch4 = Checkbutton(Atividades, text="Tucma", variable=DojoRematchVar1, font=("Arial", 12))
DojoRematch5 = Checkbutton(Atividades, text="Vumbi", variable=DojoRematchVar1, font=("Arial", 12))
DojoRematch6 = Checkbutton(Atividades, text="Neoedo", variable=DojoRematchVar1, font=("Arial", 12))
DojoRematch7 = Checkbutton(Atividades, text="Properton", variable=DojoRematchVar1, font=("Arial", 12))
DojoRematch8 = Checkbutton(Atividades, text="Lochburg", variable=DojoRematchVar1, font=("Arial", 12))

DojoRematch1.place(x=50, y=410)
DojoRematch2.place(x=50, y=440)
DojoRematch3.place(x=50, y=470)
DojoRematch4.place(x=50, y=500)
DojoRematch5.place(x=50, y=530)
DojoRematch6.place(x=50, y=560)
DojoRematch7.place(x=50, y=590)
DojoRematch8.place(x=50, y=620)

## TemPass weeklys (Não dá pra peder novas, né?)

ParadiseFeather = Label(Atividades, image=Feathericon)
ParadiseNova = Label(Atividades, image=Novaicon)

ParadiseFeather.place(x=350, y=140)
ParadiseNova.place(x=350, y=185)

ParadiseVar1 = IntVar()
ParadiseVar2 = IntVar()
ParadiseVar3 = IntVar()
ParadiseVar4 = IntVar()

tamersParadise = Label(Atividades, text="Tamers Paradise", font=("Temfont", 25))
tamersParadise.place(x=300, y=0)

Paradise1 = Checkbutton(Atividades, text="Arch Tamers", variable=ParadiseVar1, font=("Arial", 12))
Paradise2 = Checkbutton(Atividades, text="Battle Pass missions", variable=ParadiseVar3, font=("Arial", 12))
Paradise3 = Checkbutton(Atividades, text="Free Weekly Token", variable=ParadiseVar2, font=("Arial", 12))


Paradise1.place(x=350, y=50)
Paradise2.place(x=350, y=80)
Paradise3.place(x=350, y=110)


## Koish of the Week - CheckBox 4/5, 5/5

def weeklykoish():  # Feito pensando em uma imagem de Koish com as dimensões (720x570)
    global koishdaSemana
    Koish.filename = filedialog.askopenfilename(initialdir="/", title="Koish da semana",
                                                filetypes=(("Imagem Png", "*.png"), ("Outros Arquivos", "*.*")))
    koishdaSemana = ImageTk.PhotoImage(Image.open(Koish.filename))
    koishdaSemanaLabel = Label(Atividades, image=koishdaSemana)
    koishdaSemanaLabel.place(x=530, y=0)


KoishButton = Button(Atividades, text="Imagem do Koish dessa semana", command=weeklykoish)
KoishButton.place(x=800, y=580)

## FreeTem Count

FreeFeather = Label(Atividades, image=Feathericon)
FreePansun = Label(Atividades, image=Pansunicon)

FreeFeather.place()
FreePansun.place()

# Counter
FreeTem = 0

def agooddaytobeattem():
    global FreeTem
    FreeTem += 1
    FreeLabel.config(text=str(FreeTem))


FreeLabel = Label(Atividades, text='0')
FreeCounter = Button(Atividades, text="+", command= lambda:agooddaytobeattem())
FreeLabel.place(x=800, y=0)
FreeCounter.place(x=900, y=0)

## 2x Mythical Lair

LairFeather = Label(Atividades, image=Feathericon)

LairFeather.place()

LairVar1 = IntVar()
LairVar2 = IntVar()

Lair1 = Checkbutton(Atividades, text="Tyranak", variable=LairVar1, font=("Arial", 12))
Lair2 = Checkbutton(Atividades, text="Volgon", variable=LairVar2, font=("Arial", 12))

Lair1.place()
Lair2.place()

## Pansun e Penas semanais, baseados na checklist*

root.mainloop()
