from __init__ import *

class Buttons(QWidget):

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
        self.x11.pressed.connect(self.dialog)
        self.x11.setFixedSize(50,50)
        self.x12 = QPushButton("1x2")
        self.x12.pressed.connect(self.dialog)
        self.x12.setFixedSize(50,50)
        self.x13 = QPushButton("1x3")
        self.x13.setFixedSize(50,50)
        self.x13.pressed.connect(self.dialog)
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
        self.x22.pressed.connect(self.dialog)
        self.x23 = QPushButton("2x3")
        self.x23.setFixedSize(50,50)
        self.x23.pressed.connect(self.dialog)
        self.x33 = QPushButton("3x3")
        self.x33.setFixedSize(50,50)
        self.x33.pressed.connect(self.dialog)
        hlayout.setAlignment(Qt.AlignCenter)
        hlayout.addStretch()
        hlayout.addWidget(self.x22)
        hlayout.addStretch()
        hlayout.addWidget(self.x23)
        hlayout.addStretch()
        hlayout.addWidget(self.x33)
        hlayout.addStretch()
        return hlayout

    def dialog(self):
        dlg = QDialog()
        QBtn = QDialogButtonBox.Ok

        dlg.setWindowTitle("Error")
        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.setCenterButtons(True)
        buttonBox.accepted.connect(dlg.accept)

        layout = QVBoxLayout()
        msg = QLabel("This feature is not yet implemented")
        msg.setAlignment(Qt.AlignCenter)
        layout.addWidget(msg)
        layout.addWidget(buttonBox)
        dlg.setLayout(layout)
        dlg.exec()