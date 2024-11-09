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
    


window = tk.Tk()
window.title("Gerador de Proejto")
window.config(padx=50, pady=100)

# Primeira label
label_entry = Label(window, text="Digite o nome do projeto sem espaços e acentuação:")
label_entry.pack(pady=5)

# Entrada o usuario
language_entry = Entry()
language_entry.pack(pady=5)

# Segunda label
label_select_langue = Label(window, text="selecione uma linguagem")
label_select_langue.pack(pady=5)

# Seleção da linguagem
check_box = ttk.Combobox(window, values=["Python","Node"])
check_box.pack(pady=5) 

# Botão Enviar
send_buton = Button(window, text="Enviar", command=lambda : informa_rota(label= result_label,entrada=language_entry,selecao=check_box))
send_buton.pack(pady=5)

# terceira label teste
result_label = Label(window,text="")
result_label.pack(pady=5)

# Botão salvar
generate_button = Button(window, text="Gerar", command=gerar_projeto())
generate_button.pack(pady=5)





window.mainloop()

  
