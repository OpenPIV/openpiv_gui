from PySide2 import QtCore, QtGui, QtWidgets
import sys


class FileWindowClass(object):
    # Base setup of the file window
    def WindowSetup(self, FileWindow):
        # FileWindow = the object of the window
        FileWindow.setObjectName("FileWindow")
        FileWindow.resize(493, 391)

        # grid_layout = they are layout to make the program look better and to have the option to resize the window
        self.gridLayout_2 = QtWidgets.QGridLayout(FileWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # file_frame = a frame that you can orgenize element like buttons labels and more
        self.file_frame = QtWidgets.QFrame(FileWindow)
        self.file_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_frame.setObjectName("file_frame")
        self.grid_layout = QtWidgets.QGridLayout(self.file_frame)
        self.grid_layout.setObjectName("grid_layout")

        # spacer_Item = to resize the elements
        spacerItem = QtWidgets.QSpacerItem(97, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacerItem, 0, 0, 1, 1)

        # buttons = all the buttens in the window to add close and remove files
        self.add_button = QtWidgets.QPushButton(self.file_frame)
        self.add_button.setObjectName("add_button")
        self.grid_layout.addWidget(self.add_button, 0, 1, 1, 1)
        self.remove_button = QtWidgets.QPushButton(self.file_frame)
        self.remove_button.setObjectName("remove_button")
        self.grid_layout.addWidget(self.remove_button, 0, 2, 1, 1)
        self.close_button = QtWidgets.QPushButton(self.file_frame)
        self.close_button.setObjectName("close_button")
        self.grid_layout.addWidget(self.close_button, 0, 3, 1, 1)
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item1, 0, 4, 1, 2)
        spacer_item2 = QtWidgets.QSpacerItem(97, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item2, 1, 0, 1, 1)

        # file_list = the white part on the page there will be the files you selected you can ramove
        self.file_list = QtWidgets.QListView(self.file_frame)
        self.file_list.setObjectName("file_list")
        self.grid_layout.addWidget(self.file_list, 1, 1, 1, 4)
        spacer_item3 = QtWidgets.QSpacerItem(97, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item3, 1, 5, 1, 1)
        spacer_item4 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_layout.addItem(spacer_item4, 2, 3, 1, 1)
        self.gridLayout_2.addWidget(self.file_frame, 0, 0, 1, 1)

        # image = will show you the image you selected(if you didnt select it will show an image of openPIV)
        self.image = QtWidgets.QLabel(FileWindow)
        self.image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("images/openpiv_logo.png"))
        self.image.setScaledContents(False)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.gridLayout_2.addWidget(self.image, 1, 0, 1, 1)

        self.TextSetup(FileWindow)
        QtCore.QMetaObject.connectSlotsByName(FileWindow)

    # function that write all the texts in the window
    def TextSetup(self, FileWindow):
        FileWindow.setWindowTitle(QtWidgets.QApplication.translate("OpenPIV", "Images", None, -1))
        self.add_button.setText(QtWidgets.QApplication.translate("FileWindow", "Add", None, -1))
        self.remove_button.setText(QtWidgets.QApplication.translate("FileWindow", "delete", None, -1))
        self.close_button.setText(QtWidgets.QApplication.translate("FileWindow", "close", None, -1))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    FileWindow = QtWidgets.QWidget()
    ui = FileWindowClass()
    ui.WindowSetup(FileWindow)
    FileWindow.show()
    sys.exit(app.exec_())