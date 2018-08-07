from PySide2 import QtCore, QtGui, QtWidgets

FONT = QtGui.QFont()
FONT.setFamily("Gill Sans MT")
FONT.setPointSize(10)
FONT.setWeight(75)
FONT.setItalic(True)
FONT.setBold(True)


class SettingsTab(object):
    def __init__(self):
        self.settings_tab = QtWidgets.QTabBar()
        self.settings_widget_layout = QtWidgets.QGridLayout(self.settings_tab)
        self.scale_filter_jump_frame = QtWidgets.QFrame(self.settings_tab)
        self.scale_filter_jump_frame_layout = QtWidgets.QGridLayout(self.scale_filter_jump_frame)
        self.scale_label = QtWidgets.QLabel(self.scale_filter_jump_frame)
        self.outer_filter_label = QtWidgets.QLabel(self.scale_filter_jump_frame)
        self.outer_filter_spin_box = QtWidgets.QDoubleSpinBox(self.scale_filter_jump_frame)
        self.jump_label = QtWidgets.QLabel(self.scale_filter_jump_frame)
        self.jump_spin_box = QtWidgets.QSpinBox(self.scale_filter_jump_frame)
        self.scale_spin_box = QtWidgets.QDoubleSpinBox(self.scale_filter_jump_frame)
        self.roi_frame = QtWidgets.QFrame(self.settings_tab)
        self.roi_frame_layout = QtWidgets.QGridLayout(self.roi_frame)
        self.reset_roi_button = QtWidgets.QPushButton(self.roi_frame)
        self.select_roi_button = QtWidgets.QPushButton(self.roi_frame)
        self.type_value_frame = QtWidgets.QFrame(self.settings_tab)
        self.type_value_frame_layout = QtWidgets.QGridLayout(self.type_value_frame)
        self.value_spin_box = QtWidgets.QDoubleSpinBox(self.type_value_frame)
        self.type_label = QtWidgets.QLabel(self.type_value_frame)
        self.value_label = QtWidgets.QLabel(self.type_value_frame)
        self.spacing_frame = QtWidgets.QFrame(self.settings_tab)
        self.type_combo_box = QtWidgets.QComboBox(self.type_value_frame)
        self.spacing_frame_layout = QtWidgets.QGridLayout(self.spacing_frame)
        self.horizontal_combo_box = QtWidgets.QComboBox(self.spacing_frame)
        self.vertical_combo_box = QtWidgets.QComboBox(self.spacing_frame)
        self.vertical_label = QtWidgets.QLabel(self.spacing_frame)
        self.horizontal_label = QtWidgets.QLabel(self.spacing_frame)
        self.spacing_label = QtWidgets.QLabel(self.spacing_frame)
        self.interrogation_winsize_frame = QtWidgets.QFrame(self.settings_tab)
        self.interrogation_winsize_frame_layout = QtWidgets.QGridLayout(self.interrogation_winsize_frame)
        self.height_label = QtWidgets.QLabel(self.interrogation_winsize_frame)
        self.width_label = QtWidgets.QLabel(self.interrogation_winsize_frame)
        self.width_combo_box_a = QtWidgets.QComboBox(self.interrogation_winsize_frame)
        self.height_combo_box_a = QtWidgets.QComboBox(self.interrogation_winsize_frame)
        self.width_combo_box_b = QtWidgets.QComboBox(self.interrogation_winsize_frame)
        self.height_combo_box_b = QtWidgets.QComboBox(self.interrogation_winsize_frame)
        self.interrogation_winsize_label = QtWidgets.QLabel(self.interrogation_winsize_frame)
        self.start_stop_frame = QtWidgets.QFrame(self.settings_tab)
        self.start_stop_frame_layout = QtWidgets.QGridLayout(self.start_stop_frame)
        self.stop_button = QtWidgets.QPushButton(self.start_stop_frame)
        self.start_button = QtWidgets.QPushButton(self.start_stop_frame)

    def setting_widget_setup(self):
        # the set tab bar line is to make the tab text go horizontal

        self.scale_filter_jump_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.scale_filter_jump_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.scale_label.setAlignment(QtCore.Qt.AlignCenter)

        self.outer_filter_label.setAlignment(QtCore.Qt.AlignCenter)

        self.outer_filter_spin_box.setAccelerated(True)
        self.outer_filter_spin_box.setMaximum(100.0)
        self.outer_filter_spin_box.setSingleStep(0.1)

        self.jump_label.setAlignment(QtCore.Qt.AlignCenter)

        self.jump_spin_box.setMaximum(0)

        self.scale_spin_box.setProperty("value", 1.000)
        self.scale_spin_box.setDecimals(3)
        self.scale_spin_box.setSingleStep(0.010)
        self.scale_spin_box.setAccelerated(True)

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

        self.value_spin_box.setAccelerated(True)
        self.value_spin_box.setMaximum(100.00)
        self.value_spin_box.setSingleStep(0.10)

        self.type_value_frame_layout.addWidget(self.value_spin_box, 2, 1, 1, 1)

        FONT.setPointSize(10)

        self.type_label.setAlignment(QtCore.Qt.AlignCenter)

        self.type_value_frame_layout.addWidget(self.type_label, 0, 0, 1, 1)

        self.value_label.setAlignment(QtCore.Qt.AlignCenter)

        self.type_value_frame_layout.addWidget(self.value_label, 2, 0, 1, 1)

        self.type_combo_box.addItem('0')
        self.type_combo_box.addItem('1')
        self.type_combo_box.addItem('2')
        self.type_combo_box.addItem('3')

        self.type_value_frame_layout.addWidget(self.type_combo_box, 0, 1, 1, 1)

        self.settings_widget_layout.addWidget(self.type_value_frame, 3, 3, 1, 1)

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

        self.vertical_label.setAlignment(QtCore.Qt.AlignCenter)

        self.spacing_frame_layout.addWidget(self.vertical_label, 1, 3, 1, 1)

        self.horizontal_label.setAlignment(QtCore.Qt.AlignCenter)

        self.spacing_frame_layout.addWidget(self.horizontal_label, 1, 1, 1, 1)

        self.spacing_label.setFont(FONT)
        self.spacing_label.setAlignment(QtCore.Qt.AlignCenter)

        self.spacing_frame_layout.addWidget(self.spacing_label, 0, 1, 1, 3)

        self.settings_widget_layout.addWidget(self.spacing_frame, 1, 3, 1, 1)

        self.interrogation_winsize_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.interrogation_winsize_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.height_label.setAlignment(QtCore.Qt.AlignCenter)

        self.width_label.setAlignment(QtCore.Qt.AlignCenter)

        self.width_combo_box_a.addItem('8')
        self.width_combo_box_a.addItem('16')
        self.width_combo_box_a.addItem('32')
        self.width_combo_box_a.addItem('64')
        self.width_combo_box_a.addItem('128')
        self.width_combo_box_a.addItem('256')
        self.width_combo_box_a.addItem('512')

        self.height_combo_box_a.addItem('8')
        self.height_combo_box_a.addItem('16')
        self.height_combo_box_a.addItem('32')
        self.height_combo_box_a.addItem('64')
        self.height_combo_box_a.addItem('128')
        self.height_combo_box_a.addItem('256')
        self.height_combo_box_a.addItem('512')

        self.width_combo_box_b.addItem('8')
        self.width_combo_box_b.addItem('16')
        self.width_combo_box_b.addItem('32')
        self.width_combo_box_b.addItem('64')
        self.width_combo_box_b.addItem('128')
        self.width_combo_box_b.addItem('256')
        self.width_combo_box_b.addItem('512')

        self.height_combo_box_b.addItem('8')
        self.height_combo_box_b.addItem('16')
        self.height_combo_box_b.addItem('32')
        self.height_combo_box_b.addItem('64')
        self.height_combo_box_b.addItem('128')
        self.height_combo_box_b.addItem('256')
        self.height_combo_box_b.addItem('512')

        FONT.setPointSize(11)

        self.interrogation_winsize_label.setFont(FONT)
        self.interrogation_winsize_label.setAlignment(QtCore.Qt.AlignCenter)

        self.interrogation_winsize_frame_layout.addWidget(self.interrogation_winsize_label, 0, 0, 1, 3)
        self.interrogation_winsize_frame_layout.addWidget(self.height_label, 1, 2, 1, 1)
        self.interrogation_winsize_frame_layout.addWidget(self.width_label, 1, 0, 1, 1)
        self.interrogation_winsize_frame_layout.addWidget(self.width_combo_box_a, 2, 0, 1, 1)
        self.interrogation_winsize_frame_layout.addWidget(self.height_combo_box_a, 2, 2, 1, 1)
        self.interrogation_winsize_frame_layout.addWidget(self.width_combo_box_b, 3, 0, 1, 1)
        self.interrogation_winsize_frame_layout.addWidget(self.height_combo_box_b, 3, 2, 1, 1)
        self.interrogation_winsize_frame_layout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum), 2, 1, 1, 1)

        self.settings_widget_layout.addWidget(self.interrogation_winsize_frame, 0, 3, 1, 1)

        self.start_stop_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.start_stop_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        FONT.setPointSize(13)

        self.start_button.setFont(FONT)
        self.stop_button.setFont(FONT)
        self.start_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.stop_button.setCursor(QtCore.Qt.PointingHandCursor)

        self.start_stop_frame_layout.addWidget(self.start_button, 0, 0, 1, 1)
        self.start_stop_frame_layout.addWidget(self.stop_button, 1, 0, 1, 1)
        self.settings_widget_layout.addWidget(self.start_stop_frame, 6, 3, 1, 1)

        self.text_setup()

        QtCore.QMetaObject.connectSlotsByName(self.settings_tab)

    def text_setup(self):
        set_text = lambda x, text: x.setText(text)

        self.settings_tab.setWindowTitle("OpenPIV")

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


if __name__ == "__main__":
    # run the application
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window_class = SettingsTab()
    main_window_class.setting_widget_setup()
    main_window_class.settings_tab.show()
    sys.exit(app.exec_())
