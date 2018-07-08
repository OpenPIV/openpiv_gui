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

    # shows the widget of the file window only if you trigger the menu bars file action
    MAIN_WINDOW_CLASS.file_action.triggered.connect(file_window.show)

    (FILE_WINDOW_CLASS.file_list.model()).rowsInserted.connect(file_added)

    (FILE_WINDOW_CLASS.file_list.model()).rowsRemoved.connect(file_removed)

    sys.exit(app.exec_())


def file_removed():
    print(QtGui.QPixmap(FILE_WINDOW_CLASS.file_list.item(0).text()).cacheKey())
    print(QtGui.QPixmap(FILE_WINDOW_CLASS.file_list.item(1).text()).cacheKey())
    print(MAIN_WINDOW_CLASS.image_pages.widget(0).findChild(QtWidgets.QLabel).pixmap().cacheKey())
    print(MAIN_WINDOW_CLASS.image_pages.widget(1).findChild(QtWidgets.QLabel).pixmap().cacheKey())
    print(MAIN_WINDOW_CLASS.image_pages.widget(2).findChild(QtWidgets.QLabel).pixmap().cacheKey())
    j = 0
    for i in range(MAIN_WINDOW_CLASS.image_pages.count() - 1):
        print(str(i) + "   t")
        while (
                QtGui.QPixmap(
                    FILE_WINDOW_CLASS.file_list.item(i).text())).cacheKey() != MAIN_WINDOW_CLASS.image_pages.widget(
                    i + j).findChild(QtWidgets.QLabel).pixmap().cacheKey():
            print(MAIN_WINDOW_CLASS.image_pages.removeWidget(MAIN_WINDOW_CLASS.image_pages.widget(i + j)).cacheKey())
            MAIN_WINDOW_CLASS.image_pages.removeWidget(MAIN_WINDOW_CLASS.image_pages.widget(i + j))
            j += 1
            print(j + i)
            if i + j == MAIN_WINDOW_CLASS.image_pages.count():
                return 0
        if i + j == MAIN_WINDOW_CLASS.image_pages.count():
            return 0


# function that add the image that was added to the main widget
def file_added():
    if FILE_WINDOW_CLASS.file_list.item(FILE_WINDOW_CLASS.file_list.count() - 1).text() == '':
        return 0
    if FILE_WINDOW_CLASS.file_list.count() > 0:
        MAIN_WINDOW_CLASS.default_image.setPixmap(QtGui.QPixmap(FILE_WINDOW_CLASS.file_list.item(0).text()))
        if FILE_WINDOW_CLASS.file_list.count() > 1:
            MAIN_WINDOW_CLASS.image_pages.addWidget(
                create_label_pixmap(FILE_WINDOW_CLASS.file_list.item(FILE_WINDOW_CLASS.file_list.count() - 1).text()))
    # change the jump range when the images number changes
    MAIN_WINDOW_CLASS.change_jump_max_min()


def create_label_pixmap(pixmap):
    widget = QtWidgets.QWidget()
    widget_layout = QtWidgets.QGridLayout(widget)
    label = QtWidgets.QLabel()
    widget_layout.addWidget(label, 0, 0, 1, 1)
    label.setPixmap(QtGui.QPixmap(pixmap))
    label.setAlignment(QtCore.Qt.AlignCenter)
    return widget


def main():
    # run the program
    run_main_window()


if __name__ == '__main__':
    main()
