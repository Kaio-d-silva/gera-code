from PySide6.QtWidgets import QApplication
from ui import Project

if __name__ == '__main__':
    app = QApplication([])
    projeto = Project()
    projeto.show()
    app.exec()