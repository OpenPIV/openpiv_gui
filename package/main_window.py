from PySide2 import QtCore, QtGui, QtWidgets
import sys
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
        self.tab_widget = QtWidgets.QTabWidget(self.main_widget)
        self.stop_button = QtWidgets.QPushButton(self.main_widget)
        self.start_button = QtWidgets.QPushButton(self.main_widget)
        self.piv_tab = QtWidgets.QWidget()
        self.piv_layout = QtWidgets.QVBoxLayout(self.piv_tab)

        # The images_widget is a stack widget (when you add another picture you can move between the pictures)
        self.images_widget = QtWidgets.QStackedWidget(self.piv_tab)
        self.image_pages = QtWidgets.QWidget()
        self.image_pages_layout = QtWidgets.QGridLayout(self.image_pages)

        # The default_image is just that there will be something shown in the image frame all the time
        self.default_image = QtWidgets.QLabel(self.image_pages)

        self.file_tab = QtWidgets.QWidget()
        self.file_tab_layout = QtWidgets.QGridLayout(self.file_tab)

        # I putted the settings in a dock widget so you could take the settings out so that it will give you more space
        # and you can dock the setting in the left and right sides of the window
        # *** from here to the next *** are all in the settings_dock_widget
        self.settings_dock_widget = QtWidgets.QDockWidget(self.main_window)
        self.settings_widget = QtWidgets.QWidget()
        self.settings_widget_layout = QtWidgets.QGridLayout(self.settings_widget)
        self.setting_box = QtWidgets.QGroupBox(self.settings_widget)
        self.settings_box_layout = QtWidgets.QGridLayout(self.setting_box)
        self.scale_filter_jump_frame = QtWidgets.QFrame(self.setting_box)
        self.scale_filter_jump_frame_layout = QtWidgets.QGridLayout(self.scale_filter_jump_frame)
        self.scale_label = QtWidgets.QLabel(self.scale_filter_jump_frame)
        self.outer_filter_label = QtWidgets.QLabel(self.scale_filter_jump_frame)
        self.outer_filter_spin_box = QtWidgets.QDoubleSpinBox(self.scale_filter_jump_frame)
        self.jump_label = QtWidgets.QLabel(self.scale_filter_jump_frame)
        self.jump_spin_box = QtWidgets.QSpinBox(self.scale_filter_jump_frame)
        self.scale_spin_box = QtWidgets.QSpinBox(self.scale_filter_jump_frame)
        self.roi_frame = QtWidgets.QFrame(self.setting_box)
        self.roi_frame_layout = QtWidgets.QGridLayout(self.roi_frame)
        self.reset_roi_button = QtWidgets.QPushButton(self.roi_frame)
        self.select_roi_button = QtWidgets.QPushButton(self.roi_frame)
        self.type_value_frame = QtWidgets.QFrame(self.setting_box)
        self.type_value_frame_layout = QtWidgets.QGridLayout(self.type_value_frame)
        self.value_spin_box = QtWidgets.QDoubleSpinBox(self.type_value_frame)
        self.type_label = QtWidgets.QLabel(self.type_value_frame)
        self.value_label = QtWidgets.QLabel(self.type_value_frame)
        self.spacing_frame = QtWidgets.QFrame(self.setting_box)
        self.type_spin_box = QtWidgets.QDoubleSpinBox(self.type_value_frame)
        self.spacing_frame_layout = QtWidgets.QGridLayout(self.spacing_frame)
        self.horizontal_spin_box = QtWidgets.QDoubleSpinBox(self.spacing_frame)
        self.vertical_spin_box = QtWidgets.QDoubleSpinBox(self.spacing_frame)
        self.vertical_label = QtWidgets.QLabel(self.spacing_frame)
        self.horizontal_label = QtWidgets.QLabel(self.spacing_frame)
        self.spacing_label = QtWidgets.QLabel(self.spacing_frame)
        self.interrogation_winsize_frame = QtWidgets.QFrame(self.setting_box)
        self.interrogation_winsize_frame_layout = QtWidgets.QGridLayout(self.interrogation_winsize_frame)
        self.height_label = QtWidgets.QLabel(self.interrogation_winsize_frame)
        self.width_label = QtWidgets.QLabel(self.interrogation_winsize_frame)
        self.width_spin_box = QtWidgets.QDoubleSpinBox(self.interrogation_winsize_frame)
        self.height_spin_box = QtWidgets.QDoubleSpinBox(self.interrogation_winsize_frame)
        self.interrogation_winsize_label = QtWidgets.QLabel(self.interrogation_winsize_frame)
        # ***

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

        self.scale_spin_box.setProperty("value", 1)

        self.scale_filter_jump_frame_layout.addWidget(self.scale_label, 0, 0, 1, 1)
        self.scale_filter_jump_frame_layout.addWidget(self.outer_filter_label, 1, 0, 1, 1)
        self.scale_filter_jump_frame_layout.addWidget(self.outer_filter_spin_box, 1, 1, 1, 1)
        self.scale_filter_jump_frame_layout.addWidget(self.jump_label, 2, 0, 1, 1)
        self.scale_filter_jump_frame_layout.addWidget(self.jump_spin_box, 2, 1, 1, 1)
        self.scale_filter_jump_frame_layout.addWidget(self.scale_spin_box, 0, 1, 1, 1)

        self.settings_box_layout.addWidget(self.scale_filter_jump_frame, 4, 3, 1, 1)

        self.roi_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.roi_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        FONT.setPointSize(13)
        self.reset_roi_button.setFont(FONT)
        self.reset_roi_button.setCursor(QtCore.Qt.PointingHandCursor)

        self.roi_frame_layout.addWidget(self.reset_roi_button, 2, 0, 1, 1)

        self.select_roi_button.setFont(FONT)
        self.select_roi_button.setCursor(QtCore.Qt.PointingHandCursor)

        self.roi_frame_layout.addWidget(self.select_roi_button, 0, 0, 1, 1)

        self.settings_box_layout.addWidget(self.roi_frame, 5, 3, 1, 1)

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

        self.type_spin_box.setAccelerated(True)
        self.type_spin_box.setMaximum(100.0)
        self.type_spin_box.setSingleStep(0.1)

        self.type_value_frame_layout.addWidget(self.type_spin_box, 0, 1, 1, 1)

        self.settings_box_layout.addWidget(self.type_value_frame, 3, 3, 1, 1)

        self.spacing_frame.setCursor(QtCore.Qt.PointingHandCursor)
        self.spacing_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.spacing_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.horizontal_spin_box.setAccelerated(True)
        self.horizontal_spin_box.setMaximum(100.0)
        self.horizontal_spin_box.setSingleStep(1.0)

        self.spacing_frame_layout.addWidget(self.horizontal_spin_box, 2, 1, 1, 1)
        self.spacing_frame_layout.addItem(
            QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum), 2, 2, 1, 1)

        self.vertical_spin_box.setAccelerated(True)
        self.vertical_spin_box.setMaximum(100.0)
        self.vertical_spin_box.setSingleStep(1.0)

        self.spacing_frame_layout.addWidget(self.vertical_spin_box, 2, 3, 1, 1)

        self.vertical_label.setFont(FONT)
        self.vertical_label.setAlignment(QtCore.Qt.AlignCenter)

        self.spacing_frame_layout.addWidget(self.vertical_label, 1, 3, 1, 1)

        self.horizontal_label.setFont(FONT)
        self.horizontal_label.setAlignment(QtCore.Qt.AlignCenter)

        self.spacing_frame_layout.addWidget(self.horizontal_label, 1, 1, 1, 1)

        self.spacing_label.setFont(FONT)
        self.spacing_label.setAlignment(QtCore.Qt.AlignCenter)

        self.spacing_frame_layout.addWidget(self.spacing_label, 0, 1, 1, 3)

        self.settings_box_layout.addWidget(self.spacing_frame, 1, 3, 1, 1)

        self.interrogation_winsize_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.interrogation_winsize_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.height_label.setFont(FONT)
        self.height_label.setAlignment(QtCore.Qt.AlignCenter)

        self.width_label.setFont(FONT)
        self.width_label.setAlignment(QtCore.Qt.AlignCenter)

        self.width_spin_box.setAccelerated(True)
        self.width_spin_box.setMaximum(100.0)
        self.width_spin_box.setSingleStep(1.0)

        self.height_spin_box.setAccelerated(True)
        self.height_spin_box.setMaximum(100.0)
        self.height_spin_box.setSingleStep(1.0)

        FONT.setPointSize(11)

        self.interrogation_winsize_label.setFont(FONT)
        self.interrogation_winsize_label.setAlignment(QtCore.Qt.AlignCenter)

        self.interrogation_winsize_frame_layout.addWidget(self.interrogation_winsize_label, 0, 0, 1, 3)
        self.interrogation_winsize_frame_layout.addWidget(self.height_label, 1, 2, 1, 1)
        self.interrogation_winsize_frame_layout.addWidget(self.width_label, 1, 0, 1, 1)
        self.interrogation_winsize_frame_layout.addWidget(self.width_spin_box, 3, 0, 1, 1)
        self.interrogation_winsize_frame_layout.addWidget(self.height_spin_box, 3, 2, 1, 1)
        self.interrogation_winsize_frame_layout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum), 2, 1, 1, 1)

        self.settings_box_layout.addWidget(self.interrogation_winsize_frame, 0, 3, 1, 1)

        self.settings_widget_layout.addWidget(self.setting_box, 0, 0, 1, 1)

        self.settings_dock_widget.setWidget(self.settings_widget)
        self.main_window.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.settings_dock_widget)

    def main_window_setup(self):
        self.main_window.resize(866, 683)
        self.main_window.setObjectName("main_window")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/openpiv_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.main_window.setWindowIcon(icon)

        self.stop_button.setFont(FONT)
        self.stop_button.setCursor(QtCore.Qt.PointingHandCursor)

        self.start_button.setFont(FONT)
        self.start_button.setCursor(QtCore.Qt.PointingHandCursor)

        self.tab_widget.setStyleSheet("background-color: rgb(240, 240, 240);")

        self.default_image.setPixmap(QtGui.QPixmap("images/openpiv_logo.png"))
        self.default_image.setAlignment(QtCore.Qt.AlignCenter)

        self.image_pages_layout.addWidget(self.default_image, 0, 0, 1, 1)

        self.images_widget.setLineWidth(2)
        self.images_widget.addWidget(self.image_pages)

        self.piv_layout.addWidget(self.images_widget)

        self.tab_widget.addTab(self.piv_tab, "")
        self.tab_widget.addTab(self.file_tab, "")

        self.main_widget_layout.addItem(
            QtWidgets.QSpacerItem(1900, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum), 1, 1, 1, 1)
        self.main_widget_layout.addWidget(self.start_button, 1, 0, 1, 1)
        self.main_widget_layout.addWidget(self.stop_button, 1, 2, 1, 1)
        self.main_widget_layout.addWidget(self.tab_widget, 0, 0, 1, 3)

        self.main_window.setCentralWidget(self.main_widget)

        self.text_setup(self.main_window)

        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def text_setup(self, main_window):
        set_text = lambda x, text: x.setText(QtWidgets.QApplication.translate("MainWindow", text, None, -1))

        main_window.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "OpenPIV", None, -1))

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

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.piv_tab),
                                   QtWidgets.QApplication.translate("MainWindow", "PIV", None,
                                                                    -1))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.file_tab),
                                   QtWidgets.QApplication.translate("MainWindow", "Files", None, -1))
        self.setting_box.setTitle(QtWidgets.QApplication.translate("MainWindow", "Setting", None, -1))


if __name__ == "__main__":
    # run the application
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_window_class = MainWindowClass(MainWindow)
    main_window_class.setting_dock_widget_setup()
    main_window_class.main_window_setup()
    MainWindow.show()
    sys.exit(app.exec_())
