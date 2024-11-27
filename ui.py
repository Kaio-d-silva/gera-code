import tkinter as tk 
from tkinter import ttk, filedialog, Checkbutton, Label, Entry, Button
from handlers import validate_input, save_data
from comand_bash import open_vscode
from subprocess import PIPE, Popen
from maneger_dir import get_path_directory

class App():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("gerador de projetos")
        
        self.creat_widgets()
        
    def creat_widgets(self):
        # Primeira label
        self.label_entry = Label(self.window, text="Digite o nome do projeto sem espaços e acentuação:")
        self.label_entry.grid(row=0, column=0, columnspan=7)
        
        # Entrada o usuario
        self.language_entry = Entry()
        self.language_entry.grid(row=1, column=2, columnspan=2, pady=5)
        
        # label rota
        self.rota = Label(self.window, text="")    
        self.rota.grid(row=1, column=1,pady=5)

        # selecionar rota
        self.botao_de_selecao = Button(self.window, text="localizar", command=self.select_path)
        self.botao_de_selecao.grid(row=2, column=2,columnspan=2, pady=5)       
        
       
        # Segunda label
        self.label_select_langue = Label(self.window, text="selecione uma linguagem")
        self.label_select_langue.grid(row=3, column=2, columnspan=2)

        # Seleção da linguagem
        self.select_box = ttk.Combobox(self.window, values=["Python","Node"])
        self.select_box.grid(row=4, columnspan=2, column=2) 
        self.select_box.bind("<<ComboboxSelected>>", self.select_libraries)
        
        
        # Seleção de biblioteca
        self.check_box = Checkbutton(self.window, text="Tkinter ?", onvalue=1, offvalue=0)
        self.check_box.grid(column=4, row=4)
        self.check_box.grid_forget()

        # Botão Enviar
        self.send_buton = Button(self.window, text="Enviar", command=self.display_route)
        self.send_buton.grid(row=5, column=2, padx=2, pady=5)

        # Botão salvar
        self.generate_button = Button(self.window, text="Gerar", command=self.generate_project)
        self.generate_button.grid(row=5, column=3, padx=2, pady=5)
        
        # terceira label teste
        self.result_label = Label(self.window,text="")
        self.result_label.grid(row=6, column=2, columnspan=2)
        
        # tela de saida do terminal
        self.bash_output = tk.Text(self.window, height=10, width=80)
        self.bash_output.grid(row=7, column=0, columnspan=7)
        self.get_default_directory()

        
    def run(self):
        self.window.mainloop()
        
    def generate_project(self):
        name_project = self.language_entry.get()
        language = self.select_box.get()
        libs_language = self.check_box.getboolean
        
        if validate_input(name_project):
            self.run_bash("sudo apt-get update -y && sudo apt-get upgrade -y")
            path_full_new_project = save_data(name_project, language, self.path_project, libs_language)
            mensage = f"Projeto foi criado em {path_full_new_project}"
            self.result_label.config(text=mensage)
            open_vscode(path_full_new_project)
        else:
            self.result_label.config(text="Erro : Nome invalido")
            
        
    def display_route(self):
        name = self.language_entry.get()
        language = self.select_box.get()
        
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
        self.path_project = filedialog.askdirectory()
        self.rota.config(text=self.path_project)           
        # path_projeto = "home/projetos"
    
    def get_default_directory(self):
        self.path_project = get_path_directory()
        self.rota.config(text=self.path_project)           
        
    def select_libraries(self, event):
        if self.select_box.get() == "Python":
            self.check_box.grid(column=4, row=4, columnspan=2)
        else: 
            self.check_box.grid_forget()
        