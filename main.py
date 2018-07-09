from package.MainWindow import MainWindowClass
from package.FileWindow import FileWindowClass
from package.SettingTabWidget import SettingsTabWidgetClass
from PySide2 import QtCore, QtGui, QtWidgets
import sys

MAIN_WINDOW_CLASS = None
FILE_WINDOW_CLASS = None
SETTINGS_TAB_WIDGET_CLASS = None


def run_main_window():
    global MAIN_WINDOW_CLASS, FILE_WINDOW_CLASS, SETTINGS_TAB_WIDGET_CLASS
    app = QtWidgets.QApplication(sys.argv)

    SETTINGS_TAB_WIDGET_CLASS = SettingsTabWidgetClass()
    SETTINGS_TAB_WIDGET_CLASS.setting_widget_setup()

    # create the widget of the main window
    main_window_widget = QtWidgets.QMainWindow()

    MAIN_WINDOW_CLASS = MainWindowClass(main_window_widget)
    MAIN_WINDOW_CLASS.main_widget_layout.addWidget(SETTINGS_TAB_WIDGET_CLASS.settings_tab_widget, 0, 5, 3, 1)
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
    if FILE_WINDOW_CLASS.file_list.count() == 0:
        MAIN_WINDOW_CLASS.image_pages.removeWidget(MAIN_WINDOW_CLASS.image_pages.currentWidget())
        MAIN_WINDOW_CLASS.default_image.setPixmap(r"package/images/openpiv_logo.png")
        MAIN_WINDOW_CLASS.image_pages.addWidget(MAIN_WINDOW_CLASS.default_image_widget)
        return 0
    j = 0
    for i in range(MAIN_WINDOW_CLASS.image_pages.count() - 1):
        if i + j == MAIN_WINDOW_CLASS.image_pages.count():
            return 0
        while (MAIN_WINDOW_CLASS.image_pages.widget(i + j).findChild(
                QtWidgets.QLabel).pixmap().cacheKey() != QtGui.QPixmap(
            FILE_WINDOW_CLASS.file_list.item(i).text()).cacheKey()):
            MAIN_WINDOW_CLASS.image_pages.removeWidget(MAIN_WINDOW_CLASS.image_pages.widget(i + j))
            j += 1
            print(j + i)
            if i + j == MAIN_WINDOW_CLASS.image_pages.count():
                return 0
    if MAIN_WINDOW_CLASS.image_pages.count() - FILE_WINDOW_CLASS.file_list.count():
        for i in range(MAIN_WINDOW_CLASS.image_pages.count() - FILE_WINDOW_CLASS.file_list.count()):
            MAIN_WINDOW_CLASS.image_pages.removeWidget(
                MAIN_WINDOW_CLASS.image_pages.widget(MAIN_WINDOW_CLASS.image_pages.count() - i - 1))


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
    change_jump_max_min()


def create_label_pixmap(pixmap):
    widget = QtWidgets.QWidget()
    widget_layout = QtWidgets.QGridLayout(widget)
    label = QtWidgets.QLabel()
    widget_layout.addWidget(label, 0, 0, 1, 1)
    label.setPixmap(QtGui.QPixmap(pixmap))
    label.setAlignment(QtCore.Qt.AlignCenter)
    return widget


# function that changes the max and min of jump
def change_jump_max_min():
    SETTINGS_TAB_WIDGET_CLASS.jump_spin_box.setMaximum(MAIN_WINDOW_CLASS.image_pages.count() - 1)
    SETTINGS_TAB_WIDGET_CLASS.jump_spin_box.setMinimum((-1) * (MAIN_WINDOW_CLASS.image_pages.count() - 1))


def main():
    # run the program
    run_main_window()


if __name__ == '__main__':
    main()
