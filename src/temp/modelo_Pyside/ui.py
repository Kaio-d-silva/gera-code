from PySide6.QtWidgets import QWidget, QVBoxLayout

class Project(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
        
    def init_ui(self):
        self.setWindowTitle('New Project')
        self.setGeometry(100,100, 400, 300)

        layout_main = QVBoxLayout()
        self.setLayout(layout_main)