from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    # set up function for the gui
    def setupUi(self, MainWindow):
        # MainWindow = the object of the window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1068, 484)

        # icon = the icon top left (i will fix it later)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/openpiv_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(174, 79))

        # centeral_widget = everything under the menu bar
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setAutoFillBackground(False)
        self.central_widget.setObjectName("central_widget")
        MainWindow.setCentralWidget(self.central_widget)

        # writing all the titles/texts
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "OpenPIV", None, -1))

        # connecting everything to the widget
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    import sys
    # creating the widget
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
