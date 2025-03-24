from PySide6.QtWidgets import QFileDialog, QCheckBox, QTextBrowser,QComboBox ,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox, QInputDialog
from handlers.handlers import validate_input, save_data
from bash.comand_bash import open_vscode
from subprocess import PIPE, Popen
from handlers.maneger_dir import get_path_directory
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt



class GeradorDeProjetos(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("Main")
        self.setWindowTitle('Gerador de Projetos')
        self.layout_principal = QHBoxLayout()
        self.setGeometry(100,100, 600, 400)
        
         # Adiciona formulario ao layout principal
        self.layout_principal.addWidget(self.criar_formulario())
        self.layout_principal.addWidget(self.exibe_dados())
        
        # Define layout principal
        self.setLayout(self.layout_principal)
        self.get_default_directory()
            
    def criar_formulario(self):
        # Cria Formulario 
        container_formulario= QWidget()
        container_formulario.setObjectName("Container_formulario")
        layout_form = QVBoxLayout()
        
        layout_info_projeto = self.informacoes_projeto()
        layout_info_rota = self.informacoes_rota()
        
        
        layout_form.addWidget(layout_info_projeto)
        layout_form.addWidget(layout_info_rota)
        container_formulario.setLayout(layout_form)
        
        return container_formulario
        
    def informacoes_projeto(self):
        container_info_projetos = QWidget()
        container_info_projetos.setObjectName("Info_projeto")
        
        layout_info_projeto = QVBoxLayout()
        
        # Label Combobox
        layout_label = QHBoxLayout()
        label_linguagem = QLabel("Selecione uma linguagem")
        label_linguagem.setObjectName("Label_linguagem")
        layout_label.addWidget(label_linguagem, alignment=Qt.AlignHCenter)
        layout_info_projeto.addLayout(layout_label)
        
        # Combobox 
        self.layout_combobox = QHBoxLayout()
        self.combobox = QComboBox()
        self.combobox.setObjectName("Combobox")
        self.combobox.addItems(["JavaScript","Python"])
        self.combobox.setFixedSize(160,25)
        self.combobox.currentIndexChanged.connect(self.verifica_combobox)
        self.layout_combobox.addWidget(self.combobox)
        layout_info_projeto.addLayout(self.layout_combobox)
        
        # Label input
        layout_label_nome = QHBoxLayout()
        label_input_nome = QLabel("Digite o nome do projeto")
        label_input_nome.setObjectName("Label_input_nome")    
        layout_label_nome.addWidget(label_input_nome, alignment=Qt.AlignHCenter)
        layout_info_projeto.addLayout(layout_label_nome)
        
        
        # Input nome do projeto
        self.input_nome_projeto = QLineEdit()
        self.input_nome_projeto.setFixedSize(160,20)
        self.input_nome_projeto.setObjectName("Input_nome_projeto")
        layout_info_projeto.addWidget(self.input_nome_projeto, alignment=Qt.AlignHCenter)
        
        # Botão validar
        botao_validar = QPushButton("Validar")
        botao_validar.setObjectName("Botao_validar")
        botao_validar.clicked.connect(self.display_route)
        botao_validar.setFixedSize(160,20)
        layout_info_projeto.addWidget(botao_validar, alignment=Qt.AlignHCenter)
        container_info_projetos.setLayout(layout_info_projeto)
        
        return container_info_projetos

       
    def informacoes_rota(self):
        container_info_rota = QWidget()
        container_info_rota.setObjectName("Info_rota")
        
        layout_info_rota = QVBoxLayout()
        
        # Label rota projeto
        # layout_label_rota = QHBoxLayout()
        label_input_rota = QLabel("Escolha onde o projeto sera gerado")
        label_input_rota.setObjectName("Label_input_rota")
        layout_info_rota.addWidget(label_input_rota, alignment=Qt.AlignHCenter)
        # layout_info_rota.addLayout(layout_label_rota)
        
        input_rota = self.campo_input_rota()
        layout_info_rota.addWidget(input_rota)
        
        # Botão Gerar Projeto
        botao_gerar_projeto = QPushButton("Gerar Projeto")
        botao_gerar_projeto.setObjectName("Botao_gerar_projeto")
        botao_gerar_projeto.setFixedSize(160,25)
        botao_gerar_projeto.clicked.connect(self.generate_project)
        layout_info_rota.addWidget(botao_gerar_projeto, alignment=Qt.AlignHCenter)
        container_info_rota.setLayout(layout_info_rota)
        
        return container_info_rota
    
    def campo_input_rota(self):
        container_layout_input_rota = QWidget()
        # container_layout_input_rota.setMinimumWidth(30)
        container_layout_input_rota.setMaximumHeight(30)
        container_layout_input_rota.setObjectName("Campo_input_rota")
        
        layout_input_rota = QHBoxLayout()
         # Input rota do projeto
        self.input_rota = QLineEdit()
        self.input_rota.setObjectName("Input_rota")
        layout_input_rota.addWidget(self.input_rota)
        
        
        # Botão localizar
        botao_localizar = QPushButton("")
        botao_localizar.setObjectName("Botao_localizar")
        botao_localizar.setIcon(QIcon("src/ui/assets/pasta_carton_vazia.png"))
        botao_localizar.clicked.connect(self.select_path)
        layout_input_rota.addWidget(botao_localizar)
        
        
        container_layout_input_rota.setLayout(layout_input_rota)
        return container_layout_input_rota
        
    def exibe_dados(self):
        container_layout_quadro = QWidget()
        container_layout_quadro.setObjectName("Quadro_de_dados")
        layout_quadro = QVBoxLayout()
        self.quadro = QTextBrowser()
        layout_quadro.addWidget(self.quadro)
        container_layout_quadro.setLayout(layout_quadro)
        
        return container_layout_quadro
        
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
        # message_output = f"{nome}, {linguagem}"
        
        
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
        
        mensagem = f"Seu projeto sera gerado em '{self.input_rota.text()}/{name_project}'" 
        resposta = self.mensagem_de_aviso("Gerar projeto",mensagem)
        if resposta == QMessageBox.Ok:
            if validate_input(name_project):
                # self.run_bash("sudo apt-get update -y && sudo apt-get upgrade -y")
                path_full_new_project = save_data(name_project, linguagem, self.input_rota.text(), bibliotecas)
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