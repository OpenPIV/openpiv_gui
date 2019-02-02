from PySide2 import QtCore, QtGui, QtWidgets

FONT = QtGui.QFont()
FONT.setFamily("Gill Sans MT")
FONT.setPointSize(10)
FONT.setWeight(75)
FONT.setItalic(True)
FONT.setBold(True)


class SettingsTab(object):
    def __init__(self):
        self.scroll_area = QtWidgets.QScrollArea()
        self.settings_tab = QtWidgets.QWidget()
        self.settings_widget_layout = QtWidgets.QGridLayout(self.settings_tab)
        self.settings_frame_4 = QtWidgets.QFrame(self.settings_tab)
        self.settings_frame_4_layout = QtWidgets.QGridLayout(self.settings_frame_4)
        self.dt_line_edit = QtWidgets.QLineEdit(self.settings_frame_4)
        self.dt_line_edit_label = QtWidgets.QLabel(self.settings_frame_4)
        self.scale_label = QtWidgets.QLabel(self.settings_frame_4)
        self.outer_filter_label = QtWidgets.QLabel(self.settings_frame_4)
        self.interactive_check_box = QtWidgets.QCheckBox(self.settings_frame_4)
        self.outer_filter_spin_box = QtWidgets.QDoubleSpinBox(self.settings_frame_4)
        self.jump_label = QtWidgets.QLabel(self.settings_frame_4)
        self.jump_line_edit = QtWidgets.QLineEdit(self.settings_frame_4)
        self.scale_spin_box = QtWidgets.QDoubleSpinBox(self.settings_frame_4)
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
        self.spacing_label = QtWidgets.QLabel(self.spacing_frame)
        self.interrogation_winsize_frame = QtWidgets.QFrame(self.settings_tab)
        self.interrogation_winsize_frame_layout = QtWidgets.QGridLayout(self.interrogation_winsize_frame)
        self.width_label_A = QtWidgets.QLabel(self.interrogation_winsize_frame)
        self.width_label_B = QtWidgets.QLabel(self.interrogation_winsize_frame)
        self.width_combo_box_a = QtWidgets.QComboBox(self.interrogation_winsize_frame)
        self.height_combo_box_a = QtWidgets.QComboBox(self.interrogation_winsize_frame)
        self.width_combo_box_b = QtWidgets.QComboBox(self.interrogation_winsize_frame)
        self.height_combo_box_b = QtWidgets.QComboBox(self.interrogation_winsize_frame)
        self.interrogation_winsize_label = QtWidgets.QLabel(self.interrogation_winsize_frame)
        self.start_stop_frame = QtWidgets.QFrame(self.settings_tab)
        self.start_stop_frame_layout = QtWidgets.QGridLayout(self.start_stop_frame)
        self.stop_button = QtWidgets.QPushButton(self.start_stop_frame)
        self.start_button = QtWidgets.QPushButton(self.start_stop_frame)
        self.jump_max = 0
        self.jump_min = 0

    def setting_widget_setup(self):
        self.scroll_area.setWidget(self.settings_tab)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area.adjustSize()

        self.settings_tab.setMinimumSize(QtCore.QSize(340, 800))
        self.settings_tab.setStyleSheet(
            "QDoubleSpinBox{border: 1px solid gray; padding: 2 13px; border-radius: 3px;}"
            "QComboBox{border: 1px solid gray; padding: 2 13px; border-radius: 3px;}"
            "QLineEdit{border: 1px solid gray; padding: 2 13px; border-radius: 3px;}"
            "QPushButton{border: 1px solid gray; padding: 2 13px; border-radius: 3px;}"
            "QFrame{border: 1px solid gray; padding: 2 13px; border-radius: 3px;}"
            "QLabel{border: 1px transparent; padding: 2 13px; border-radius: 3px;}")

        self.settings_frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.settings_frame_4.setFrameShape(QtWidgets.QFrame.Box)

        self.scale_label.setAlignment(QtCore.Qt.AlignCenter)

        self.outer_filter_label.setAlignment(QtCore.Qt.AlignCenter)

        self.outer_filter_spin_box.setAccelerated(True)
        self.outer_filter_spin_box.setMaximum(100.0)
        self.outer_filter_spin_box.setSingleStep(0.1)

        self.jump_label.setAlignment(QtCore.Qt.AlignCenter)

        self.scale_spin_box.setProperty("value", 1.000)
        self.scale_spin_box.setDecimals(3)
        self.scale_spin_box.setSingleStep(0.010)
        self.scale_spin_box.setAccelerated(True)

        self.dt_line_edit.setText("1.00")

        self.settings_frame_4_layout.addWidget(self.scale_label, 0, 0, 1, 1)
        self.settings_frame_4_layout.addWidget(self.outer_filter_label, 1, 0, 1, 1)
        self.settings_frame_4_layout.addWidget(self.outer_filter_spin_box, 1, 1, 1, 1)
        self.settings_frame_4_layout.addWidget(self.jump_label, 2, 0, 1, 1)
        self.settings_frame_4_layout.addWidget(self.jump_line_edit, 2, 1, 1, 1)
        self.settings_frame_4_layout.addWidget(self.scale_spin_box, 0, 1, 1, 1)
        self.settings_frame_4_layout.addWidget(self.interactive_check_box, 3, 0, 1, 1)
        self.settings_frame_4_layout.addWidget(self.dt_line_edit, 3, 1, 1, 1)
        self.settings_frame_4_layout.addWidget(self.dt_line_edit_label, 3, 0, 1, 1)
        self.settings_frame_4_layout.addWidget(self.interactive_check_box, 4, 0, 1, 1)

        self.settings_frame_4.setMinimumSize(60, 100)

        self.roi_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.roi_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        FONT.setPointSize(13)
        self.reset_roi_button.setFont(FONT)
        self.reset_roi_button.setCursor(QtCore.Qt.PointingHandCursor)

        self.roi_frame_layout.addWidget(self.reset_roi_button, 2, 0, 1, 1)

        self.select_roi_button.setFont(FONT)
        self.select_roi_button.setCursor(QtCore.Qt.PointingHandCursor)

        self.roi_frame_layout.addWidget(self.select_roi_button, 0, 0, 1, 1)

        self.type_value_frame.setEnabled(True)
        self.type_value_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.type_value_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.value_spin_box.setAccelerated(True)
        self.value_spin_box.setMaximum(100.00)
        self.value_spin_box.setSingleStep(0.10)

        self.type_value_frame_layout.addWidget(self.value_spin_box, 2, 1, 1, 1)

        FONT.setPointSize(10)

        self.type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dt_line_edit_label.setAlignment(QtCore.Qt.AlignCenter)

        self.type_value_frame_layout.addWidget(self.type_label, 0, 0, 1, 1)

        self.value_label.setAlignment(QtCore.Qt.AlignCenter)

        self.type_value_frame_layout.addWidget(self.value_label, 2, 0, 1, 1)

        self.type_combo_box.addItem('1')
        self.type_combo_box.addItem('2')
        self.type_combo_box.addItem('3')
        self.type_combo_box.setCurrentIndex(0)

        self.value_spin_box.setValue(1.00)

        self.type_value_frame_layout.addWidget(self.type_combo_box, 0, 1, 1, 1)

        self.spacing_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.spacing_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.horizontal_combo_box.setToolTip("Horizontal")
        self.horizontal_combo_box.addItem('8')
        self.horizontal_combo_box.addItem('16')
        self.horizontal_combo_box.addItem('32')
        self.horizontal_combo_box.addItem('64')
        self.horizontal_combo_box.addItem('128')
        self.horizontal_combo_box.addItem('256')
        self.horizontal_combo_box.addItem('512')
        self.horizontal_combo_box.setCurrentIndex(1)

        self.spacing_frame_layout.addWidget(self.horizontal_combo_box, 1, 0, 1, 1)

        self.vertical_combo_box.setToolTip("Vertical")
        self.vertical_combo_box.addItem('8')
        self.vertical_combo_box.addItem('16')
        self.vertical_combo_box.addItem('32')
        self.vertical_combo_box.addItem('64')
        self.vertical_combo_box.addItem('128')
        self.vertical_combo_box.addItem('256')
        self.vertical_combo_box.addItem('512')
        self.vertical_combo_box.setCurrentIndex(1)

        self.spacing_frame_layout.addWidget(self.vertical_combo_box, 1, 1, 1, 1)

        self.spacing_frame.setToolTip("Horizontal and Vertical Values")

        self.spacing_label.setFont(FONT)
        self.spacing_label.setAlignment(QtCore.Qt.AlignCenter)

        self.spacing_frame_layout.addWidget(self.spacing_label, 0, 0, 1, 2)

        self.interrogation_winsize_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.interrogation_winsize_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.width_combo_box_a.setToolTip("Image A Width")
        self.width_combo_box_a.addItem('8')
        self.width_combo_box_a.addItem('16')
        self.width_combo_box_a.addItem('32')
        self.width_combo_box_a.addItem('64')
        self.width_combo_box_a.addItem('128')
        self.width_combo_box_a.addItem('256')
        self.width_combo_box_a.addItem('512')
        self.width_combo_box_a.setCurrentIndex(2)

        self.height_combo_box_a.setToolTip("Image A Height")
        self.height_combo_box_a.addItem('8')
        self.height_combo_box_a.addItem('16')
        self.height_combo_box_a.addItem('32')
        self.height_combo_box_a.addItem('64')
        self.height_combo_box_a.addItem('128')
        self.height_combo_box_a.addItem('256')
        self.height_combo_box_a.addItem('512')
        self.height_combo_box_a.setCurrentIndex(2)

        self.width_combo_box_b.setToolTip("Image B Width")
        self.width_combo_box_b.addItem('8')
        self.width_combo_box_b.addItem('16')
        self.width_combo_box_b.addItem('32')
        self.width_combo_box_b.addItem('64')
        self.width_combo_box_b.addItem('128')
        self.width_combo_box_b.addItem('256')
        self.width_combo_box_b.addItem('512')
        self.width_combo_box_b.setCurrentIndex(3)

        self.height_combo_box_b.setToolTip("Image B Height")
        self.height_combo_box_b.addItem('8')
        self.height_combo_box_b.addItem('16')
        self.height_combo_box_b.addItem('32')
        self.height_combo_box_b.addItem('64')
        self.height_combo_box_b.addItem('128')
        self.height_combo_box_b.addItem('256')
        self.height_combo_box_b.addItem('512')
        self.height_combo_box_b.setCurrentIndex(3)

        FONT.setPointSize(11)

        self.interrogation_winsize_label.setFont(FONT)
        self.interrogation_winsize_label.setAlignment(QtCore.Qt.AlignCenter)

        self.interrogation_winsize_frame.setToolTip("Image A and B Width and Height values")
        self.interrogation_winsize_frame_layout.addWidget(self.interrogation_winsize_label, 0, 0, 1, 5)
        self.interrogation_winsize_frame_layout.addWidget(self.width_label_A, 1, 0, 1, 1)
        self.interrogation_winsize_frame_layout.addWidget(self.width_label_B, 2, 0, 1, 1)
        self.interrogation_winsize_frame_layout.addWidget(self.width_combo_box_a, 1, 1, 1, 2)
        self.interrogation_winsize_frame_layout.addWidget(self.height_combo_box_a, 1, 3, 1, 2)
        self.interrogation_winsize_frame_layout.addWidget(self.width_combo_box_b, 2, 1, 1, 2)
        self.interrogation_winsize_frame_layout.addWidget(self.height_combo_box_b, 2, 3, 1, 2)

        self.start_stop_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.start_stop_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        FONT.setPointSize(13)

        self.start_button.setFont(FONT)
        self.stop_button.setFont(FONT)
        self.start_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.stop_button.setCursor(QtCore.Qt.PointingHandCursor)

        self.start_stop_frame_layout.addWidget(self.start_button, 0, 0, 1, 1)
        self.start_stop_frame_layout.addWidget(self.stop_button, 1, 0, 1, 1)

        self.settings_widget_layout.addWidget(self.interrogation_winsize_frame, 0, 3, 1, 1)
        self.settings_widget_layout.addWidget(self.spacing_frame, 1, 3, 1, 1)
        self.settings_widget_layout.addWidget(self.type_value_frame, 2, 3, 1, 1)
        self.settings_widget_layout.addWidget(self.settings_frame_4, 3, 3, 2, 1)
        self.settings_widget_layout.addWidget(self.roi_frame, 5, 3, 1, 1)
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
        set_text(self.spacing_label, "spacing/Overlap")
        set_text(self.width_label_A, "A")
        set_text(self.width_label_B, "B")
        set_text(self.interrogation_winsize_label, "Interrogation window size")
        set_text(self.interactive_check_box, "Interactive")
        set_text(self.dt_line_edit_label, "dt:")


if __name__ == "__main__":
    # run the application
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window_class = SettingsTab()
    main_window_class.setting_widget_setup()
    main_window_class.settings_tab.show()
    sys.exit(app.exec_())
