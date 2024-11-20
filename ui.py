import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from handlers import validate_input, save_data
from comand_bash import open_vscode
from subprocess import PIPE, Popen

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
        
        # teste rota
        self.rota = Label(self.window, text="")    
        self.rota.pack(ipady=5)

        # selecionar rota
        self.botao_de_selecao = Button(self.window, text="localizar", command=self.select_path)
        self.botao_de_selecao.pack(padx=5)        
        
       
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
        
        # tela de saida do terminal
        self.bash_output = tk.Text(self.window, height=10, width=80)
        self.bash_output.pack(pady=5)
        self.select_path()

        
    def run(self):
        self.window.mainloop()
        
    def generate_project(self):
        name_project = self.language_entry.get()
        language = self.check_box.get()
        
        if validate_input(name_project):
            self.run_bash("sudo apt-get update -y && sudo apt-get upgrade -y")
            path_full_new_project = save_data(name_project, language)
            mensage = f"Projeto foi criado em {path_full_new_project}"
            self.result_label.config(text=mensage)
            open_vscode(path_full_new_project)
        else:
            self.result_label.config(text="Erro : Nome invalido")
            
        
    def display_route(self):
        name = self.language_entry.get()
        language = self.check_box.get()
        
        if validate_input(name):
            self.result_label.config(text=f"{name}, {language}")
        else:
            self.result_label.config(text="Nome invalido")

    def run_bash(self, command):
        process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE) 
        stdout, stderr = process.communicate() 
        self.bash_output.delete(1.0, tk.END) 
        self.bash_output.insert(tk.END, stdout.decode()) 
        if stderr: 
            self.bash_output.insert(tk.END, stderr.decode())          
            
    def select_path(self):
        path_projeto = filedialog.askdirectory()
        self.rota.config(text=path_projeto)           
        # path_projeto = "home/projetos"
