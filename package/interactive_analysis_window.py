from PySide2 import QtCore, QtGui, QtWidgets


class InteractiveAnalysisWindow(object):
    def __init__(self):
        self.interactive_analysis_window = QtWidgets.QDialog()
        self.interactive_analysis_window_layout = QtWidgets.QGridLayout(self.interactive_analysis_window)
        self.piv_scroll_area = QtWidgets.QScrollArea(self.interactive_analysis_window)
        self.piv_scroll_area_widget = QtWidgets.QWidget()
        self.piv_scroll_area_widget_layout = QtWidgets.QGridLayout(self.piv_scroll_area_widget)
        self.piv_image_area = QtWidgets.QLabel(self.piv_scroll_area_widget)
        self.interactive_analysis_settings_frame = QtWidgets.QFrame(self.interactive_analysis_window)
        self.interactive_analysis_settings_frame_layout = QtWidgets.QGridLayout(
        self.interactive_analysis_settings_frame)
        self.redraw_iws_check_box = QtWidgets.QCheckBox(self.interactive_analysis_settings_frame)
        self.sequential_frames_combo_box = QtWidgets.QComboBox(self.interactive_analysis_settings_frame)
        self.horizontalSlider = QtWidgets.QSlider(self.interactive_analysis_settings_frame)
        self.prev_frame = QtWidgets.QPushButton(self.interactive_analysis_settings_frame)
        self.iw_frame = QtWidgets.QFrame(self.interactive_analysis_settings_frame)
        self.iw_frame_layout = QtWidgets.QGridLayout(self.iw_frame)
        self.small_iw_size_combo_box = QtWidgets.QComboBox(self.iw_frame)
        self.big_iw_overlap_size_combo_box = QtWidgets.QComboBox(self.iw_frame)
        self.big_iw_size_combo_box = QtWidgets.QComboBox(self.iw_frame)
        self.big_iw_overlap_size_label = QtWidgets.QLabel(self.iw_frame)
        self.big_iw_size_label = QtWidgets.QLabel(self.iw_frame)
        self.small_iw_size_label = QtWidgets.QLabel(self.iw_frame)
        self.pushButton = QtWidgets.QPushButton(self.iw_frame)
        self.toolButton = QtWidgets.QToolButton(self.interactive_analysis_settings_frame)
        self.label_5 = QtWidgets.QLabel(self.interactive_analysis_settings_frame)
        self.next_frame = QtWidgets.QPushButton(self.interactive_analysis_settings_frame)
        self.label_6 = QtWidgets.QLabel(self.interactive_analysis_settings_frame)

    def interactive_analysis_window_setup(self):
        self.interactive_analysis_window.setObjectName("interactive_analysis_window")
        self.interactive_analysis_window.resize(550, 686)
        self.interactive_analysis_window.setMinimumSize(QtCore.QSize(550, 686))
        self.interactive_analysis_window.setMaximumSize(QtCore.QSize(550, 686))

        self.piv_scroll_area.setWidgetResizable(True)

        self.piv_scroll_area_widget.setGeometry(QtCore.QRect(0, 0, 530, 465))

        self.piv_scroll_area_widget_layout.addWidget(self.piv_image_area, 0, 0, 1, 1)

        self.piv_scroll_area.setWidget(self.piv_scroll_area_widget)

        self.interactive_analysis_window_layout.addWidget(self.piv_scroll_area, 0, 0, 1, 1)

        self.interactive_analysis_settings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.interactive_analysis_settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.interactive_analysis_settings_frame_layout.addWidget(self.redraw_iws_check_box, 4, 6, 1, 1)

        self.sequential_frames_combo_box.addItem("Sequential frames (1-2,2-3,3-4...)")
        self.sequential_frames_combo_box.addItem("Sequential frames (1-2,3-4,5-6...)")

        self.interactive_analysis_settings_frame_layout.addWidget(self.sequential_frames_combo_box, 4, 0, 1, 6)

        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.interactive_analysis_settings_frame_layout.addWidget(self.horizontalSlider, 0, 0, 1, 9)

        self.interactive_analysis_settings_frame_layout.addWidget(self.prev_frame, 2, 2, 1, 1)

        self.iw_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.iw_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.small_iw_size_combo_box.setMaximumSize(QtCore.QSize(50, 16777215))
        self.small_iw_size_combo_box.addItem("8")
        self.small_iw_size_combo_box.addItem("16")
        self.small_iw_size_combo_box.addItem("32")
        self.small_iw_size_combo_box.addItem("64")
        self.small_iw_size_combo_box.addItem("128")
        self.small_iw_size_combo_box.addItem("256")
        self.small_iw_size_combo_box.addItem("512")

        self.iw_frame_layout.addWidget(self.small_iw_size_combo_box, 0, 1, 1, 1)

        self.big_iw_overlap_size_combo_box.setMaximumSize(QtCore.QSize(50, 16777215))
        self.big_iw_overlap_size_combo_box.addItem("8")
        self.big_iw_overlap_size_combo_box.addItem("16")
        self.big_iw_overlap_size_combo_box.addItem("32")
        self.big_iw_overlap_size_combo_box.addItem("64")
        self.big_iw_overlap_size_combo_box.addItem("128")
        self.big_iw_overlap_size_combo_box.addItem("256")
        self.big_iw_overlap_size_combo_box.addItem("512")

        self.iw_frame_layout.addWidget(self.big_iw_overlap_size_combo_box, 2, 1, 1, 1)

        self.big_iw_size_combo_box.setMaximumSize(QtCore.QSize(50, 16777215))
        self.big_iw_size_combo_box.addItem("8")
        self.big_iw_size_combo_box.addItem("16")
        self.big_iw_size_combo_box.addItem("32")
        self.big_iw_size_combo_box.addItem("64")
        self.big_iw_size_combo_box.addItem("128")
        self.big_iw_size_combo_box.addItem("256")
        self.big_iw_size_combo_box.addItem("512")

        self.iw_frame_layout.addWidget(self.big_iw_size_combo_box, 1, 1, 1, 1)
        self.iw_frame_layout.addWidget(self.big_iw_overlap_size_label, 2, 0, 1, 1)
        self.iw_frame_layout.addWidget(self.big_iw_size_label, 1, 0, 1, 1)
        self.iw_frame_layout.addWidget(self.small_iw_size_label, 0, 0, 1, 1)
        self.iw_frame_layout.addWidget(self.pushButton, 3, 0, 1, 2)

        self.interactive_analysis_settings_frame_layout.addWidget(self.iw_frame, 2, 8, 2, 1)
        self.interactive_analysis_settings_frame_layout.addWidget(self.toolButton, 2, 1, 1, 1)

        self.label_5.setMinimumSize(QtCore.QSize(70, 70))
        self.label_5.setMaximumSize(QtCore.QSize(70, 70))

        self.interactive_analysis_settings_frame_layout.addWidget(self.label_5, 3, 2, 1, 1)
        self.interactive_analysis_settings_frame_layout.addWidget(self.next_frame, 2, 3, 1, 1)

        self.label_6.setMinimumSize(QtCore.QSize(92, 92))
        self.label_6.setMaximumSize(QtCore.QSize(92, 92))

        self.interactive_analysis_settings_frame_layout.addWidget(self.label_6, 3, 3, 1, 1)

        self.interactive_analysis_window_layout.addWidget(self.interactive_analysis_settings_frame, 1, 0, 1, 1)

        self.text_setup(self.interactive_analysis_window)
        QtCore.QMetaObject.connectSlotsByName(self.interactive_analysis_window)

    def text_setup(self, interactive_analysis_window):
        interactive_analysis_window.setWindowTitle("Interactive analysis")
        self.redraw_iws_check_box.setText("Redraw IWs")
        self.prev_frame.setText("Prev.Frame")
        self.big_iw_overlap_size_label.setText("Big IW overlap size:")
        self.big_iw_size_label.setText("Big IW size:")
        self.small_iw_size_label.setText("Small IW size:")
        self.pushButton.setText("Plot Correlation Matrix")
        self.toolButton.setText("...")
        self.label_5.setText("TextLabel")
        self.next_frame.setText("Next Frame")
        self.label_6.setText("TextLabel")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = InteractiveAnalysisWindow()
    ui.interactive_analysis_window_setup()
    ui.interactive_analysis_window.show()
    sys.exit(app.exec_())
