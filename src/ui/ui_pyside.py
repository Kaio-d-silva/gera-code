from PySide6.QtWidgets import QFileDialog, QCheckBox, QTextBrowser,QComboBox ,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox, QInputDialog
from handlers.handlers import validate_input, save_data
from bash.comand_bash import open_vscode
from subprocess import PIPE, Popen
from handlers.maneger_dir import get_path_directory



class GeradorDeProjetos(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gerador de Projetos')
        self.layout_principal = QHBoxLayout()
        self.setGeometry(100,100, 300, 100)
        
         # Adiciona formulario ao layout principal
        self.layout_principal.addLayout(self.criar_formulario())
        self.layout_principal.addLayout(self.exibe_dados())
        
        # Define layout principal
        self.setLayout(self.layout_principal)
        self.get_default_directory()
            
    def criar_formulario(self):
        # Cria Formulario 
        layout_form = QVBoxLayout()
        
        # Label Combobox
        layout_label = QHBoxLayout()
        label_linguagem = QLabel("Selecione uma linguagem")
        layout_label.addStretch()
        layout_label.addWidget(label_linguagem)
        layout_label.addStretch()
        layout_form.addLayout(layout_label)
        
        # Combobox 
        self.layout_combobox = QHBoxLayout()
        self.combobox = QComboBox()
        self.combobox.addItems(["JavaScript","Python"])
        self.combobox.currentIndexChanged.connect(self.verifica_combobox)
        self.layout_combobox.addWidget(self.combobox)
        layout_form.addLayout(self.layout_combobox)
        
        # Label input
        layout_label_nome = QHBoxLayout()
        label_input_nome = QLabel("Digite o nome do projeto")
        layout_label_nome.addStretch()
        layout_label_nome.addWidget(label_input_nome)
        layout_label_nome.addStretch()
        layout_form.addLayout(layout_label_nome)
        
        
        # Input nome do projeto
        self.input_nome_projeto = QLineEdit()
        layout_form.addWidget(self.input_nome_projeto)
        
        # Botão validar
        botao_validar = QPushButton("Validar")
        botao_validar.clicked.connect(self.display_route)
        layout_form.addWidget(botao_validar)
        
        # Label rota projeto
        layout_label_rota = QHBoxLayout()
        label_input_rota = QLabel("Escolha onde o projeto sera gerado")
        layout_label_rota.addStretch()
        layout_label_rota.addWidget(label_input_rota)
        layout_label_rota.addStretch()
        layout_form.addLayout(layout_label_rota)
        
        # Input rota do projeto
        self.input_rota = QLineEdit()
        layout_form.addWidget(self.input_rota)
        
        
        # Botão localizar
        botao_localizar = QPushButton("Localizar")
        botao_localizar.clicked.connect(self.select_path)
        layout_form.addWidget(botao_localizar)
        
        # Botão Gerar Projeto
        botao_gerar_projeto = QPushButton("Gerar Projeto")
        botao_gerar_projeto.clicked.connect(self.generate_project)
        layout_form.addWidget(botao_gerar_projeto)
        
        return layout_form
        
       
    def exibe_dados(self):
        layout_quadro = QVBoxLayout()
        self.quadro = QTextBrowser()
        layout_quadro.addWidget(self.quadro)
        return layout_quadro
        
    def atualizar_label(self):
        print("teste")
        
    def verifica_combobox(self):
        linguagem = self.combobox.currentText()
      
        if linguagem == "Python":
            self.checkbox = QCheckBox("Tkinter ?")
            self.layout_combobox.addWidget(self.checkbox)
        else:
            self.layout_combobox.removeWidget(self.checkbox)
            self.checkbox.deleteLater()
            self.checkbox = None
        
    def display_route(self):
        nome = self.input_nome_projeto.text()
        linguagem = self.combobox.currentText()
        message_output = f"{nome}, {linguagem}"
        
        
        if len(nome) == 0:
            QMessageBox.warning(self, "INVALIDO", "O nome do projeto\nnão pode ser vazio")
        elif len(linguagem) == 0:
            QMessageBox.warning(self, "INVALIDO", "Selecione uma linguagem")
            
        elif validate_input(nome):
            QMessageBox.information(self, "Tudo certo", f"Escolha onde o projeto sera gerado")
            # self.result_label.config(text=f"{name}, {language}") 
        else:
            QMessageBox.warning(self, "INVALIDO", "O nome do projeto não deve\n ter espaços e nem acentos")
            # self.result_label.config(text="Nome invalido")
            
    def select_path(self):
        diretorio = QFileDialog.getExistingDirectory(self, "Escolha um diretorio")
        self.input_rota.clear()
        self.input_rota.insert(diretorio)
        
    def run_bash(self, command):
        process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE) 
        stdout, stderr = process.communicate() 
        # self.quadro.delete(1.0, END) 
        self.quadro.append(stdout.decode()) 
        if stderr: 
            self.quadro.append(stderr.decode()) 
            
            
    # FALTA ISSO PRA MEXER O RESTO FOI PELO VISTO
    def generate_project(self):
        name_project = self.input_nome_projeto.text()
        linguagem = self.combobox.currentText()
        # Vou ver esse ainda
        bibliotecas = None
        try:
            bibliotecas = self.checkbox.isChecked()
        except:
            print("Sem bibliotecas")
        
        mensagem = f"Seu projeto sera gerado em '/{self.input_rota.text()}/{name_project}'" 
        resposta = self.mensagem_de_aviso("Gerar projeto",mensagem)
        if resposta == QMessageBox.Ok:
            if validate_input(name_project):
                # self.run_bash("sudo apt-get update -y && sudo apt-get upgrade -y")
                path_full_new_project = save_data(name_project, linguagem, self.path_project, bibliotecas)
                menssage = f"Projeto foi criado em {path_full_new_project}"
                QMessageBox.information(self,"Informações",menssage)
                open_vscode(path_full_new_project)
            else:
                QMessageBox.warning(self,"Não gerado", "ERRO : Nome ou linguagem invalidos")
                
    
    def mensagem_de_aviso(self, titulo, mensagem):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(titulo)
        msg_box.setText(mensagem)
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        resposta = msg_box.exec()
        return resposta
    
    def get_default_directory(self):
        self.path_project = get_path_directory()
        self.input_rota.insert(self.path_project)