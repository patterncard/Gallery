from __init__ import *

class Window(QMainWindow):

    def __init__(self, parent=None):
        #setting up windows title for the whole class
        super().__init__(parent)
        self.setWindowTitle('SE Image viewer')
        self.initUI()

    def initUI(self):
        self.createMenu()
        self.examplaryUI()

    def createMenu(self):
        # Create a menu bar
        self.menu = self.menuBar()
        # Add a drop-down list of the name File
        self.fileMenu = self.menu.addMenu("File")
        # Extend the file menu with exit position
        self.fileMenu.addAction('Exit', self.close)

    def examplaryUI(self):
        mainwindow = QWidget()

        vbox = QVBoxLayout()

        actionMenu = QTextEdit()
        loadedImages = QTextEdit()
        fileList = QTextEdit()
        workSpace = QTextEdit()

        splitter1 = QSplitter(Qt.Horizontal)
        splitter2 = QSplitter(Qt.Horizontal)
        splitter3 = QSplitter(Qt.Vertical)

        splitter1.addWidget(actionMenu)
        splitter1.addWidget(loadedImages)
        splitter1.setSizes([100,200])

        splitter2.addWidget(fileList)
        splitter2.addWidget(workSpace)
        splitter2.setSizes([100,200])
        
        splitter3.addWidget(splitter1)
        splitter3.addWidget(splitter2)
        splitter3.setSizes([100,200])

        splitter1.splitterMoved.connect(lambda: splitter2.setSizes(splitter1.sizes()))
        splitter2.splitterMoved.connect(lambda: splitter1.setSizes(splitter2.sizes()))
        vbox.addWidget(splitter3)

        mainwindow.setLayout(vbox)

        self.setCentralWidget(mainwindow)
    