from PySide2 import QtCore, QtGui, QtWidgets
from package.font import FONT

class MainWindowClass(object):
    def __init__(self, main_window):
        self.main_window = main_window

        self.main_widget = QtWidgets.QWidget(self.main_window)
        self.main_widget_layout = QtWidgets.QGridLayout(self.main_widget)

        self.image_pages = QtWidgets.QStackedWidget(self.main_widget)
        self.default_image_widget = QtWidgets.QWidget()
        self.default_image_widget_layout = QtWidgets.QGridLayout(self.default_image_widget)
        self.right_button = QtWidgets.QPushButton(self.main_widget)
        self.left_button = QtWidgets.QPushButton(self.main_widget)
        self.current_image_number = QtWidgets.QLabel(self.main_widget)

        # The default_image is just that there will be something shown in the image frame all the time
        self.default_image = QtWidgets.QLabel(self.default_image_widget)

        self.menuBar = QtWidgets.QMenuBar(self.main_window)
        self.menu_bar_file = QtWidgets.QMenu(self.menuBar)
        # all the menu actions
        self.load_action = QtWidgets.QAction(self.menu_bar_file)
        self.quit_action = QtWidgets.QAction(self.menu_bar_file)
        self.save_action = QtWidgets.QAction(self.menu_bar_file)

    def main_window_setup(self):
        self.main_window.resize(866, 683)
        self.main_window.setObjectName("main_window")

        self.main_widget.setMinimumSize(QtCore.QSize(580, 630))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"package/images/openpiv_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.main_window.setWindowIcon(icon)

        self.default_image.setPixmap(QtGui.QPixmap(r"package/images/openpiv_logo.png"))

        self.default_image.setAlignment(QtCore.Qt.AlignCenter)

        self.image_pages.addWidget(self.default_image_widget)

        left_right_buttons_spacer = QtWidgets.QSpacerItem(4000, 20, QtWidgets.QSizePolicy.Expanding,
                                                          QtWidgets.QSizePolicy.Minimum)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        self.main_widget.setSizePolicy(sizePolicy)

        self.image_pages.setSizePolicy(sizePolicy)

        self.default_image.setSizePolicy(sizePolicy)

        self.default_image_widget_layout.addWidget(self.default_image, 0, 0, 1, 1)

        self.main_widget_layout.addWidget(self.image_pages, 0, 0, 1, 4)
        self.main_widget_layout.addWidget(self.right_button, 1, 3, 1, 1)
        self.main_widget_layout.addWidget(self.left_button, 1, 1, 1, 1)
        self.main_widget_layout.addWidget(self.current_image_number, 1, 2, 1, 1)
        self.main_widget_layout.addItem(left_right_buttons_spacer, 1, 0, 1, 1)

        self.menuBar.setGeometry(QtCore.QRect(0, 0, 866, 21))
        self.main_window.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menu_bar_file.menuAction())

        self.load_action.setShortcut('CTRL+A')
        self.load_action.setStatusTip('Load')

        self.quit_action.setShortcut('ALT+F4')
        self.quit_action.setStatusTip('Quit')

        self.save_action.setShortcut('ALT+S')
        self.save_action.setStatusTip('Save')

        self.menu_bar_file.addAction(self.load_action)
        self.menu_bar_file.addAction(self.quit_action)
        self.menu_bar_file.addAction(self.save_action)

        self.main_window.setCentralWidget(self.main_widget)

        self.text_setup()

        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def text_setup(self):
        self.main_window.setWindowTitle("OpenPIV")

        self.load_action.setText("Add")
        self.quit_action.setText("Quit")
        self.save_action.setText("Save")
        self.left_button.setText("<")
        self.right_button.setText(">")
        self.current_image_number.setText("0")

        self.menu_bar_file.setTitle("file")


# if __name__ == "__main__":
#     # run the application
#     import sys

#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     main_window_class = MainWindowClass(MainWindow)
#     main_window_class.main_window_setup()
#     main_window_class.default_image.setPixmap(QtGui.QPixmap("images/openpiv_logo.png"))
#     MainWindow.show() 
#     sys.exit(app.exec_())
