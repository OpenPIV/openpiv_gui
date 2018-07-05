from PySide2 import QtCore, QtGui, QtWidgets


class FileWindowClass(object):
    def __init__(self, file_window):
        self.file_window = file_window
        self.gridLayout = QtWidgets.QGridLayout(self.file_window)
        self.add_button = QtWidgets.QPushButton(self.file_window)
        self.remove_button = QtWidgets.QPushButton(self.file_window)
        self.close_button = QtWidgets.QPushButton(self.file_window)
        self.file_list = QtWidgets.QListWidget(self.file_window)

    def window_setup(self):
        self.file_window.setObjectName("file_window")
        self.file_window.setWindowModality(QtCore.Qt.NonModal)
        self.file_window.resize(320, 240)
        self.file_window.setMinimumSize(QtCore.QSize(320, 240))
        self.file_window.setMaximumSize(QtCore.QSize(320, 240))

        self.remove_button.setEnabled(False)

        self.gridLayout.addWidget(self.add_button, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.remove_button, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.close_button, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.file_list, 1, 0, 1, 3)

        self.text_setup()
        QtCore.QObject.connect(self.add_button, QtCore.SIGNAL("clicked()"), self.add_file)
        QtCore.QObject.connect(self.close_button, QtCore.SIGNAL("clicked()"), file_window.close)
        QtCore.QObject.connect(self.file_list, QtCore.SIGNAL("itemPressed()"), self.remove_button.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(self.file_window)

    def text_setup(self):
        self.file_window.setWindowTitle(QtWidgets.QApplication.translate("file_window", "OpenPIV file", None, -1))
        self.add_button.setText(QtWidgets.QApplication.translate("file_window", "Add", None, -1))
        self.remove_button.setText(QtWidgets.QApplication.translate("file_window", "Remove", None, -1))
        self.close_button.setText(QtWidgets.QApplication.translate("file_window", "Close", None, -1))

    def add_file(self):
        self.file_list.addItem(str(
            (QtWidgets.QFileDialog.getOpenFileName(self.file_list, path=QtCore.QDir, filter=('(*.png)')))[0]))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    file_window = QtWidgets.QWidget()
    file_window_class = FileWindowClass(file_window)
    file_window_class.window_setup()
    file_window.show()
    sys.exit(app.exec_())
