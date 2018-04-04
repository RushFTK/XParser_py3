import sys
import XParser_GUI.MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindowAdapter(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowAdapter,self).__init__()
        self.ui = XParser_GUI.MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("XParser")

    def quick_run(self):
        """根据界面参数快速运行XPaser"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindowAdapter();
    MainWindow.show()
    sys.exit(app.exec_())