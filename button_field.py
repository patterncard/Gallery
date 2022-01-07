from PyQt5.QtWidgets import QPushButton
from __init__ import *

class Buttons(QWidget):
    # clickedSignal = pyqtSignal([int, int])

    def __init__(self):
        super(Buttons, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.vlayout = QVBoxLayout(self)
        self.vlayout.addStretch()
        self.hlayout1 = self.upperRow()
        self.hlayout2 = self.lowerRow()
        self.vlayout.addLayout(self.hlayout1)
        self.vlayout.addStretch()
        self.vlayout.addLayout(self.hlayout2)
        self.vlayout.addStretch()
        self.setLayout(self.vlayout)
        self.vlayout.setAlignment(Qt.AlignCenter)
        self.vlayout.setContentsMargins(0, 0, 0, 0)

    def upperRow(self):
        hlayout = QHBoxLayout()
        # buttons don't do antyhing for now, 
        self.x11 = QPushButton("1x1")
        # self.x11.pressed.connect(lambda: self.clickedSignal.emit(1,1))
        self.x11.setFixedSize(50,50)
        self.x12 = QPushButton("1x2")
        # self.x12.pressed.connect(lambda: self.clickedSignal.emit(1,2))
        self.x12.setFixedSize(50,50)
        self.x13 = QPushButton("1x3")
        self.x13.setFixedSize(50,50)
        # self.x13.pressed.connect(lambda: self.clickedSignal.emit(1,3))
        hlayout.setAlignment(Qt.AlignCenter)
        hlayout.addStretch()
        hlayout.addWidget(self.x11)
        hlayout.addStretch()
        hlayout.addWidget(self.x12)
        hlayout.addStretch()
        hlayout.addWidget(self.x13)
        hlayout.addStretch()
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
        hlayout.addStretch()
        hlayout.addWidget(self.x22)
        hlayout.addStretch()
        hlayout.addWidget(self.x23)
        hlayout.addStretch()
        hlayout.addWidget(self.x33)
        hlayout.addStretch()
        return hlayout
