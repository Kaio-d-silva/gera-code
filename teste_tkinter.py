import tkinter as tk
from tkinter import ttk
from tkinter import *

def gerar_projeto():
    ...

def valida_input(input):
    return input.isalnum()
    ...
def informa_rota(label,entrada,selecao):
    nome = entrada.get()
    linguagem = selecao.get()
    
    if valida_input(nome):
        label.config(text=f"{nome}, {linguagem}")
    else:
        label.config(text="Nome invalido")

# def enviar():
#     nome = project_entry.get()
#     linguagem = project_entry.get()
    
    


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

# terceira label teste
label_teste = Label(window,text="")
label_teste.grid(row=7,column=0)

# Seleção da linguagem
caixa_de_selecao = ttk.Combobox(window, values=["Python","Node"])
caixa_de_selecao.grid(row=4, column=0, columnspan=2)

# Botão Enviar
botão_enviar = Button(window, text="Enviar", command=lambda : informa_rota(label= label_teste,entrada=project_entry,selecao=caixa_de_selecao))
botão_enviar.grid(row=5, column=0)

# Botão salvar
botão_enviar = Button(window, text="Gerar", command=gerar_projeto())
botão_enviar.grid(row=6, column=0)


window.mainloop()

  
