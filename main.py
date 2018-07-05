from package.MainWindow import MainWindowClass
from package.FileWindow import FileWindowClass
from PySide2 import QtCore, QtWidgets
import sys
from threading import Thread


def run_main_window():
    app = QtWidgets.QApplication(sys.argv)

    main_window_widget = QtWidgets.QMainWindow()

    main_window_class = MainWindowClass(main_window_widget)
    main_window_class.setting_dock_widget_setup()
    main_window_class.main_window_setup()

    main_window_widget.show()

    file_window = QtWidgets.QWidget()

    file_window_class = FileWindowClass(file_window)
    file_window_class.window_setup()

    main_window_class.file_action.triggered.connect(file_window.show)

    sys.exit(app.exec_())


def main():
    run_main_window()


if __name__ == '__main__':
    main()
