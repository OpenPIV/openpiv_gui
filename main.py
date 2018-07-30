from package.MainWindow import MainWindowClass
from package.SettingTabWidget import SettingsTabWidgetClass
from package.PIVPlot import PIVPlot
from package.FileWindow import FileWindowClass
from package.SettingsTab import SettingsTab
from package.ImagePivPostTab import PostProcessingTabClass
from PySide2 import QtWidgets, QtCore
from _functools import partial
import sys

MAIN_WINDOW_CLASS = None
SETTINGS_TAB_WIDGET_CLASS = None
PIV_PLOT_CLASS = None
FILE_WINDOW_CLASS = None
SETTINGS_TAB_CLASS = None
POST_PROCESSING_TAB_CLASS = None


def run_main_window():
    global MAIN_WINDOW_CLASS, FILE_WINDOW_CLASS, SETTINGS_TAB_WIDGET_CLASS, PIV_PLOT_CLASS, SETTINGS_TAB_CLASS, \
        POST_PROCESSING_TAB_CLASS
    app = QtWidgets.QApplication(sys.argv)

    # setup for the file window to add for the image processing tab
    file_window_frame = QtWidgets.QFrame()
    FILE_WINDOW_CLASS = FileWindowClass(file_window_frame)
    FILE_WINDOW_CLASS.window_setup()

    SETTINGS_TAB_CLASS = SettingsTab()
    SETTINGS_TAB_CLASS.setting_widget_setup()

    POST_PROCESSING_TAB_CLASS = PostProcessingTabClass()
    POST_PROCESSING_TAB_CLASS.post_processing_tab_setup()

    SETTINGS_TAB_WIDGET_CLASS = SettingsTabWidgetClass()
    SETTINGS_TAB_WIDGET_CLASS.settings_widget_setup()
    SETTINGS_TAB_WIDGET_CLASS.image_processing_tab_class.image_processing_tab_layout.addWidget(file_window_frame, 1, 0,
                                                                                               1, 1)
    SETTINGS_TAB_WIDGET_CLASS.settings_tab_widget.insertTab(1, SETTINGS_TAB_CLASS.settings_tab, "piv")
    SETTINGS_TAB_WIDGET_CLASS.settings_tab_widget.insertTab(2, POST_PROCESSING_TAB_CLASS.post_processing_tab,
                                                            "post")
    SETTINGS_TAB_WIDGET_CLASS.settings_tab_widget.setStyleSheet("background-color: rgb(240, 240, 240);")

    # create the widget that will hold the plot
    piv_plot_widget = QtWidgets.QWidget()
    PIV_PLOT_CLASS = PIVPlot(piv_plot_widget)

    # here is where the connection with the start button and piv function is
    # (is uses lambda to get the the current values)
    SETTINGS_TAB_CLASS.start_button.clicked.connect(
        lambda: PIV_PLOT_CLASS.start_piv(
            int(SETTINGS_TAB_CLASS.width_combo_box.currentText()),
            int(SETTINGS_TAB_CLASS.height_combo_box.currentText()),
            int(SETTINGS_TAB_CLASS.horizontal_combo_box.currentText()),
            int(SETTINGS_TAB_CLASS.vertical_combo_box.currentText()),
            int(SETTINGS_TAB_CLASS.type_combo_box.currentText()),
            SETTINGS_TAB_CLASS.value_spin_box.value(),
            SETTINGS_TAB_CLASS.scale_spin_box.value(),
            SETTINGS_TAB_CLASS.outer_filter_spin_box.value(),
            SETTINGS_TAB_CLASS.jump_spin_box.value()
        ))

    SETTINGS_TAB_WIDGET_CLASS.image_processing_tab_class.invert_button.clicked.connect(invert_button)

    # a max and a min to the file window frame to make it look better
    file_window_frame.setMinimumSize(QtCore.QSize(198, 200))

    # create the widget of the main window
    main_window_widget = QtWidgets.QMainWindow()

    MAIN_WINDOW_CLASS = MainWindowClass(main_window_widget)
    MAIN_WINDOW_CLASS.main_widget_layout.addWidget(SETTINGS_TAB_WIDGET_CLASS.settings_tab_widget, 0, 5, 3, 1)
    MAIN_WINDOW_CLASS.main_window_setup()
    MAIN_WINDOW_CLASS.image_pages.addWidget(piv_plot_widget)

    # show the widget of the main window
    main_window_widget.show()

    # exit the program only if you trigger the exit action
    MAIN_WINDOW_CLASS.quit_action.triggered.connect(partial(sys.exit, partial(app.exec_)))

    # add a file only when the load button is triggered
    MAIN_WINDOW_CLASS.load_action.triggered.connect(FILE_WINDOW_CLASS.add_file)

    # add/remove an image when it is added/removed from the list
    (FILE_WINDOW_CLASS.file_list.model()).rowsInserted.connect(file_added)
    (FILE_WINDOW_CLASS.file_list.model()).rowsRemoved.connect(file_removed)

    # change the image to the left/right next image
    MAIN_WINDOW_CLASS.left_button.clicked.connect(change_image_number_left)
    MAIN_WINDOW_CLASS.right_button.clicked.connect(change_image_number_right)

    FILE_WINDOW_CLASS.file_list.itemEntered.connect(file_order_changed)

    # activating the ROI buttons to work when called
    SETTINGS_TAB_CLASS.select_roi_button.clicked.connect(partial(PIV_PLOT_CLASS.ROI_buttons, True))
    SETTINGS_TAB_CLASS.reset_roi_button.clicked.connect(partial(PIV_PLOT_CLASS.ROI_buttons, False))

    SETTINGS_TAB_WIDGET_CLASS.image_processing_tab_class.bit_combo_box.currentIndexChanged.connect(
        lambda: change_bit(str(SETTINGS_TAB_WIDGET_CLASS.image_processing_tab_class.bit_combo_box.currentText())))

    sys.exit(app.exec_())


def file_removed():
    if FILE_WINDOW_CLASS.file_list.count() == 0:
        del (PIV_PLOT_CLASS.piv_images_list[0])
        MAIN_WINDOW_CLASS.image_pages.setCurrentIndex(0)
        return 0

    for i in range(0, FILE_WINDOW_CLASS.file_list.count()):
        if PIV_PLOT_CLASS.piv_images_list[i][1] != FILE_WINDOW_CLASS.file_list.item(i).text():
            del (PIV_PLOT_CLASS.piv_images_list[i])
            PIV_PLOT_CLASS.show_plot(0)
            MAIN_WINDOW_CLASS.current_image_number.setText("1")
            # change the jump range when the images number changes
            change_jump_max_min()
            return 0

    if len(PIV_PLOT_CLASS.piv_images_list) - (FILE_WINDOW_CLASS.file_list.count()) > 0:
        del (PIV_PLOT_CLASS.piv_images_list[-1])

    PIV_PLOT_CLASS.show_plot(0)
    MAIN_WINDOW_CLASS.current_image_number.setText("1")

    # change the jump range when the images number changes
    change_jump_max_min()


# function that add the image that was added to the main widget
def file_added():
    if FILE_WINDOW_CLASS.file_list.item(FILE_WINDOW_CLASS.file_list.count() - 1).text() == '':
        FILE_WINDOW_CLASS.file_Window_class.file_list.takeItem(
            FILE_WINDOW_CLASS.file_list.item(
                FILE_WINDOW_CLASS.file_list.count() - 1))
        return 0

    if FILE_WINDOW_CLASS.file_list.count() == 1:
        MAIN_WINDOW_CLASS.image_pages.setCurrentIndex(1)
        PIV_PLOT_CLASS.add_image(FILE_WINDOW_CLASS.last_file)
        PIV_PLOT_CLASS.show_plot(0)
        MAIN_WINDOW_CLASS.current_image_number.setText("1")

    elif FILE_WINDOW_CLASS.file_list.count() > 1:
        PIV_PLOT_CLASS.add_image(FILE_WINDOW_CLASS.last_file)
        PIV_PLOT_CLASS.show_plot(FILE_WINDOW_CLASS.file_list.count() - 1)
        MAIN_WINDOW_CLASS.current_image_number.setText(
            str(FILE_WINDOW_CLASS.file_list.count()))

    # change the jump range when the images number changes
    change_jump_max_min()


# function that changes the max and min of jump
def change_jump_max_min():
    SETTINGS_TAB_CLASS.jump_spin_box.setMaximum(len(PIV_PLOT_CLASS.piv_images_list) - 1)
    SETTINGS_TAB_CLASS.jump_spin_box.setMinimum((-1) * (len(PIV_PLOT_CLASS.piv_images_list) - 1))


# function that moves to the next right image
def change_image_number_right():
    if len(PIV_PLOT_CLASS.piv_images_list) == 0:
        return 0

    if int(MAIN_WINDOW_CLASS.current_image_number.text()) == len(PIV_PLOT_CLASS.piv_images_list):
        MAIN_WINDOW_CLASS.current_image_number.setText("1")
        PIV_PLOT_CLASS.show_plot(0)
        if PIV_PLOT_CLASS.piv_images_list[0][3] == 8:
            SETTINGS_TAB_WIDGET_CLASS.image_processing_tab_class.bit_combo_box.setCurrentIndex(0)
        elif PIV_PLOT_CLASS.piv_images_list[0][3] == 16:
            SETTINGS_TAB_WIDGET_CLASS.image_processing_tab_class.bit_combo_box.setCurrentIndex(1)
    else:
        PIV_PLOT_CLASS.show_plot(int(MAIN_WINDOW_CLASS.current_image_number.text()))
        MAIN_WINDOW_CLASS.current_image_number.setText(str(int(MAIN_WINDOW_CLASS.current_image_number.text()) + 1))
        if PIV_PLOT_CLASS.piv_images_list[int(MAIN_WINDOW_CLASS.current_image_number.text()) - 1][3] == 8:
            SETTINGS_TAB_WIDGET_CLASS.image_processing_tab_class.bit_combo_box.setCurrentIndex(0)
        elif PIV_PLOT_CLASS.piv_images_list[int(MAIN_WINDOW_CLASS.current_image_number.text()) - 1][3] == 16:
            SETTINGS_TAB_WIDGET_CLASS.image_processing_tab_class.bit_combo_box.setCurrentIndex(1)


# function that moves to the next left image
def change_image_number_left():
    if len(PIV_PLOT_CLASS.piv_images_list) == 0:
        return 0

    if int(MAIN_WINDOW_CLASS.current_image_number.text()) == 1:
        MAIN_WINDOW_CLASS.current_image_number.setText(str(len(PIV_PLOT_CLASS.piv_images_list)))
        PIV_PLOT_CLASS.show_plot(len(PIV_PLOT_CLASS.piv_images_list) - 1)
        if PIV_PLOT_CLASS.piv_images_list[len(PIV_PLOT_CLASS.piv_images_list) - 1][3] == 8:
            SETTINGS_TAB_WIDGET_CLASS.image_processing_tab_class.bit_combo_box.setCurrentIndex(0)
        elif PIV_PLOT_CLASS.piv_images_list[len(PIV_PLOT_CLASS.piv_images_list) - 1][3] == 16:
            SETTINGS_TAB_WIDGET_CLASS.image_processing_tab_class.bit_combo_box.setCurrentIndex(1)

    else:
        PIV_PLOT_CLASS.show_plot(int(MAIN_WINDOW_CLASS.current_image_number.text()) - 2)
        MAIN_WINDOW_CLASS.current_image_number.setText(str(int(MAIN_WINDOW_CLASS.current_image_number.text()) - 1))
        if PIV_PLOT_CLASS.piv_images_list[int(MAIN_WINDOW_CLASS.current_image_number.text()) - 1][3] == 8:
            SETTINGS_TAB_WIDGET_CLASS.image_processing_tab_class.bit_combo_box.setCurrentIndex(0)
        elif PIV_PLOT_CLASS.piv_images_list[int(MAIN_WINDOW_CLASS.current_image_number.text()) - 1][3] == 16:
            SETTINGS_TAB_WIDGET_CLASS.image_processing_tab_class.bit_combo_box.setCurrentIndex(1)


def invert_button():
    for i in FILE_WINDOW_CLASS.file_list.selectedItems():
        if FILE_WINDOW_CLASS.file_list.item(FILE_WINDOW_CLASS.file_list.row(i)).text().lower().endswith(
                ('.png', '.jpg', '.jpeg')):
            PIV_PLOT_CLASS.piv_images_list[FILE_WINDOW_CLASS.file_list.row(i)][2] = PIV_PLOT_CLASS.invert(
                PIV_PLOT_CLASS.piv_images_list[FILE_WINDOW_CLASS.file_list.row(i)][2],
                False)
            PIV_PLOT_CLASS.show_plot(FILE_WINDOW_CLASS.file_list.row(i))
        else:
            PIV_PLOT_CLASS.piv_images_list[FILE_WINDOW_CLASS.file_list.row(i)][2] = PIV_PLOT_CLASS.invert(
                PIV_PLOT_CLASS.piv_images_list[FILE_WINDOW_CLASS.file_list.row(i)][2],
                True)
            PIV_PLOT_CLASS.show_plot(FILE_WINDOW_CLASS.file_list.row(i))


def file_order_changed():
    file_list_list = []
    for i in range(FILE_WINDOW_CLASS.file_list.count()):
        file_list_list.append(FILE_WINDOW_CLASS.file_list.item(i).text())

    PIV_PLOT_CLASS.piv_images_list.sort(key=lambda x: file_list_list.index(x[1]))


def change_bit(bit):
    if bit == "8 bit":
        PIV_PLOT_CLASS.piv_images_list[int(MAIN_WINDOW_CLASS.current_image_number.text()) - 1][3] = 8
    else:
        PIV_PLOT_CLASS.piv_images_list[int(MAIN_WINDOW_CLASS.current_image_number.text()) - 1][3] = 16
    PIV_PLOT_CLASS.show_plot(int(MAIN_WINDOW_CLASS.current_image_number.text()) - 1)


def main():
    # run the program
    run_main_window()


if __name__ == '__main__':
    main()
