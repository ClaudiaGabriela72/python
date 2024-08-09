import tkinter
from tkinter import *
from tkinter import ttk
#     cores     
cor0 = "#444466" #Preto
cor1 = "#feffff" #branco
cor2 = "#6f9fbd" #azul

fundo_dia = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb86d"

fundo = fundo_dia

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, column=1, ipadx=157)

# Frames
frame_top = Frame(janela, width=320, height=50, bg=fundo, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# configurando frame top place, overrlife
e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='raised')
e_local.place(x=15, y=10)
b_ent = Button(frame_top, text='Enter', bg="#feffff", fg="#6f9fbd", font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE )
b_ent.place(x=250, y=10)

# configurando frame corpo
l_cidade = Label(frame_corpo, text='Cabina - Angola / Africa', anchor='center', bg=fundo, fg="#6f9fbd", font=("Arial 14"), relief='raised' )
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text='09 03 2022 | 10:30:00 AM', anchor='center', bg=fundo, fg=, font=("Arial 10"))
l_data.place(x=10, y=54)

l_humidade = Label(frame_corpo, text='84', anchor='center', bg=fundo, fg=, font=("Arial 45"))
l_humidade.place(x=10, y=100)

l_h_simbol = Label(frame_corpo, text='%', anchor='center', bg=fundo, fg=, font=("Arial 10 bold"))
l_h_simbol.place(x=10, y=100)

l_h_nome = Label(frame_corpo, text='84', anchor='center', bg=fundo, fg=, font=("Arial 45"))
l_h_nome.place(x=10, y=100)




janela.mai_simbol