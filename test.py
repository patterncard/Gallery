from __init__ import *

class Test(QWidget):
    receiveSignal = pyqtSignal([int, int])
    def __init__(self):
        super(Test, self).__init__()
        self.layout = QVBoxLayout(self)
        self.field = QTextEdit()
        self.layout.addWidget(self.field)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.receiveSignal.connect(self.set)

    def set(self, value1, value2):
        self.field.setText("[" + str(value1) + "," + str(value2) +"]")