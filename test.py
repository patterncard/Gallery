from __init__ import *

class Test(QWidget):
    receiveSignal = pyqtSignal([str, int])
    def __init__(self):
        super(Test, self).__init__()
        self.checkStates = {}
        self.empty_pixmap = QPixmap("empty_slot.png")
        self.layout = QHBoxLayout()
        self.layout.setSpacing(0)
        self.initialize_labels()

        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.receiveSignal.connect(self.set)

    def initialize_labels(self):

        self.image1 = QLabel()
        self.image1.setFixedSize(150,150)
        self.image1.setPixmap(self.empty_pixmap)
        self.image1.setScaledContents(True)
        self.image1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.layout.addWidget(self.image1)

        self.image2 = QLabel()
        self.image2.setFixedSize(150, 150)
        self.image2.setPixmap(self.empty_pixmap)
        self.image2.setScaledContents(True)
        self.image2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.layout.addWidget(self.image2)

        self.image3 = QLabel()
        self.image3.setFixedSize(150, 150)
        self.image3.setPixmap(self.empty_pixmap)
        self.image3.setScaledContents(True)
        self.image3.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.layout.addWidget(self.image3)

        self.image4 = QLabel()
        self.image4.setFixedSize(150, 150)
        self.image4.setPixmap(self.empty_pixmap)
        self.image4.setScaledContents(True)
        self.image4.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.layout.addWidget(self.image4)

        self.image5 = QLabel()
        self.image5.setFixedSize(150, 150)
        self.image5.setPixmap(self.empty_pixmap)
        self.image5.setScaledContents(True)
        self.image5.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.layout.addWidget(self.image5)

        self.image6 = QLabel()
        self.image6.setFixedSize(150, 150)
        self.image6.setPixmap(self.empty_pixmap)
        self.image6.setScaledContents(True)
        self.image6.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.layout.addWidget(self.image6)

    def fill_images(self):
        print(self.checkStates)
        directories = []
        for path in self.checkStates:
            directories.append(path)
        i = len(directories)
        curr_dir = 0
        not_empty = bool(i)

        if not_empty:
            print("we about to set")
            pixmap = QPixmap(directories[curr_dir])
            print(directories[curr_dir])
            self.image1.setPixmap(pixmap)
            curr_dir +=1
            i-=1
            not_empty = bool(i)
        else:
            self.image1.setPixmap(self.empty_pixmap)

        if not_empty:
            print("we about to set")
            pixmap = QPixmap(directories[curr_dir])
            print(directories[curr_dir])
            self.image2.setPixmap(pixmap)
            curr_dir +=1
            i-=1
            not_empty = bool(i)
        else:
            self.image2.setPixmap(self.empty_pixmap)

        if not_empty:
            print("we about to set")
            pixmap = QPixmap(directories[curr_dir])
            print(directories[curr_dir])
            self.image3.setPixmap(pixmap)
            curr_dir +=1
            i-=1
            not_empty = bool(i)
        else:
            self.image3.setPixmap(self.empty_pixmap)

        if not_empty:
            print("we about to set")
            pixmap = QPixmap(directories[curr_dir])
            print(directories[curr_dir])
            self.image4.setPixmap(pixmap)
            curr_dir +=1
            i-=1
            not_empty = bool(i)
        else:
            self.image4.setPixmap(self.empty_pixmap)

        if not_empty:
            print("we about to set")
            pixmap = QPixmap(directories[curr_dir])
            print(directories[curr_dir])
            self.image5.setPixmap(pixmap)
            curr_dir +=1
            i-=1
            not_empty = bool(i)
        else:
            self.image5.setPixmap(self.empty_pixmap)

        if not_empty:
            print("we about to set")
            pixmap = QPixmap(directories[curr_dir])
            print(directories[curr_dir])
            self.image6.setPixmap(pixmap)
            curr_dir +=1
            i-=1
            not_empty = bool(i)
        else:
            self.image6.setPixmap(self.empty_pixmap)

    def set(self, dir, state):
        if state == 2:
            if dir not in self.checkStates:
                self.checkStates[dir] = state
        else:
            self.checkStates.pop(dir)

        self.fill_images()



