from __init__ import *

class ClickLabel(QLabel):
    clicked = pyqtSignal()
    DIR = "123"

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)

class Gallery(QWidget):
    receiveSignal = pyqtSignal([str, int])
    sendSignal = pyqtSignal(str)
    def __init__(self):
        super(Gallery, self).__init__()
        self.checkStates = {}
        self.empty_pixmap = QPixmap("empty_slot.png")
        self.layout = QHBoxLayout()
        self.layout.setSpacing(45)
        self.initialize_labels()

        self.setLayout(self.layout)
        self.layout.setContentsMargins(45, 0, 45, 0)
        self.receiveSignal.connect(self.set)

    def initialize_labels(self):

        self.image1 = ClickLabel()
        self.image1.setFixedSize(150,150)
        self.image1.setPixmap(self.empty_pixmap)
        self.image1.setScaledContents(True)
        self.image1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image1.clicked.connect(self.imageToEdit)
        self.layout.addWidget(self.image1)

        self.image2 = ClickLabel()
        self.image2.setFixedSize(150, 150)
        self.image2.setPixmap(self.empty_pixmap)
        self.image2.setScaledContents(True)
        self.image2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image2.clicked.connect(self.imageToEdit)
        self.layout.addWidget(self.image2)

        self.image3 = ClickLabel()
        self.image3.setFixedSize(150, 150)
        self.image3.setPixmap(self.empty_pixmap)
        self.image3.setScaledContents(True)
        self.image3.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image3.clicked.connect(self.imageToEdit)
        self.layout.addWidget(self.image3)

        self.image4 = ClickLabel()
        self.image4.setFixedSize(150, 150)
        self.image4.setPixmap(self.empty_pixmap)
        self.image4.setScaledContents(True)
        self.image4.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image4.clicked.connect(self.imageToEdit)
        self.layout.addWidget(self.image4)

        self.image5 = ClickLabel()
        self.image5.setFixedSize(150, 150)
        self.image5.setPixmap(self.empty_pixmap)
        self.image5.setScaledContents(True)
        self.image5.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image5.clicked.connect(self.imageToEdit)
        self.layout.addWidget(self.image5)

        self.image6 = ClickLabel()
        self.image6.setFixedSize(150, 150)
        self.image6.setPixmap(self.empty_pixmap)
        self.image6.setScaledContents(True)
        self.image6.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image6.clicked.connect(self.imageToEdit)
        self.layout.addWidget(self.image6)

    def fill_images(self):
        directories = []
        for path in self.checkStates:
            directories.append(path)
        i = len(directories)
        curr_dir = 0
        not_empty = bool(i)

        if not_empty:
            pixmap = QPixmap(directories[curr_dir])
            self.image1.DIR = directories[curr_dir]
            self.image1.setPixmap(pixmap)
            curr_dir +=1
            i-=1
            not_empty = bool(i)
        else:
            self.image1.setPixmap(self.empty_pixmap)
            self.image1.DIR = ""

        if not_empty:
            pixmap = QPixmap(directories[curr_dir])
            self.image2.DIR = directories[curr_dir]
            self.image2.setPixmap(pixmap)
            curr_dir +=1
            i-=1
            not_empty = bool(i)
        else:
            self.image2.setPixmap(self.empty_pixmap)
            self.image2.DIR = ""

        if not_empty:
            pixmap = QPixmap(directories[curr_dir])
            self.image3.DIR = directories[curr_dir]
            self.image3.setPixmap(pixmap)
            curr_dir +=1
            i-=1
            not_empty = bool(i)
        else:
            self.image3.setPixmap(self.empty_pixmap)
            self.image3.DIR = ""

        if not_empty:
            pixmap = QPixmap(directories[curr_dir])
            self.image4.DIR = directories[curr_dir]
            self.image4.setPixmap(pixmap)
            curr_dir +=1
            i-=1
            not_empty = bool(i)
        else:
            self.image4.setPixmap(self.empty_pixmap)
            self.image4.DIR = ""

        if not_empty:
            pixmap = QPixmap(directories[curr_dir])
            self.image5.DIR = directories[curr_dir]
            self.image5.setPixmap(pixmap)
            curr_dir +=1
            i-=1
            not_empty = bool(i)
        else:
            self.image5.setPixmap(self.empty_pixmap)
            self.image4.DIR = ""

        if not_empty:
            pixmap = QPixmap(directories[curr_dir])
            self.image6.DIR = directories[curr_dir]
            self.image6.setPixmap(pixmap)
            curr_dir +=1
            i-=1
            not_empty = bool(i)
        else:
            self.image6.setPixmap(self.empty_pixmap)
            self.image6.DIR = ""

    def set(self, dir, state):
        if state == 2:
            if dir not in self.checkStates:
                self.checkStates[dir] = state
        else:
            self.checkStates.pop(dir)

        self.fill_images()

    def imageToEdit(self):
        label = self.sender()
        self.sendSignal.emit(label.DIR)
