from ui.ui_pyside import GeradorDeProjetos
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    
    app = QApplication([])
    
       
    with open("src/ui/style.qss", "r") as arquivo:
        app.setStyleSheet(arquivo.read())
    
    gerador = GeradorDeProjetos()
    gerador.show()
    app.exec()