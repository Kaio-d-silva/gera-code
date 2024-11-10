import tkinter as tk 
from tkinter import ttk
from tkinter import *
from handlers import validate_input, save_data

class App():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("gerador de projetos")
        
        self.creat_widgets()
        
    def creat_widgets(self):
        # Primeira label
        self.label_entry = Label(self.window, text="Digite o nome do projeto sem espaços e acentuação:")
        self.label_entry.pack(pady=5)
        
        # Entrada o usuario
        self.language_entry = Entry()
        self.language_entry.pack(pady=5)

        # Segunda label
        self.label_select_langue = Label(self.window, text="selecione uma linguagem")
        self.label_select_langue.pack(pady=5)

        # Seleção da linguagem
        self.check_box = ttk.Combobox(self.window, values=["Python","Node"])
        self.check_box.pack(pady=5) 

        # Botão Enviar
        self.send_buton = Button(self.window, text="Enviar", command=self.display_route)
        self.send_buton.pack(pady=5)

        # Botão salvar
        self.generate_button = Button(self.window, text="Gerar", command=self.generate_project)
        self.generate_button.pack(pady=5)
        
         # terceira label teste
        self.result_label = Label(self.window,text="")
        self.result_label.pack(pady=5)

        
    def run(self):
        self.window.mainloop()
        
    def generate_project(self):
        name = self.language_entry.get()
        language = self.check_box.get()
        
        if validate_input(name):
            diretorio = save_data(name, language)
        
        
    def display_route(self):
        name = self.language_entry.get()
        language = self.check_box.get()
        
        if validate_input(name):
            self.result_label.config(text=f"{name}, {language}")
        else:
            self.result_label.config(text="Nome invalido")

                
            
            
