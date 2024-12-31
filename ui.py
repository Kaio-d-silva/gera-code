# import tkinter as tk 
from tkinter import ttk, filedialog, Checkbutton, Label, Entry, Button, messagebox, END, Text, Tk
from handlers import validate_input, save_data
from comand_bash import open_vscode
from subprocess import PIPE, Popen
from maneger_dir import get_path_directory

class App():
    def __init__(self):
        self.window = Tk()
        self.window.title("gerador de projetos")
        
        self.creat_widgets()
        
    def creat_widgets(self):
        # self.window.geometry("500x500")
        
        # label seleção da linguagem
        self.label_select_langue = Label(self.window, text="selecione uma linguagem")
        self.label_select_langue.grid(row=0, column=0, columnspan=2)
        
        # Seleção da linguagem
        self.select_box = ttk.Combobox(self.window, values=["Python","Node"])
        self.select_box.grid(row=1, columnspan=2, column=0) 
        self.select_box.bind("<<ComboboxSelected>>", self.select_libraries)
        
        # Seleção de biblioteca
        self.check_box = Checkbutton(self.window, text="Tkinter ?", onvalue=1, offvalue=0,width=10)
        self.check_box.grid(row=1, column=3)
        self.check_box.grid_forget()

        # label titulo
        self.label_entry = Label(self.window, text="Digite o nome do projeto")
        self.label_entry.grid(row=2, column=0, columnspan=2)
        
        # Entrada o usuario - nome do projeto
        self.name_project_entry = Entry(self.window)
        self.name_project_entry.grid(row=3, column=0, columnspan=2, pady=5)
        
        # Botão validar
        self.validate_buton = Button(self.window, text="Validar", command=self.display_route)
        self.validate_buton.grid(row=4, column=0, columnspan=2, padx=2, pady=5)
        
        # # label rota
        # self.path = Label(self.window, text="")    
        # self.path.grid(row=6, column=0,pady=5)

        # label localizar pasta
        self.find_path = Label(self.window, text="escolha onde o projeto sera gerado")
        self.find_path.grid(row=6, column=0, columnspan=2)
        
        # entrada localiza pasta
        self.path_entry = Entry(self.window)
        self.path_entry.grid(row=7, column=0, columnspan=2, pady=5)

        # selecionar rota
        self.find_button = Button(self.window, text="localizar", command=self.select_path)
        self.find_button.grid(row=8, column=0,columnspan=2, pady=5)       
        
        # Botão gerar
        self.generate_button = Button(self.window, text="Gerar Projeto", command=self.generate_project)
        self.generate_button.grid(row=9, column=0, columnspan=2,pady=5)
        
        # valida nome do projeto
        # self.result_label = Label(self.window,text="")
        # self.result_label.grid(row=6, column=2, columnspan=2)
        
        # tela de saida do terminal
        self.bash_output = Text(self.window, width=30)
        self.bash_output.grid(row=0, column=4, rowspan=13)
        
        # mostra diretorios padrao
        self.get_default_directory()

        
    def run(self):
        self.window.mainloop()
        
    def generate_project(self):
        name_project = self.name_project_entry.get()
        language = self.select_box.get()
        libs_language = self.check_box.getboolean
        
        menssage = f"Seu projeto sera gerado em '/{self.path_project}/{name_project}'" 
        resposta = messagebox.askokcancel("Gerar projeto",menssage)
        if resposta:
            if validate_input(name_project):
                # self.run_bash("sudo apt-get update -y && sudo apt-get upgrade -y")
                path_full_new_project = save_data(name_project, language, self.path_project, libs_language)
                menssage = f"Projeto foi criado em {path_full_new_project}"
                # self.result_label.config(text=mensage)
                messagebox.showinfo("Informações",menssage)
                open_vscode(path_full_new_project)
            else:
                messagebox.showerror("Não gerado", "ERRO : Nome ou linguagem invalidos")
                # self.result_label.config(text="Erro : Nome invalido")
            
        
    def display_route(self):
        name = self.name_project_entry.get()
        language = self.select_box.get()
        message_output = f"{name}, {language}"
        
        
        if len(name) == 0:
            messagebox.showerror(title="INVALIDO", message="O nome do projeto\nnão pode ser vazio")
        elif len(language) == 0:
            messagebox.showerror(title="INVALIDO", message="Selecione uma linguagem")
            
        elif validate_input(name):
            messagebox.showinfo(title="Informações", message=f"       *** Tudo certo ***\nescolha onde o projeto sera gerado")
            # self.result_label.config(text=f"{name}, {language}") 
        else:
            print(len(message_output))
            messagebox.showerror(title="INVALIDO", message="O nome do projeto não deve\n ter espaços e nem acentos")
            # self.result_label.config(text="Nome invalido")

    def run_bash(self, command):
        process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE) 
        stdout, stderr = process.communicate() 
        self.bash_output.delete(1.0, END) 
        self.bash_output.insert(END, stdout.decode()) 
        if stderr: 
            self.bash_output.insert(END, stderr.decode())          
            
    def select_path(self):
        self.path_project = filedialog.askdirectory()
        self.path_entry.delete(0,END)
        self.path_entry.insert(0, self.path_project)           
        # path_projeto = "home/projetos"
    
    def get_default_directory(self):
        self.path_project = get_path_directory()
        # self.rota.config(text=self.path_project) 
        self.path_entry.insert(0,self.path_project)
                  
        
    def select_libraries(self, event):
        if self.select_box.get() == "Python":
            self.check_box.grid(column=2, row=1, columnspan=2)
        else: 
            self.check_box.grid_forget()
        
