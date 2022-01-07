from __init__ import *

class Test(QWidget):
    def __init__(self):
        super(Test, self).__init__()
        self.layout = QVBoxLayout(self)
        self.field = QTextEdit("preview of choosen images should be here")
        self.layout.addWidget(self.field)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)