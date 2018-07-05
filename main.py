from package.MainWindow import MainWindowClass
from package.FileWindow import FileWindowClass
from PySide2 import QtWidgets
import sys


def run_main_window():
    app = QtWidgets.QApplication(sys.argv)

    # create the widget of the main window
    main_window_widget = QtWidgets.QMainWindow()

    main_window_class = MainWindowClass(main_window_widget)
    main_window_class.setting_dock_widget_setup()
    main_window_class.main_window_setup()

    # show the widget of the main window
    main_window_widget.show()

    # create the widget of the file window
    file_window = QtWidgets.QWidget()

    file_window_class = FileWindowClass(file_window)
    file_window_class.window_setup()

    # show the widget of the file window only if you trigger the menu bars file action
    main_window_class.file_action.triggered.connect(file_window.show)

    sys.exit(app.exec_())


def main():
    # run the program
    run_main_window()


if __name__ == '__main__':
    main()
