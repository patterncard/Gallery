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
        #adding save layout and set layout to potions menu
        save_layout = QAction('Save layout', self)
        save_layout.triggered.connect(self.layoutSave)
        self.optionsMenu.addAction(save_layout)
        set_layout = QAction('Set layout', self)
        set_layout.triggered.connect(self.layoutSet)
        #TODO, hopefully will make it so user can choose a letter here
        set_layout.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_H))
        self.optionsMenu.addAction(set_layout)

    def layoutSave(self):
        #checks if config exists, if yes saves the splitters sizes, if no, creates a file and writes them
        if os.path.exists('./config.json'):
            f = open('config.json')
            data = json.load(f)
            f.close()
            #TODO check if that part works when theese keys do not exist in json
            data["splitter|"] = self.splitter1.sizes()
            data["splitter-"] = self.splitter3.sizes()
            data = json.dumps(data, indent = 4)
            with open("config.json", "w") as outfile:
                outfile.write(data)
        else:
            data = {"splitter|": self.splitter1.sizes(), "splitter-": self.splitter3.sizes()}
            data = json.dumps(data, indent = 4)
            with open("config.json", "w") as outfile:
                outfile.write(data)

    def layoutSet(self):
        #checks if config exists, if yes sets splitters sizes, if no does nothing
        if os.path.exists('./config.json'):
            f = open('config.json')
            data = json.load(f)
            f.close()
            #TODO Error handling if file exists but the keys don't
            self.splitter1.setSizes(data['splitter|'])
            self.splitter2.setSizes(data['splitter|'])
            self.splitter3.setSizes(data['splitter-'])
        else:
            return 0

    def examplaryUI(self):
        #TODO has to be later rewriten to contain parts created by others
        mainwindow = QWidget()

        vbox = QVBoxLayout()

        actionMenu = QTextEdit()
        loadedImages = QTextEdit()
        # substitute Tree in main
        fileList = QTextEdit()
        workSpace = QTextEdit()

        self.splitter1 = QSplitter(Qt.Horizontal)
        self.splitter2 = QSplitter(Qt.Horizontal)
        self.splitter3 = QSplitter(Qt.Vertical)

        self.splitter1.addWidget(actionMenu)
        self.splitter1.addWidget(loadedImages)
        self.splitter1.setSizes([100,200])

        self.splitter2.addWidget(fileList)
        self.splitter2.addWidget(workSpace)
        self.splitter2.setSizes([100,200])
        
        self.splitter3.addWidget(self.splitter1)
        self.splitter3.addWidget(self.splitter2)
        self.splitter3.setSizes([100,200])

        self.splitter1.splitterMoved.connect(lambda: self.splitter2.setSizes(self.splitter1.sizes()))
        self.splitter2.splitterMoved.connect(lambda: self.splitter1.setSizes(self.splitter2.sizes()))
        vbox.addWidget(self.splitter3)

        mainwindow.setLayout(vbox)

        self.setCentralWidget(mainwindow)
    