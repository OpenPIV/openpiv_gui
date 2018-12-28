from PySide2 import QtCore, QtWidgets, QtGui
from package.font import FONT


# the image processing tab ibn the settings tab widget
class ImageProcessingTabClass(object):
    def __init__(self):
        self.image_processing_tab = QtWidgets.QTabBar()

        self.image_processing_tab_layout = QtWidgets.QGridLayout(self.image_processing_tab)
        self.bit_invert_frame = QtWidgets.QFrame()
        self.image_processing_tab_settings_farm_layout = QtWidgets.QGridLayout(self.bit_invert_frame)
        self.invert_button = QtWidgets.QPushButton(self.bit_invert_frame)
        self.invert_label = QtWidgets.QLabel()
        self.bit_combo_box = QtWidgets.QComboBox(self.bit_invert_frame)
        self.bit_combo_box_label = QtWidgets.QLabel()
        self.brightness_frame = QtWidgets.QFrame()
        self.brightness_frame_layout = QtWidgets.QGridLayout(self.brightness_frame)
        self.brightness_label = QtWidgets.QLabel(self.bit_invert_frame)
        self.brightness_level_slider = QtWidgets.QSlider(self.bit_invert_frame)

    def image_processing_tab_setup(self):
        self.bit_invert_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.bit_invert_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.bit_combo_box.addItem("8 bit")
        self.bit_combo_box.addItem("16 bit")

        self.brightness_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.brightness_frame.setFrameShadow(QtWidgets.QFrame.Sunken)


        self.brightness_label.setAlignment(QtCore.Qt.AlignCenter)
        self.brightness_label.setFont(FONT)
        self.bit_combo_box_label.setFont(FONT)
        self.invert_label.setFont(FONT)

        self.brightness_level_slider.setOrientation(QtCore.Qt.Horizontal)

        self.image_processing_tab_settings_farm_layout.addWidget(self.invert_label, 1, 0, 1, 1)
        self.image_processing_tab_settings_farm_layout.addWidget(self.bit_combo_box_label, 2, 0, 1, 1)
        self.image_processing_tab_settings_farm_layout.addWidget(self.invert_button, 1, 1, 1, 1)
        self.image_processing_tab_settings_farm_layout.addWidget(self.bit_combo_box, 2, 1, 1, 1)

        self.brightness_frame_layout.addWidget(self.brightness_label, 0, 0, 1, 1)
        self.brightness_frame_layout.addWidget(self.brightness_level_slider, 1, 0, 1, 1)

        self.image_processing_tab_layout.addWidget(self.bit_invert_frame, 1, 0, 1, 1)
        self.image_processing_tab_layout.addWidget(self.brightness_frame, 2, 0, 1, 1)

        image_processing_tab_spacer = QtWidgets.QSpacerItem(20, 2000, QtWidgets.QSizePolicy.Minimum,
                                                            QtWidgets.QSizePolicy.Expanding)

        self.image_processing_tab_layout.addItem(image_processing_tab_spacer, 3, 0, 1, 1)

        self.text_setup()
        QtCore.QMetaObject.connectSlotsByName(self.image_processing_tab)

    def text_setup(self):
        set_text = lambda x, text: x.setText(text)

        set_text(self.invert_button, "invert")
        set_text(self.brightness_label, "brightness")
        set_text(self.invert_label, "Invert:")
        set_text(self.bit_combo_box_label, "Bit:")


# if __name__ == "__main__":
#     # run the program
#     import sys

#     app = QtWidgets.QApplication(sys.argv)
#     image_processing_tab_class = ImageProcessingTabClass()
#     image_processing_tab_class.image_processing_tab_setup()
#     image_processing_tab_class.image_processing_tab.show()
#     sys.exit(app.exec_())
