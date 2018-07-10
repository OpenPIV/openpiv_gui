from PySide2 import QtCore, QtGui, QtWidgets

FONT = QtGui.QFont()
FONT.setFamily("Gill Sans MT")
FONT.setPointSize(21)
FONT.setWeight(75)
FONT.setItalic(True)
FONT.setBold(True)


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
        self.file_action = QtWidgets.QAction(self.menu_bar_file)

    def main_window_setup(self):
        self.main_window.resize(866, 683)
        self.main_window.setObjectName("main_window")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"package/images/openpiv_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.main_window.setWindowIcon(icon)

        self.default_image.setPixmap(QtGui.QPixmap(r"package/images/openpiv_logo.png"))

        self.default_image.setAlignment(QtCore.Qt.AlignCenter)

        self.image_pages.addWidget(self.default_image_widget)

        left_right_buttons_spacer = QtWidgets.QSpacerItem(2000, 20, QtWidgets.QSizePolicy.Expanding,
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

        self.file_action.setShortcut('Ctrl+F')
        self.file_action.setStatusTip('manage files')

        self.menu_bar_file.addAction(self.file_action)

        self.main_window.setCentralWidget(self.main_widget)

        self.text_setup()

        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def text_setup(self):
        set_text = lambda x, text: x.setText(text)

        self.main_window.setWindowTitle("OpenPIV")

        """
        set_text(self.stop_button, "STOP")
        set_text(self.start_button, "START")
        set_text(self.scale_label, "Scale:")
        set_text(self.outer_filter_label, "Outer filter:")
        set_text(self.jump_label, "Jump:")
        set_text(self.reset_roi_button, "Reset ROI")
        set_text(self.select_roi_button, "Select ROI")
        set_text(self.type_label, "S/N type:")
        set_text(self.value_label, "S/N value:")
        set_text(self.vertical_label, "Vertical")
        set_text(self.horizontal_label, "Horizontal")
        set_text(self.spacing_label, "spacing/Overlap")
        set_text(self.height_label, "Height")
        set_text(self.width_label, "Width")
        set_text(self.interrogation_winsize_label, "Interrogation window size")
        """
        set_text(self.file_action, "manage file")
        set_text(self.left_button, "<")
        set_text(self.right_button, ">")
        set_text(self.current_image_number, "0")

        self.menu_bar_file.setTitle("file")

    """
    # function that changes the max and min of jump
    def change_jump_max_min(self):
        self.jump_spin_box.setMaximum(self.image_pages.count() - 1)
        self.jump_spin_box.setMinimum((-1) * (self.image_pages.count() - 1))
    """


if __name__ == "__main__":
    # run the application
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_window_class = MainWindowClass(MainWindow)
    main_window_class.main_window_setup()
    main_window_class.default_image.setPixmap(QtGui.QPixmap("images/openpiv_logo.png"))
    MainWindow.show()
    sys.exit(app.exec_())
