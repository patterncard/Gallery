from __init__ import *

class Window(QMainWindow):

    def __init__(self, parent=None):
        #setting up windows title for the whole class
        super().__init__(parent)
        self.setWindowTitle('SE Image viewer')
        self.initUI()

    def initUI(self):
        self.createMenus()
        self.examplaryUI()

    def createMenus(self):
        # Create a menu bar
        self.menu = self.menuBar()
        # Add a drop-down list of the name File
        self.createFileMenu()
        # Add a drop-down list of the name Options
        self.createOptionsMenu()

    def createFileMenu(self):
        self.fileMenu = self.menu.addMenu("File")
        self.fileMenu.addAction('Exit', self.close)

    def createOptionsMenu(self):
        self.optionsMenu = self.menu.addMenu("Options")
        self.save_layout = QAction('Save layout', self)
        #self.save_layout.triggered.connect(None)
        self.optionsMenu.addAction(self.save_layout)
        self.set_layout = QAction('Set layout', self)
        #self.set_layout.triggered.connect(None)
        self.set_layout.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_H))
        self.optionsMenu.addAction(self.set_layout)

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
    