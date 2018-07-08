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

        # I putted the settings in a dock widget so you could take the settings out so that it will give you more space
        # and you can dock the setting in the left and right sides of the window
        # *** from here to the next *** are all in the settings_dock_widget
        self.settings_dock_widget = QtWidgets.QDockWidget(self.main_window)
        self.settings_widget = QtWidgets.QWidget()
        self.settings_widget_layout = QtWidgets.QGridLayout(self.settings_widget)
        self.scale_filter_jump_frame = QtWidgets.QFrame(self.settings_dock_widget)
        self.scale_filter_jump_frame_layout = QtWidgets.QGridLayout(self.scale_filter_jump_frame)
        self.scale_label = QtWidgets.QLabel(self.scale_filter_jump_frame)
        self.outer_filter_label = QtWidgets.QLabel(self.scale_filter_jump_frame)
        self.outer_filter_spin_box = QtWidgets.QDoubleSpinBox(self.scale_filter_jump_frame)
        self.jump_label = QtWidgets.QLabel(self.scale_filter_jump_frame)
        self.jump_spin_box = QtWidgets.QSpinBox(self.scale_filter_jump_frame)
        self.scale_spin_box = QtWidgets.QDoubleSpinBox(self.scale_filter_jump_frame)
        self.roi_frame = QtWidgets.QFrame(self.settings_dock_widget)
        self.roi_frame_layout = QtWidgets.QGridLayout(self.roi_frame)
        self.reset_roi_button = QtWidgets.QPushButton(self.roi_frame)
        self.select_roi_button = QtWidgets.QPushButton(self.roi_frame)
        self.type_value_frame = QtWidgets.QFrame(self.settings_dock_widget)
        self.type_value_frame_layout = QtWidgets.QGridLayout(self.type_value_frame)
        self.value_spin_box = QtWidgets.QDoubleSpinBox(self.type_value_frame)
        self.type_label = QtWidgets.QLabel(self.type_value_frame)
        self.value_label = QtWidgets.QLabel(self.type_value_frame)
        self.spacing_frame = QtWidgets.QFrame(self.settings_dock_widget)
        self.type_combo_box = QtWidgets.QComboBox(self.type_value_frame)
        self.spacing_frame_layout = QtWidgets.QGridLayout(self.spacing_frame)
        self.horizontal_combo_box = QtWidgets.QComboBox(self.spacing_frame)
        self.vertical_combo_box = QtWidgets.QComboBox(self.spacing_frame)
        self.vertical_label = QtWidgets.QLabel(self.spacing_frame)
        self.horizontal_label = QtWidgets.QLabel(self.spacing_frame)
        self.spacing_label = QtWidgets.QLabel(self.spacing_frame)
        self.interrogation_winsize_frame = QtWidgets.QFrame(self.settings_dock_widget)
        self.interrogation_winsize_frame_layout = QtWidgets.QGridLayout(self.interrogation_winsize_frame)
        self.height_label = QtWidgets.QLabel(self.interrogation_winsize_frame)
        self.width_label = QtWidgets.QLabel(self.interrogation_winsize_frame)
        self.width_combo_box = QtWidgets.QComboBox(self.interrogation_winsize_frame)
        self.height_combo_box = QtWidgets.QComboBox(self.interrogation_winsize_frame)
        self.interrogation_winsize_label = QtWidgets.QLabel(self.interrogation_winsize_frame)
        self.start_stop_frame = QtWidgets.QFrame(self.settings_dock_widget)
        self.start_stop_frame_layout = QtWidgets.QGridLayout(self.start_stop_frame)
        self.stop_button = QtWidgets.QPushButton(self.start_stop_frame)
        self.start_button = QtWidgets.QPushButton(self.start_stop_frame)
        # ***
        self.menuBar = QtWidgets.QMenuBar(self.main_window)
        self.menu_bar_file = QtWidgets.QMenu(self.menuBar)
        self.file_action = QtWidgets.QAction(self.menu_bar_file)

    def setting_dock_widget_setup(self):
        self.settings_dock_widget.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFloatable | QtWidgets.QDockWidget.DockWidgetMovable)
        self.settings_dock_widget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.settings_dock_widget.setWindowTitle("Settings")

        self.scale_filter_jump_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.scale_filter_jump_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        FONT.setPointSize(10)
        self.scale_label.setFont(FONT)
        self.scale_label.setAlignment(QtCore.Qt.AlignCenter)

        self.outer_filter_label.setFont(FONT)
        self.outer_filter_label.setAlignment(QtCore.Qt.AlignCenter)

        self.outer_filter_spin_box.setAccelerated(True)
        self.outer_filter_spin_box.setMaximum(100.0)
        self.outer_filter_spin_box.setSingleStep(0.1)

        self.jump_label.setFont(FONT)
        self.jump_label.setAlignment(QtCore.Qt.AlignCenter)

        self.jump_spin_box.setMaximum(0)

        self.scale_spin_box.setProperty("value", 1.00)
        self.scale_spin_box.setSingleStep(0.1)

        self.scale_filter_jump_frame_layout.addWidget(self.scale_label, 0, 0, 1, 1)
        self.scale_filter_jump_frame_layout.addWidget(self.outer_filter_label, 1, 0, 1, 1)
        self.scale_filter_jump_frame_layout.addWidget(self.outer_filter_spin_box, 1, 1, 1, 1)
        self.scale_filter_jump_frame_layout.addWidget(self.jump_label, 2, 0, 1, 1)
        self.scale_filter_jump_frame_layout.addWidget(self.jump_spin_box, 2, 1, 1, 1)
        self.scale_filter_jump_frame_layout.addWidget(self.scale_spin_box, 0, 1, 1, 1)

        self.settings_widget_layout.addWidget(self.scale_filter_jump_frame, 4, 3, 1, 1)

        self.roi_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.roi_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        FONT.setPointSize(13)
        self.reset_roi_button.setFont(FONT)
        self.reset_roi_button.setCursor(QtCore.Qt.PointingHandCursor)

        self.roi_frame_layout.addWidget(self.reset_roi_button, 2, 0, 1, 1)

        self.select_roi_button.setFont(FONT)
        self.select_roi_button.setCursor(QtCore.Qt.PointingHandCursor)

        self.roi_frame_layout.addWidget(self.select_roi_button, 0, 0, 1, 1)

        self.settings_widget_layout.addWidget(self.roi_frame, 5, 3, 1, 1)

        self.type_value_frame.setEnabled(True)
        self.type_value_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.type_value_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.value_spin_box.setCursor(QtCore.Qt.PointingHandCursor)
        self.value_spin_box.setAccelerated(True)
        self.value_spin_box.setMaximum(100.0)
        self.value_spin_box.setSingleStep(0.1)

        self.type_value_frame_layout.addWidget(self.value_spin_box, 2, 1, 1, 1)

        FONT.setPointSize(10)
        self.type_label.setFont(FONT)
        self.type_label.setAlignment(QtCore.Qt.AlignCenter)

        self.type_value_frame_layout.addWidget(self.type_label, 0, 0, 1, 1)

        self.value_label.setFont(FONT)
        self.value_label.setAlignment(QtCore.Qt.AlignCenter)

        self.type_value_frame_layout.addWidget(self.value_label, 2, 0, 1, 1)

        self.type_combo_box.addItem('0')
        self.type_combo_box.addItem('1')
        self.type_combo_box.addItem('2')
        self.type_combo_box.addItem('3')

        self.type_value_frame_layout.addWidget(self.type_combo_box, 0, 1, 1, 1)

        self.settings_widget_layout.addWidget(self.type_value_frame, 3, 3, 1, 1)

        self.spacing_frame.setCursor(QtCore.Qt.PointingHandCursor)
        self.spacing_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.spacing_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.horizontal_combo_box.addItem('8')
        self.horizontal_combo_box.addItem('16')
        self.horizontal_combo_box.addItem('32')
        self.horizontal_combo_box.addItem('64')
        self.horizontal_combo_box.addItem('128')
        self.horizontal_combo_box.addItem('256')
        self.horizontal_combo_box.addItem('512')

        self.spacing_frame_layout.addWidget(self.horizontal_combo_box, 2, 1, 1, 1)
        self.spacing_frame_layout.addItem(
            QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum), 2, 2, 1, 1)

        self.vertical_combo_box.addItem('8')
        self.vertical_combo_box.addItem('16')
        self.vertical_combo_box.addItem('32')
        self.vertical_combo_box.addItem('64')
        self.vertical_combo_box.addItem('128')
        self.vertical_combo_box.addItem('256')
        self.vertical_combo_box.addItem('512')

        self.spacing_frame_layout.addWidget(self.vertical_combo_box, 2, 3, 1, 1)

        self.vertical_label.setFont(FONT)
        self.vertical_label.setAlignment(QtCore.Qt.AlignCenter)

        self.spacing_frame_layout.addWidget(self.vertical_label, 1, 3, 1, 1)

        self.horizontal_label.setFont(FONT)
        self.horizontal_label.setAlignment(QtCore.Qt.AlignCenter)

        self.spacing_frame_layout.addWidget(self.horizontal_label, 1, 1, 1, 1)

        self.spacing_label.setFont(FONT)
        self.spacing_label.setAlignment(QtCore.Qt.AlignCenter)

        self.spacing_frame_layout.addWidget(self.spacing_label, 0, 1, 1, 3)

        self.settings_widget_layout.addWidget(self.spacing_frame, 1, 3, 1, 1)

        self.interrogation_winsize_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.interrogation_winsize_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.height_label.setFont(FONT)
        self.height_label.setAlignment(QtCore.Qt.AlignCenter)

        self.width_label.setFont(FONT)
        self.width_label.setAlignment(QtCore.Qt.AlignCenter)

        self.width_combo_box.addItem('8')
        self.width_combo_box.addItem('16')
        self.width_combo_box.addItem('32')
        self.width_combo_box.addItem('64')
        self.width_combo_box.addItem('128')
        self.width_combo_box.addItem('256')
        self.width_combo_box.addItem('512')

        self.height_combo_box.addItem('8')
        self.height_combo_box.addItem('16')
        self.height_combo_box.addItem('32')
        self.height_combo_box.addItem('64')
        self.height_combo_box.addItem('128')
        self.height_combo_box.addItem('256')
        self.height_combo_box.addItem('512')

        FONT.setPointSize(11)

        self.interrogation_winsize_label.setFont(FONT)
        self.interrogation_winsize_label.setAlignment(QtCore.Qt.AlignCenter)

        self.interrogation_winsize_frame_layout.addWidget(self.interrogation_winsize_label, 0, 0, 1, 3)
        self.interrogation_winsize_frame_layout.addWidget(self.height_label, 1, 2, 1, 1)
        self.interrogation_winsize_frame_layout.addWidget(self.width_label, 1, 0, 1, 1)
        self.interrogation_winsize_frame_layout.addWidget(self.width_combo_box, 3, 0, 1, 1)
        self.interrogation_winsize_frame_layout.addWidget(self.height_combo_box, 3, 2, 1, 1)
        self.interrogation_winsize_frame_layout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum), 2, 1, 1, 1)

        self.settings_widget_layout.addWidget(self.interrogation_winsize_frame, 0, 3, 1, 1)

        self.settings_dock_widget.setWidget(self.settings_widget)
        self.main_window.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.settings_dock_widget)

        self.start_stop_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.start_stop_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.start_button.setFont(FONT)
        self.start_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.stop_button.setFont(FONT)
        self.stop_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.start_stop_frame_layout.addWidget(self.start_button, 0, 0, 1, 1)
        self.start_stop_frame_layout.addWidget(self.stop_button, 1, 0, 1, 1)
        self.settings_widget_layout.addWidget(self.start_stop_frame, 6, 3, 1, 1)

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

        self.main_widget_layout.addWidget(self.image_pages, 1, 0, 1, 4)
        self.main_widget_layout.addWidget(self.right_button, 2, 3, 1, 1)
        self.main_widget_layout.addWidget(self.left_button, 2, 1, 1, 1)
        self.main_widget_layout.addWidget(self.current_image_number, 2, 2, 1, 1)
        self.main_widget_layout.addItem(left_right_buttons_spacer, 2, 0, 1, 1)

        self.menuBar.setGeometry(QtCore.QRect(0, 0, 866, 21))
        self.main_window.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menu_bar_file.menuAction())

        self.file_action.setShortcut('Ctrl+F')
        self.file_action.setStatusTip('manage files')

        self.menu_bar_file.addAction(self.file_action)

        self.main_window.setCentralWidget(self.main_widget)

        self.text_setup()

        self.left_button.clicked.connect(self.change_image_number_left)

        self.right_button.clicked.connect(self.change_image_number_right)

        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def text_setup(self):
        set_text = lambda x, text: x.setText(QtWidgets.QApplication.translate("MainWindow", text, None, -1))

        self.main_window.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "OpenPIV", None, -1))

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
        set_text(self.file_action, "file")
        set_text(self.left_button, "<")
        set_text(self.right_button, ">")
        set_text(self.current_image_number, "0")

        self.menu_bar_file.setTitle(QtWidgets.QApplication.translate("MainWindow", "file", None, -1))

    # function that changes the max and min of jump
    def change_jump_max_min(self):
        self.jump_spin_box.setMaximum(self.image_pages.count() - 1)
        self.jump_spin_box.setMinimum((-1) * (self.image_pages.count() - 1))

    # function that moves to the next left image
    def change_image_number_left(self):
        if int(self.current_image_number.text()) == 0:
            self.current_image_number.setText(
                QtWidgets.QApplication.translate("MainWindow", str(self.image_pages.count() - 1), None, -1))
            self.image_pages.setCurrentIndex(self.image_pages.count() - 1)
        else:
            self.current_image_number.setText(
                QtWidgets.QApplication.translate("MainWindow", str(self.image_pages.currentIndex() - 1), None, -1))
            self.image_pages.setCurrentIndex(self.image_pages.currentIndex() - 1)

    # function that moves to the next right image
    def change_image_number_right(self):
        if self.image_pages.currentIndex() == self.image_pages.count() - 1:
            self.current_image_number.setText(
                QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
            self.image_pages.setCurrentIndex(0)
        else:
            self.current_image_number.setText(
                QtWidgets.QApplication.translate("MainWindow", str(self.image_pages.currentIndex() + 1), None, -1))
            self.image_pages.setCurrentIndex(self.image_pages.currentIndex() + 1)


if __name__ == "__main__":
    # run the application
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_window_class = MainWindowClass(MainWindow)
    main_window_class.setting_dock_widget_setup()
    main_window_class.main_window_setup()
    main_window_class.default_image.setPixmap(QtGui.QPixmap("images/openpiv_logo.png"))
    MainWindow.show()
    sys.exit(app.exec_())
