from PySide2 import QtCore, QtGui, QtWidgets
from package.HorizontalTextBar import HorizontalTextBar
from package.SettingsTab import SettingsTab
from package.ImageProcessingTab import ImageProcessingTabClass

FONT = QtGui.QFont()
FONT.setFamily("Gill Sans MT")
FONT.setPointSize(21)
FONT.setWeight(75)
FONT.setItalic(True)
FONT.setBold(True)


class SettingsTabWidgetClass(object):
    def __init__(self):
        self.settings_tab_widget = QtWidgets.QTabWidget()
        self.settings_tab_widget_layout = QtWidgets.QGridLayout(self.settings_tab_widget)
        self.image_processing_tab_class = ImageProcessingTabClass()
        self.image_processing_tab_class.image_processing_tab_setup()
        self.image_processing_tab = self.image_processing_tab_class.image_processing_tab
        self.image_processing_tab_layout = QtWidgets.QGridLayout(self.image_processing_tab)
        self.post_processing_tab = QtWidgets.QWidget()

    def settings_widget_setup(self):

        self.settings_tab_widget.setTabBar(HorizontalTextBar())
        self.settings_tab_widget.setTabPosition(QtWidgets.QTabWidget.East)

        self.settings_tab_widget.setMinimumSize(QtCore.QSize(350, 669))

        self.settings_tab_widget.addTab(self.image_processing_tab, "image processing")
        self.image_processing_tab.setStyleSheet("background-color: rgb(240, 240, 240);")

        self.settings_tab_widget.addTab(self.post_processing_tab, "post processing")
        self.post_processing_tab.setStyleSheet("background-color: rgb(240, 240, 240);")

        self.settings_tab_widget.tabBar().setStyleSheet("font-size: 11pt;")

        self.text_setup()

        QtCore.QMetaObject.connectSlotsByName(self.settings_tab_widget)

    def text_setup(self):
        self.settings_tab_widget.setWindowTitle("OpenPIV")


if __name__ == "__main__":
    # run the application
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window_class = SettingsTabWidgetClass()
    main_window_class.settings_widget_setup()
    main_window_class.settings_tab_widget.show()
    sys.exit(app.exec_())
