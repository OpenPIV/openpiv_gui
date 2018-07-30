from PySide2 import QtGui, QtWidgets, QtCore

FONT = QtGui.QFont()
FONT.setFamily("Ari")
FONT.setPointSize(11)
FONT.setWeight(100)
FONT.setItalic(False)
FONT.setBold(False)


class PostProcessingTabClass(object):
    def __init__(self):
        self.post_processing_tab = QtWidgets.QTabWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.post_processing_tab)
        self.filter_group_box = QtWidgets.QGroupBox(self.post_processing_tab)
        self.filter_group_box_layout = QtWidgets.QGridLayout(self.filter_group_box)
        self.local_filter_group_box = QtWidgets.QGroupBox(self.filter_group_box)
        self.local_filter_group_box_layout = QtWidgets.QGridLayout(self.local_filter_group_box)
        self.local_mean_median_spin_box = QtWidgets.QDoubleSpinBox(self.local_filter_group_box)
        self.local_mean_median_combo_box = QtWidgets.QComboBox(self.local_filter_group_box)
        self.smoothing_group_box = QtWidgets.QGroupBox(self.filter_group_box)
        self.smoothing_group_box_layout = QtWidgets.QGridLayout(self.smoothing_group_box)
        self.smoothing_mean_median_combo_box = QtWidgets.QComboBox(self.smoothing_group_box)
        self.smoothing_mean_median_spin_box = QtWidgets.QDoubleSpinBox(self.smoothing_group_box)
        self.global_filter_group_box = QtWidgets.QGroupBox(self.filter_group_box)
        self.global_filter_group_box_layout = QtWidgets.QGridLayout(self.global_filter_group_box)
        self.global_filter_spin_box_1 = QtWidgets.QDoubleSpinBox(self.global_filter_group_box)
        self.global_filter_spin_box_2 = QtWidgets.QDoubleSpinBox(self.global_filter_group_box)
        self.global_filter_local_filter_line = QtWidgets.QFrame(self.filter_group_box)
        self.local_filter_smoothing_line = QtWidgets.QFrame(self.filter_group_box)
        self.smoothing_interpolation_line = QtWidgets.QFrame(self.filter_group_box)
        self.interpolation_group_box = QtWidgets.QGroupBox(self.filter_group_box)
        self.interpolation_group_box_layout = QtWidgets.QGridLayout(self.interpolation_group_box)
        self.times_spin_box = QtWidgets.QSpinBox(self.interpolation_group_box)
        self.action_label = QtWidgets.QLabel(self.interpolation_group_box)
        self.action_combo_box = QtWidgets.QComboBox(self.interpolation_group_box)
        self.times_label = QtWidgets.QLabel(self.interpolation_group_box)
        self.activate_button = QtWidgets.QPushButton(self.interpolation_group_box)

    def post_processing_tab_setup(self):
        self.post_processing_tab.setObjectName("post_processing_tab")
        self.post_processing_tab.resize(318, 527)
        self.filter_group_box.setFont(FONT)

        self.local_filter_group_box_layout.addWidget(self.local_mean_median_spin_box, 0, 1, 1, 1)

        self.local_mean_median_combo_box.addItem("mean")
        self.local_mean_median_combo_box.addItem("median")
        self.local_mean_median_combo_box.view().setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff))

        self.smoothing_mean_median_combo_box.addItem("mean")
        self.smoothing_mean_median_combo_box.addItem("median")
        self.local_filter_group_box_layout.addWidget(self.local_mean_median_combo_box, 0, 0, 1, 1)
        self.filter_group_box_layout.addWidget(self.local_filter_group_box, 2, 0, 1, 1)

        self.smoothing_group_box_layout.addWidget(self.smoothing_mean_median_combo_box, 0, 0, 1, 1)

        self.smoothing_group_box_layout.addWidget(self.smoothing_mean_median_spin_box, 0, 1, 1, 1)

        self.filter_group_box_layout.addWidget(self.smoothing_group_box, 5, 0, 1, 1)

        self.global_filter_group_box_layout.addWidget(self.global_filter_spin_box_1, 0, 0, 1, 1)

        self.global_filter_group_box_layout.addWidget(self.global_filter_spin_box_2, 0, 1, 1, 1)
        self.filter_group_box_layout.addWidget(self.global_filter_group_box, 0, 0, 1, 1)

        self.global_filter_local_filter_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.global_filter_local_filter_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.filter_group_box_layout.addWidget(self.global_filter_local_filter_line, 1, 0, 1, 1)

        self.local_filter_smoothing_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.local_filter_smoothing_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.filter_group_box_layout.addWidget(self.local_filter_smoothing_line, 4, 0, 1, 1)

        self.smoothing_interpolation_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.smoothing_interpolation_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.filter_group_box_layout.addWidget(self.smoothing_interpolation_line, 6, 0, 1, 1)

        self.interpolation_group_box_layout.addWidget(self.times_spin_box, 1, 1, 1, 1)

        self.interpolation_group_box_layout.addWidget(self.action_label, 0, 0, 1, 1)

        self.action_combo_box.addItem("cubic")
        self.action_combo_box.addItem("linear")
        self.action_combo_box.addItem("nearest")
        self.interpolation_group_box_layout.addWidget(self.action_combo_box, 0, 1, 1, 1)

        self.interpolation_group_box_layout.addWidget(self.times_label, 1, 0, 1, 1)

        self.interpolation_group_box_layout.addWidget(self.activate_button, 2, 0, 1, 2)
        self.filter_group_box_layout.addWidget(self.interpolation_group_box, 7, 0, 1, 1)
        self.gridLayout.addWidget(self.filter_group_box, 0, 0, 1, 1)

        self.text_setup()

    def text_setup(self):
        self.filter_group_box.setTitle("filters")
        self.local_filter_group_box.setTitle("local filter")
        self.smoothing_group_box.setTitle("smoothing")
        self.global_filter_group_box.setTitle("global filter")
        self.interpolation_group_box.setTitle("interpolation")
        self.action_label.setText("action:")
        self.times_label.setText("times:")
        self.activate_button.setText("Activate")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    post_processing_tab = QtWidgets.QTabWidget()
    post_processing_tab_class = PostProcessingTabClass()
    post_processing_tab_class.post_processing_tab_setup()
    post_processing_tab.show()
    sys.exit(app.exec_())
