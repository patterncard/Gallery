from __init__ import *

class CheckableFileSystemModel(QFileSystemModel):
    #Needed inside the class
    checkStateChanged = pyqtSignal(str, bool)
    #needed outside the class
    send_Dir = pyqtSignal([str, int])
    def __init__(self):
        super().__init__()
        #list of checkstates
        self.checklist = {}
        self.checkStates = {}
        self.setNameFilterDisables(False)

        #Functions used in the checking procedure
        self.rowsInserted.connect(self.AddCheckMark)
        self.rowsRemoved.connect(self.RemoveCheckMark)
        self.rowsAboutToBeRemoved.connect(self.RemoveCheckMark)

    #Returns the state of the index
    def checkState(self, index):
        return self.checkStates.get(self.filePath(index), Qt.Unchecked)

    #Sets the state of the checkbox, while making sure it is not overwritten an equal state and emits the change if needed
    def AddCheckMark(self, index, state, emitStateChange=True):
        path = self.filePath(index)
        if self.checkStates.get(path) == state:
            return
        if path == "":
            return
        if state == 2:
            if len(self.checklist) <= 6:
                self.checkStates[path] = state
                self.checklist[path] = 'added'
                print(self.checklist)
                if emitStateChange:
                    self.checkStateChanged.emit(path, bool(state))
                    self.send_Dir.emit(path, state)
        else:
            self.checkStates[path] = state
            if emitStateChange:
                self.checkStateChanged.emit(path, bool(state))




    #Removing a checkmark from the file
    def RemoveCheckMark(self, index):
        if not index.isValid():
            print("index invalid")
            return
        path = self.filePath(index)
        if path in self.checkStates:
            self.checkStates.pop(path)
            self.checklist.pop(path)
            self.send_Dir.emit(path, 0)

        print(self.checklist)

    def flags(self, index):
            return super().flags(index) | Qt.ItemIsUserCheckable

    def data(self, index, role=Qt.DisplayRole):
        info = QFileInfo(self.filePath(index))
        size = info.size();
        if role == Qt.CheckStateRole and index.column() == 0 and self.isDir(index) == False and size < 7000000:
            return self.checkState(index)
        return super().data(index, role)

    #Setting the data of chosen index with a given value
    def setData(self, index, value, role, emitStateChange=True):
        if role == Qt.CheckStateRole and index.column() == 0:
            if value == 2:
                self.AddCheckMark(index, value, emitStateChange)
            elif value == 0:
                self.RemoveCheckMark(index)
            else:
                print("unwanted action")
            self.dataChanged.emit(index, index)
            return True
        return super().setData(index, value, role)

class DeselectableTreeView(QTreeView):
    def mousePressEvent(self, event):
        self.clearSelection()
        QTreeView.mousePressEvent(self, event)



class Tree(QWidget):
    def __init__(self, dir = r'C:\Users\User\Desktop'):
        super(Tree, self).__init__()
        self.final_root_path = ''
        self.layout = QVBoxLayout(self)

        self.tree = DeselectableTreeView()
        self.layout.addWidget(self.tree)
        self.layout.setContentsMargins(0, 0, 0, 0)


        self.model = CheckableFileSystemModel()
        self.model.setRootPath(dir)
        self.model.setNameFilters(["*.jpg", "*.png", "*.jpeg"])
        self.tree.setModel(self.model)
        self.tree.setSortingEnabled(True)
        self.tree.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tree.setItemsExpandable(False)
        self.tree.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tree.setRootIndex(self.model.index(dir))
        self.tree.viewport()


        returnToParentDir = QAction("Go Back", self)
        returnToParentDir.triggered.connect(lambda: self.returnToParent())
        self.tree.addAction(returnToParentDir)

        chooseDir = QAction("Set as default directory", self)
        chooseDir.triggered.connect(lambda: self.choose_dir(self.tree.currentIndex()))
        self.tree.addAction(chooseDir)

        self.tree.doubleClicked.connect(self.doubleClickAction)

    def doubleClickAction(self):
        if self.model.isDir(self.tree.currentIndex()):
            self.tree.setRootIndex(self.tree.currentIndex())

    def returnToParent(self):
        self.tree.setRootIndex(self.tree.rootIndex().parent())

    def choose_dir(self, index):
        if self.model.isDir(index) == True:
            self.tree.setRootIndex(index)
            self.final_root_path = self.model.filePath(index)
            print(self.final_root_path)
