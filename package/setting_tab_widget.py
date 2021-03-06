from PySide2 import QtCore, QtGui, QtWidgets
from package.image_processing_tab import ImageProcessingTabClass

FONT = QtGui.QFont()
FONT.setFamily("MS Shell Dig 2")
FONT.setPointSize(15)
FONT.setWeight(75)
FONT.setItalic(False)
FONT.setBold(False)


class SettingsTabWidgetClass(object):
    def __init__(self):
        self.settings_tab_widget = QtWidgets.QTabWidget()
        self.settings_tab_widget_layout = QtWidgets.QGridLayout(self.settings_tab_widget)
        self.image_processing_tab_class = ImageProcessingTabClass()
        self.image_processing_tab_class.image_processing_tab_setup()
        self.image_processing_tab = self.image_processing_tab_class.image_processing_tab

    def settings_widget_setup(self):
        self.settings_tab_widget.setUsesScrollButtons(True)
        self.settings_tab_widget.setDocumentMode(False)

        self.settings_tab_widget.addTab(self.image_processing_tab, "image")
        self.image_processing_tab.setStyleSheet("background-color: rgb(240, 240, 240);")

        self.settings_tab_widget.tabBar().setStyleSheet("font-size: 11pt; background-color: rgb(240, 240, 240);")

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
