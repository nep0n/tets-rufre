from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connect()
        self.set_appear()
        self.show()
        
    def initUI(self):
        pass
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

