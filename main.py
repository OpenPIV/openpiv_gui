from package.MainWindow import MainWindowClass
from package.FileWindow import FileWindowClass
from package.SettingTabWidget import SettingsTabWidgetClass
from package.PIVPlot import PIVPlot
from PySide2 import QtWidgets
import sys

MAIN_WINDOW_CLASS = None
FILE_WINDOW_CLASS = None
SETTINGS_TAB_WIDGET_CLASS = None
PIV_PLOT_CLASS = None


def run_main_window():
    global MAIN_WINDOW_CLASS, FILE_WINDOW_CLASS, SETTINGS_TAB_WIDGET_CLASS, PIV_PLOT_CLASS
    app = QtWidgets.QApplication(sys.argv)

    SETTINGS_TAB_WIDGET_CLASS = SettingsTabWidgetClass()
    SETTINGS_TAB_WIDGET_CLASS.setting_widget_setup()

    # create the widget that will hold the plot
    piv_plot_widget = QtWidgets.QWidget()
    PIV_PLOT_CLASS = PIVPlot(piv_plot_widget)

    # create the widget of the main window
    main_window_widget = QtWidgets.QMainWindow()

    MAIN_WINDOW_CLASS = MainWindowClass(main_window_widget)
    MAIN_WINDOW_CLASS.main_widget_layout.addWidget(SETTINGS_TAB_WIDGET_CLASS.settings_tab_widget, 0, 5, 3, 1)
    MAIN_WINDOW_CLASS.main_window_setup()
    MAIN_WINDOW_CLASS.image_pages.addWidget(piv_plot_widget)

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

    MAIN_WINDOW_CLASS.left_button.clicked.connect(change_image_number_left)
    MAIN_WINDOW_CLASS.right_button.clicked.connect(change_image_number_right)

    sys.exit(app.exec_())


def file_removed():
    if FILE_WINDOW_CLASS.file_list.count() == 0:
        del (PIV_PLOT_CLASS.piv_images_list[0])
        MAIN_WINDOW_CLASS.image_pages.setCurrentIndex(0)
        return 0

    for i in range(0, FILE_WINDOW_CLASS.file_list.count()):
        if PIV_PLOT_CLASS.piv_images_list[i] != FILE_WINDOW_CLASS.file_list.item(i).text():
            del (PIV_PLOT_CLASS.piv_images_list[i])
            PIV_PLOT_CLASS.show_plot(0)
            MAIN_WINDOW_CLASS.current_image_number.setText("0")
            # change the jump range when the images number changes
            change_jump_max_min()
            return 0

    if len(PIV_PLOT_CLASS.piv_images_list) - FILE_WINDOW_CLASS.file_list.count() > 0:
        del (PIV_PLOT_CLASS.piv_images_list[-1])

    PIV_PLOT_CLASS.show_plot(0)
    MAIN_WINDOW_CLASS.current_image_number.setText("0")

    # change the jump range when the images number changes
    change_jump_max_min()


# function that add the image that was added to the main widget
def file_added():
    if not FILE_WINDOW_CLASS.file_list.item(FILE_WINDOW_CLASS.file_list.count() - 1).text():
        FILE_WINDOW_CLASS.file_list.takeItem(FILE_WINDOW_CLASS.file_list.item(FILE_WINDOW_CLASS.file_list.count() - 1))
        return 0

    if FILE_WINDOW_CLASS.file_list.count() == 1:
        MAIN_WINDOW_CLASS.image_pages.setCurrentIndex(1)
        PIV_PLOT_CLASS.add_image(FILE_WINDOW_CLASS.file_list.item(0).text())
        PIV_PLOT_CLASS.show_plot(0)
        MAIN_WINDOW_CLASS.current_image_number.setText("0")

    if FILE_WINDOW_CLASS.file_list.count() > 1:
        PIV_PLOT_CLASS.add_image(FILE_WINDOW_CLASS.file_list.item(FILE_WINDOW_CLASS.file_list.count() - 1).text())
        PIV_PLOT_CLASS.show_plot(FILE_WINDOW_CLASS.file_list.count() - 1)
        MAIN_WINDOW_CLASS.current_image_number.setText(str(FILE_WINDOW_CLASS.file_list.count() - 1))

    # change the jump range when the images number changes
    change_jump_max_min()


# function that changes the max and min of jump
def change_jump_max_min():
    SETTINGS_TAB_WIDGET_CLASS.jump_spin_box.setMaximum(len(PIV_PLOT_CLASS.piv_images_list) - 1)
    SETTINGS_TAB_WIDGET_CLASS.jump_spin_box.setMinimum((-1) * (len(PIV_PLOT_CLASS.piv_images_list) - 1))


# function that moves to the next right image
def change_image_number_right():
    if len(PIV_PLOT_CLASS.piv_images_list) == 0:
        return 0

    if int(MAIN_WINDOW_CLASS.current_image_number.text()) == len(PIV_PLOT_CLASS.piv_images_list) - 1:
        MAIN_WINDOW_CLASS.current_image_number.setText("0")
        PIV_PLOT_CLASS.show_plot(0)
    else:
        PIV_PLOT_CLASS.show_plot(int(MAIN_WINDOW_CLASS.current_image_number.text()) + 1)
        MAIN_WINDOW_CLASS.current_image_number.setText(str(int(MAIN_WINDOW_CLASS.current_image_number.text()) + 1))


# function that moves to the next left image
def change_image_number_left():
    if len(PIV_PLOT_CLASS.piv_images_list) == 0:
        return 0

    if int(MAIN_WINDOW_CLASS.current_image_number.text()) == 0:
        MAIN_WINDOW_CLASS.current_image_number.setText(str(len(PIV_PLOT_CLASS.piv_images_list) - 1))
        PIV_PLOT_CLASS.show_plot(len(PIV_PLOT_CLASS.piv_images_list) - 1)
    else:
        PIV_PLOT_CLASS.show_plot(int(MAIN_WINDOW_CLASS.current_image_number.text()) - 1)
        MAIN_WINDOW_CLASS.current_image_number.setText(str(int(MAIN_WINDOW_CLASS.current_image_number.text()) - 1))


def main():
    # run the program
    run_main_window()


if __name__ == '__main__':
    main()
