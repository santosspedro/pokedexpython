from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from dados import *
import random

#cores

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha
co6 = "#993399" # Roxa
co7 = "#210B61" #Roxo escuro
co8 = "#14b8b8" #ciano
co9 = "#964b00" #marrom
co10 = "#008000" #verde

# janela

janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#frame

frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

def trocar_pokemon(i):
    global img_pk, pk_img

    #trocar cor do fundo do frame

    frame_pokemon['bg'] = pokemon[i]['Tipo'][3]

    #tipo do pokemon
    pk_name['text']=i
    pk_name['bg'] = pokemon[i]['Tipo'][3]
    pk_tipo['text']= pokemon[i]['Tipo'][1]
    pk_tipo['bg'] = pokemon[i]['Tipo'][3]
    pk_id['text']= pokemon[i]['Tipo'][0]
    pk_id['bg'] = pokemon[i]['Tipo'][3]

    img_pk = pokemon[i]['Tipo'][2]

    # ilustração pokemon

    img_pk = Image.open(img_pk)
    img_pk = img_pk.resize((238, 238))
    img_pk = ImageTk.PhotoImage(img_pk)

    pk_img = Label(frame_pokemon, image=img_pk, relief='flat', anchor=CENTER, bg=pokemon[i]['Tipo'][3], fg=co1)
    pk_img.place(x=60, y=50)

    pk_tipo.lift()

    #pk status

    pk_hp['text'] = pokemon[i]['Status'][0]
    pk_at['text'] = pokemon[i]['Status'][1]
    pk_df['text'] = pokemon[i]['Status'][2]
    pk_vl['text'] = pokemon[i]['Status'][3]
    pk_tt['text'] = pokemon[i]['Status'][4]

    #habilidades
    pk_hb1['text'] = pokemon[i]['Habilidades'][0]
    pk_hb2['text'] = pokemon[i]['Habilidades'][1]

#frame nome
pk_name = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=co1)
pk_name.place(x=12, y=15)

#frame tipo
pk_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 10'), bg =co7, fg=co1)
pk_tipo.place(x=12, y=50)

#frame id
pk_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Tvy 10 bold'), bg =co1, fg=co1)
pk_id.place(x=12, y=75)


# status
pk_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg =co1, fg=co0)
pk_status.place(x=15, y=310)

#hp
pk_hp = Label(janela, text='HP: 60', relief='flat', anchor=CENTER, font=('Verdana 10'), bg =co1, fg=co4)
pk_hp.place(x=15, y=350)

#ataque
pk_at = Label(janela, text='ATAQUE: 65', relief='flat', anchor=CENTER, font=('Verdana 10'), bg =co1, fg=co4)
pk_at.place(x=15, y=370)

#defesa
pk_df = Label(janela, text='DEFESA: 60', relief='flat', anchor=CENTER, font=('Verdana 10'), bg =co1, fg=co4)
pk_df.place(x=15, y=390)

#velocidade
pk_vl = Label(janela, text='VELOCIDADE: 110', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pk_vl.place(x=15, y=410)

#total
pk_tt = Label(janela, text='TOTAL: 295', relief='flat', anchor=CENTER, font=('Verdana 15'), bg=co1, fg=co5)
pk_tt.place(x=15, y=430)

# habilidades
pk_skill = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg =co1, fg=co0)
pk_skill.place(x=150, y=310)

# habilidades
pk_hb1 = Label(janela, text='Cursed Body', relief='flat', anchor=CENTER, font=('Verdana 10'), bg =co1, fg=co0)
pk_hb1.place(x=150, y=350)

pk_hb2 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg =co1, fg=co0)
pk_hb2.place(x=150, y=370)


# criando botões

#Gengar

img_pk_1 = Image.open('mini sprite/_094___gengar_by_briannabellerose_ddfctcm.png')
img_pk_1 = img_pk_1.resize((40, 40))
img_pk_1 = ImageTk.PhotoImage(img_pk_1)

b1_pk_img = Button(janela, command=lambda: trocar_pokemon('Gengar'), image=img_pk_1, text='Gengar', width=150 , relief= 'raised', overrelief=RIDGE, compound=LEFT,  anchor=NW, padx=5, font=("Verdana 12"), bg =co1, fg=co0)
b1_pk_img.place(x=370, y=10)

#Blastoise
img_pk_2 = Image.open('sprites/blastoise.png')
img_pk_2 = img_pk_2.resize((40, 40))
img_pk_2 = ImageTk.PhotoImage(img_pk_2)

b2_pk_img = Button(janela, command=lambda: trocar_pokemon('Blastoise'),image=img_pk_2, text='Blastoise', width=150 , relief= 'raised', overrelief=RIDGE, compound=LEFT,  anchor=NW, padx=5, font=("Verdana 12"), bg =co1, fg=co0)
b2_pk_img.place(x=370, y=60)

#Dragonite
img_pk_3 = Image.open('sprites/dragonite.png')
img_pk_3 = img_pk_3.resize((40, 40))
img_pk_3 = ImageTk.PhotoImage(img_pk_3)

b3_pk_img = Button(janela,command=lambda: trocar_pokemon('Dragonite'), image=img_pk_3, text='Dragonite', width=150 , relief= 'raised', overrelief=RIDGE, compound=LEFT,  anchor=NW, padx=5, font=("Verdana 12"), bg =co1, fg=co0)
b3_pk_img.place(x=370, y=110)

#Rayquaza

img_pk_4 = Image.open('sprites/rayquaza.png')
img_pk_4 = img_pk_4.resize((40, 40))
img_pk_4 = ImageTk.PhotoImage(img_pk_4)

b4_pk_img = Button(janela,command=lambda: trocar_pokemon('Rayquaza'), image=img_pk_4, text='Rayquaza', width=150 , relief= 'raised', overrelief=RIDGE, compound=LEFT,  anchor=NW, padx=5, font=("Verdana 12"), bg =co1, fg=co0)
b4_pk_img.place(x=370, y=160)

#Tyranitar

img_pk_5 = Image.open('sprites/tyranitar.png')
img_pk_5 = img_pk_5.resize((40, 40))
img_pk_5 = ImageTk.PhotoImage(img_pk_5)

b5_pk_img = Button(janela,command=lambda: trocar_pokemon('Tyranitar'), image=img_pk_5, text='Tyranitar', width=150 , relief= 'raised', overrelief=RIDGE, compound=LEFT,  anchor=NW, padx=5, font=("Verdana 12"), bg =co1, fg=co0)
b5_pk_img.place(x=370, y=210)

#Chesnaught

img_pk_6 = Image.open('sprites/chesnaught.png')
img_pk_6 = img_pk_6.resize((40, 40))
img_pk_6 = ImageTk.PhotoImage(img_pk_6)

b6_pk_img = Button(janela,command=lambda: trocar_pokemon('Chesnaught'), image=img_pk_6, text='Chesnaught', width=150 , relief= 'raised', overrelief=RIDGE, compound=LEFT,  anchor=NW, padx=5, font=("Verdana 12"), bg =co1, fg=co0)
b6_pk_img.place(x=370, y=260)


lista = ["Gengar","Dragonite", "Rayquaza","Chesnaught","Tyranitar", "Blastoise"]
pk_random = random.sample(lista, 1)

trocar_pokemon(pk_random[0])


janela.mainloop()