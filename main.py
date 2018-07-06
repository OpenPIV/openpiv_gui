import sip

sip.setapi('QListWidgetItem', 2)
from package.MainWindow import MainWindowClass
from package.FileWindow import FileWindowClass
from PySide2 import QtCore, QtGui, QtWidgets
import sys

MAIN_WINDOW_CLASS = None
FILE_WINDOW_CLASS = None


def run_main_window():
    global MAIN_WINDOW_CLASS, FILE_WINDOW_CLASS
    app = QtWidgets.QApplication(sys.argv)

    # create the widget of the main window
    main_window_widget = QtWidgets.QMainWindow()

    MAIN_WINDOW_CLASS = MainWindowClass(main_window_widget)
    MAIN_WINDOW_CLASS.setting_dock_widget_setup()
    MAIN_WINDOW_CLASS.main_window_setup()

    # show the widget of the main window
    main_window_widget.show()

    # create the widget of the file window
    file_window = QtWidgets.QWidget()

    FILE_WINDOW_CLASS = FileWindowClass(file_window)
    FILE_WINDOW_CLASS.window_setup()

    # show the widget of the file window only if you trigger the menu bars file action
    MAIN_WINDOW_CLASS.file_action.triggered.connect(file_window.show)

    (FILE_WINDOW_CLASS.file_list.model()).rowsInserted.connect(windows_setup)

    sys.exit(app.exec_())


def windows_setup():
    if FILE_WINDOW_CLASS.file_list.count() > 0:
        MAIN_WINDOW_CLASS.default_image.setPixmap(QtGui.QPixmap(FILE_WINDOW_CLASS.file_list.item(0).text()))
        if FILE_WINDOW_CLASS.file_list.count() > 1:
            print(MAIN_WINDOW_CLASS.image_pages.addWidget(
                create_label_pixmap(FILE_WINDOW_CLASS.file_list.item(FILE_WINDOW_CLASS.file_list.count() - 1).text())))
    # change the jump range when the images number changes
    MAIN_WINDOW_CLASS.change_jump_max_min()


def create_label_pixmap(pixmap):
    widget = QtWidgets.QWidget()
    widget_layout = QtWidgets.QGridLayout(widget)
    label = QtWidgets.QLabel()
    widget_layout.addWidget(label, 0, 0, 1, 1)
    label.setPixmap(pixmap)
    label.setAlignment(QtCore.Qt.AlignCenter)
    return widget


def main():
    # run the program
    run_main_window()


if __name__ == '__main__':
    main()
