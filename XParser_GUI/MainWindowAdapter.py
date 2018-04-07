import sys
from XParser_GUI import MainWindow,GeneralOutputAdapter
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindowAdapter(QtWidgets.QMainWindow):
    """
        成员变量:
        ui :                该窗体的界面元素
        log_dialog :        该窗体所关联的"日志对话框"窗体对象
    """
    def __init__(self):
        super(MainWindowAdapter,self).__init__()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("XParser")
        self.log_dialog = GeneralOutputAdapter.GeneralOutputAdapter()

        self.ui.pushButton_quickstartanalyze

    def showEvent(self, *args, **kwargs):
        pass

    def call_logdialog(self):
        """显示日志窗口，如果不未运行，则创建一个"""
        if (self.log_dialog.flag_running):
            self.log_dialog.show()
        else :
            self.log_dialog.exec()
            self.log_dialog.flag_running = True
        self.show()

    def quick_run(self):
        """根据界面参数快速运行XPaser"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindowAdapter()
    MainWindow.show()
    sys.exit(app.exec_())