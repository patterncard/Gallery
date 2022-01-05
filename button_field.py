from PyQt5.QtWidgets import QPushButton
from __init__ import *

class Buttons(QWidget):
    def __init__(self):
        super(Buttons, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.vlayout = QVBoxLayout(self)
        self.hlayout1 = self.upperRow()
        self.hlayout2 = self.lowerRow()
        self.vlayout.addLayout(self.hlayout1)
        self.vlayout.addLayout(self.hlayout2)
        self.setLayout(self.vlayout)
        self.resize(100,100)
        self.vlayout.setAlignment(Qt.AlignCenter)
        self.vlayout.setContentsMargins(0, 0, 0, 0)

    def upperRow(self):
        hlayout = QHBoxLayout()
        self.x11 = QPushButton("1x1")
        self.x11.setFixedSize(50,50)
        self.x12 = QPushButton("1x2")
        self.x12.setFixedSize(50,50)
        self.x13 = QPushButton("1x3")
        self.x13.setFixedSize(50,50)
        hlayout.setAlignment(Qt.AlignCenter)
        hlayout.addWidget(self.x11)
        hlayout.addWidget(self.x12)
        hlayout.addWidget(self.x13)
        return hlayout

    def lowerRow(self):
        hlayout = QHBoxLayout()
        self.x22 = QPushButton("2x2")
        self.x22.setFixedSize(50,50)
        self.x23 = QPushButton("2x3")
        self.x23.setFixedSize(50,50)
        self.x33 = QPushButton("3x3")
        self.x33.setFixedSize(50,50)
        hlayout.setAlignment(Qt.AlignCenter)
        hlayout.addWidget(self.x22)
        hlayout.addWidget(self.x23)
        hlayout.addWidget(self.x33)
        return hlayout
