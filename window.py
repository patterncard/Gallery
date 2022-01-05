from __init__ import *
from directory_handler import Tree
from test import *
from ViewCellClass import ViewCellClass
from button_field import Buttons

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
            try:
                self.splitter1.setSizes(data['splitter|'])
                self.splitter2.setSizes(data['splitter|'])
                self.splitter3.setSizes(data['splitter-'])
            except KeyError:
                return 0
        else:
            return 0

    def examplaryUI(self):
        #TODO has to be later rewriten to contain parts created by others
        mainwindow = QWidget()

        vbox = QVBoxLayout()

        self.actionMenu = Buttons()
        self.actionMenu.clickedSignal.connect(self.test)
        self.loadedImages = Test()
        self.fileList = Tree()
        self.workSpace = ViewCellClass()

        self.splitter1 = QSplitter(Qt.Horizontal)
        self.splitter2 = QSplitter(Qt.Horizontal)
        self.splitter3 = QSplitter(Qt.Vertical)

        self.splitter1.insertWidget(1, self.actionMenu)
        self.splitter1.insertWidget(2, self.loadedImages)

        self.splitter2.insertWidget(1, self.fileList)
        self.splitter2.insertWidget(2, self.workSpace)
        
        self.splitter3.insertWidget(1, self.splitter1)
        self.splitter3.insertWidget(2, self.splitter2)

        self.splitter1.splitterMoved.connect(lambda: self.splitter2.setSizes(self.splitter1.sizes()))
        self.splitter2.splitterMoved.connect(lambda: self.splitter1.setSizes(self.splitter2.sizes()))
        vbox.addWidget(self.splitter3)

        mainwindow.setLayout(vbox)

        self.setSplitters()

        self.setCentralWidget(mainwindow)
    
    def setSplitters(self):
        if self.layoutSet() == 0:
            self.splitter1.setSizes([100,200])
            self.splitter2.setSizes([100,200])
            self.splitter3.setSizes([100,200])

    def test(self, value1, value2):
        self.loadedImages.receiveSignal.emit(value1,value2)