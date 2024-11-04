import tkinter as tk
from tkinter import ttk
from tkinter import *


def teste():
    print("teste")



window = tk.Tk()
window.title("Gerador de Proejto")
window.config(padx=50, pady=100)

# Primeira label
label_entry = Label(window, text="Digite o nome do projeto sem espaços e acentuação:")
label_entry.grid(row=0,column=0)

# Entrada
project_entry = Entry()
project_entry.grid(row=1,column=0,columnspan=2)

# Segunda label
label_select_langue = Label(window, text="selecione uma linguagem")
label_select_langue.grid(row=2,column=0)

# Seleção da linguagem
teste = ttk.Combobox(window, values=["Python","Node"])
teste.grid(row=4, column=0, columnspan=2)

# Botão Enviar
botão_enviar = Button(window, text="Enviar", command=teste)
botão_enviar.grid(row=5, column=0)

# Botão salvar
botão_enviar = Button(window, text="Salvar", command=teste)
botão_enviar.grid(row=6, column=0)


window.mainloop()

  
