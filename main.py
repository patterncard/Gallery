from __init__ import *
from window import *

if __name__ == '__main__':
    # Run the window
    app = QApplication(sys.argv)
    win = Window()
    win.resize(640,640)
    win.show()
    sys.exit(app.exec_())
