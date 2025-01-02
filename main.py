from ui_pyside import GeradorDeProjetos
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])
    gerador = GeradorDeProjetos()
    gerador.show()
    app.exec()