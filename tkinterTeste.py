from PySide6.QtWidgets import QFileDialog, QCheckBox, QTextBrowser,QComboBox ,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox, QInputDialog
class Teste(QWidget):
    def __init__(self):
        super().__init__()
        self.tela()
        
    def tela(self):
        layout = QVBoxLayout()
        botao_teste = QPushButton('teste kaio')
        botao_teste.clicked.connect(self.exibir_mensagem)
        layout.addWidget(botao_teste)
        self.setLayout(layout)
        
    def exibir_mensagem(self):
        # Criar uma instância do QMessageBox
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirmação")
        msg_box.setText("Você deseja continuar?")
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # Exibe o QMessageBox e captura a resposta
        resposta = msg_box.exec()

        if resposta == QMessageBox.Ok:
            print("Usuário clicou em OK")
        elif resposta == QMessageBox.Cancel:
            print("Usuário clicou em Cancelar")



app = QApplication([])
teste = Teste()
teste.show()
app.exec()